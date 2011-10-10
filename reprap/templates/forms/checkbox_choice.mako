# -*- coding: utf-8 -*-
<input type="hidden" name="__start__" value="${field.name}:sequence"/>
  <ul class="deformSet">
    % for (index, (value, title)) in enumerate(field.widget.values):
    <li class="deformSet-item">
      <input
        % if value in cstruct:
        checked="True"
        % endif
        % if field.widget.css_class:
        class="${field.widget.css_class}"
        % endif
        type="checkbox"
        name="checkbox"
        value="${value}"
        id="${field.oid}-${index}"/>
      <label for="${field.oid}-${index}">${title}</label>
    </li>
    % endfor
  </ul>
<input type="hidden" name="__end__" value="${field.name}:sequence"/>

