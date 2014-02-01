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

// This will be prepended to ids to get the path to POST to.
WrappedSketch.newPanelPathPrefix = '/edit/';

// The type of the image to convert the sketch to.
WrappedSketch.mimeType = 'image/png';

/* Sends a data URL based on a snapshot of this WrappedSketch to the server. */
WrappedSketch.prototype.sendPanelData = function(onSuccess, onFailure) {
    var url = document.URL;
    var prevId = url.slice(url.lastIndexOf('/') + 1);
    var image = this.$canvas[0].toDataURL(WrappedSketch.mimeType);
    var whatsHappening = this.$desc[0].value;
    var data = {
        image: image,
        whatsHappening: whatsHappening
    };
    $.ajax({
        type: 'POST',
        url: WrappedSketch.newPanelPathPrefix + prevId,
        data: data
    }).done(onSuccess).fail(onFailure);
}
