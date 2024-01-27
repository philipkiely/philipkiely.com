Title: The Undergraduate's Guide to Becoming a Professional Developer
Date: 2021-08-28
Modified: 2021-08-28
Slug: professional_skills
Authors: Philip Kiely
Summary: The skills needed to get and succeed at a software development internship or job are somewhat different than the skills that most computer science classes teach. In some cases, classes teach exactly the opposite of what you need for a job. In my opinion, the job skills are substantially easier than the class skills and you can pick them up quickly.

Having achieved the first steps toward success in my career, I sometimes find myself giving advice to college students. This post distills the most essential advice so that kids can get off my lawn more expediently.

The fundamental issue is that the skills needed to get and succeed at a software development internship or job are somewhat different than the skills that most computer science classes teach. In some cases, classes teach exactly the opposite of what you need for a job. In my opinion, the job skills are substantially easier than the class skills and you can pick them up quickly.

I got my first programming job at 18 years old, before many of my friends who were much better computer science students than I was, because I understood these skills. Because people told me about them. Like I'm telling you.

One quick note before we get started is that this is not a blog post written to flame undergraduate computer science curriculums or pedagogy or to be cynical about the type of work software developers do. Most classwork is very effective at what it teaches. And class skills can be very helpful in the workplace. Especially when you get to do unique and interesting things which many jobs offer. But without job skills, you'll have trouble giving your class skills the opportunity to shine.

## Other People's Code

Most classroom assignments are analogous to something called "green-field projects:" when you build something starting from scratch. The professor says, "Here is this wonderful blank file, go ahead and implement mergesort in Java." Or, the boss says, "Hey, we need a mobile app, go write one."

In most workplaces green-field projects are rare, especially for interns and new developers. It is incredibly rare that you would work on one by yourself. Instead, you spend most of your time building on other people's code.

In school, they go a step further and say you have to write your own code. You can't just use your language's standard library sorting function because that wouldn't teach you anything, you have to write it yourself. In the so-called real world, writing your own code is hard and takes a long time and results in way more code to maintain so you generally don't do it. You use other people's code whenever you can.

Two great sources of other people's code are libraries and frameworks. I use these things all of the time. There are external libraries and frameworks maintained by third parties, and internal libraries that your company maintains itself. That means with the passage time even code you write could become like "other people's code" in that you re-use it rather than writing new code. Outside of class, every project I've ever built solo or worked on in a team has relied on a great number of libraries and frameworks, otherwise I wouldn't have gotten any of them done.

Another great source of other people's code is, without loss of generality, Stack Overflow. Sometimes these snippets can be difficult to place in context or use without documentation, but solving a problem yourself is slower than using someone else's solution. In school, using someone else's code is cheating. In the workplace, **as long as the code you're using is appropriately licensed,** using someone else's code is how you get your job done.

Of course, there is more to programming than copying and pasting other people's code. You have to know which code to copy and paste. And then once you've copied and pasted it, you have to know what to do with it.

## Glue Code

When you have two chunks of other people's code, whether from libraries or stack overflow or frameworks or APIs or the stuff last year's intern wrote, usually they don't play nice out of the box. So you have to write something called "glue code" to stick them together. Glue code is pretty different from what you're used to writing in class.

Usually, you have to take output from one system and re-format it to make it valid input for another system. These programs bridge the interstitial space between the bricks you build your software with; a digital mortar.

Also once you write this code you have to test it. Which is really another entire blog post. But carefully thinking through the potential inputs to a system and its expected outputs is actually a skill that I was fortunate to be taught in class as tests were often required on assignments. However, testing your code (and everything elseing your code) now requires thinking about it in the context of the broader application.

## Development Environment

This sounds like a detour but I promise it isn't. For your first 2 days (if you're lucky) or 2 weeks (or more if you are particularly unlucky or work for a very enterprisey company), any time not spent in onboarding meetings be mostly devoted to setting up your development environment. Before you get to glue together other people's code, you have to set up your computer so that you can actually work on stuff. A development environment must provide three pairs of things:

* A way to write your code, and
* A way to read other people's code in context.
* A way to run your code, and
* A way to see how it interacts with other people's code. 
* A way to save versions your code, and
* A way to reconcile changes you make with changes other people make.

What provides these functions varies wildly depending on what you're making. Generally, you have a text editor to write code in and a terminal to run it from, though some development environments use tools that provide both (an integrated development environment or IDE).

Sometimes you get a computer that is set up for you which is nice. Certainly, you want the right general software and permissions out of the box along with precise and updated documentation about the steps you need to take. But I think that setting up your own development environment is a valuable exercise because it teaches you about the context you're writing code in. Installing tools and dependencies (other people's code) yourself lets you know what to reach for first to solve your problems.

You know your development environment is set up when you can run whatever programs you're going to be working on locally (on your own computer) and they work the same as they do live (on the production servers). Having your local environment closely match the live environment is essential because it gives you confidence that the code you write locally will still work once it is deployed.

The final key piece of your development environment is version control. Without knowing your job, I can say your version control will probably be Git via GitHub or maybe GitLab. Learning how to use Git confidently is among the highest returns on investment an aspiring developer can get on a single afternoon spent learning.

In school, your code is done when it works on your computer and you send it to the professor. At work, your code is done when it is reviewed and shipped. Being able to execute Git workflows yourself means you won't be dependent on other people to check in your code. While you may or may not be able to deploy to production yourself, at minimum being able to run your code in a live staging environment without help will greatly boost your productivity and perceived competence.

As you learn Git and its associated tools, focus on how they work when collaborating with multiple developers. Understand how to check out code at a certain point in time, make changes, and reconcile your changes with changes that other developers made while you were working.

## Projects

A natural question is, "Hey Philip, this all sounds great, but how do I develop these skills and then communicate them to potential employers."

Projects, mostly.

Make a GitHub with your real name or a professional alias. A personal website is cool but not strictly necessary. Demonstrate that you have these skills by putting your projects on GitHub. Final projects from class can be a good fit if publishing the code after is allowed. Hackathons are good for this. So is just making stuff with your friends. You don't need a bunch of projects. You don't need huge projects. But 3-5 projects that go beyond basic tutorials and show that you can glue together other people's code in a development environment are proof to a potential employer that you have these skills. (Also, list these projects on your resume with links and short, keyword-heavy descriptions.)

This is an overgeneralization but smaller companies — who really appreciate when you show up with these skills — are also more likely to actually take a look at your projects. Same goes when you get a referral to any company or are able to talk to your prospective boss directly during the hiring process. And small companies or direct referrals are, in my experience, where a lot of students get their first jobs.

There are plenty of other skills that go into being a professional developer. But if you can make these job skills part of your repertoire you'll have a much smoother time getting and excelling in your first job.
