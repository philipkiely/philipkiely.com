Title: How to Reserve (and Request) a Package Name on PyPi
Date: 2023-03-31
Modified: 2023-03-31
Slug: pypi_name
Authors: Philip Kiely
Summary: If you want to publish a Python package for other people to `pip install`, you'll need to first upload it to [PyPi, the Python Package Index](https://pypi.org). Just like with domain names, once there's a package with a given name on PyPi, your package can't have exactly the same name.

If you want to publish a Python package for other people to `pip install`, you'll need to first upload it to [PyPi, the Python Package Index](https://pypi.org).

Every PyPi package has a unique name. For example, `pip install truss` installs a package named [Truss](https://pypi.org/project/truss), an open-source package that I named and helped publish to PyPi at my job.

Just like with domain names, once there's a package with a given name on PyPi, your package can't have exactly the same name.

## How to reserve a name on PyPi

**Important**: Please **do not** use this tutorial to reserve a bunch of names that you are never going to use. Only reserve a name if you are **definitely** going to publish a package with that name **in the immediate future**.

To complete this tutorial, you'll need a [PyPi account](https://pypi.org/account/register/).

### Check if the name is available

First, make sure the name you want is available. Go to `https://pypi.org/project/myawesomename` (replacing `myawesomename` with your chosen package name). If you get a 404 page, you're in luck. The name is most likely available.

If it isn't available, see [how to request a name](#how-to-request-a-name-on-pypi).

### Make your Python package

You reserve an unused name on PyPi by uploading a Python package with that name.

To create your package, run these commands (replacing `myawesomename` with your chosen package name):

```
mkdir myawesomename
cd myawesomename
touch pyproject.toml
mkdir myawesomename
touch myawesomename/__init__.py
```

This should result in the following file structure:

```
myawesomename/
    myawesomename/
        __init__.py
    pyproject.toml
```

Next, open `pyproject.toml` and add this information:

```
[project]
name = "myawesomename"
authors = [
    {name = "Your Name", email = "you@example.com"},
]
version = 0.0.0
description = "Coming soon"
```

### Upload your Python package to PyPi

Now that your minimal package is ready, you can upload it. Just run:

```
python -m pip install build twine
python -m build
twine upload dist/*
```

You'll be prompted for the username and password, then your project will be uploaded.

For more information, see the [PyPi docs](https://packaging.python.org/en/latest/tutorials/installing-packages/).

## How to request a name transfer on PyPi

If you really want a specific name and it's already taken, you might still be able to get it. Now, if there is any kind of active package with that name, you're out of luck. But some names are taken up by unused in incomplete projects and may be available to you.

This is actually what happened with Truss. The name on PyPi was taken by an unused, decade-old package, and I was able to contact the package's original creator, who graciously transferred the name to me.

### Contacting the package maintainer

All packages on PyPi list at least one author or maintainer. Try to track down this person on GitHub or social media and reach out to them about the package name. You'll need to provide evidence that you tried this first if you use the second approach.

### Requesting a package name from PyPi administrators

If a project is [abandoned](https://peps.python.org/pep-0541/#abandoned-projects) and you cannot reach its maintainer, you can use [PEP 541](https://peps.python.org/pep-0541/) to request the package name.

To request a name transfer, [follow the steps in the PEP](https://peps.python.org/pep-0541/#how-to-request-a-name-transfer). Read the instructions carefully and format your transfer request exactly as specified for the best chance of success.