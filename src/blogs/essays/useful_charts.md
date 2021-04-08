Title: Making Useful Charts and Diagrams when you Suck at Drawing
Date: 2020-04-03
Modified: 2020-04-03
Slug: useful_charts
Authors: Philip Kiely
Summary: I write technical articles. As part of that work, I make charts and diagrams to explain concepts to my readers. I also irredeemably suck at drawing and my handwriting defaults to illegible. Nevertheless, I manage to deliver useful diagrams with my articles that explain complex ideas with intuitive visual metaphors. **I'm able to do this because most aesthetic properties are not relevant to a diagram's usefulness, and the ones that are can be achieved relatively easily.** I harbor no delusions about any ability to show you how to become a better artist. I do believe that you can use a few simple techniques to create more effective graphics at your current level of skill.

I write [technical articles](/notes/posts.html). As part of that work, I make charts and diagrams to explain concepts to my readers. I also irredeemably suck at drawing and my handwriting defaults to illegible. Nevertheless, I manage to deliver useful diagrams with my articles that explain complex ideas with intuitive visual metaphors. **I'm able to do this because most aesthetic properties are not relevant to a diagram's usefulness, and the ones that are can be achieved relatively easily.**

I'm not a designer, illustrator, or painter, and I have no formal training to speak of in any kind of visual art. This is not a guide for actually getting good at this stuff, it's a hastily-scrawled note in the margins of a much better work on how to hack it at this one aspect of the job of technical content development that's disproportionately difficult and time-consuming and requires skills and equipment outside of the normal scope of our work. I harbor no delusions about any ability to show you how to become a better artist. I do believe that you can use a few simple techniques to create more effective graphics at whatever your current skill level is.

### What Makes a Diagram Useful?

A diagram is a succinct visual representation of an idea. Diagrams are great at showing relationships and providing visual metaphors.

I'm using the term "relationship" pretty loosely here. Sure, database diagrams show relationships quite literally within a relational database, but concepts like cause-and-effect, relative quantities, and matching are prime diagram material. Diagrams are uniquely good at conveying connection and structure and text is quite bad at it. Trying to explain a many-to-many relationship takes O(n squared) phrases for n objects but only O(1) diagrams.

Visual metaphor is another compelling use case for graphics in your technical content. Like with relationships, visual metaphors help the reader gain an intuition for the concepts described, allowing your text to focus on specific details and concrete aspects of the topic at hand.

### On the Benefits of Approximation

If your drawings are imprecise, they communicate to the reader that the ideas you're presenting are an approximation or intuition. This is probably what you want. If you don't want this, fire up Python or R and make a graph with data; the computer-generated image will give readers an accurate impression that the information communicated is precise. Even computer-generated plots sometimes want to signal approximation with this visual effect, which is why `matplotlib` offers [a package for making your charts look hand-drawn, xkcd style](https://matplotlib.org/xkcd/examples/showcase/xkcd.html).

Lean into this general effect. If you can't get something unimportant exactly right, get it deliberately wrong. Make slight asymmetries larger. If something is two pixels off of center, push it another twenty in that direction. If your lines aren't straight, your circles aren't round, your squares aren't even, embrace it and make sure that you're not accidentally signaling the importance of some trivial aspect of your diagram by inconsistently achieving aesthetic patterns.

### Good Artists Borrow ...

Great artists reverse engineer. Reverse engineering, or the practice of observing an object or system and reconstructing it, applies outside of technical systems. A couple of months ago, very disappointed in the quality of graphics I was producing, I sat down to figure out specific changes I could make to improve my work. Knowing that it would be a long and difficult process to legitimately improve my artistic skills, I tried to find a style of drawing that was achievable and acceptable. I found it in the ever-relevant [xkcd](https://xkcd.com) by Randall Munroe. The incredibly popular comic demonstrates the magnitude of what is possible using very simple techniques in an unsophisticated style, relying on content rather than raw artistry. xkcd's art is simple, not bad, and that means that its style is achievable.

Renaissance artists like Michelangelo learned painting technique by copying their mentors' work stroke for stroke. I learned martial arts by copying moves then sequences from instructors. Similarly, I improved my illustrating style by copying specific elements from xkcd, re-drawing my work to incorporate these changes.

Here are some things that I took from xkcd.

- **Small Caps**: My handwriting is atrocious. Not only are the individual letters misshapen, but the kerning is inconsistent, the lines are uneven, and I tend to write smaller at the end of the line than the beginning. Munroe writes entirely in capital letters in xkcd, which I adopted to address this problem. It works great, as writing in caps forces me to write slower, gives me more tools to address character spacing and size, and improves overall legibility for short phrases.
- **Straight Borders**: Every line in my work is hand-drawn except for the box around a graphic, which I use a software rectangle tool to draw. This is based on xkcd's panel design, where the panels are perfect boxes and the contents are hand-drawn.
- **Consistent Stroke Weight**: In xkcd, most comics use the same stroke weight. All of my drawings use a single pen tool, and most of them use a single stroke size.
- **Make Legends**: While Munroe's legends are often for humorous effect, embedding a guide to interpreting a graphic within the graphic itself helps all readers grasp the information you're trying to communicate.
- **Limit use of Color**: Most xkcd comics are black and white. Using color is extra work, presents accessibility challenges to colorblind readers, and often doesn't contribute information that can't be conveyed in greyscale. When I do use color, which is rare, I rely on another element like shape or position to communicate the same information.
- **Keep it 2D**: If Munroe only needs two dimensions to entertain and educate millions, I only need two dimensions in my graphs and diagrams. I do not have the artistic skill for any kind of forced three-dimensional perspective and thus I do not attempt it, as a third dimension would add visual complexity without efficiently communicating additional information.

Of course, it is important to develop your own style. I don't think anyone would mistake my work for Munroe's, if for no other reason than that he is so much more practiced in the style. My graphics are generally one or two panels, rather than a whole comic, and focus on a diagram or other non-character aspect, while his tend to prominently feature stick figures. This points to an important note when emulating style: it's much better to emulate style from one genre and topic and apply it to yours than to find something within your own sphere and copy that. The former is taking inspiration, the latter is being derivative.

### Four Examples

Here are four examples of effective graphics with limited artistry, three from my own work published with clients and one from Nathan Barry's blog. The first two demonstrate diagrams showing relationships, the latter two exemplify visual metaphor.

#### Semantic HTML

![Semantic page layout on computer and phone: Website Setup](https://websitesetup.org/wp-content/uploads/2020/03/SemanticHTML-1536x1073.jpg)

In [an article for Website Setup](https://websitesetup.org/html-vs-html5/), I wanted to demonstrate how semantic elements could be rearranged on screens of different sizes without embedding a CodePen or similar because the intended audience was somewhat less technical than I'm used to writing for. Thus, I created a diagram to express a relationship between a semantic element and its intended location on the page. This diagram incorporates many of the lessons from xkcd. It also is full of crooked lines and unevenly sized text. However, it's a decent approximation of how an actual webpage would look because I included only the essential elements of the diagram and nothing more.

#### Spectrum of Automation

![HTML Spectrum of Automation: Smashing Magazine](https://cloud.netlifyusercontent.com/assets/344dbf88-fdf9-42bb-adb4-46f01eedd629/4d0b8556-c7f8-40a8-bb26-ab876e11945c/htmlspectrum.png)

In [an article for Smashing Magazine](https://www.smashingmagazine.com/2020/04/django-highlights-templating-saves-lines/), I added one simple diagram showing how explicit a programmer had to be in hand-writing HTML for web development approaches with different levels of automation in HTML generation. This graphic relies on the principle of approximation: there is no real scale or quantitative measurement for level of automation, the diagram simply presents approaches relative to each other for the reader's understanding. 

#### Content Blocking

![Content Security Policy blocking scripts: Website Setup](https://websitesetup.org/wp-content/uploads/2020/03/ContentSecurityPolicy-1536x702.jpg)

In [the above article for Website Setup](https://websitesetup.org/html-vs-html5/), one graphic I created was intended to give non-technical or newly technical readers an intuition of how a content security policy works. I've already discussed much of what makes this graphic effective in previous examples, but there are two things left to highlight: color and metaphor.

Above, I said to limit color and always indicate the same concept with a secondary attribute. In this example, I use red and green, nearly universally recognized as stop and go, to indicate that some scripts go through a content security policy and others are stopped by it. However, red-green colorblindness is one of the most common kinds of colorblindness, so I indicate the same information by making the green icon a check and the red icon an X, similarly universal symbols.

As a visual metaphor, I insert the content security policy between the scripts and the client and show scripts entering and exiting the policy after being compared to a whitelist. While that is not exactly the process, it's a useful way to think about blocking scripts without distracting the reader with a more involved metaphor achieved by textually mapping components of the technical process to real-world non-technical systems.

#### Ladders of Wealth Creation

![Ladders of Wealth Creation: Nathan Barry](https://lh3.googleusercontent.com/qWcgH_BoOwaDJ3f5lo9YG5f4WCKaLRwWYQZCb4aEJWA41Fm1KDVjLu5B9LudqY_1W6NwI0eSTtb5R8F1FmD2fcmSg-UcnhebLyh2dDyCQ_f1WpoWGna3WyuM1txea36M2T54v_T5)

I'm not solely here to talk up my own work. One of my favorite examples of an essay centered around a visual metaphor is [The Ladders of Wealth Creation](https://nathanbarry.com/wealth-creation/) by [Nathan Barry](https://nathanbarry.com/). Barry favors a very different style from my own, using entirely typed text, color and background, and a variety of stroke styles. Still, the image leans into the approximation allowed by a rough sketch, with wavering lines and uneven positioning. Barry's work is, while more aesthetically pleasing than my own, far from passing as professional illustration. Still, it anchors a six-thousand-word blog post as one of the only graphics, providing readers an early insight into the contents of the article and a touchstone to refer to as they parse Barry's extended metaphor on different types of income generation. If that simple illustration were missing from the post, readers would have more trouble understanding the directional moves that Barry relies on in communicating his ideas.

### A Note on Equipment

Currently, I use an 11 inch 2018 iPad Pro with the 2nd generation Apple Pencil. For software, I use the free Autodesk Sketchbook for creating charts and diagrams and the default "Photos" app's built-in markup features for annotating existing images. I'm very happy with this setup as it provides all of the features I need and, importantly, very few features that I don't need. Airdrop makes the process of moving files between devices pretty seamless. I recommend every part of this equipment set and workflow, but not particularly strongly, as even slightly different needs might merit different tools.

Everyone is going to have a set of equipment that works well for them. I'd say the minimum viable set of equipment is pen or pencil, paper, and a smartphone camera, although taking a good photograph of a sketch is difficult because you don't want the camera's shadow hanging over the image. There are several hardware options like Wacom and other drawing tablets, various types of iPads, and Microsoft's Surface line. For each hardware option, there are dozens of software options that I won't even start to list. The important thing is to find something that works for you. You don't need the best tool, or even the best tool for you, just something that gets the job done. Don't feel compelled to spend a bunch of money on equipment, see what you can do with what you have.

### General Encouragement

If you like creating graphics and want to make more artistic and beautiful charts and diagrams for your articles, you should by all means invest the time in learning to do so and then acquire good equipment that helps your work. Your well-drafted creations will stand out from a scrawled crowd and garner admiration. There are a number of ways to make your technical content stand out, and having legitimately excellent graphics is a great method of doing so.

For the rest of us, remember to focus on the important aspects of a design that actually communicate useful information to the reader. It is possible to learn enough drawing to be dangerous, I'm missing a couple fingers and I'm able to draw at a level that is practical though not pretty. Find an illustrator in another genre whose work you admire, like I did with Munroe's xkcd, and practice recreating specific craft elements of their work into your own drawing. Over time, you'll develop confidence in your ability to create graphics and use them to help educate your readers.

If you're interested in creating technical content, check out my book [Writing for Software Developers](/wfsd).
