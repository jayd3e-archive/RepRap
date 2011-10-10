# -*- coding: utf-8 -*-
<textarea class="tinymce"
          id="${field.oid}"
          name="${field.name}">${cstruct}</textarea>
<script language="javascript"
	type="text/javascript">
  tinyMCE.init({
    height: '${field.widget.height}',
    mode : 'textareas',
    readonly : 1,
    theme : '${field.widget.theme}',
    theme_advanced_resizing : true,
    theme_advanced_toolbar_align : 'left',
    theme_advanced_toolbar_location : 'top',
    width: '${field.widget.width}'
  });
</script>
