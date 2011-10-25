from pyramid.view import view_config
from reprap.models.users_comments import UsersCommentsModel
from reprap.models.issue_comments import IssueCommentsModel

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
        
        db = self.request.db
        comment = db.query(IssueCommentsModel).filter_by(id=comment_id).first()
        if vote=='up':
            vote = 1
        elif vote=='down':
            vote = -1
        else:
            return {'status' : 'unchanged', 'score' : comment.score}
        
        voted_comment = db.query(UsersCommentsModel).filter_by(user_id=user_id,
                                                               comment_id=comment_id).first()
        # Vote exists                                                             
        if voted_comment:
            if voted_comment.vote != vote:
                voted_comment.vote = vote
                db.flush()
                status = 'changed'
            else:
                db.delete(voted_comment)
                db.flush()
                status = 'deleted'
                
        # Vote doesn't exist
        else:
            voted_comment = UsersCommentsModel(user_id=user_id,
                                               comment_id=comment_id,
                                               vote=vote)
            db.add(voted_comment)
            db.flush()
            status = 'added'
        
        score = self.calculateScore(comment)
        comment.score = score
        db.flush()
        return {'status' : status, 'score' : score}
        
    def calculateScore(self, comment):
        score = 0
        for users_comments in comment.users_comments:
            score += users_comments.vote
        return score