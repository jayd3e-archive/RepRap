<%inherit file="../layouts/base.mako"/>

<%def name="body()">
    <div class="content_column">
        <h1>ADD ISSUE</h1>
        ${form | n}
    </div>
    <div class="action_column">
        <h1>ACTIONS</h1>
        <a href="/issues/add">Add Issue</a>
    </div>
</%def>