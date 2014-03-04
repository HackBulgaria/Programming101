We are going to make our first steps in the Git and Github world.

Before we step in, here are few very helpful link, that are going to guide us:

* http://guides.github.com/
* http://scotch.io/bar-talk/git-cheat-sheet
* http://stackoverflow.com/questions/7076164/terminology-used-by-git

## Step 0 - Terminology

First, we have to get familiar with the terminology, used by Git.

For a reference, you can check here - http://stackoverflow.com/questions/7076164/terminology-used-by-git

## Step 1 - Create yourself a Github account

This is the easiest step. Open github.com and create yourself an account!

## Step 2 - Setup your local git

__The most important thing is that we are not going to use the Git UI! Shell is how we play.__

For installing ```Git```, follow this link : http://git-scm.com/download/linux

Or just type:

```
sudo apt-get intall git
```

After that, you have to follow the setup manual here - https://help.github.com/articles/set-up-git

## Step 3 - In the land of SSH

This one is the most tricky part. You have to generate SSH keys and the public one to your Github profile.

To get this done, follow the instructions here - https://help.github.com/articles/generating-ssh-keys

Here, we are going to stop and explain how SSH works:

![SSH Diagram](http://images.devshed.com/wh/stories/sshprivatepublickey1.jpg)

## Step 4 - Create your first repository

We are going to push the code we have written for week 0 in Github. This is going to be a good start!

Create a repository, named something like ```HackBulgaria-Programming101``` in Github.

__Do not click on__: ```Initialize this repository with a README```. We are going to see why in a second.

## Step 5 - Your repository is in Github. Now lets bring it local.

Okay.

First, create a folder somewhere on your hard drive, named just like your repository.

You can use ```mkdir``` to do the trick:

```
$ mkdir HackBulgaria-Programming101
$ cd HackBulgaria-Programming101/
```

Now, we have to tell that this folder is a Git repository. We do that with the ```git init``` command:

```
$ git init
Initialized empty Git repository in /home/radorado/code/hackbulgaria/TestGit/.git/
```

That's it! No magic here.

In order to make sure that the directory is a git repository, run the following command:

```
$ ls -la
drwxrwxr-x  3 radorado radorado 4096 Mar  4 10:22 .
drwxrwxr-x 10 radorado radorado 4096 Mar  4 10:22 ..
drwxrwxr-x  7 radorado radorado 4096 Mar  4 10:22 .git
```

If you see the ```.git``` folder - everything is ok!

Now, create a file, called ```README.md``` and add something to it. For example - ```I am using Git and I am feeling awesome!```

You can achieve that with the following commands:

```
$ touch README.md
$ echo "I am using Git and I am feeling awesome" > README.md
$ cat README.md
I am using Git and I am feeling awesome
```

Now, we have to stop and look at this diagram:


![](http://i.stack.imgur.com/zLTpo.png)

![](http://progit.couchone.com/progit/_design/chacon/figures/18333fig0201-tn.png)

Now, let's check the status with ```git status```

```
$ git status
# On branch master
#
# Initial commit
#
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#
#   README.md
nothing added to commit but untracked files present (use "git add" to track)
```

We have to add ```README.md``` to the staged files with ```git add```

```
$ git add README.md
$ git status
# On branch master
#
# Initial commit
#
# Changes to be committed:
#   (use "git rm --cached <file>..." to unstage)
#
#   new file:   README.md
#
```

And commit it with ```git commit```.
For now, we are going to use ```git commit``` with ```-m``` flag.

```
git commit -m 'Initial commit of README.md'
[master (root-commit) f1faf78] Initial commit of README.md
 1 file changed, 1 insertion(+)
 create mode 100644 README.md
```

```
git status
# On branch master
nothing to commit (working directory clean)
```

Great! We have created our first commit and our first version of the file ```README.md```


## Step 6 - What happened to Github? Bring the remote!

So far, we have done things locally. Git can be used as a local repository and can work without Github!

But if we want our code to live in the cloud, we have to connect with Github.
This is achieved by adding a ```remote``` to our local git.

If you run the following command, that lists all remotes, you will see nothing.

```
$ git remote -v
```

You have to add your remote. The algorithm is:

```
git remote add <name_of_remote> <url_to_remote>
```

So, for a user called ```RadoRado``` and a repo called ```TestGit```:

```
git remote add origin git@github.com:RadoRado/TestGit.git
```

Now if we check our remotes again:

```
$ git remote -v
origin  git@github.com:RadoRado/TestGit.git (fetch)
origin  git@github.com:RadoRado/TestGit.git (push)
```

All we have to do is make our first push!

```
$ git push -u origin master
Counting objects: 3, done.
Writing objects: 100% (3/3), 269 bytes, done.
Total 3 (delta 0), reused 0 (delta 0)
To git@github.com:RadoRado/TestGit.git
 * [new branch]      master -> master
Branch master set up to track remote branch master from origin.
```

The algorithm is the following:

```
git push <name_of_remote> <name_of_branch>
```

If we are pushing for the first time in the given repo, we use ```-u``` flag.
