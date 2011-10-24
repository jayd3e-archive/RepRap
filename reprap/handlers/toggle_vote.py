from pyramid.view import view_config
from reprap.models.users_comments import UsersCommentsModel

class ToggleVoteHandler(object):
    def __init__(self, request):
        self.request = request
        self.here = request.environ['PATH_INFO']
        self.matchdict = request.matchdict
        
    @view_config(route_name='toggle_vote', renderer='json')
    def toggle_vote(self):
        user_id = self.matchdict['user_id']
        comment_id = self.matchdict['comment_id']
        vote = self.matchdict['vote']
        
        if vote=='up':
            vote = 1
        elif vote=='down':
            vote = -1
        else:
            return {'status' : 'unchanged'}
        
        db = self.request.db
        voted_comment = db.query(UsersCommentsModel).filter_by(user_id=user_id,
                                                               comment_id=comment_id).first()
        # Vote exists                                                             
        if voted_comment:
            if voted_comment.vote != vote:
                voted_comment.vote = vote
                db.flush()
                return {'status' : 'changed'}
            return {'status' : 'unchanged'}
        # Vote doesn't exist
        else:
            voted_comment = UsersCommentsModel(user_id=user_id,
                                               comment_id=comment_id,
                                               vote=vote)
            db.add(voted_comment)
            db.flush()
            return {'status' : 'added'}