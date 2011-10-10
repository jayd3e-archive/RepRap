# -*- coding: utf-8 -*-
<input type="hidden" name="__start__" value="${field.name}:mapping"/>
<ul class="inline">
  <li>
	  <label for="${field.oid}">Year</label>
	  <input type="text" name="year" value="${year}"
		% if field.widget.size:
		size="${field.widget.size}"
		% endif
		% if field.widget.css_class:
		class="${field.widget.css_class}"
		% endif
                id="${field.oid}"/>
  </li>
  <li>
	  <label for="${field.oid}-month">Month</label>
	  <input type="text" name="month" value="${month}"
		% if field.widget.size:
		size="${field.widget.size}"
		% endif
		% if field.widget.css_class:
		class="${field.widget.css_class}"
		% endif
                id="${field.oid}-month"/>
  </li>
  <li>
	  <label for="${field.oid}-day">Day</label>
	  <input type="text" name="day" value="${day}"
		% if field.widget.size:
		size="${field.widget.size}"
		% endif
		% if field.widget.css_class:
		class="${field.widget.css_class}"
		% endif
                id="${field.oid}-day"/>
  </li>
</ul>
<input type="hidden" name="__end__" value="${field.name}:mapping"/>
