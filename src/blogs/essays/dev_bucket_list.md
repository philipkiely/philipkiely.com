Title: My Software Developer Bucket List
Date: 2019-06-13
Modified: 2019-06-13
Slug: software-bucket-list
Authors: Philip Kiely
Summary: This is a living document. The list will be updated accordingly as I have new ideas that stick around for a while and, much more infrequently, as I actually do anything on this list. Currently the list stands at 8 to do and 2 done...

This is a living document. The list will be updated accordingly as I have new ideas that stick around for a while and, much more infrequently, as I actually do anything on this list. Currently the list stands at 8 to do and 2 done.

Each item inherits standard acceptance criteria. For something to be checked off, I have to ship something, whatever shipping means (literally deploying, merging a PR, solving some problem). If I have help doing something, for example, I write a mobile app at a hackathon with my friends and deploy it, that still counts. The items are in no particular order.

### // ToDo

#### Deploy a mobile app

This one is really straightforward: write an app (probably in Flutter or Swift) and have it accepted on a store (App Store and/or Play Store, depending on the application). I have taken one semester of mobile development, which was taught in Kotlin, and I took a student-lead informal class on Swift my first year, but otherwise I have very little experience with native apps. Mobile development offers opportunities and challenges missing from web development: offline operation, system resources, and the device APIs.

#### Write a programming book

I [write programming tutorials](https://philipkiely.com/essays/posts.html) and other technical content (I strive for those README.md style points). I harbor ambitions of writing a full-length programming book, probably in Django but maybe about something else, as there are already a lot of really good Django books. I have a couple of outlines but nothing sizable completed, but as I develop my skills in both writing and programming the project will come within reach.

#### Build a PC

Building a PC is not super complicated; it’s basically six parts: a CPU, a motherboard, RAM, a GPU, a boot drive, and a power supply. Then add cooling and a case. It can get much more complex from there, especially when systems like water cooling come into the equation, but it is a very doable process. I've watched enough Linus Tech Tips to feel pretty confident that I can complete a standard build.

I love the MacOS operating system, and I prefer to develop on Apple products. I have used a variety of windows 7 laptops at jobs, and I can confidently say that a Windows PC results in a serious decrease in development quality of life for me. However, Windows 10 seems to be a very capable operating system for a variety of tasks. Of course, any PC I would build would have two boot drives: one for Windows 10 and one for Linux.

#### Bug Bounty

A bug bounty program is a channel for responsibly reporting vulnerabilities in software. Google runs the largest individual program, and their rewards for serious vulnerabilities go up to five figures. [Bugcrowd](https://www.bugcrowd.com) is a website that organizes a large number of smaller bounties, offering a unified platform for reporting. Other companies maintain their own programs, both public and unofficial.

Discovering and exploiting a bug takes serious knowledge. You have to know common vulnerabilities and where they might manifest, and then poke the code until something breaks in a meaningful way. While I don’t have deep security knowledge, I have taken a couple of classes in the subject. I have written a bunch of web apps; then patched my own security bugs. I know the basics of where to look. The great thing about bug bounties is that new software gets written every day, and a non-zero amount of it is broken in interesting ways. All I need to do is find it.


#### Contribute to a piece of OSS that I use regularly

I wrote about my first experience with improving an open source tool [here](https://philipkiely.com/essays/first-open-source.html). However, that was a fairly minor improvement with a major structural change, so I did not attempt a pull request to integrate my changes back into the main repository because the result was so different from the original.

Arbitrarily outlining criteria for this project, I would classify success as the acceptance of a pull request to the master branch of an active project with 1000 or more stars on GitHub where the pull request contains a new feature, extension, documentation, or non-trivial bug fix.

#### Go Low

This category is incredibly vague. Most stuff I've developed is pretty standard and high level: CRUD web apps, responsive pages, and Python implementations of standard algorithms. While I'm not a researcher or an embedded developer (usually, if physics is something I have to think about while programming, I've gone too low), I strive to one day write something substantial in a language where I do my own memory management. Thanks to CS 213 (operating systems), I have the foundation to do this, all I need is something that I want to work on where using C is the best (meaning probably the only) option.

#### Serious Automation

I listen to [podcasts](https://www.relay.fm) about automation, power user features, and new releases while I commute. I write most of my code in scripting languages and I use Terminal.app an appropriate amount for a programmer. Despite this, I have very few real automations that I made myself (although this blog has required a few new ones). While of course I harbor fantasies of creating J.A.R.V.I.S. (voiced by Paul Bettany), I think Apple and Amazon might beat me there. However, I think I can get to the point where the entirety of my keyboard falls under "don't touch that, you don't know what it does." Or, I'll just get into iOS shortcuts, who knows. I'm particularly interested in automation for email and other communication, work and productivity enhancement, and daily logistics. This description is pretty vague, so I'll say the acceptance criteria is having enough personal automations written to keep an EC2 instance or a Mac Mini sitting in the corner fairly busy.

### Make a game 

I rarely play video games, mostly I play Kart or Smash socially at school or in the conference room after work. I'm really bad at video games, mostly because I don't play often, but partially because most video games require an impossible-for-me controller grip (actually alleviated for Kart and Smash by a classic gamecube controller). I am also aware of the difficult economics of the video game industry and the incredible odds against even a moderately successful independent video game project. None of that stops me from the cliché software developer reaction of looking at a simple or even complicated game and saying "I should make something like that." Whatever. That's what bucket lists and hackathons are for.

### git commit -m "Done"

#### Win a prize at a hackathon

I've been to four hackathons (really, two hackathons twice each). HackISU in spring 2017 was a turning point in my interest in computer science. Then, Hack UIowa fall 2017 was the first time that I won something, and the same event led to my first development job. I've been back to each since, and won two more category prizes at Hack UIowa.

A fair extension to this entry is to attend a Hackathon out of state, and another is to place in the top three rather than winning a category prize. This is why lists like these are never finished.

[More on hackathons here](https://philipkiely.com/essays/hackathon.html).

#### Deploy a website on a cloud hosting platform

[GrammieGram](https://grammiegram.com) was the first. It started on Digital Ocean and I changed it over to AWS. I've done a few others on AWS since then. Every time I deploy a website on AWS, I use Elastic Beanstalk to make sure everything is in place and communicating nicely, but recently I've branched out to using AWS Lambda and related services as well.
