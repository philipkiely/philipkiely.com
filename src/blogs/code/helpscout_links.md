Title: A Tiny Case Study in Automation
Date: 2020-12-04
Modified: 2020-12-04
Slug: helpscout_links
Authors: Philip Kiely
Summary: Recently, I've been learning about high-leverage work. Automation is a great example of high-leverage work because you can save people time. Help Scout has a little box on some far-flung page that you can use to add custom JavaScript to a site. I think it is designed for analytics trackers and such, but I used it to save my support team hours on the way to saving our users even more time.

Recently, I've been learning about high-leverage work. Automation is a great example of high-leverage work because you can save people time. The easiest way to add automation to your platform is to let users add their own code. Help Scout has a little box on some far-flung page that you can use to add custom JavaScript to a site. I think it is designed for analytics trackers and such, but I used it to save my support team hours on the way to saving our users even more time.

Gumroad maintains over 200 help documents for creators and their customers. Many of these documents are long, with many pictures, gifs, headers, and paragraphs. When I'm writing a customer support email, I want to link specific parts of the help page.

An anchor link is an HTML attribute that lets you link to somewhere in the page. Help Scout supports anchor links, but you have to set them manually. With over 200 documents between the creator and customer docs, this would be hours of tedious manual work to add, and then they would need to be kept up to date as the docs are edited over time.

Example: [https://help.gumroad.com/article/82-membership-products#MultipleTiers](https://help.gumroad.com/article/82-membership-products#MultipleTiers)

Help Scout supports custom JavaScript, so I wrote a snippet that dynamically assigns anchor links to each h2 and h3 on the page. I also had it exclude the main pages because they are not articles, so those pages are unaffected by the change (otherwise, their UI breaks). Thus, every single header is now directly linkable and those links will stay up to date over time.

2 small drawbacks:

1. The links are the first 20 characters of the header, so they can end in the middle of a word, which is not ideal but shouldn’t be an issue, they are still descriptive.
2. If you change the header text, old anchor links will no longer work, as the anchor is dynamically generated so it automatically updates. However, if an anchor link is broken, it just brings the user to the top of the page, which was the previous functionality, so it isn’t a worse user experience. Still, these links are designed for a message or other temporary place, not for permanent use.

The code, in case you’re interested (note for the custom script in `help.gumroad.com` the `window.location.href` check has an accordingly different value):

```javascript
//auto link all h2 and h3
function linkText(s) {
    return s.replace(/\W/g, '').substring(0, 20)
}
function makeTitleLink(tag) {
    Array.from(document.getElementsByTagName(tag)).forEach(
        function(element, index, array) {
            console.log(element, index, array)
            element.id = linkText(element.innerText)
            element.innerHTML = "<a href=\"#" + element.id + "\">" + element.innerHTML + "</a>"
        }
    );
}
document.addEventListener("DOMContentLoaded", function(){
    loc = window.location.href.substring(6, window.location.href.length)
    if (loc != "//customers.gumroad.com" && loc != "//customers.gumroad.com/") {
        makeTitleLink("h2")
        makeTitleLink("h3")
    }
});
```

The thing I found most interesting about all of this is how anchor links interact with the page load sequence. The function doesn't trigger until the DOM contents are fully loaded, but the browser still knows to jump to the appropriate place on the page.

If you are a Help Scout user, feel free to adopt this code snippet under the MIT License.