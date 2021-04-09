Title: Get Started with Python Watchdog
Date: 2021-04-09
Modified: 2021-04-09
Slug: python_watchdog
Authors: Philip Kiely
Summary: The [Watchdog library](https://github.com/gorakhargosh/watchdog) in Python is a fantastic open-source tool for writing programs that monitor for and respond to changes in a filesystem. This short guide gets you up and running with a `Watcher` object to use Watchdog's powerful capabilities in your own projects.

The [Watchdog library](https://github.com/gorakhargosh/watchdog) in Python is a fantastic open-source tool for writing programs that monitor for and respond to changes in a filesystem. This short guide gets you up and running with a `Watcher` object to use Watchdog's powerful capabilities in your own projects. Then, we cover important parts of the Watchdog API to adapt the example for your own needs.

## Requirements

This tutorial is written for Python 3.6+ for Watchdog 2.0.z. I've run this code on MacOS 11 and Linux (Ubuntu) without issue, I have no idea whether it would work on Windows.

Before we begin, run `pip install watchdog`.

Copy the following into your project (don't worry, I'll break down this code in the next section).

```python
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Watcher:

    def __init__(self, directory=".", handler=FileSystemEventHandler()):
        self.observer = Observer()
        self.handler = handler
        self.directory = directory

    def run(self):
        self.observer.schedule(
            self.handler, self.directory, recursive=True)
        self.observer.start()
        print("\nWatcher Running in {}/\n".format(self.directory))
        try:
            while True:
                time.sleep(1)
        except:
            self.observer.stop()
        self.observer.join()
        print("\nWatcher Terminated\n")


class MyHandler(FileSystemEventHandler):

    def on_any_event(self, event):
        print(event) # Your code here

if __name__=="__main__":
    w = Watcher(".", MyHandler())
    w.run()
```

## Example Program

This code is boilerplate for any program that needs to monitor a folder and react when files are changed. Here are some example use cases:

* A file management program for ingesting and processing files such as images from an SD card.
* A static site generator development environment watches for changes to the source code and rebuilds the site on save.
* Various home and workplace automation tasks

Essentially, your Watchdog is two parts: a `Watcher` and a `Handler`. The `Watcher` object initializes and manages monitoring the specified folder (and its subfolders). The `Handler` object applies your code to determine what to do in response to events. Let's take a closer look at each.

```python
class Watcher:

    def __init__(self, directory=".", handler=FileSystemEventHandler()):
        self.observer = Observer()
        self.handler = handler
        self.directory = directory
```

The `Observer()` object is doing most of the work here, but it will need to be configured with a directory to watch (it also keeps an eye on all of the subdirectories) and a handler, which you'll write yourself.

```python
def run(self):
    self.observer.schedule(
        self.handler, self.directory, recursive=True)
    self.observer.start()
    print("\nWatcher Running in {}/\n".format(self.directory))
    try:
        while True:
            time.sleep(1)
    except:
        self.observer.stop()
    self.observer.join()
    print("\nWatcher Terminated\n")
```

First, we configure the observer. After starting the observer, sleep until the program is quit, then stop and join the observer to clean up. 

This could end on a different condition. You could have the watcher run for a certain period of time or until a function returns some value.

```python
class MyHandler(FileSystemEventHandler):

    def on_any_event(self, event):
        print(event) # Your code here
```

This is where your unique code goes! Check out the API reference in the next section to understand what to put here.

```python
w = Watcher(".", MyHandler())
w.run()
```

Initialize the `Watcher` object with a target directory and a `Handler` object, then run it. `w.run()` will continue until quit, so call any functions from the handler as lines after `w.run()` will not execute until the user hits `Control-C` (useful for things like killing subprocesses).

## Partial API Reference

Watchdog has plenty of capabilities, but the code you write with the above example will mostly interface with the `FileSystemEvent` object and its derivatives, so that's what I've documented a selection of here. You can see the source code [on this page on GitHub](https://github.com/gorakhargosh/watchdog/blob/master/src/watchdog/events.py).

### event.event_type | str

The `event_type` parameter is one of five options listed below:

```python
types = ['created', 'deleted', 'modified', 'moved', 'closed']
```

To be honest, I've never had cause to use `moved` or `closed` but I assume they're useful otherwise the library wouldn't have them. The `modified` event only triggers when the file is saved (written to) so if you're using a program with autosave it might fire often.

```python
class MyHandler(FileSystemEventHandler):

    def on_any_event(self, event):
        if event.event_type == "deleted":
            print("Oh no! It's gone!")
```

This parameter is quite useful for flow control, you may want to take different actions when a file is created than when it is deleted.

Depending on your use case, you might be better served by swapping `on_any_event` for `on_created`, `on_deleted`, and so on for the five event types.

### event.src_path | str

The `src_path` parameter is a string with the **absolute path** to the file or folder that has experienced the event.

```python
class MyHandler(FileSystemEventHandler):

    def on_any_event(self, event):
        if event.src_path[-5:] == ".docx":
            print("Microsoft Word documents not supported.")            
```

I use this parameter for filtering; I often need to ignore events from certain directories or file types.

### event.is_directory | bool

The `is_directory` parameter is a boolean to let you know if the event came from a folder (True) or file (False).

```python
import os

class MyHandler(FileSystemEventHandler):

    def on_any_event(self, event):
        if event.is_directory:
            os.system("cp -r {} ~/folders".format(event.src_path))
        else:
            os.system("cp {} ~/files".format(event.src_path))
```

This information can be useful for flow control or to avoiding taking an incorrect action on a folder.

More often, I use this parameter to avoid duplicating event handling. Many events that affect a file also affect the directory that it is in (for example, creating a file creates a "file created" event and a "directory modified" event). This parameter is helpful for deduplicating these events.

On a similar note, if an event within a target folder triggers another event somewhere else within the watched file tree, it is easy to accidentally write infinite loops. Use these three parameters to guard against that.

```python
class MyHandler(FileSystemEventHandler):

    def on_any_event(self, event):
        if not event.is_directory:
            f = open(event.src_path, "a")
            f.write("\nInfinite Loop\n")
            f.close()
```

In this example, when a file is created, "Infinite Loop" will be written to it as every "modified" event triggers the event handler.

This is just what I consider the important parts of the library to know, there are tons of other features that you can learn from reading the [code on GitHub](https://github.com/gorakhargosh/watchdog/).