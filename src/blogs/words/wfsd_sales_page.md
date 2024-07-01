Title: Building the <i>Writing for Software Developers</i> Landing Page
Date: 2020-06-02
Modified: 2020-06-02
Slug: wfsd_sales_page
Authors: Philip Kiely
Summary: This post outlines the decisions I made while implementing the landing page for *Writing for Software Developers* and logs changes to the page over time.

I am not an expert marketer or sales page copywriter. However, the sales and feedback from my page for [*Writing for Software Developers*](https://wfsd.com) were strong signals that I got a few things right in creating the page. This post outlines the decisions I made while implementing the landing page for *Writing for Software Developers* and logs changes to the page over time. It is broken down by section, so you can scroll along with the sales page itself to compare the descriptions with the actual website.

In *Authority*, Nathan Barry describes the two roles of a sales page: introduce the product and overcome objections. Each aspect of the page is designed to achieve at least one of these goals. The order of information on the page is also inspired by the book and is a pretty good starting place for outlining your own landing page.

### Above the Fold

Here, we are clearly in "introduce the product" mode. Even though I am selling an ebook, a prominent render of a physical book with the cover art immediately signals that this is the sales page for a book. The image answers every visitor's first question: "what is this?" The copy on the right (or below on mobile) is somewhat less important. Rather than describing the book itself, these four short paragraphs focus on the importance of writing. This begins the process of overcoming a major objection to most products: "why should I care?"

### First CTA (+ Social Proof)

If someone is returning to this page, it is important that they can find a purchase link without scrolling through tons of information. This section continues to introduce the book on the left by including information about pricing, but also begins providing social proof, which is useful for overcoming all sorts of objections. I include the number of copies sold (updated every couple of weeks, so I say "xyz+"). More importantly, I include a quote from a tweet, as well as the tweet itself to the right. The image of the tweet links back to the original thread on Twitter. I got permission from everyone whose tweets I used to quote them in this manner on my site.

These tweets were not included on the site during launch week because they didn't exist yet. I had a launch announcement in their place.

### Interviews

I include the photo (or recognizable avatar), name, association(s), and bio of each one of the eleven people who I interviewed for the book. This section is long. I could have compressed it by putting the interviewees into a grid, but I decided it would be more effective to give everyone their own row and help readers understand just how many awesome people had contributed their wisdom to the book. This section both serves to introduce the product (what is in it) and to provide social proof.

### Free Chapter

Potential objection: "I don't know if I will like the book." The first chapter, formatted as a PDF just like the book (I extracted the pages from the actual book itself), serve to provide visitors with the opportunity to read thousands of words of the book itself and decide if the content, tone, and style are right for them. I chose to include Chapter 1 because it is about generating ideas. My hope is that people use the chapter to come up with exciting ideas for technical content and then purchase the book to figure out how to execute on these ambitions.

### Table of Contents

To provide visitors with information about the book, I include the table of contents. The chapter titles include many keywords and give a complete overview of the topics covered in the book. I also include a render of the book cover on an iPad to remind visitors that they are considering purchasing an ebook.

### Second CTA (+ Social Proof)

This section is nearly identical to the previous one. I chose to include this tweet in particular because it is from a verified account (extra-strong social proof) and because it reminds visitors that some may be interested in purchasing a team license (which generates extra revenue for me).

### About the Author

At this point, I have fully explained the product, and these next sections are purely to overcome objections. One potential issue people might have is "who is this author and why does he know enough to write this book?" This section addresses that by explaining my professional background and listing client logos to verify my work experience, providing, you guessed it, social proof.

### Questions

Finally, I explicitly address potential objections that I was not able to cover organically in the rest of the page. I mention the return policy, the team license, my free-book policy, and answer questions about the audience for the book and the formats available. I also engage in a bit of recreational keyword bingo.

### Third CTA (+ Social Proof)

This section is nearly identical to the previous two. I chose to feature this tweet because it compliments the pricing and encourages people outside of my core audience to give the book a shot.

### Optimizations and Decisions

I hosted this page on my own website rather than establishing a separate domain. This way, the visitors were able to explore the rest of the site to get a sense of who I am and what I do. This gave me an unexpected boost of traffic on projects like my email newsletter and my YouTube channel. However, I did mirror the website onto three vanity domains (writingforsoftwaredevelopers.com, writingforsoftwareengineers.com, and writingforprogrammers.com) which some people say will help me with SEO and other say will hurt SEO. Regardless, it took a few minutes to set up (a script just copies a subset of my site and deploys with Netlify and GitHub) and I have already seen traffic convert through those URLs so they have paid for themselves for the year.

I host my site on Netlify and my build scripts use Jinja and Pelican to make the magic happen. I use Bootstrap for CSS, and the site is designed with mobile visitors in mind (54% of my launch week traffic was on a phone). I have already done a lot with the site itself to make it lightweight so it loads quickly and does not use much bandwidth from Netlify. For this site, I did not self-host the 11 interview subjects' profiles or my clients' logos during launch, among other optimizations (I later did self-host these images due to content blocking issues with Firefox). Serving launch-week pageviews took only 20GB of bandwidth, or 1/5 of Netlify's free plan.

This post is one of four about *Writing for Software Developers*.

1. [Writing *Writing for Software Developers*](/essays/writing_wfsd.html)
2. [Marketing *Writing for Software Developers*](/essays/marketing_wfsd.html)
3. [Building the *Writing for Software Developers* Landing Page](/essays/wfsd_sales_page.html) (You are here)
4. [*Writing for Software Developers* Financial Performance](/essays/wfsd_financials.html)

