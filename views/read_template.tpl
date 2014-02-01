<!doctype html>

<head>
  <title>Choose Your Own...</title>
  <link href="../static/css/reset.css" rel="stylesheet" type="text/css">
  <link href="../static/css/comical.css" rel="stylesheet" type="text/css">
</head>

<body>

  <div id="viewer">
    <div id="left-sidebar" class="sidebar">
    % if prevID != None:
      <a class="button" id="prev" href="/read?panelID={{prevID}}"></a>
    % end
    </div>

    <div id="panel-view">
    <img src="{{img}}"/>
    </div>

    <div id="right-sidebar" class="sidebar">
    % if prevID != None:
      <a class="button" id="new" href="/edit?prevID={{prevID}}"></a>
    % end

    % if numChildren == 0:
      <a class="button" id="next" href="/edit?prevID={{panelID}}"></a>
    % elif numChildren == 1:
      <a class="button" id="next" href="/read?panelID={{nextID}}"></a>
    % else:
      <a class="button" id="next" href="/choose?panelID={{panelID}}"></a>
    % end

    </div>
  </div>

</body>

</html>
