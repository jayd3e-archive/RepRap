# -*- coding: utf-8 -*-
<div class="deformFileupload">

  <input type="hidden" name="__start__" value="${field.name}:mapping"/>

  % if cstruct.get('uid'):
  <div class="deformReplaces">
    <input type="hidden" name="uid" value="${cstruct['uid']}"
           id="${field.oid}-uid"/>
    <span id="${field.oid}-filename">
    ${cstruct.get('filename')}
    </span>
  </div>
  % endif

  <input type="file" name="upload"
         % if field.widget.size:
         size="${field.widget.size}"
         % endif
         % if field.widget.css_class:
         class="${field.widget.css_class}"
         % endif
         id="${field.oid}"/>

  <input type="hidden" name="__end__" value="${field.name}:mapping"/>

</div>
