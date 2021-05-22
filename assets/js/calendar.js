var navState = "client"
var subNavState = "client-intro"
var url = new URL(window.location);


function navToggle(dest) {
    document.getElementById("n-" + navState).classList.remove("active", "btn-active");
    document.getElementById("n-" + dest).classList.add("active", "btn-active");
    document.getElementById("sn-" + navState).hidden = true;
    document.getElementById("sn-" + dest).hidden = false;
    navState = dest
    if (dest == "student") {
        subNavToggle(dest + "-" + "resume")
    } else {
        subNavToggle(dest + "-" + "intro")
    }
}

function subNavToggle(dest) {
    document.getElementById("sn-" + subNavState).classList.remove("active");
    document.getElementById("sn-" + dest).classList.add("active");
    document.getElementById(subNavState).hidden = true;
    document.getElementById(dest).hidden = false;
    subNavState = dest
    url.searchParams.set("dest", dest)
    window.history.pushState({}, '', url);
}

function toggleFromQuery() {
    if (url.searchParams.has("dest")) {
        var dest = url.searchParams.get("dest")
        navToggle(dest.split("-")[0])
        subNavToggle(dest)
    }
}

window.onload = function () {
    toggleFromQuery();
}