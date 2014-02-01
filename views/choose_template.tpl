<!doctype html>

<head>
  <title>Choose Your Own...</title>
  <link rel="shortcut icon" href="/static/img/chooseyourown.ico" />
  <link href="../static/css/reset.css" rel="stylesheet" type="text/css">
  <link href="../static/css/comical.css" rel="stylesheet" type="text/css">
</head>

<body>

  <div id="viewer">
    <div id="left-sidebar" class="sidebar">
      <a class="button" id="home" href="/"></a>
      <a class="button" id="prev" href="/read?panelID={{panelID}}"></a>
    </div>

    <div id="panel-view">
      <div id="question-wrapper">
        % if len(children) == 0:
        <div>The End</div>
        % else:
        <div>What happens next?</div>
        % end
      </div>
      <div id="choices-wrapper">
        % for (chID,text) in children:
        <a class="choice" href="/read?panelID={{chID}}">{{text}}</a>
        % end
        % if len(children) == 0:
        <a class="choice" href="/edit?prevID={{panelID}}">
          Continue?
        </a>
        % else:
        <a class="choice" href="/edit?prevID={{panelID}}">
          Or something else...
        </a>
        % end
      </div>
    </div>

    <div id="right-sidebar" class="sidebar">
    </div>
  </div>

</body>

</html>
