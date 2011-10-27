from colander import MappingSchema
from colander import SequenceSchema
from colander import SchemaNode
from colander import String
from colander import Boolean
from colander import Integer
from colander import Length
from colander import OneOf
from deform.widget import TextInputWidget
from reprap.forms.validators import commaSpaceSeparatedListFactory

class AddTagSchema(MappingSchema):
    tags = SchemaNode(String(),
                      description="Tags",
                      widget=TextInputWidget(css_class="tag_add_textinput"),
                      validator=commaSpaceSeparatedListFactory(1))