Title: Analytics Eats Last
Date: 2023-03-31
Modified: 2023-03-31
Slug: analytics_eat_last
Authors: Philip Kiely
Summary: Errors in analytics should never break your user experience. Wrap analytics in a try-catch block to make sure they don't cause issues.

Errors in analytics should never break your user experience. Recently, I had an issue with my [poetry generator](/rhymes) where a poem would be generated and shown to the user successfully, but an error message would also pop up.

This issue only occured for users with an adblocker running. Let's figure out why.

Here was the original code. Can you figure out the issue?

```
try {
    var poem = body["output"]["poem"];
    navigator.clipboard.writeText(poem);
    document.getElementById("poem-output").innerHTML = "<h3>" + topic + "</h3>" + poem.replaceAll("\n", "<br>")
    document.getElementById("poem-form").reset()
    document.getElementById("sonnet-button").disabled = false;
    if (poemType == "haiku") {
        fathom.trackGoal('20KJR8P8', 0);
    } else if (poemType == "limerick") {
        fathom.trackGoal('HLJDNNM0', 0);
    } else if (poemType == "villanelle") {
        fathom.trackGoal('1UIQVGVB', 0);
    } else { //sonnet
        fathom.trackGoal('LZYBY4WB', 0);
    }
    
} catch {
    document.getElementById("function-failed").hidden = false
    document.body.scrollTop = document.documentElement.scrollTop = 0;
    document.getElementById("sonnet-button").disabled = false;
}
```

I thought I was adhering to the principle of not letting analytics affect my site by putting the analytics code after the UX code. But when a user with adblock visited the site, the `fathom` object is undefined because the script that defines it is blocked. So the `catch` statement is triggered and the user sees an error.

To fix this, I wrapped my analytics code in another try-catch block:

```
try {
    var poem = body["output"]["poem"];
    navigator.clipboard.writeText(poem);
    document.getElementById("poem-output").innerHTML = "<h3>" + topic + "</h3>" + poem.replaceAll("\n", "<br>")
    document.getElementById("poem-form").reset()
    document.getElementById("sonnet-button").disabled = false;
    try {
        if (poemType == "haiku") {
            fathom.trackGoal('20KJR8P8', 0);
        } else if (poemType == "limerick") {
            fathom.trackGoal('HLJDNNM0', 0);
        } else if (poemType == "villanelle") {
            fathom.trackGoal('1UIQVGVB', 0);
        } else { //sonnet
            fathom.trackGoal('LZYBY4WB', 0);
        }
    } catch {
        //noop
    }
    
} catch {
    document.getElementById("function-failed").hidden = false
    document.body.scrollTop = document.documentElement.scrollTop = 0;
    document.getElementById("sonnet-button").disabled = false;
}
```

Now, no error appears.