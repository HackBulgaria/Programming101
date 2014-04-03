# pip and Python plugins

We are going to deal with pip - the Python package manager that we are going to use in order to install 3rd party librariers.

## Glossary

Here are the things, that we are going to use:

* pip - A tool for installing & managing Python packages -  https://pypi.python.org/pypi/pip
* virtualenv - A tool for creating isolated Python environments - http://www.virtualenv.org/en/latest/virtualenv.html
* PyPI - the Python Package Index, where all packages are listed - https://pypi.python.org/pypi

The setup is as following:

* Install ```pip``` via apt-get
* Install ```virtualenv``` via ```pip```
* Run ```virtualenv``` in  your project, to get your local ```pip```
* Install packages via pip install ```<Package Name>```

## How to Setup Everything

A very good starting article is this one - http://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/

The bad thing is that virtualenv creates env with python 2.7. We have to deal with that problem:

```
$ virtualenv -p /usr/bin/python3 yourenv
$ source yourenv/bin/activate
$ pip install package-name
```

Where ```/usr/bin/python3``` is the path to your python3 binary!
