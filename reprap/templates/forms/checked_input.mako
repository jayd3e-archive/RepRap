# -*- coding: utf-8 -*-
<input type="hidden" name="__start__" value="${field.name}:mapping"/>
<ul>
  <li>
    <label for="${field.oid}">${subject}</label>
    <input type="text" name="value" value="${cstruct}"
        % if field.widget.size:
        size="${field.widget.size}"
        % endif
        % if field.widget.css_class:
        class="${field.widget.css_class}"
        % endif
        id="${field.oid}"/>
  </li>

  <li>
    <label for="${field.oid}-confirm">${confirm_subject}</label>
    <input type="text" name="confirm" value="${confirm}"
        % if field.widget.size:
        size="${field.widget.size}"
        % endif
        % if field.widget.css_class:
        class="${field.widget.css_class}"
        % endif
        id="${field.oid}-confirm"/>
  </li>
</ul>
  % if field.widget.mask:
  <script type="text/javascript">
    deform.addCallback(
        '${field.oid}',
        function (oid) {
           $("#" + oid).mask("${field.widget.mask}",
                              {placeholder:"${field.widget.mask_placeholder}"});
           $("#" + oid + "-confirm").mask("${field.widget.mask}",
                              {placeholder:"${field.widget.mask_placeholder}"});
        }
        );

  </script>
  % endif

<input type="hidden" name="__end__" value="${field.name}:mapping"/>
