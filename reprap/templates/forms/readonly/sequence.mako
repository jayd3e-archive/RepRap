# -*- coding: utf-8 -*-
<%
rndr = field.renderer
tmpl = field.widget.readonly_item_template
%>
<div class="deformSeq readonly">
  <!-- sequence -->
  % for tup in subfields:
  ${rndr(tmpl, field=tup[1], cstruct=tup[0])}
  % endfor
  <!-- /sequence -->
</div>
