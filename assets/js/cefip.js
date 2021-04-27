function setDiscount() {
    const params = new URLSearchParams(window.location.search);
    if (params.has("code")) {
        var links = document.getElementsByTagName("a")
        Array.prototype.slice.call(links).forEach((l) => {
            if ((l.href.includes("https://gum.co") || l.href.includes("https://gumroad.com/l/")) && !l.href.includes("free")) {
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

function setOption() {
    const params = new URLSearchParams(window.location.search);
    if (params.has("option")) {
        var option = params.get("option")
        var links = document.getElementsByTagName("a")
        Array.prototype.slice.call(links).forEach((l) => {
            if ((l.href.includes("https://gum.co") || l.href.includes("https://gumroad.com/l/")) && !l.href.includes("free")) {
                if (option == "sp") {
                    l.href = "https://gum.co/cefip_sp"
                } else if (!isNaN(option)) {
                    l.href = "https://gum.co/cefip_upgrade?variant=Day%20" + option
                } else {
                    //original link, error handle one day
                }
            }
        });
    }
}

window.onload = function () {
    setOption();
    setDiscount();
}