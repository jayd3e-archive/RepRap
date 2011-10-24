from pyramid.view import view_config
from reprap.models.users_comments import UsersCommentsModel

class ToggleVoteHandler(object):
    def __init__(self, request):
        self.request = request
        self.here = request.environ['PATH_INFO']
        self.matchdict = request.matchdict
        
    @view_config(route_name='toggle_vote', renderer='toggle_vote/index.mako')
    def index(self):
        user_id = self.matchdict['user_id']
        comment_id = self.matchdict['comment_id']
        vote = self.matchdict['vote']
        
        if vote=='up':
            vote = 1
        elif vote=='down':
            vote = -1
        else:
            return {}
        
        db = self.request.db
        voted_comment = db.query(UsersCommentsModel).filter_by(user_id=user_id,
                                                               comment_id=comment_id)
        if voted_comment:
            
        return {}