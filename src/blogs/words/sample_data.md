Title: Improving Technical Tutorials by Providing Sample Data
Date: 2020-04-22
Modified: 2020-04-22
Slug: sample_data
Authors: Philip Kiely
Summary: Let's say you're writing a technical tutorial. If you have a sample application in your article, you should also include sample data. In Django, you can distribute sample data using fixtures.

Let's say you're writing a technical tutorial (or if you're really fancy, a video tutorial) about how to do something in Django. This post should be applicable to the web framework of your choice, but I'll use Django as an example because I usually write about Django. Django's fixtures make this process easy, I hope that your framework of choice has a comparable feature or available package.

Anyway, you're writing a technical article, so you're probably whipping up a nice simple example project, maybe a todo list. Your readers will begin the tutorial by cloning the repository from GitHub and getting the application up and running in their dev environment. Assuming nothing went wrong, in a couple of minutes they are ready to go through your article and take in whatever aspect of developing in Django you have written about. Our scene is set.

**If you have a sample application in your article, consider including sample data.**

Without sample data, after your reader has set everything up, they load the application on localhost and see ... probably very little. While the database is set up, it is mostly empty, except for the superuser you may have had them create so that they can access the admin panel. The first thing you'll need to direct your readers to do is add a few rows to the database, possibly first requiring the implementation of a function to do so. Sometimes, this is fine, but often it is just more boilerplate in between your reader and the point of your article. This is where distributing sample data can come in handy: you can present the application in any state.

I used this technique in [a tutorial on front-end development](https://www.smashingmagazine.com/2020/04/django-highlights-templating-saves-lines/) and [another on models and admin](https://www.smashingmagazine.com/2020/04/django-highlights-models-admin-relational-database/) for Smashing Magazine. It made the process of writing both articles much smoother. In the first tutorial, I used a fixture to fill in a table presented in the template I was recreating. In the second link, I created a few example books and patrons so that readers could instantly see how the models connected when poking around in the admin panel.

**In Django, you can distribute sample data using fixtures.**

A [fixture](https://docs.djangoproject.com/en/3.0/howto/initial-data/) is some sort of formatted text file (I use JSON) that contains structured data that Django's admin can read into the database.

You create this data using [dumpdata](https://docs.djangoproject.com/en/3.0/ref/django-admin/#django-admin-dumpdata)

Your readers use the data using [loaddata](https://docs.djangoproject.com/en/3.0/ref/django-admin/#django-admin-loaddata).

Using fixtures, you can make a dump of only some tables from the database, and if the included options aren't enough you can generate or modify the data in your text editor. For the todo list example, you could distribute only data for the todos model without including anything from your users table.

Fixtures are mostly intended for testing, not distributing sample data with an article, so there are a few things you need to keep in mind. First, fixtures do not update with migrations, so you must ensure that the data you distribute has the same schema as the the database your readers will be using. Also, IDs and foreign keys are hardcoded. Django generates primary key ids sequentially, so if you create a superuser as your first user and instruct your readers to do the same, you will want to remove your superuser from the data dump. The trick with using fixtures in a technical tutorial is to have your reader load them at the correct time and check that everything works with a run-through of the article in a clean environment prior to publication.

For more on technical content development, check out my book, *[Writing for Software Developers](/wfsd)*