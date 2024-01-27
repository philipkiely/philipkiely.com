import datetime
from jinja2 import Environment, FileSystemLoader, select_autoescape
import markdown
import os
import signal
import subprocess
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#####################
# UTILITY FUNCTIONS #
#####################

def ls(path, ignore=[]):
    names = subprocess.run(
        ["ls", path],
        capture_output=True
    ).stdout.decode('utf-8').split('\n')
    return [n for n in names if n != "" and n not in ignore]

##################
# BLOG GENERATOR #
##################

def parse_article_metadata(filename):
    f = open("src/blogs/" + filename, "r")
    contents = f.read()
    f.close()
    meta = contents.split("\n\n")[0].split("\n")
    parsed = {}
    parsed["title"] = meta[0].split(": ")[1]
    parsed["date"] = datetime.datetime.strptime(
        meta[1].split(": ")[1], "%Y-%m-%d")
    parsed["modified"] = datetime.datetime.strptime(
        meta[2].split(": ")[1], "%Y-%m-%d")
    parsed["slug"] = meta[3].split(": ")[1]
    parsed["authors"] = [meta[4].split(": ")[1]]
    parsed["summary"] = markdown.markdown(meta[5].split(": ")[1])
    parsed["blog"] = filename.split("/")[0]
    parsed["content"] = markdown.markdown("\n\n".join(
        contents.split("\n\n")[1:]), extensions=['extra', 'codehilite'])
    return parsed


def generate_page(template, route, **kwargs):
    env = Environment(
        loader=FileSystemLoader(["theme/templates/"]), # TODO: Essays, Notes, etc each have own index with shared base in templates, unsure where own files live
        autoescape=select_autoescape(["html", "xml"]), # TODO: Ought to break out base into multiple bases and have pluggable header, footer, etc as separate files to justify templates folder.
        auto_reload=True
    )
    html = env.get_template(template).render(kwargs)
    f = open("dist/{}.html".format(route), "w")
    f.write(html)
    f.close()


def build_article(blog, article):
    generate_page(
        "article.html",
        blog + "/" + article["slug"],
        article=article
    )


def build_index(blog, articles):
    generate_page(
        "blog_index.html",
        blog + "/" + "index",
        articles=articles
    )

def build_bytes():
    os.makedirs(os.path.dirname("dist/bytes/"), exist_ok=True)
    posts = ls("src/blogs/bytes")
    articles = []
    for post in posts:
        f = open("src/blogs/bytes/" + post, "r")
        contents = f.read()
        f.close()
        meta = contents.split("\n\n")[0].split("\n")
        parsed = {}
        parsed["title"] = meta[0].split(": ")[1]
        parsed["date"] = datetime.datetime.strptime(
            meta[1].split(": ")[1], "%Y-%m-%d")
        parsed["slug"] = meta[2].split(": ")[1]
        parsed["content"] = markdown.markdown("\n\n".join(
            contents.split("\n\n")[1:]), extensions=['extra', 'codehilite'])
        articles.append(parsed)
    articles.sort(key=lambda x: x["date"], reverse=True)
    generate_page(
        "bytes_index.html",
        "bytes/index",
        articles=articles
    )
    for article in articles:
        generate_page(
            "byte.html",
            "bytes/" + article["slug"],
            article=article
        )

def blogs():
    blogs = ["words", "code"]
    for blog in blogs:
        os.makedirs(os.path.dirname("dist/" + blog + "/"), exist_ok=True)
        posts = ls("src/blogs/" + blog)
        articles = []
        for post in posts:
            articles.append(parse_article_metadata(blog + "/" + post))
        articles.sort(key=lambda x: x["date"], reverse=True)
        build_index(blog, articles)
        for article in articles:
            build_article(blog, article)
    #build_bytes()
    print("Blogs built")

################
# JINJA BUILDS #
################

# Render Individual pages from base templates
def pages():
    # Load folder and templates
    env = Environment(
        loader=FileSystemLoader(
            ["src/pages/", "theme/templates/"]),
        autoescape=select_autoescape(["html", "xml"]),
        auto_reload=True
    )
    # list pages, dropping index (handled separately) and empty
    pages = ls("src/pages/", ["index.html", "404.html"])
    # Each page should be put as index for pretty URLs
    for page in pages:
        html = env.get_template(page).render()
        url = page[:-5] # Drop .html
        os.makedirs(os.path.dirname("dist/" + url + "/"), exist_ok=True)
        f = open("dist/" + url + "/index.html", "w")
        f.write(html)
        f.close()
    # Handle index as special case
    html = env.get_template("index.html").render()
    f = open("dist/" + "index.html", "w")
    f.write(html)
    f.close()
    # Handle 404 as special case
    html = env.get_template("404.html").render()
    f = open("dist/" + "404.html", "w")
    f.write(html)
    f.close()
    print("Jinja Built")


#############
# OTHER SSG #
#############

# Clear out dist for rebuild
def clean_dist():
    if os.path.exists("dist"):
        os.system("rm -r dist/*")
    else:
        os.makedirs("dist")

# Copy Files and Images
def files_and_images():
    os.system("cp -r assets/files dist/assets/files")
    os.system("cp -r assets/img dist/assets/img")
    os.system("cp assets/img/favicon.ico dist/")
    os.system("cp assets/img/favicon.png dist/")

# Prod Assets
def assets_prod():
    if os.path.exists("dist/assets"):
        os.system("rm -r dist/assets/*")
    else:
        os.makedirs("dist/assets")
    files_and_images()
    os.system("npx sass --load-path=node_modules assets/style.scss dist/assets/style.css")
    os.system("npx sass --load-path=node_modules assets/scss:dist/assets/css")
    os.system("npx postcss -u autoprefixer -r dist/assets/**/*.css")
    os.system("cp -r assets/js dist/assets/js")
    os.system("cp assets/script.js dist/assets/script.js")
    os.system("npx browserify -p tinyify assets/bundle.js -o dist/assets/bundle.js")
    # If I need a single-page import, make bundle-page.js in assets/js to go with page.js
    #scripts = ls("assets/js")
    #for s in scripts:
    #    os.system("npx browserify assets/js/{} -o dist/assets/js/{}".format(s, s))
    print("Assets Copied\n")

# Faster Dev Assets
def assets_dev():
    if os.path.exists("dist/assets"):
        os.system("rm -r dist/assets/*")
    else:
        os.makedirs("dist/assets")
    files_and_images()
    os.system("sass --load-path=node_modules assets/style.scss dist/assets/style.css")
    os.system("sass --load-path=node_modules assets/scss:dist/assets/css")
    os.system("npx postcss -u autoprefixer -r dist/assets/**/*.css")
    os.system("cp -r assets/js dist/assets/js")
    os.system("cp assets/script.js dist/assets/script.js")
    os.system("npx browserify assets/bundle.js -o dist/assets/bundle.js")
    print("Assets Copied\n")

# Copy Over Singles
def singles():
    os.system("cp -r src/singles/* dist/")
    print("Singles Copied\n")

# Run Corvette Autoindex
def corvette():
    os.system("python -m corvette corvetteconf.json")
    print("Corvette Revved")


##################
# NETLIFY DEPLOY #
##################

def build_site(prod):
    clean_dist()
    blogs()
    pages()
    singles()
    if prod:
        assets_prod()
    else:
        assets_dev()
    corvette()
    # Corvair


def deploy_site_from_main():
    p = input("\nHave you incremented your version, blog post dates, and footer date yet?\n\nAdmit: ")
    if p != "yes":
        return None
    msg = input("Commit Message: ")
    os.system("git add .")
    os.system("git commit -m \"{}\"".format(msg))
    os.system("git push origin main")


###############
# LIVE RELOAD #
###############

class Watcher:

    def __init__(self, directory=".", handler=FileSystemEventHandler()):
        self.observer = Observer()
        self.handler = handler
        self.directory = directory

    def run(self):
        self.observer.schedule(
            self.handler, self.directory, recursive=True)
        self.observer.start()
        print("Watcher Running in {}/".format(self.directory))
        try:
            while True:
                time.sleep(1)
        except:
            self.observer.stop()
        self.observer.join()
        print("\nWatcher Terminated")


class PKHandler(FileSystemEventHandler):

    def on_any_event(self, event):
        if event.is_directory or "/dist/" in event.src_path:
            return None
        elif "/assets/" in event.src_path:
            assets_dev()
        else:
            blogs()
            pages()
            singles()
            corvette()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: `python colander.py [--dev, --deploy, --prod]`")
        exit
    elif sys.argv[1] == "--prod":
        build_site(prod=True)
    elif sys.argv[1] == "--deploy":
        deploy_site_from_main()
    elif sys.argv[1] == "--dev":
        print("Initializing PK")
        src_watcher = Watcher(".", PKHandler())
        build_site(prod=False)
        server_proc = subprocess.Popen(
            ["npx", "netlify", "dev"])
        src_watcher.run()
        if server_proc.pid:
            os.kill(server_proc.pid, signal.SIGTERM)
    else:
        print("Usage: `python colander.py [--dev, --deploy, --prod]`")
        exit
