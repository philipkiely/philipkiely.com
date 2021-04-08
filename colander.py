import datetime
from jinja2 import Environment, FileSystemLoader, select_autoescape
import markdown
import os
import signal
import subprocess
import sys
import time
import webbrowser
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

##################
# BLOG GENERATOR #
##################

def parse_article_metadata(filename): # TODO
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
    parsed["summary"] = meta[5].split(": ")[1]
    if len(meta) == 7:
        parsed["note"] = meta[6].split(": ")[1]
    parsed["content"] = markdown.markdown("\n\n".join(
        contents.split("\n\n")[1:]), extensions=['extra'])
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


def blogs():
    blogs = subprocess.run(
        ["ls", "src/blogs"],
        capture_output=True
    ).stdout.decode('utf-8').split('\n')
    blogs = [b for b in blogs if b != ""]
    for blog in blogs:
        os.makedirs(os.path.dirname("dist/" + blog + "/"), exist_ok=True)
        posts = subprocess.run(
            ["ls", "src/blogs/" + blog],
            capture_output=True
        ).stdout.decode('utf-8').split('\n')
        posts = [p for p in posts if p != ""]
        articles = []
        for post in posts:
            articles.append(parse_article_metadata(blog + "/" + post))
        articles.sort(key=lambda x: x["modified"], reverse=True)
        build_index(blog, articles)
        for article in articles:
            build_article(blog, article)
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
    pages = subprocess.run(
        ["ls", "src/pages/"],
        capture_output=True
    ).stdout.decode('utf-8').split('\n')
    pages = [p for p in pages if p != '' and p != 'index.html']
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

# Increment Patch Version in Footer
def version(): # TODO: Meta dict passed into all jinja
    f = open(root+"dev/theme/templates/base.html", "r")
    page = f.read()
    f.close()
    delim = "<!--PATCH-->"
    page = page.split(delim)
    page[1] = str(int(page[1]) + 1)
    page = delim.join(page)
    f = open(root+"dev/theme/templates/base.html", "w")
    f.write(page)
    f.close()
    print("Patch Version Incremented")

# Copy Over Assets
def assets():
    if os.path.exists("dist/assets"):
        os.system("rm -r dist/assets/*")
    else:
        os.makedirs("dist/assets")
    os.system("cp -r assets/* dist/assets/")
    os.system("cp -r theme/assets/* dist/assets/")
    os.system("cp theme/assets/img/favicon.ico dist/")
    os.system("cp theme/assets/img/favicon.png dist/")
    print("Assets Copied\n")

# Copy Over Singles
def singles():
    os.system("cp -r src/singles/ dist/")
    print("Singles Copied\n")

# Run Corvette Autoindex
def corvette():
    os.system("python -m corvette corvetteconf.json")
    print("Corvette Revved")


##################
# NETLIFY DEPLOY #
##################

def build_site():
    clean_dist()
    blogs()
    pages()
    singles()
    assets()
    corvette()
    # Corvair


def deploy_site():
    os.system("git checkout prod")
    os.system("git rebase main")
    os.system("git push origin prod")
    os.system("git checkout main")


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
        build_site()


if __name__ == "__main__": # TODO: Git Helpers
    if len(sys.argv) != 2:
        print("Usage: `python colander.py --dev` or `python colander.py --prod`")
        exit
    elif sys.argv[1] == "--prod":
        build_site()
    elif sys.argv[1] == "--dev":
        print("Initializing PK")
        src_watcher = Watcher(".", PKHandler())
        build_site()
        server_proc = subprocess.Popen(
            ["python", "-m", "http.server", "--directory", "dist"])
        webbrowser.open("http://127.0.0.1:8000")
        src_watcher.run()
        if server_proc.pid:
            os.kill(server_proc.pid, signal.SIGTERM)
    else:
        print("Usage: `python colander.py --dev` or `python colander.py --prod`")
        exit
