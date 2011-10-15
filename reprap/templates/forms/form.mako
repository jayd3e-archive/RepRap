# -*- coding: utf-8 -*-
<%
rndr = field.renderer
tmpl = field.widget.item_template
%>
<form \
id="${field.formid}" \
action="${field.action}" \
method="${field.method}" \
enctype="multipart/form-data" \
accept-charset="utf-8" \
% if field.css_class:
 class="${field.css_class}"\
% endif
>

% if field.title:
<legend>${field.title}</legend>
% endif

<input type="hidden" name="_charset_" />
<input type="hidden" name="__formid__" value="${field.formid}"/>
<table cellpadding="0" cellspacing="0">

  % if field.error:
  <tr class="errorLi">
    <h1 class="errorMsgLbl">${"There was a problem with your submission"}</h1>
    <p class="errorMsg">${"Errors have been highlighted below"}</p>
  </tr>
  % endif

  % if field.title:
  <tr class="section first">
    <h3>${field.title}</h3>
    % if field.description:
    <div>${field.description}</div>
    % endif
  </tr>
  % endif

  % for f in field.children:
    ${rndr(tmpl, field=f, cstruct=cstruct.get(f.name, null))}
  % endfor

  <tr class="buttons">
    % for button in field.buttons:
      <td>
      <button
          id="${field.formid+button.name}"
          name="${button.name}"
          type="${button.type}"
          class="btnText submit"
          value="${button.value}"
          % if button.disabled:
           disabled="disabled"
          % endif
          >
        <span>${button.title}</span>
      </button
      </td>
    % endfor
  </tr>

</table>

% if field.use_ajax:
<script type="text/javascript">
  deform.addCallback(
     '${field.formid}',
     function(oid) {
         var options = {
           target: '#' + oid,
           replaceTarget: true,
         };
         var extra_options = ${field.ajax_options};
         var name;
         if (extra_options) {
           for (name in extra_options) {
             options[name] = extra_options[name];
           };
         };
         $('#' + oid).ajaxForm(options);
   });
</script>
% endif

</form>
