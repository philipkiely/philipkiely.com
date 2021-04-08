# https://philipkiely.com

This repository contains the static site generator that powers my personal website, https://philipkiely.com

## Getting Started

Requires Python 3.7+ and a virtual environment.

### First Install

```
git clone $THIS_REPO
cd philipkiely.com
mkvirtualenv philipkiely.com
pip install -r requirements.txt
```

### Work on Stuff

```
cd /path/to/philipkiely.com
workon philipkiely.com
python colander.py --dev
```

Go to [http://127.0.0.1:8000](http://127.0.0.1:8000) to see the site.

If you need a new branch (make new branches from main):

```
git checkout -b my_branch
```

### Create a PR & Site Preview

Descriptive commits & PR

rebase & Squash (Use GOMP)

### Deploy the Site

Note: you probably shouldn't need to do this unless your name is in the URL.

From main, run `python colander.py --prod`.

## Colander

Colander, named for the kitchen utensil used to strain spaghetti, is the meta static site generator that orchestrates the other generators. It is responsible for:

* Running each underlying generator at the appropriate time
* Performing ad-hoc tasks like asset copying and static checking (any of which may be factored out into future packages)
* Unifying the development environment to make a smooth developer experience

## Main (Jinja)

Most stand-alone pages

## Blog

A modified Jinja with Markdown to HTML

## Singleton

Old stuff gets copied straight in

## Corvette

/assets auto-generated

corvetteconf.py

## Corvair

Sitemaps, to be developed

## Assets

Assets folder structure for images models rest of source to make images easier to find.

Site-wide and template-specific CSS, JS, and images are stored in src/static.

## Theme

## Netlify Deploy

This site uses Netlify and GitHub and tracks everything deploy-related using `netlify.toml` to maintain infrastructure as code.

Do not make any configuration changes via the netlify UI, only make programmatic changes to `netlify.toml`.