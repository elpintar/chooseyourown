<!doctype html>

<head>
  <title>Choose Your Own...</title>
  <link href="static/css/reset.css" rel="stylesheet" type="text/css">
  <link href="static/css/comical.css" rel="stylesheet" type="text/css">
</head>

<body>

  <div id="viewer">
    <div id="left-sidebar" class="sidebar">
      <a class="button" id="prev"></a>
    </div>

    <div id="panel-view">
      <div id="question-wrapper">
        <div>{{questionText}}</div>
        <div>Choose Your Own...</div>
      </div>
      <div id="choices-wrapper">
	{{choiceList}}
        <a class="choice" id="somethingElse">{{newComicText}}</a>
      </div>
    </div>

    <div id="right-sidebar" class="sidebar">
    </div>
  </div>

</body>

</html>
