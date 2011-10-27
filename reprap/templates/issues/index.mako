<%inherit file="../layouts/base.mako"/>

<%def name="body()">
    <div class="left_column">
        <h1>Recently Added Issues</h1>
        % for issue in recent_issues:
            <a href="/issues/view/${issue.id}"><h2>${issue.title}</h2></a>
            % for image in issue.images:
                <a href="/issues/view/${issue.id}">
                    <img width="50" 
                        height="50" 
                        class="issue_thumbnail" 
                        src="/static/img/issue_images/${image.directory}/thumbnail.jpeg" />
                </a>
            % endfor
            <p>${issue.description}</p>
        % endfor
    </div>
    <div class="right_column">
        <h1>Recently Solved Issues</h1>
        % for issue in recent_solved_issues:
            <h2>${issue.title}</h2>
            % for image in issue.images:
                <img width="50" 
                    height="50" 
                    class="issue_thumbnail" 
                    src="/static/img/issue_images/${image.directory}/thumbnail.jpeg" />
            % endfor
            <p>${issue.description}</p>
        % endfor
    </div>
    <div class="action_column">
        <h1>Actions</h1>
        <a href="/issues/add">Add Issue</a>
    </div>
</%def>