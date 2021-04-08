function setYear() {
    document.getElementById("year").innerHTML = (new Date()).getFullYear();
}

const sleep = (milliseconds) => {
  return new Promise(resolve => setTimeout(resolve, milliseconds))
}

function setDiscount() {
    const params = new URLSearchParams(window.location.search);
    if (params.has("code")) {
        var links = document.getElementsByTagName("a")
        Array.prototype.slice.call(links).forEach((l) => {
            if (l.href.includes("https://gum.co")) {
                if (!l.href.endsWith("/")) {
                    l.href += "/"
                }
                l.href += params.get("code")
            }
        });
        var prices = document.getElementsByClassName("price-text")
        Array.prototype.slice.call(prices).forEach((p) => {
            full = parseInt(p.innerHTML.substring(1));
            p.innerHTML = "<s>$" + full + "</s> $" + (full - (parseInt(params.get("discount")/100)));
        });
    }
}

window.onload = function () {
    setYear();
    setDiscount();
}

function emailListSignup() {
    var email = document.getElementById("get-email").value
    if (email.indexOf("@") != -1 && email.indexOf(".") != -1) {
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "https://2opt1v52m0.execute-api.us-east-1.amazonaws.com/default/EmailListNewMember", true);
        xhr.setRequestHeader('Content-Type', 'text/plain');
        xhr.send(JSON.stringify({
            email: email
        }));
        document.getElementById("get-email").value = "";
        document.getElementById("invalid-email").hidden = true;
        document.getElementById("valid-email").hidden = false;
        sleep(5000).then(() => {
            document.getElementById("valid-email").hidden = true;
        })
    }
    else {
        document.getElementById("invalid-email").hidden = false;
    }
    
}
