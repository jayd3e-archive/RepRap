# -*- coding: utf-8 -*-
% if not (field.widget.hidden or field.widget.category == 'structural'):
<li title="${field.description}">
  <!-- mapping_item -->
  % if not (field.widget.hidden or field.widget.category == 'structural'):
  <p class="desc"
     title="${field.description}"
     >${field.title}</p>
  % endif
  ${field.serialize(cstruct, readonly=True)}
  <!-- /mapping_item -->
</li>
% endif
