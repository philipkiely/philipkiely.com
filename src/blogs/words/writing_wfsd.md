Title: The Writing of <i>Writing for Software Developers</i>
Date: 2020-05-28
Modified: 2020-05-28
Slug: writing_wfsd
Authors: Philip Kiely
Summary: I wrote my first book, *Writing for Software Developers*, in six months. This post details every step of the process. Read about the initial idea, the interviews, the writing process, the editing stage, and putting it all together for publication.

"I have this idea for a book," I told my mother, certainly not for the first time, over Thanksgiving break. "I think I can get it finished by the end of winter break." I ended up launching [*Writing for Software Developers*](https://wfsd.com/) over six months later, achieving my revised goal of launching six days before I graduated from college.

![Progress of *Writing for Software Developers*](/assets/img/snowball_charts.jpg)

This post details every step of the writing process. Read about the initial idea, the interviews, the writing process, the editing stage, and putting it all together for publication.

### December 2019: Outline

After pitching the idea to anyone who would listen, I sat down to actually outline the book. I started by listing every topic that I could think of that related to the title, which at the time was "Technical Content Development Handbook," a terrible title that I clung to for months longer than I should have. With a list of dozens of topics, I connected ideas into an outline.

Here is the outline word-for-word from a commit timestamped to December 8, 2019. It is quite similar to the final table of contents.

```
Outline: Technical Content Development Handbook

-   Preamble: Why write online
    -   Grow Your Skills
    -   Work in Public
    -   Gain an Audience
    -   Big Money Dollars
-   Section: The Work
    -   Chapter: Creating and Validating Ideas
        -   Introduce Examples
        -   9 questions process
        -   Versioning, shelf life, link rot, and obsolescence
    -   Chapter: Finding and Pitching Publishers
        -   Finding Publishers
        -   Pitching
        -   Templates
    -   Chapter: Sources
        -   Finding and Evaluating Sources
        -   Interviewing
            -   Finding and pitching the right interviewees
            -   Asynchronous (Email) interviews
            -   Synchronous interviews (multiple recording devices)
            -   What to ask
                -   Not what's been asked before (warren buffet story)
    -   Chapter: Writing
        -   Outlining
            -   Consider your audience
        -   Writing Sample Code
            -   More code is written than ends up in the article
            -   "Clean Code:" Concise but easy to understand
        -   Writing Body Copy
            -   Writer's Block
                -   Problem: Insufficient familiarity with subject
                    -   Read more Sources
                    -   Write more test code
                    -   think of example use cases
                -   Problem: topic too big
                    -   Identify audience
                    -   Gather prerequisite and further reading resources
    -   Chapter: Editing
        -   Reading Aloud
    -   Chapter: Publishing (mechanics, platforms, etc)
        -   Print vs Digital
        -   Formatting
-   Section: The Process in Action
    -   Chapter: The Project-Based Tutorial
        -   Features of project-based tutorial
        -   Work through outlining, writing, and editing process for Shakespeare sonnet mixer
        -   Provide starting and finishing resources
    -   Chapter: Example: Writing Shakespearean sonnets
        -   Complete article from previous chapter
    -   Chapter: The Topic-Based Article
        -   Features of topic-based article
        -   Case Studies
        -   Work through outlining, writing, and editing process for Ensuring Correctness in Migrations
    -   Chapter: Example: Ensuring Correctness in Migrations
        -   Complete article from previous chapter
        -   Not Django-Specific
-   Section: The Business of Writing
    -   Chapter: How content is monetized online
        -   Ads
        -   Sponsorships
        -   Subscriptions
        -   Content Marketing
    -   Chapter: Promoting your work and growing an audience
        -   Platforms: LinkedIn, HN, Reddit, Twitter, etc.
        -   Email List
        -   Ben's content strategy
    -   Chapter: IP and Publication Rights
        -   Rights, explained
    -   Chapter: Pricing (in order of goodness)
        -   Per Article
        -   Per Word
        -   Per Hour
        -   Free
    -   Chapter: Contracts
    -   Chapter: Invoicing
        -   Payment processors, Stripe, PayPal
    -   Chapter: Longer-term engagements
        -   Books
        -   Series
        -   Columns (regular fixed-schedule contributions)
        -   Jobs (editor, writer for AWS, etc)
```

Looking back, I'm surprised by how many of the original ideas made it into print. All three sections survived the writing process, although I renamed them "Acts" prior to publication to clarify my naming and expand the Shakespeare motif. Act 1 changed the least; the ideas appeared in the same order in the book as in this outline, though the chapter divides shifted. Act 2 changed several times during the writing process but remained committed to providing examples of the previous act's ideas. Act 3's chapters shifted in order and scope, but I can see how they could be cut apart and rearranged to match this outline in relatively short order.

### January 2020: Interviews

With my outline in place, I realized that I would have to draw from much more than just my own experience to deliver useful information on all of the topics that I wanted to cover. I decided to bring in expert interviews to bolster my ideas and add credibility to the book.

At the time, I was in college and had just a dozen Twitter followers and a modest professional network. I immediately set my sights on interviewing people who were far too busy to talk to me. Still, eleven of them did. People are constantly asking about this: How did I get these interviews? Did I have preexisting relationships? Was I somehow everyone's nephew? Did I use some hitherto unknown psychological trick to convince these people to appear in my book? No, to all of the above. I just sent short, honest cold emails, almost 100 of them, to drum up these interviews.

While I did send a lot of requests, I did not send them at random. I did plenty of background research on each person who I considered querying. I thought less about each person's notoriety and more about what unique ideas they could contribute to the book. While every single person who I interviewed was very successful and accomplished, not all of them were famous, or at least not all well-known in the same general circle.

I suppose I did use two small tricks. First, I sent email from my student email address, figuring that both spam filters and busy professionals would be more likely to trust a .edu address. Second, I made sure to include a sentence mentioning something specific that I admire about each person's work. Here is the approximate template:

```
Dear [FirstName],

[1 sentence about their work]

I'm a college student working on a book, “Technical Content Development Handbook,” designed to teach the writing and business skills I've learned writing technical tutorials for clients like FloydHub AI Blog and Smashing Magazine. I would sincerely appreciate a 30-minute interview with you about the craft of writing. I am free any time (central time USA) between now and 1/21, when school starts again, with availability after that date as well on Mondays, Wednesdays, and Fridays. Please let me know if you are interested and, if so, what time and date work for you.
 
Thank you,
 
Philip Kiely
```

I was very flexible on scheduling. One interviewee responded to my email with "would right now work" and I dropped everything to set up my recording equipment and find my list of questions. Some interviewees needed a few rounds of follow-up to schedule and reschedule. Every interview subject was doing me a huge favor by getting on the phone, and I was more than happy to accommodate them however I could.

As for the interviews themselves, I began with lots of preparation. With people like Jeff Atwood and Patrick McKenzie, whose prolific blogging spans decades, I read widely in search of interesting artifacts to ask them about. I read books and articles on subjects I don't understand and topics I mastered long ago to get a sense of each interviewee's style. Only after doing substantial research could I pose interesting, original questions that would inspire fresh insights from these oft-interviewed people to include in my book.

### February 2020: Transcribing and Drafting

Transcribing the interviews was physically difficult. Using an ergonomic mechanical keyboard and a foot pedal (well, re-mapping a button on my mouse and setting it on the floor) made it possible. Transcribing the interviews myself was essential to the writing process later and to my personal development as I now have the collective wisdom of my panel of experts seared into my head from repetition.

I must pause to introduce an important character to these proceedings. My mother has an MFA in Creative Nonfiction from the University of Iowa Writer's Workshop. She has been doing developmental editing, copyediting, technical editing, and proofreading for longer than I've been alive. When I say "I edited the transcripts myself, then sent them to my mother for a proofread," replace that in your mental model of how to write a book with "hire a professional editor to proofread technical content. Budget thousands of dollars." Make this same replacement every time I mention my mother's work. If you are writing a technical book, hire someone like my mother, or just go ahead and hire my mother to edit it.

Each interview, ranging from 30 to 60 minutes, took a few hours to transcribe. Then I sent them to my mother for proofreading, considered her edits, and sent them to the subjects for approval. Although I was receiving back polished transcripts, I did not yet begin incorporating the interview content into my draft. One of the best decisions I made while writing this book was to write a complete draft without referencing the interviews before I added the block quotes. This forced me to fully develop my ideas on my own, create something valuable with my own work, and provide the block quotes something substantial to rest upon when the time came to add them.

In February, I had my first real streak of deep writing for days. I was still on campus at the time, and my draft of beefed-up outlines was about 10,000 words. For seven days, I wrote a chapter a day. I finished my homework by dinnertime, and after dinner sat down at a study table with my friends and typed until it was drafted, however long it took. This is not to say that I published the equivalent of a crammed paper. I had been thinking about this material for weeks, but it still took hours to phrase and type. As you'll read later, the words from these sessions that were eventually published only made it onto the page by surviving three rounds of editing. What's important during this drafting phase is putting enough characters in the file that you will have something to revise later.

### March 2020: Writing

In March, I found out that my college would be sending everyone home due to COVID-19. For the last week on campus and my first week at home, I barely touched the book. One day, I sat down and started writing again, which kicked off a second streak of deep writing that lasted until the book was completely drafted and gave me the momentum for a productive stretch all the way until launch.

There were certain advantages, productivity-wise, to living at home. My classes were suddenly easier and less time-consuming. I was no longer able to spend time hanging out with my friends. What little domestic work (e.g., laundry) that I had to do on campus vanished. At first, I said I was writing three times a day, but it quickly turned into writing all day, every day for a while and then four days a week once classes started. In this manner, I finished my original 30,000 word first draft.

Immediately, I set out to double the length by adding and contextualizing block quotes from my interviews. I built a custom Django application (basically using the admin panel for out-of-the-box CRUD on a relational database) to copy in quotes and assign them to a chapter and interview. After reading through the transcripts and extracting over 100 quotes, I ordered them by chapter and went through the manuscript, adding the quotes in just two days. There were some rough seams that needed to be edited away, but overall using that system helped me remap the interview quotes from their original context into my book. This draft was the longest, at 64,000 words. If I were less technically inclined, I might have reordered index cards in pursuit of the same control.

### April 2020: Editing

As I completed the first draft, I sent it out to a group of friends from college to beta read. Mindful that everyone was busy, I didn't ask anyone to read the whole book. Instead, I assigned chapters by interest and ability so that every chapter would be reviewed at least twice. With their recommendations in hand, I revised each chapter, most of them substantially. I didn't make every change the beta readers suggested, and I made a lot of changes that they didn't ask for, but it was effective to incorporate many sources of feedback relatively early in the editing process.

For the second round, my mother performed a thorough developmental copyedit. Together, we reordered and reimagined the content until it became the book. Where she identified gaps and inconsistencies, I filled them. She also helped me cut thousands of words from the main text, mostly by shortening block quotes. This process shortened the work to 58,000 words, which cut a lot of fluff from the book.

If I had done these stages linearly, it would have added a month or more to the process and added a lot of slack and downtime. Instead, I went through these stages on a chapter-by-chapter basis. In some cases I was doing first- and second-round edits on the same day in different chapters.

### May 2020: Formatting

When I was confident in the content of the book, I printed the manuscript on paper for a final proofread. My mother read first and marked up the pages in ink; I read second and penciled in fixes. I then copied in the hundreds of minor changes. The paper read took five days, copying the changes took two. With the paper proofread done, I declared the book finished, three days before publication. It wasn't perfect, but no book is on release. One keen-eyed reader sent me a list of five errors they found while reading the book, which they said was comparable to books they've read from major technical publishing houses who send each manuscript through multiple rounds with several professional technical editors.

I wrote the book in Markdown, expecting to be able to use pandoc to quickly create a PDF, EPUB, and MOBI versions. Unfortunately, after hours of configuration attempts guided by every blog post on the internet related to the subject, I was only able to make the EPUB (pandoc does not support MOBI, and the PDF had issues no matter how I made it). However, pandoc does a great job converting from Markdown to Microsoft Word (which is how I had been getting track-changes comments from my mother). I used the surprisingly easy to use and capable design and layout tools in Microsoft Word to create exactly the PDF I wanted in about an hour. Calibre handled converting the EPUB into a MOBI, and I was in business. 

The EPUB and MOBI are for applications with their own default styles and fonts, so I paid little attention to customizing those beyond ensuring that the metadata was correct and the images were positioned properly. However, the PDF required some design work. I settled on Baskerville for the font and made some small modifications to the overall look and feel using styles, which are basically rules applied to certain types of text within the document. Again, pandoc does well with Microsoft Word, so the document had straightforward styles that were easy to modify. I also auto-generated a linking table of contents, included page numbers, and set the page size to A5 rather than US Letter paper, more closely matching the size and appearance of a print book. After prepending the cover (commissioned from a classmate at college), the book was complete.

I purchased a block of 10 ISBNs from Bowker, a company granted the exclusive right to act as the ISBN registrar for the United States. I used three of them in registering the three different formats of *Writing for Software Developers*. At the time of writing, two weeks after the book was published, it does not yet appear in registries like ISBNSearch.org even though the book is registered on Goodreads and I have used the ISBN to file for copyright. I thought that Bowker's myidentifiers.com was the worst piece of software I would have to interface with while registering my book, and then I met eCO, the US Government's copyright registration portal.

Despite bad design, an apparent lack of CSS, and truly baffling sessions issues (on Firefox, the only officially supported browser for eCO, which you are also only supposed to access on Windows 7), I diligently filed for copyright on my book. Driven by stories about people's ebooks being uploaded to platforms like Amazon by bad actors and the platforms being reluctant to take them down, I navigated the copyright system and, on my third try, managed to submit an application. Assuming it is approved, I will have the big stick of the DMCA to carry while I speak softly with anyone who wishes to illicitly profit from my book. I'm not particularly concerned with protecting myself against individual piracy; my book is DRM-free and anyone who needs a free copy for financial reasons can email me and get one for free (I have already given away dozens of copies in this matter). Rather, I filed for this copyright in case I need it to defend my work from large platforms.

With everything in place, I uploaded my book to Gumroad and launched it on Tuesday, May 12, 2020, at 8AM.

This post is one of four about [*Writing for Software Developers*](https://wfsd.com/).

1. [The Writing of *Writing for Software Developers*](/essays/writing_wfsd.html) (You are here)
2. [Marketing *Writing for Software Developers*](/essays/marketing_wfsd.html)
3. [Building the *Writing for Software Developers* Landing Page](/essays/wfsd_sales_page.html)
4. [*Writing for Software Developers* Financial Performance](/essays/wfsd_financials.html)