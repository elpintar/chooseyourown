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

    // go to edit passing the situation
    window.location = '/edit?situation=' + encodeURIComponent(situation);
}
