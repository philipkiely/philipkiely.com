Title: My First Open Source Contribution
Date: 2019-06-24
Modified: 2019-06-24
Slug: first-open-source
Authors: Philip Kiely
Summary: I put almost every line of code that I write outside of work on GitHub. Anytime I make a public repository, I make sure to stick a license on it so that people can actually use the contents; usually I use MIT, sometimes Apache 2.0. Thus, I could say that I have published thousands of lines of open source code across dozens of projects. However, most of that code is pretty useless to other people, so I don't go around saying that...

Like most developers, I use open source software every day. I'm writing this article on [Atom](https://atom.io), an open source text editor, and I will publish it using [Pelican](https://github.com/getpelican/pelican), an open source static site generator. Pelican, in turn, is written in [Python](https://www.python.org), which itself is open source. I use [Bootstrap](https://getbootstrap.com) for most of the styling on this site, and I have taken code snippets and inspiration from various freely available templates for components like the nav bar and footer.

I put almost every line of code that I write outside of work on GitHub. Anytime I make a public repository, I make sure to stick a license on it so that people can actually use the contents; usually I use MIT, sometimes Apache 2.0. Thus, I could say that I have published thousands of lines of open source code across dozens of projects. However, most of that code is [pretty useless](https://github.com/philipkiely/spectrumcompose) to other people, so I don't go around saying that.

### Contribution Story

One promise of open source is that with many people using a tool, they will improve it and share those improvements. Over time, the tool grows beyond what the original authors could have created given their time and resources. This is the story of my first time improving a tool that I use.

The library in question is [devices.css](https://github.com/marvelapp/devices.css), which can render a variety of phones in CSS for using in websites. I used it on a couple of projects, but I quickly ran into the same issue that someone [raised back in 2015](https://github.com/marvelapp/devices.css/issues/21): the css devices are the same absolute size regardless of screen size. Someone in the comments on that issue came up with a clever workaround setting very small font sizes, however, that approach was broken on Google Chrome, which enforces a minimum font size. Someone else posted a link to a project that provided truly responsive devices, but they were not as detailed and you had to buy a license to use them in commercial projects. [My solution](https://github.com/philipkiely/devices.css) lets you generate a device library of any size by modifying the underlying code directly.

After I published my library, I left comments on the relevant issues in the original library. A few days later, [this guy](https://github.com/Romainpetit) came along, starred the repository, and left the comment "Nice endeavour @philipkiely, it looks like you nailed it." on the original repository. That made my day. This is another promise of open source: community recognition for making worthwhile improvements.

I will not attempt to merge these changes back into the original project because the code is significantly different from the original. I only used a single file from the original as the source of this project, not the whole library, so it would not be a continuous history. The comments on the relevant issues should be sufficient to direct people who need it to my library. If the maintainers of the original library release a new version with new devices, I would be able to easily incorporate those changes into my version.

### Technical Details

The original library is written in scss, a language that compiles to css. After parsing through the syntax to understand how it works, I realized that I could add a variable to change the scale of the devices. However, the original library was over two thousand lines, and every third line or so needed one of two changes to use the new variable. I wrote a python script that read through the code and applied the changes. I started by trying regular expressions, and if I knew regular expressions better I'm sure I could have done it without the script, but I don't. 

This script generated an scss file with a single variable that you can change to change the scale. The library isn't by default *responsive* but it is *resizable*. Developers can generate whatever size of devices they want and use that css file in websites. For fairly responsive resizing, a decent strategy is to generate css files for a few different scales (I recommend .33, .67, and 1 as a starting point) and switch between them using media queries. 

### Afterwards

After this experience, the next thing I want to do in open source is actually make a contribution to the main repository of a project that I use, hopefully a python library like Django. [It's on my bucket list](https://philipkiely.com/essays/software-bucket-list.html).
