# https://philipkiely.com

This repository contains the static site generator and source files that power my personal website, https://philipkiely.com

The code for this site is open-source under the MIT license, but the content (blog posts, sales page copy, original images, etc) is copyright Philip Kiely & Company, please don't reproduce that part.

## Getting Started

Requires Python 3.7+ and a virtual environment.

### First Install

```
git clone git@github.com:philipkiely/philipkiely.com.git
cd philipkiely.com
mkvirtualenv philipkiely.com
pip install -r requirements.txt
npm i
```

Note: you also need Dart Sass. If you're using MacOS, you should have already installed this as part of the general PK&C getting started flow, but if not it is `brew install sass/sass/sass`

### Work on Stuff

```
cd /path/to/philipkiely.com
workon philipkiely.com
python colander.py --dev
```

If it wasn't automatically launched, go to [http://127.0.0.1:8000](http://127.0.0.1:8000) to see the site.

Use `Control-C` in terminal to quit.

When you edit site files, it will automatically rebuild. You must refresh the page to see changes. If you're working with static assets and don't see changes, clear caches and refresh.

If you make changes to the build script, you must quit and re-run it.

If you need a new branch (make new branches from main):

```
git checkout -b my_branch
```

From there, stay on your branch as you work.

Make a commit:

```
git add .
git commit -m "your commit message here (short but descriptive)"
git push origin my_branch
```

### Create a Pull Request (PR)

1. Go to [https://github.com/philipkiely/philipkiely.com](https://github.com/philipkiely/philipkiely.com).
2. Click on the "pull request" tab and then the "new pull request" button
3. Choose your branch to compare
4. Make the PR
5. Give it a title and description.

### Merge the Site

Write descriptive commits and pull requests.

Use GOMP and make sure that all commits are squashed into one before rebasing. Do not merge directly, instead rebase to merge.

Make sure you update the version and any relevant dates.

The pull request will be live once rebased onto main.

Pull Request Checklist:

[] Update version and dates
[] Run `python href_checker.py` to check for broken links
[] Commits squashed into one
[] Rebase, don't merge, into main
[] Spot check live site after ~60 seconds

### Deploy the Site from Main

Note: you probably shouldn't need to do this unless your name is in the URL.

From main, run `python colander.py --deploy`.

This reminds for version and date (type "yes") and then prompts for a commit message.

Netlify deploys the site directly from the main branch.

## Colander

Colander, named for the kitchen utensil used to strain spaghetti, is the meta static site generator that orchestrates the other generators. It is responsible for:

* Running each underlying generator at the appropriate time
* Performing ad-hoc tasks like asset copying and static checking (any of which may be factored out into future packages)
* Unifying the development environment to make a smooth developer experience

### Pages (Jinja)

Generates most standard pages including the main page.

### Blogs

Accepts markdown posts with metadata and renders them.

### Singletons

Directly copy old pages including assets, maintaining relative paths.

### Corvette

Autoindex directory listing for `/assets/`. Modify with `corvetteconf.py` and `theme/templates/corvette.html`.

### Corvair

Still under development.

### Images & Asset Files

Assets folder structure for images models rest of source to make images easier to find.

Within `assets/img` the following folder structure applies:

* blogs
  * posts
    * post.slug for post in posts where post.images >= 2
  * notes
    * Same as above
* pages
  * page.url
* individual images

If an image is used in multiple pages, put it at the deepest folder accessible to all applicable pages.

### CSS

The site uses SCSS for more customizable CSS. This gets turned into CSS during the build process. The build also includes an autoprefixer. At the moment, there is no purging or minifying.

The CSS imports Bootstrap 5 and other libraries like heropatterns, installed with NPM. 

The main CSS file is `style.scss` which becomes `style.css` and is available on all pages through `base.html`.

Individual pages may have their own SCSS file, for example `assets/scss/cefip.scss` is loaded by `src/cefip.html`.

### JavaScript

JavaScript is front-end only. At the moment, the site doesn't use any frameworks like React or anything, but it does support using NPM packages.

The build uses browserify to load packages like Bootstrap's JavaScript in the front end. Each JS file has an associated bundle file that specifies its dependencies. This makes it quick to change individual files.

The main JavaScript file is `script.js` with an associated `bundle.js` and is available on all pages thanks to the `base.html` template.

Individual pages may have their own JS file, for example `assets/js/cefip.js` to correspond with `src/cefip.html`.

### Theme

Jinja templates are a base for blogs and pages.

## Netlify Deploy

This site uses Netlify and GitHub and tracks everything deploy-related using `netlify.toml` to maintain infrastructure as code.

Do not make any configuration changes via the netlify UI, only make programmatic changes to `netlify.toml`.
