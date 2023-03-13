async function processForm(event) {
    event.preventDefault();
    //reset UI
    document.getElementById("form-failed").hidden = true
    document.getElementById("function-failed").hidden = true
    // Gather Data
    var topic = document.getElementById("topic").value;
    // Validate Required Fields
    if (topic == "") {
        document.getElementById("form-failed").hidden = false
        document.getElementById("poem-form").reset()
        document.body.scrollTop = document.documentElement.scrollTop = 0;
        return
    }
    document.getElementById("poem-output").innerHTML = "<p>Your poem is being written. This may take up to one minute.</p>";
    document.getElementById("poem-container").hidden = false;
    document.getElementById("sonnet-button").disabled = true;
    // JSON Data
    var formData = {
        "topic": topic.substring(0, 100)
    }
    //Send to the blueprint function
    var response = await fetch("https://app.baseten.co/routes/VqKK3Yq/poem", {
        method: "POST",
        body: JSON.stringify(formData)
    });
    var body = await response.json()
    try {
        var poem = body["output"]["poem"];
        navigator.clipboard.writeText(poem);
        document.getElementById("poem-output").innerHTML = "<h3>" + topic + "</h3>" + poem.replaceAll("\n", "<br>")
        document.getElementById("poem-form").reset()
        document.getElementById("sonnet-button").disabled = false;
    } catch {
        document.getElementById("function-failed").hidden = false
        document.body.scrollTop = document.documentElement.scrollTop = 0;
        document.getElementById("sonnet-button").disabled = false;
    }
}

function copyPoem() {
}

// GLOBALS

var form = document.getElementById("poem-form");
form.addEventListener("submit", processForm);

var copyButton = document.getElementById("copy-button")
copyButton.addEventListener("click", copyPoem())