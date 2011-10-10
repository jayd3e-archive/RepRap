# -*- coding: utf-8 -*-
  <input type="text"
         name="${field.name}"
         value="${cstruct}"
         % if field.widget.size:
         size="${field.widget.size}"
         % endif
         % if field.widget.css_class:
         class="${field.widget.css_class}"
         % endif
         id="${field.oid}"/>
  % if field.widget.values:
  <script type="text/javascript">
    deform.addCallback(
      '${field.oid}',
      function (oid) {
          $('#' + oid).autocomplete({source: ${values}});
          $('#' + oid).autocomplete("option", ${options});
      }
    );
  </script>
  % endif
