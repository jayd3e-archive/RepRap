# -*- coding: utf-8 -*-
% for value, description in field.widget.values:
<p>
  <span>${description}</span>
  <em>
  % if value == cstruct:
  Selected
  % else:
  Not Selected
  % endif
  </em>
</p>
% endfor
