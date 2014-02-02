<!DOCTYPE HTML>
<html>
<head>
  <title>Edit Your Own...</title>
  <link rel="shortcut icon" href="/static/img/chooseyourown.ico" />
  <link href="../static/css/reset.css" rel="stylesheet" type="text/css">
  <link href="../static/css/comical.css" rel="stylesheet" type="text/css">
  <script src="../static/js/jquery-2.0.2.min.js"></script>
  <script src="../static/js/purl.js"></script>
  <script src="../static/js/sketch.js"></script>
  <script src="../static/js/WrappedSketch.js"></script>
</head>

<body>

  <div id="viewer">
    <div id="left-sidebar" class="sidebar">
      <a class="color button selected" id="black" href="#panel-canvas" data-color="#000"></a>
      <a class="color button" id="red" href="#panel-canvas" data-color="#f00"></a>
      <a class="color button" id="yellow" href="#panel-canvas" data-color="#ff0"></a>
      <a class="color button" id="green" href="#panel-canvas" data-color="#0f0"></a>
      <a class="color button" id="blue" href="#panel-canvas" data-color="#00f"></a>
      <a class="color button" id="brown" href="#panel-canvas" data-color="#842"></a>
      <a class="color button" id="white" href="#panel-canvas" data-color="#fff"></a>
    </div>

    <div id="panel-view">
      <canvas id="panel-canvas" width="480" height="360"> </canvas>
      <input id="panel-desc" type="text" maxlength="40" size="40"
       placeholder="Description">
    </div>

    <div id="right-sidebar" class="sidebar">
      <a class="size button" id="tiny" href="#panel-canvas" data-size="1"></a>
      <a class="size button" id="little" href="#panel-canvas" data-size="3"></a>
      <a class="size button selected" id="med" href="#panel-canvas" data-size="5"></a>
      <a class="size button" id="big" href="#panel-canvas" data-size="15"></a>
      <a class="size button" id="huge" href="#panel-canvas" data-size="50"></a>
      <a class="button" id="cancel" onclick="ws.cancel()"></a> <!-- TODO: is this the right syntax? also, this is sort of redundant with sending prevId in the URL -->
      <a class="button" id="submit" onclick="ws.sendPanelData()"></a>
    </div>
  </div>

  <script>
    var ws;
    $(document).ready(function() {
      ws = new WrappedSketch("panel-canvas", "panel-desc");
    });
  </script>

  <script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-47695999-1', 'chooseyourown.herokuapp.com');
  ga('send', 'pageview');

  </script>
</body>

</html>
