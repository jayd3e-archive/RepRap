# -*- coding: utf-8 -*-
<div>
  % for index, choice in enumerate(field.widget.values):
      <span>${choice.description}</span>
        <em id="${field.oid}-${index}">
          % if choice.value in cstruct:
            Yes
          % else:
            No
          % endif
        </em>
  % endfor
</div>

