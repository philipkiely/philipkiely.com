Title: How to Disable a Stretched-Link Button in Bootstrap 5
Date: 2021-11-20
Modified: 2021-11-20
Slug: disable_stretched
Authors: Philip Kiely
Summary: Disabling links is useful and Bootstrap 5 provides built-in styles for disabled links and buttons. However, `.stretched-link` and `disabled` don't play nice unless you introduce a few lines of custom CSS.

In Bootstrap 5, the `.stretched-link` class lets you turn a complex element into a clickable area bounded by a containing block. Here's the [official page on the class](https://getbootstrap.com/docs/5.0/helpers/stretched-link/
).

This is one of my favorite little utilities in Bootstrap, I use it all of the time to make cards clickable. For example, on [whopaystechnicalwriters.com](https://whopaystechnicalwriters.com), every publication card is a clickable link.

![Stretched Link Cards on wptw](/assets/img/blogs/code/disable_button/wptw_disabled_link.png)

Disabling links is useful and Bootstrap 5 provides built-in styles for disabled links and buttons. However, `.stretched-link` and `disabled` don't play nice unless you introduce a few lines of custom CSS:

```css
.inactive {
     background-color: #C1C1C0;
     pointer-events: none;
     cursor: default;
 }
```

The `pointer-events` and `cursor` lines nullify the `.stretched-link` class and make the area no longer clickable. The `background-color` is optional to visually indicate to the user that the link is disabled.

Note: unlike the traditional "disabled" flag that goes on the `<a>` tag, the `.inactive` class is applied to the containing block.