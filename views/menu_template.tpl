<!doctype html>

<head>
  <title>Choose Your Own...</title>
  <link href="../static/css/reset.css" rel="stylesheet" type="text/css">
  <link href="../static/css/comical.css" rel="stylesheet" type="text/css">
  <script src="../static/js/jquery-2.0.2.min.js"></script>
  <script src="../static/js/mainMenu.js"></script>
</head>

<body>
  <div id="viewer">

    <div id="main-view">
      <h1 id="title">
        <div>Choose Your Own...</div>
      </h1>
      <h3>
        Once upon a time, there was a
      </h3>
  
      <div id="create-area">
        <form>
          <hr>
          <input id="situation-entry" type="text" name="new-situation" size="30">
          <hr>
        </form>
        <div id="situation-create" class="button" onclick="newComic()">Create</div>
      </div>
      
      <div id="start-wrapper">
        <a class="start">boy looking for revenge...</a>
        <a class="start">squirrel and a unicorn...</a>
        <a class="start">asteroid hurtling toward Earth...</a>
        <a class="start">dangerous criminal on the loose...</a>
        <a class="start">boy and his tiger...</a>
      </div>

    </div>
  </div>

</body>

</html>