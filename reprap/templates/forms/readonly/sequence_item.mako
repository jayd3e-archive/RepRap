# -*- coding: utf-8 -*-
% if not field.widget.hidden:
<li title="${field.description}">
% endif
  <!-- sequence_item -->
  ${field.serialize(cstruct, readonly=True)}
  <!-- /sequence_item -->
% if not field.widget.hidden:
</li>
% endif
