function togglePhoto(version) {
    document.getElementById("headline-photo").src = "/assets/img/SeatedPortrait" + version + ".jpg"
}

//For Bio Selector
//Also yes, this is an inline script
// I store all of my spaghetti in my personal website.
var options = ["short", "long", "guest"]
var colors = ["secondary", "info", "primary"]

function activate(bio) {
    var activeBio = document.getElementById(bio + "-bio")
    var activeBioButton = document.getElementById(bio + "-bio-button")
    activeBio.hidden = false
    activeBioButton.classList = "btn btn-lg btn-block disabled btn-" + colors[options.indexOf(bio)]
    options.forEach((opt) => {
        if (opt != bio) {
            deactivate(opt)
        }
    })
}

function deactivate(bio) {
    var inactiveBio = document.getElementById(bio + "-bio")
    var inactiveBioButton = document.getElementById(bio + "-bio-button")
    inactiveBio.hidden = true
    inactiveBioButton.classList = "btn btn-lg btn-block btn-outline-" + colors[options.indexOf(bio)]
}

window.onload = function () {
    document.getElementById("photo-toggle-1").addEventListener("click", function () {
        togglePhoto("Cropped")
    });
    document.getElementById("photo-toggle-2").addEventListener("click", function () {
        togglePhoto("Painted")
    });
    document.getElementById("photo-toggle-3").addEventListener("click", function () {
        togglePhoto("Drawn")
    });

    activate("short")
}