from colander import MappingSchema
from colander import SequenceSchema
from colander import SchemaNode
from colander import String
from colander import Boolean
from colander import Integer
from colander import Length
from colander import OneOf
from deform.widget import TextInputWidget
from deform.widget import TextAreaWidget
from deform.widget import FileUploadWidget
from deform import FileData
from reprap.forms.validators import commaSpaceSeparatedListFactory

class MemoryTmpStore(dict):
    def preview_url(self, name):
        return None

store = MemoryTmpStore()

#Schemas
class ImageSequence(SequenceSchema):
            image = SchemaNode(FileData(),
                               description="Issue Image",
                               widget=FileUploadWidget(store, size=77))

class AddIssueSchema(MappingSchema):
    images = ImageSequence()
    title = SchemaNode(String(),
                       description="Issue Tittle",
                       widget=TextInputWidget(css_class="issue_add_textinput"))
    description = SchemaNode(String(),
                             description="Issue Description",
                             widget=TextAreaWidget(css_class="issue_add_textarea"))
    tags = SchemaNode(String(),
                      description="Issue Tags",
                      widget=TextInputWidget(css_class = "issue_add_textinput"),
                      validator=commaSpaceSeparatedListFactory(3))