<%inherit file="../layouts/base.mako"/>

<%def name="body()">
    <div class="content_column">
        <h1>View Issue</h1>
        <div class="image_gallery">
            <div class="image_slide">
            % for image in images:
                <div class="image">
                    <img src="/static/img/issue_images/${image.directory}/tile.jpeg" />
                </div>
            % endfor
            </div>
            <div class="left_arrow" onClick="javascript: slide(this, 'left');">
            </div>
            <div class="right_arrow" onClick="javascript: slide(this, 'right');">
            </div>
        </div>
    </div>
    <div class="action_column">
        <h1>Actions</h1>
        <a href="/issues/add">Add Issue</a>
    </div>
</%def>