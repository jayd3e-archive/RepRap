from pyramid.response import Response
from pyramid.view import view_config

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
        return {'title' : 'Add Issue',
                'here' : self.here}