from pyramid.response import Response
from pyramid.view import view_config
from reprap.forms.issues.add import AddIssueSchema
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
                form.validate(controls)
            except ValidationFailure as e:
                return {'form':e.render(),
                        'here':self.here,
                        'title':title}
            return {'form':'OK'}
        
        return {'here':self.here,
                'title':title,
                'form':form.render()}