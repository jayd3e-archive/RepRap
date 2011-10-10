from colander import MappingSchema
from colander import SequenceSchema
from colander import SchemaNode
from colander import String
from colander import Boolean
from colander import Integer
from colander import Length
from colander import OneOf
import colander
from deform.widget import TextAreaWidget
from deform.widget import FileUploadWidget
from deform import FileData

class MemoryTmpStore(dict):
    def preview_url(self, name):
        return None

store = MemoryTmpStore()

class AddIssueSchema(MappingSchema):
    file = SchemaNode(FileData(),
                      description = "Issue Image",
                      widget=FileUploadWidget(store))
    title = SchemaNode(String(),
                       description = "Issue Tittle")
    description = SchemaNode(String(),
                             description = "Issue Description",
                             widget=TextAreaWidget())
    tags = SchemaNode(String(),
                      description = "Issue Tags")