# Problems to be solved by using SQLAlchemy's ORM

## Guidelines

* Start with the database and first create your classes, that are going to be mapped.
* Add the interface later - when you are OK with the classes and you are sure that they are mapping correctly to the tables.
* Use sqlite
* You can skip the tests for now. [__We are going to make this a spike!__](http://www.extremeprogramming.org/rules/spike.html)
* Experiment with the library and don't be afraid if your program is not working correctly. The given specifications are not that strict!

## The "Do you even math?" game

We are going to implement a dead-simple console game, that asks the user to give the right answer to a random mathematical expression.

__For example:__

```
What is the answer to 6 x 6?
?>36
?>Correct!

What is the answer to 2 ^ 8?
?>10
Incorrect! Ending game. You score is: 1
```

__We want to have the following features:__

* The game can be played by different user. In the beginning, a user can choose his playername to play with
* We want to keep the score for every user that played the game
* We want to be able to display a highscores table, that lists the top 10 users, played this game

__The implementation details are up to you!__

### Calculating the score

We will have a function, that will calculate the score for each player.

The game ends when a player gives a wrong answer to the asked mathematical expression.

If we have `n` consecutive right answers, the final score is calculated by:

```
score(n) = n * n
```

It's just the square of `n`

### Example of playing the game

```
Welcome to the "Do you even math?" game!
Here are your options:
- start
- highscores
?>start

Enter your playername>radorado
Welcome radorado! Let the game begin!

Question #1:
What is the answer to 6 x 6?
?> 36
Correct!

Question #2:
What is the answer to 5 + 1?
?> 6
Correct!

Question #3:
What is the answer to 1 + 1?
?> 3
Incorrect! Ending game. You score is: 4
```

```
?>highscores

This is the current top10:

1. radorado with 4 points
```

## The Social Address book

We are going to implement a simple program, that keeps a list of our friends and their corresponding social accounts (Facebook, Twitter, GitHub, email etc.)

The social account types should not be predefined.

We should be able to perform the following tasks:

* Add new friend by giving his/her first and last name
* Attach social accounts to him/her (Facebook, Twitter, GitHub, email, etc.)
* Attach social accounts to already added friends in our list
* List all social accounts for a given friend
* List all specific accounts (For example - twitter) for all friends in our list
* Perform a check which social account is present in all friends in our list. For example, everyone have a Facebook and Twitter account.

__The implementation details are up to you!__

### Example usage

```
>add_friend
First Name: Rado
Last Name: Rado
Friend with unique id of 1 was created!
>add_social 1
Adding social account to Rado Rado:
Social account type: twitter
Handle or url?: @Rado_g
@Rado_g added as twitter to Rado Rado
Add more accounts? (y/n): n
```

Now, if we continue, check that the program is smart:

```
>add_friend
First Name: Ivo
Last Name: Ivo
Friend with unique id of 2 was created!
>add_social 1
Adding social account to Ivo Ivo:
Social account type: Twitter

WAIT! We have found somethinf similar in the database:
twitter
Do you want me to use twitter instead of Twitter? (y/n): y
Handle or url?: @IvoIvo
@IvoIvo added as twitter to Ivo Ivo
Add more accounts? (y/n): n
```
