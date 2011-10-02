from pyramid.response import Response

class IssuesHandler(object):
    @view_config(route_name='issues_root', renderer='issues/index.mako')
    def index(self, request):
        return {'text' : 'Hello')