# -*- coding: utf-8 -*-
<textarea
    % if field.widget.rows:
    rows="${field.widget.rows}"
    % endif
    % if field.widget.cols:
    cols="${field.widget.cols}"
    % endif
    % if field.widget.css_class:
    class="${field.widget.css_class}"
    % endif
    id="${field.oid}"
    name="${field.name}">${cstruct}</textarea>
