window.onload = function () {
    [].forEach.call(document.getElementsByTagName("img"),
        function (img) {
            img.classList.add("img-fluid");
        });
    document.getElementById("cover-image").classList.remove("img-fluid");
    [].forEach.call(document.getElementsByTagName("table"),
        function (tbl) {
            tbl.classList.add("table", "table-condensed", "table-bordered");
        });
}