<!doctype html>

<head>
  <title>Choose Your Own...</title>
<<<<<<< HEAD
  <link rel="shortcut icon" href="/static/img/chooseyourown.ico" />
  <link href="../static/css/reset.css" rel="stylesheet" type="text/css">
  <link href="../static/css/comical.css" rel="stylesheet" type="text/css">
=======
  <link href="/static/css/reset.css" rel="stylesheet" type="text/css">
  <link href="/static/css/comical.css" rel="stylesheet" type="text/css">
>>>>>>> 8031e52540a3e71eed1858a07b9ffbc6fc4af4a8
</head>

<body>

  <!-- Enable Facebook like button -->
  <div id="fb-root"></div>
  <script>(function(d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
    js = d.createElement(s); js.id = id;
    js.src = "//connect.facebook.net/en_US/all.js#xfbml=1";
    fjs.parentNode.insertBefore(js, fjs);
  }(document, 'script', 'facebook-jssdk'));</script>

  <div id="viewer">
    <div id="left-sidebar" class="sidebar">
      % if len(children) != 0:
      <a class="button" id="home" href="/"></a>
      % else:
      <a class="button hidden" id="home" href="/"></a>
      % end
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
          Continue Story?
        </a>
        <a class="choice" href="/">
          Back to Menu
        </a>

        % else:
        <a class="choice" href="/edit?prevID={{panelID}}">
          Or something else...
        </a>
        % end

        % if len(children) == 0:
            <div class="fb-share-button" data-href="http://chooseyourown.herokuapp.com/read?panelID={{panelID}}" data-type="button_count"></div>
        % end
      </div>
    </div>

    <div id="right-sidebar" class="sidebar">
    </div>
  </div>

</body>

</html>
