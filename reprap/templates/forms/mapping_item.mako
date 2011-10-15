# -*- coding: utf-8 -*-
% if not field.widget.hidden:
<tr\
% if field.error and field.widget.error_class:
 class="${field.widget.error_class}"\
% endif
 title="${field.description}" id="item-${field.oid}">
% endif
<!-- mapping_item -->
% if not (field.widget.hidden or field.widget.category=='structural'):
<th class="desc" title="${field.description}" for="${field.oid}">\
${field.title}\
% if field.required:
<span class="req" id="req-${field.oid}">*</span>\
% endif
</th>
% endif

  <td>
    ${field.serialize(cstruct)}
  </td>

<!-- /mapping_item -->
% if not field.widget.hidden:
</tr>
% endif

<tr>
  <td colspan="2">
    % if field.error and not field.widget.hidden:
      % for index, msg in enumerate(field.error.messages()):
        <%
          errstr = 'error-%s' % field.oid
          pid = (index==0 and errstr) or ('%s-%s' % (errstr, index))
        %>
        <p id="${pid}" class="${field.widget.error_class}">${msg}</p>
      % endfor
    % endif
  </td>
</tr>