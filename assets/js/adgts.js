function setDiscount() {
    const params = new URLSearchParams(window.location.search);
    if (params.has("code")) {
        var links = document.getElementsByTagName("a")
        Array.prototype.slice.call(links).forEach((l) => {
            if (l.href.includes("https://gum.co") || l.href.includes("https://gumroad.com/l/")) {
                if (l.href.includes("?")) {
                    var base = l.href.split("?")[0]
                    var rem = "?" + l.href.split("?")[1] //Max 1 "?" in URL
                } else {
                    var base = l.href
                    var rem = ""
                }
                if (!base.endsWith("/")) {
                    base += "/"
                }
                l.href = base + params.get("code") + "/" + rem
            }
        });
        var prices = document.getElementsByClassName("price-text")
        Array.prototype.slice.call(prices).forEach((p) => {
            full = parseInt(p.innerHTML.substring(1));
            p.innerHTML = "<s>$" + full + "</s> $" + (full - (parseInt(params.get("discount") / 100)));
        });
    }
}

window.onload = function () {
    setDiscount();
}