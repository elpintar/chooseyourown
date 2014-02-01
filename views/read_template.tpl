<!doctype html>

<head>
  <title>Choose Your Own...</title>
  <link href="../static/css/reset.css" rel="stylesheet" type="text/css">
  <link href="../static/css/comical.css" rel="stylesheet" type="text/css">
</head>

<body>

  <div id="viewer">
    <div id="left-sidebar" class="sidebar">
      <a class="button" id="prev" href="{{prevLink}}"></a>
    </div>

    <div id="panel-view">
    <img src="{{img}}"/>
    </div>

    <div id="right-sidebar" class="sidebar">
      <a class="button" id="new"></a>
      <a class="button" id="next" href="{{nextLink}}"></a>
    </div>
  </div>

</body>

</html>
