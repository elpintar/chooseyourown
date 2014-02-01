/*
 * Creates a new comic, and navigates to an edit view for that comic's first
 * panel.
 */
function newComic() {
    var situation = document.getElementById("situation-entry").value;

    // Require situation to be non-empty.
    if (!situation) {
        alert("Enter a situation!");
        return;
    }

    var data = {
        situation: situation
    };
    $.ajax({
        type: 'POST',
        url: '/',
        data: data
    }).done(function(comID) {
        window.location = '/edit?comicID=' + comID;
    });
}
