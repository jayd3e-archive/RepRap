# -*- coding: utf-8 -*-
<ul>
% for value, description in field.widget.values:
<li>
  <span>${description}</span>
  <em>
  % if value == cstruct:
  Selected
  % else:
  Not Selected
  % endif
  </em>
</li>
% endfor
</ul>
