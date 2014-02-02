<!doctype html>

<head>
  <title>Choose Your Own...</title>
  <link rel="shortcut icon" href="/static/img/chooseyourown.ico" />
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
          <input id="situation-entry" type="text" name="new-situation" 
           size="25" maxlength="40">
          <hr>
        </form>
        <div id="situation-create" class="button" onclick="newComic()">Create</div>
      </div>
      
      <div id="start-wrapper">
        % for (panelID,sit) in comicList:
        <a class="choice" href="/read?panelID={{panelID}}">{{sit}}</a>
        % end
      </div>

    </div>
  </div>

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
