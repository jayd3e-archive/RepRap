# -*- coding: utf-8 -*-
<%
rndr = field.renderer
tmpl = field.widget.readonly_item_template
%>
<div class="deform"\
% if field.name or None:
 id="${field.name or None}"\
% endif
>

  <div class="deformFormFieldset">
      % if field.title:
      <li class="section first">
        <h3>${field.title}</h3>
        % if field.description:
        <div>${field.description}</div>
        % endif
      </li>
      % endif

  </div>

  % for f in field.children:
  ${rndr(tmpl, field=f, cstruct=cstruct.get(f.name, null))}
  % endfor
</div>
