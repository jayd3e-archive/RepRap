# -*- coding: utf-8 -*-
<%
rndr = field.renderer
tmpl = field.widget.item_template
item_tmpl = field.widget.item_template
min_len = field.widget.min_len or 0
max_len = field.widget.max_len or 100000
now_len = len(subfields)
prototype = field.widget.prototype(field)
%>

<div class="deformSeq" id="${field.oid}">
<!-- sequence -->
<input type="hidden" name="__start__" value="${field.name}:sequence" class="deformProto" prototype="${prototype}" />
<ul>
% for c, f in subfields:
${rndr(item_tmpl, field=f, cstruct=c, parent=field)}
% endfor

<span class="deformInsertBefore"\
% if min_len:
 min_len="${min_len}"\
% endif
% if max_len:
 max_len="${max_len}"\
% endif
% if now_len:
 now_len="${now_len}"\
% endif
></span>
</ul>

<a href="#" class="deformSeqAdd" id="${field.oid}-seqAdd" onclick="javascript: return deform.appendSequenceItem(this);">\
<small id="${field.oid}-addtext">${_(add_subitem_text)}</small>\
</a>

<script type="text/javascript">
   deform.addCallback(
     '${field.oid}',
     function(oid) {
       oid_node = $('#'+ oid);
       deform.processSequenceButtons(oid_node, ${min_len},
                                     ${max_len}, ${now_len});
     }
   )
</script>
<input type="hidden" name="__end__" value="${field.name}:sequence"/>
<!-- /sequence -->
</div>
