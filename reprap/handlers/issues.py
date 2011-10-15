from datetime import datetime
from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from reprap.forms.issues.add import AddIssueSchema
from reprap.models.issues import IssuesModel
from deform import Form
from deform.exception import ValidationFailure

class IssuesHandler(object):
    def __init__(self, request):
        self.request = request
        self.here = request.environ['PATH_INFO']
        
    @view_config(route_name='issues_root', renderer='issues/index.mako')
    def index(self):
        return {'title' : 'Issue Tracker',
                'here' : self.here}
                
    @view_config(route_name='issues_add', renderer='issues/add.mako')
    def add(self):
        title = "Add Issue"
        
        schema = AddIssueSchema()
        form = Form(schema, buttons=['submit'])
    
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
            db.add(issue)
            db.flush()
            return HTTPFound(location="/issues/view/" + str(issue.id))
        
        return {'here':self.here,
                'title':title,
                'form':form.render()}
    
    @view_config(route_name='issues_view', renderer='issues/view.mako')
    def view(self):
        title = "View Issue"
        return {'title' : title,
                'here' : self.here}