from colander import MappingSchema
from colander import SequenceSchema
from colander import SchemaNode
from colander import String
from colander import Boolean
from colander import Integer
from colander import Length
from colander import OneOf
from deform.widget import TextAreaWidget

class AddIssueCommentSchema(MappingSchema):
    body = SchemaNode(String(),
                      description="Issue Comment",
                      widget=TextAreaWidget(css_class="issue_comment_add_textarea"))