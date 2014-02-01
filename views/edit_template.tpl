<!DOCTYPE HTML>
<html>
<head>
  <title>Choose Your Own...</title>
  <link href="static/css/reset.css" rel="stylesheet" type="text/css">
  <link href="static/css/comical.css" rel="stylesheet" type="text/css">
  <script src="jquery-2.0.2.min.js"></script>
  <script src="sketch.js"></script>
  <script src="WrappedSketch.js"></script>
</head>

<body>

  <div id="viewer">
    <div id="left-sidebar" class="sidebar">
      <a class="color button" id="black" href="#panel-canvas" data-color="#000"></a>
      <a class="color button" id="gray" href="#panel-canvas" data-color="#888"></a>
      <a class="color button" id="red" href="#panel-canvas" data-color="#f00"></a>
      <a class="color button" id="yellow" href="#panel-canvas" data-color="#ff0"></a>
      <a class="color button" id="green" href="#panel-canvas" data-color="#0f0"></a>
      <a class="color button" id="blue" href="#panel-canvas" data-color="#00f"></a>
      <a class="color button" id="brown" href="#panel-canvas" data-color="#842"></a>
    </div>

    <div id="panel-view">
      <canvas id="panel-canvas" width="480" height="360" />
      <input id="panel-desc" type="text" />
    </div>

    <div id="right-sidebar" class="sidebar">
      <a class="size button" id="tiny" href="#panel-canvas" data-size="1"></a>
      <a class="size button" id="little" href="#panel-canvas" data-size="3"></a>
      <a class="size button" id="med" href="#panel-canvas" data-size="5"></a>
      <a class="size button" id="big" href="#panel-canvas" data-size="10"></a>
      <a class="size button" id="huge" href="#panel-canvas" data-size="15"></a>
      <a class="button" id="cancel" href="{{prevLink}}"></a> <!-- TODO: is this the right syntax? also, this is sort of redundant with sending prevId in the URL -->
      <a class="button" id="submit" onclick="ws.sendPanelData()"></a>
    </div>
  </div>

  <script>
    var ws;
    $(document).ready(function() {
      ws = new WrappedSketch("panel-canvas", "panel-desc");
    });
  </script>
</body>

</html>
