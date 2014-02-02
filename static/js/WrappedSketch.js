// TODO: update URLs to new query string format

/*
 * A thin wrapper around sketch.js which allows for text entry and sending over
 * the network.
 *
 * @param canvas The id of the canvas object to use as a sketchpad.
 * @param desc The id of the text object where the sketch description will be
 * entered.
 */
function WrappedSketch(canvas, desc) {
    this.$canvas = $("#" + canvas);
    this.$desc = $("#" + desc);
    this.$canvas.sketch();
}

// The type of the image to convert the sketch to.
WrappedSketch.mimeType = 'image/png';

/* Return to the main menu of the parent panel. */
WrappedSketch.prototype.cancel = function() {
    // Give the user a chance to avoid cancelling.
    if (!confirm("Do ya really wanna leave?")) {
        return;
    }

    // If prevID is set in the query string, return to the previous panel.
    // Otherwise, this was to be the first panel in a comic. Return to the main
    // menu.
    var prevID = $.url().param("prevID");
    var urlID = $.url().param("comID");
    if (prevID) {
        window.location = '/read?panelID=' + prevID
    } else {
        window.location = '/';
    }
}

/* Sends a data URL based on a snapshot of this WrappedSketch to the server. */
WrappedSketch.prototype.sendPanelData = function() {
    var img = this.$canvas[0].toDataURL(WrappedSketch.mimeType);
    var whatIsHappening = this.$desc[0].value;
    var prevID = $.url().param("prevID");
    var situation = decodeURIComponent( $.url().param("situation") );

    // Require description to be non-empty.
    if (!whatIsHappening) {
        alert("Enter a description/choice below!");
        return;
    }

    var data = {
        img: img,
        whatIsHappening: whatIsHappening,
        prevID: prevID,
        situation: situation
    };
    $.ajax({
        type: 'POST',
        url: '/edit',
        data: data
    }).done(function(panelID) {
        // Redirect to the page which holds the newly created panel.
        window.location = '/read?panelID=' + panelID;
    });
}


/* make certain boxes selected or not */
$(document).ready(function(){

    $(".color").click(function(){
        $(".color.selected").removeClass("selected");
        $(this).addClass("selected");
    })

    $(".size").click(function(){
        $(".size.selected").removeClass("selected");
        $(this).addClass("selected");
    })

});









