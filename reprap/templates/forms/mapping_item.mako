# -*- coding: utf-8 -*-
% if not field.widget.hidden:
<li\
% if field.error and field.widget.error_class:
 class="${field.widget.error_class}"\
% endif
 title="${_(field.description)}" id="item-${field.oid}">
% endif
<!-- mapping_item -->
% if not (field.widget.hidden or field.widget.category=='structural'):
<label class="desc" title="${_(field.description)}" for="${field.oid}">\
${_(field.title)}\
% if field.required:
<span class="req" id="req-${field.oid}">*</span>\
% endif
</label>
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

  <!-- /mapping_item -->
% if not field.widget.hidden:
</li>
% endif
