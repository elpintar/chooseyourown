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
    // menu, and delete that comic.
    var prevID = $.url().param("prevID");
    var urlID = $.url().param("comID");
    if (prevID) {
        window.location = '/read/' + prevID
    } else {
        var data = {
            comID: comID
        };
        $.ajax({
            type: 'DELETE',
            url: '/',
            data: data
        });
        window.location = '/';
    }
}

/* Sends a data URL based on a snapshot of this WrappedSketch to the server. */
WrappedSketch.prototype.sendPanelData = function() {
    var img = this.$canvas[0].toDataURL(WrappedSketch.mimeType);
    var whatsHappening = this.$desc[0].value;
    var prevID = $.url().param("prevID");
    var comID = $.url().param("comID");

    // Require description to be non-empty.
    if (!whatsHappening) {
        alert("Entery a description!");
        return;
    }

    var data = {
        img: img,
        whatsHappening: whatsHappening,
        prevID: prevID,
        comID: comID
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
