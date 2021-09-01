Title: Track Fathom Goals/Fathom Events in Gumroad
Date: 2021-09-23
Modified: 2021-09-23
Slug: fathom_gumroad
Authors: Philip Kiely
Summary: If you use Fathom Analytics and sell stuff on Gumroad like I do, here is how you add Fathom to Gumroad.

Let's say you have a website with Fathom Analytics on it and you also have a Gumroad account. And you want to see your Gumroad sales in Fathom. Follow these steps:

1. Create an event in your Fathom dashboard
2. Add the below code to your Gumroad third-party analytics page & remember to save your changes
3. Return to your Fathom dashboard and watch the sales roll in!

Note: In Fathom, "Goals" and "Events" seem to mean the same thing and are used interchangeably.

Resources:

* [How to set Events/Goals on Fathom](https://usefathom.com/docs/features/goals)
* [How to add your Fathom script](https://usefathom.com/docs/script/script)
* [Fathom script parameters](https://usefathom.com/docs/script/script-advanced)
* [How to add third-party analytics on Gumroad](https://help.gumroad.com/article/174-third-party-analytics)

The Code:

```html
<script src="https://cdn.usefathom.com/script.js" data-site="SITE_ID" data-auto="false"></script>
<script>
var price = document.getElementsByClassName("receipt-price")[0].innerText
price = parseFloat(price.slice(1)) * 100
window.fathom.trackGoal('EVENT_ID', price);
</script>
```

There are a few "gotchas" in this process that I discovered along the way:

* By default, the Fathom script uses `defer` to help your page load faster. You have to delete this so that the scripts load in order.
* Set `data-auto` to `false` in the Fathom script. Otherwise, the purchase ID of every transaction will show up in your Fathom dashboard, polluting your results and potentially leaking (relatively harmless) data if the dashboard is public.
* The code is only run on successful purchases.
* Set the value of the event based on the amount the customer actually paid with the whole `var price` situation. If Gumroad materially changes their receipt page, this code snippet may break.
* The conversion rate on the goal might not be a particularly meaningful figure, you'll have to calculate

A final note: this doesn't actually let me do the thing I was trying to do. What I want to be able to do is answer the following question:

100 people from Hacker News and 100 people from Twitter each click on a link to my website. 4 of those people buy the book on Gumroad in the same session. How many of those people came from Hacker News, and how many from Twitter?

Fixing this (for some cases, still not the general case) requires persisting UTM parameters to Gumroad's analytics callback URL which I asked Gumroad to do a couple of weeks ago so we will see if they do that.