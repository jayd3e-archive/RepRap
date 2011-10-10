<%inherit file="../layouts/base.mako"/>

<%def name="body()">
    <div class="content_column">
        <h1>Add Issue</h1>
        ${form | n}
    </div>
    <div class="action_column">
        <h1>Actions</h1>
        <a href="/issues/add">Add Issue</a>
    </div>
</%def>