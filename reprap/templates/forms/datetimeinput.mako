# -*- coding: utf-8 -*-
<input type="text"\
 name="${field.name}"\
 value="${cstruct}"\
% if field.widget.size:
 size="${field.widget.size}"\
% endif
% if field.widget.css_class:
 class="${field.widget.css_class}"\
% endif
 id="${field.oid}"/>
<script type="text/javascript">
  deform.addCallback(
    '${field.oid}',
    function(oid) {
        $('#' + oid).datetimepicker(${options});
    }
  );
</script>
