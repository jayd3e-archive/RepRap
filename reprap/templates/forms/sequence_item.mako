# -*- coding: utf-8 -*-
% if not field.widget.hidden:
<li\
% if field.error and field.widget.error_class:
 class="${field.widget.error_class}"\
% endif
 title="${field.description}">
% endif
<!-- sequence_item -->
  % if not field.widget.hidden:
  <span class="deformClosebutton" id="${field.oid}-close" title="Remove" onclick="javascript:deform.removeSequenceItem(this);"></span>
  % endif
  ${field.serialize(cstruct)}
  % if field.error and not field.widget.hidden:
  % for index, msg in enumerate(field.error.messages()):
<%
errstr = 'error-%s' % field.oid
pid = (index==0 and errstr) or ('%s-%s' % (errstr, index))
%>
  <p id="${pid}" class="${field.widget.error_class}">${_(msg)}</p>
  % endfor
  % endif

  <!-- /sequence_item -->
% if not field.widget.hidden:
</li>
% endif