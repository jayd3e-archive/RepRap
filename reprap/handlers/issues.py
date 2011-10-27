from datetime import datetime
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from reprap.forms.issues.add import AddIssueSchema
from reprap.forms.issue_comments.add import AddIssueCommentSchema
from reprap.forms.tags.add import AddTagSchema
from reprap.models.issues import IssuesModel
from reprap.models.issue_comments import IssueCommentsModel
from reprap.models.issue_images import IssueImagesModel
from reprap.models.tags import TagsModel
from reprap.image import Image
from deform import Form
from deform import Button
from deform.widget import SequenceWidget
from deform.exception import ValidationFailure

class IssuesHandler(object):
    def __init__(self, request):
        self.request = request
        self.here = request.environ['PATH_INFO']
        self.matchdict = request.matchdict
        
    @view_config(route_name='issues_root', renderer='issues/index.mako')
    def index(self):
        db = self.request.db
        recent_issues = db.query(IssuesModel).order_by(IssuesModel.created).all()
        recent_solved_issue = db.query(IssuesModel).filter_by(solved=1).order_by(IssuesModel.solved_time).all()
        return {'title' : 'Issue Tracker',
                'here' : self.here}
                
    @view_config(route_name='issues_add', renderer='issues/add.mako')
    def add(self):
        title = "Add Issue"
        
        schema = AddIssueSchema()
        form = Form(schema, buttons=['submit'])
        form['images'].widget = SequenceWidget(min_len=1)
    
        if 'submit' in self.request.POST:
            controls = self.request.POST.items()
            try:
                captured = form.validate(controls)
            except ValidationFailure as e:
                return {'form':e.render(),
                        'here':self.here,
                        'title':title}
            db = self.request.db
            
            issue = IssuesModel(title=captured['title'],
                                description=captured['description'],
                                solved=0,
                                created=datetime.now(),
                                edited=datetime.now())
            
            tags = self.separateTags(captured['tags'])  
            for tag in tags:
                issue.tags.append(TagsModel(name=tag))
                
            for image_info in captured['images']:
                base_image = Image(image_info)
                base_image.resize((300, 300))
                base_image.thumbnail((50, 50))
                image = IssueImagesModel(directory = base_image.uid,
                                         filename = base_image.filename,
                                         filesize = base_image.filesize,
                                         mimetype = base_image.mimetype)
                issue.images.append(image)
            
            db.add(issue)
            db.flush()
            return HTTPFound(location="/issues/view/" + str(issue.id))

        return {'here':self.here,
                'title':title,
                'form':form.render()}
    
    @view_config(route_name='issues_view', renderer='issues/view.mako')
    def view(self):
        title = "View Issue"
        issue_id = self.matchdict['id']
        
        db = self.request.db
        issue = db.query(IssuesModel).filter_by(id=issue_id).first()
        
        add_issue_comment_schema = AddIssueCommentSchema()
        add_issue_comment_button = Button(name="comment_submit", title="Add Comment")
        add_issue_comment_form = Form(add_issue_comment_schema, buttons=[add_issue_comment_button])
        add_issue_comment_form['body'].title = False
        
        add_tag_schema = AddTagSchema()
        add_tag_form = Form(add_tag_schema, css_class='add_tag_form')
        add_tag_form['tags'].title = False
        
        if 'comment_submit' in self.request.POST:
            controls = self.request.POST.items()
            try:
                captured = add_issue_comment_form.validate(controls)
            except ValidationFailure as e:
                return {'add_issue_comment_form':e.render(),
                        'add_tag_form':add_tag_form.render(),
                        'here':self.here,
                        'issue':issue,
                        'title':title}
            db = self.request.db
            
            issue_comment = IssueCommentsModel(body=captured['body'],
                                               created=datetime.now(),
                                               change_time=datetime.now())
            issue.comments.append(issue_comment)
            
            db.flush()
            return HTTPFound(location="/issues/view/" + str(issue.id))
        elif 'tags' in self.request.POST:
            controls = self.request.POST.items()
            try:
                captured = add_tag_form.validate(controls)
            except ValidationFailure as e:
                return {'add_tag_form':e.render(),
                        'add_issue_comment_form':add_issue_comment_form.render(),
                        'here':self.here,
                        'issue':issue,
                        'title':title}
            db = self.request.db
            
            tags = self.separateTags(captured['tags'])
            for tag in tags:
                issue.tags.append(TagsModel(name=tag))
            
            db.flush()
            return HTTPFound(location="/issues/view/" + str(issue.id))
        
        return {'title':title,
                'here':self.here,
                'issue':issue,
                'add_tag_form':add_tag_form.render(),
                'add_issue_comment_form':add_issue_comment_form.render()}
                
    def separateTags(self, tag_string):
        tags = []
        if ', ' in tag_string:
            tags = tag_string.split(', ')
        elif ' ' in tag_string:
            tags = tag_string.split(' ')
        elif ',' in tag_string:
            tags = tag_string.split(',')
        else:
            tags = [tag_string]
        return tags