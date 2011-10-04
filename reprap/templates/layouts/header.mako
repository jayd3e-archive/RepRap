<%def name="header(here)">
    <a href="/">
        <div class="logo">
        </div>
    </a>
    <ul class="main_nav">
        <li class="arrow0">
            <div class="main">
                <a 
                ${' class="active" ' if '/wiki' in here else '' | n}
                href="#">1. Read the Wiki</a>
            </div>
        </li>
        <li class="arrow0">
            <div class="separator">
            </div>
        </li>
        <li class="arrow1">
            <div class="main">
                <a 
                ${' class="active" ' if '/parts' in here else '' | n}
                href="#">2. Buy the Parts</a>
            </div>
        </li>
        <li class="arrow1">
            <div class="separator">
            </div>
        </li>
        <li class="arrow2">
            <div class="main">
                <a 
                ${' class="active" ' if '/issues' in here else '' | n}
                href="#">3. Fix Issues</a>
            </div>
        </li>
        <li class="arrow2">
            <div class="separator">
            </div>
        </li>
    </ul>
    <div class="search">
        <form>    
            <input class="search" type="text"></input>
        </form>
    </div>
    <div class="account">
        <a>jayd3e - logout</a>
    </div>
</%def>