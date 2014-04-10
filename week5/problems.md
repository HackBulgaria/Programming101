## The GitHub Problem!

Once you have ```virtualenv``` and ```pip``` set up, we are going to use the ```requests``` library.

[Requests is a library](http://www.python-requests.org/) for making http calls that can be installed via pip.

We are going to use the GitHub API!

The API reference can be found here - https://developer.github.com/v3/

We are going to do the following things:

1. Fetch all public repositories for a given user
2. Download the repositories as a tarball / zip
3. Unzip them
4. Run some statistics on the files
5. When the script is done, delete all the downloaded files

### Some help - repos, downloading & unzipping

To fetch all public repositories for a given user, you have to make request for:

```
https://api.github.com/users/:user
```

Where ```:user``` can be any account. For example:

```
https://api.github.com/users/RadoRado
```

To download a repo, you have to make a request to the following url:

```
https://github.com/RadoRado/Programming101/archive/master.zip
```

To disect the url, it has the following parts, that can be given as parameters:

```
https://github.com/:user/:repo_name/archive/master.zip
```

This will download the master branch.

To work with zip files, you can check this reference -  https://docs.python.org/3.4/library/zipfile.html

### Statistics

When you have all repos for the given user downloaded, the script should output the following things:

* For every repo, the number of lines of code that are written
* For every repo, the number of different source files, grouped by their extension:

```
"*.js" - 5 files
"*.css" - 3 files
etc.
```

* For all repos (summary) - lines of code written
* For all repos (summary) - number of different source files, grouped by their extension
