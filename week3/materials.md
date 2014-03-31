## Github Multiplayer

During this week, we are going to start using GitHub to do some team work. We call that - __GitHub Multiplayer__!

We are going to talk about workflows. Git and GitHub are just tools that will help us be more productive, when working in teams. But if we don't have an established workflow - everything is going to be chaos!

Here are few selected resources for Git and Github:

* The most general one is here - https://help.github.com/articles/what-are-other-good-resources-for-learning-git-and-github
* Pull Requests - This is GitHub related (Not a Git feature). Pull Requests are one of the best visual ways, to work in teams, without the pain - https://help.github.com/articles/using-pull-requests
* The workflow, used by GitHub is called the ```GitHub Flow```. This workflow is visually described here - http://guides.github.com/overviews/flow/


## GitHub Flow

If the Visual guide for the flow was not enough for you, you can check a bigger article on that topic here - http://scottchacon.com/2011/08/31/github-flow.html

To sum it up, the GitHub flow is:

### 1. Anything in the master branch is deployable

We can translate this to : "The code in master should run all tests without failing".

### 2. Create descriptive branches off of master

This means, __it's not a good idea to use your names as branch names!__

Be descriptive about what you are coding in that branch.

### 3. Push to named branches constantly

This means - every time you do a local commit, you should do push.

```
$ git push origin your-branch-name
```

### 4. Open a pull request at any time

Even if you have 10 lines of code, you can open a pull request to master, in order to notify other developers that you are working on a feature.

The pull request is updated automatically with every commit you push to your branch and __it's a perfect place, to start a discussion about your code!__

### 5. Merge only after pull request review

This means - don't merge code that was not checked by other programmers. Remember that our ```master``` should be stable!

### 6. Deploy immediately after review

Once the code is in master, there should be a way to deploy the changes automatically.

We will concern ourselves with deployment, later in this course.

## Other workflows

There are other workflows, similar to the GitHub one:

* Check here - https://www.atlassian.com/git/workflows
* And here - http://nvie.com/posts/a-successful-git-branching-model/
