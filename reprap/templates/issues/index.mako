<%inherit file="../layouts/base.mako"/>

<%def name="body()">
    <div class="left_column">
        <h1>Recently Added Issues</h1>
    </div>
    <div class="right_column">
        <h1>Recently Solved Issues</h1>
    </div>
    <div class="action_column">
        <h1>Actions</h1>
        <a href="/issues/add">Add Issue</a>
    </div>
</%def>