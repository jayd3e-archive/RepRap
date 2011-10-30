<%inherit file="../layouts/base.mako"/>

<%def name="body()">
    <div class="left_column">
        <h1>RECENTLY ADD ISSUES</h1>
        % for issue in recent_issues:
            <div class="issue_small_descrip">
                <a href="/issues/view/${issue.id}"><h2>${issue.title}</h2></a>
                <div class="thumbnails">
                % for image in issue.images:
                    <a href="/issues/view/${issue.id}">
                        <img width="50" 
                            height="50" 
                            class="issue_thumbnail" 
                            src="/static/img/issue_images/${image.directory}/thumbnail.jpeg" />
                    </a>
                % endfor
                </div>
                <p>${issue.description}</p>
            </div>
        % endfor
    </div>
    <div class="right_column">
        <h1>RECENTLY SOLVED ISSUES</h1>
        % for issue in recent_solved_issues:
            <div class="issue_small_descrip">
                <h2>${issue.title}</h2>
                % for image in issue.images:
                    <img width="50" 
                        height="50" 
                        class="issue_thumbnail" 
                        src="/static/img/issue_images/${image.directory}/thumbnail.jpeg" />
                % endfor
                <p>${issue.description}</p>
            </div>
        % endfor
    </div>
    <div class="action_column">
        <h1>ACTIONS</h1>
        <a href="/issues/add">Add Issue</a>
    </div>
</%def>