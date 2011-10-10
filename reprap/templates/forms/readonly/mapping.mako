# -*- coding: utf-8 -*-
<%
rndr = field.renderer
tmpl = field.widget.readonly_item_template
%>
<div class="deformMappingFieldset">
  <!-- mapping -->
  % if field.title:
  <p>${field.title}</p>
  % endif
  <ul class="readonly">
    % if field.description:
    <li class="section">
      <div>${field.description}</div>
    </li>
    % endif
    % for f in field.children:
    ${rndr(tmpl, field=f, cstruct=cstruct.get(f.name, null))}
    % endfor
  </ul>
  <!-- /mapping -->
</div>
