Title: How to Write a Technical Article
Date: 2019-08-20
Modified: 2019-08-20
Slug: technical_article
Authors: Philip Kiely
Summary: Every great writer writes stories, and so do all of the good ones. Technical writers are not immune from this requirement, nor are we barred from the tools of the craft. Stories have conflict. Our writing has characters, these characters have motivations, desire outcomes. Despite this legacy and these tools, technical writing is often held to a lower standard than even the humble blog post...

Every great writer tells stories, and so do all of the good ones. 

Technical writers are not immune from this requirement, nor are we barred from the tools of the craft. Stories have conflict. Consider the vulnerability disclosure: a simple battle of wits, Man against Man. The introductory guide? Man versus Nature, squeezing bits against entropy into a useful form. A post detailing how to fix a certain bug masquerades as Man versus Technology but ultimately reveals itself as Man versus Self.

Our writing has characters, these characters have motivations, desire outcomes. Through expository technical writing we have a unique privilege of delivering our character an outcome and having the outcome repeat itself for real people indefinitely, or at least until it is obviated by the next minor version of the framework in question.

Despite this legacy and these tools, technical writing is often held to a lower standard than even the humble blog post. A bit of `inline code` does not remove the need for clear, engaging communication. On the contrary, it increases the need. Nontrivial code without context is worse than useless; it tricks its way into systems as dark magic, an untouchable solution to an unknown problem. Furthermore, it does not diminish the need for proofreading and copyediting.

Let me tell you a story, then, of how to write a technical article. This guide is based on [my writing for clients](/notes/posts.html), but writing for your own blog or project follows the same path. If you would like me to write you a story, please send me an email to [philip@kiely.xyz](mailto:philip@kiely.xyz).

## Steps of the Journey

On the wall beside my desk I have a paper Kanban-inspired board that tracks my writing. It has six columns, and each article lives as an index card moving across the board. Let's trace the journey of [an article I wrote for FloydHub](https://blog.floydhub.com/web-scraping-with-python/) across the board.

### Preflight

I had an existing relationship with FloydHub at the time, having published there before, but I started this article in the same place as with a new client: an informal query to gauge interest in the project. The entire pitch was simple, just a one sentance suggestion. "How about a project-based article on web scraping with Python that can run in a Jupyter notebook on your cloud CPU platform?"

In my system, I create an index card for an article when I have an agreed upon topic, length, and price. I try to keep an article in the queue at all times for each client, so my Preflight and Outline columns are often busy places.

### Outline

This is where the real work begins. I rely on a strong outline to guide me through the writing process. The outline step is where I do the research to validate the feasibility of my idea and cover the gaps in knowledge that I have acquired over the course of my own work with whatever technologies I am presenting. I also consider the scope and audience of the work.

Fortunately, I tend to have an easy time picking a target audience. I think back along my journey to becoming a developer and I think something along the lines of "yes, this is what I needed to read during winter break of my sophomore year." I then formalize that into a reader profile, like "this article is for someone with moderate familiarity with basic web development and Python, and also contains data of interest to all Hacker News readers."

Determining my audience is critical to limiting the scope of the article. Generally, the things that I write are 1500 to 2000 words plus sample code, so I can really only cover a small amount of material in that time. The outline step is where I make the hard decisions about the level of setup required (for example, do I walk the reader through setting up Python on their local machine) and the level of background knowledge assumed (for example, should I define a web browser? A for loop? HTTP methods?)

Ultimately, outlining helps me remember that I am not writing documentation. I am creating a story, not a reference, and a story needs a beginning, middle, and end. Usually, my article exposes a technology by working through a contrived example project. After determining the components of the project, I consider the best order to present them and that becomes the outline.

### Content

For the FloydHub article in question, I had to develop the scraper before I wrote about it. Depending on the topic, I either write all of the example code then write the article or I alternate back and forth, but I never write about code that I haven't yet written. For first-time writers, I recommend writing all of the code first, as the combined structure of your outline and your sample project will carry you through the writing process.

The content-writing phase is the longest, but I have the least to say about it. I just write until the article is done. The writing process demands nothing more than an active mind and time in the chair.

That said, for me writing an article has two distinct phases. Even with an outline, even with nearly-complete sample code, I am still figuring out the article as I write it. However, there comes a time with each article, either when I stumble into a strong thesis, develop a clean solution for a technical issue, or add a dimension to my example use case when I "crack" the article. To me, an article isn't certain until it's cracked, but once it is all I have to do is write.

In the FloydHub article, I knew that I had cracked it when I had scraped all of the data that I needed for the exploratory data analysis. Once I had 8 million words of job listings, the rest was just writing.

### Review

With the article drafted, I read it aloud to myself, run the sample code again just to be sure, then send it to the publisher or client. My clients are usually the editors for the blog or publication that I am submitting to, and depending on the company the article goes through a round or two of review then is approved for publication. The most important part of the review process is staying open to feedback and working with the editor to create the best piece possible.

If you are publishing for yourself, it's still a great idea to have someone review what you have written both for technical accuracy and normal editorial feedback like grammar and usage.

Also as part of the review phase, either you or the client will format the article for the publication system. I tend to write my articles in markdown, and many systems have good markdown support. FloydHub has writers input their own articles, which gives me more control, while most other places do it themselves, which is also nice as it saves me a few minutes. When the article is ready to preview, give it another check for typos and consider details like image placement and captions.

When writing for clients, in my experience the general practice is to issue an invoice upon acceptance of an article for publication. Frequently, I get paid before the article is actually published, as there may be a couple of weeks between an article being accepted and it getting published.

### Resolve

After an article is accepted for publication, there is still work to be done. I leave it in the "Resolve" column from after the invoice is paid until the article is published. When an article is published, I add it to my [list of articles](/notes/posts.html) and post links in my various social media profiles. If I find a discussion on Reddit or Hacker News, I identify myself as the author so that I can answer questions.

### Success

"I hate writing, but I love having written" is attributable to any number of famous authors. I often feel the same way. I have a sixth column, success, that holds the index cards for finished, published articles as a reminder of the work that I have already done.

## Finding a Client

If this process seems appealing to you, the real first step is finding a client. The first client is always the hardest; I published my first article for a company that I had worked with previously on website updates. However, even a small publication history can quickly lead to a strong response rate to your queries.

In addition to publishing on your own blog, I recommend querying somewhere like FloydHub or Smashing Magazine for your first article, depending on your skill set. You want your first client to have a strong, established editorial process and a wide readership to help develop your content and your audience. I suppose I should say that though I am proud to count both of those sites among my clients, neither paid or asked me to write this article or to call their editorial processes "strong and established."

Technical writing is a fantastic way to grow your skills, get your name out there, and make a bit of money on the side. Most importantly, it is a great way to tell a story.
