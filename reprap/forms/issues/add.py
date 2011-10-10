from colander import MappingSchema
from colander import SequenceSchema
from colander import SchemaNode
from colander import String
from colander import Boolean
from colander import Integer
from colander import Length
from colander import OneOf

class AddIssueSchema(MappingSchema):
    name = SchemaNode(String(),
                      description = "Add Issue Description")