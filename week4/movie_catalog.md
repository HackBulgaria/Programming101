#Command Line Movie ~~Database~~ Catalog
We are going to create a small movie catalog that will help us keep track of movies we have seen - their titles, rating and even the names of the actors who star in them.
## Creating the tables

First, we would like to create two tables in our ```movie_catalog``` database. [Here's a little reminder how to create a table in SQLite](https://github.com/HackBulgaria/Polyglot/blob/master/polyglot_creation_script/create_db.py). Our tables should look like this (only in structure, however; the rest will be added later):

movie_id|title|year|rating
--------|-----|----|------
1|"12 Angry Men"|1957|10
2|"12 Angry Men"|1997|8
3|"The Avengers"|2012|7

actor_id|name
--------|-----
1|Henry Fonda
2|"Robert Downey Jr."
3|Jennifer Lawrence

Note that instead of ```CREATE TABLE``` you can use the command ```CREATE TABLE IF NOT EXISTS``` which (*duh*) creates a table only if it doesn't already exist in the database. 

When you create your tables, you can make the movie_id and the actor_id of the type ```INTEGER PRIMARY KEY``` which will free you of the burden of having to keep track of ids and count the rows of your tables.

To represent the relationship between the two tables, it might be a good idea to create a third table that stores only movie_ids and actor_ids. For additional pointers, scroll to the end of the document.

## Commands

Create a program ```movie_catalog.py``` that can take (and carry out) the following commands:

- ```add_movie``` <-> The program promts the user to provide the *title* of the movie, the *year* it came out in and the *rating*.
- ```add_actor <movie_id> [<actor_id>]``` <-> Adds the actor with the given ``` actor_id```  to the cast of the movie corresponding to the movie_id provided. If you're adding to a movie an actor who hasn't been added *anywhere* before, you don't have to provide an id for the actor but be prompted for the name of the actor.
- ```rate_movie <movie_id>``` <-> You can rate a movie with an integer from 1 to 10.
- ```find_movies <rating>``` <-> Prints the titles of all movies with rating equal to the one provided.
- ```actor_info <actor_id>```  <-> Prints the name of the actor and the title of every movie he/she stars in.
- ```movie_info <movie_id>``` <-> Prints movie title, year, rating and the name of every actor who stars in the movie.
- ```list_movies``` <-> Prints the titles of all movies in your catalog, along with their ids.
- ```list_actors``` <-> Prints the names of all actors who star in the movies in your catalog, along with their ids.
- ```exit``` <-> Summon the green fairy that will take you to Neverland. Or just exit the program. Whatever.

If something is unclear, please look at the examples below.

### Adding movies
Below you can see an example of how this process should look like.
```
> add_movie
title> "12 Angry Men"
year> 1957
rating> 10
"12 Angry Men" (1957) was added to your catalog!

> add_movie
title> "12 Angry Men"
year> 1997
rating> 8
"12 Angry Men" (1997) was added to your catalog!

> add_movie
title> "The Avengers"
year> 2012
rating> 7
"The Avengers" (2012) was added to your catalog!

> add_movie
title> "The Avengers"
year> 2012
rating> 7
"The Avengers" (2012) is already in your catalog!
```
You can add two movies with the same title *if they have not been released in the same year*. If *both* the title *and* the year are the same, the program assumes that the movie is already in your catalog.

### Listing movies
```
> list_movies
[1] "12 Angry Men" (1957)
[2] "12 Angry Men" (1997)
[3] "The Avengers" (2012)

> add_movie
title> "The Avengers"
year> 1998
rating> 6
"The Avengers" (1998) was added to your catalog!

> list_movies
[1] "12 Angry Men" (1957)
[2] "12 Angry Men" (1997)
[3] "The Avengers" (2012)
[4] "The Avengers" (1998)
```

### Adding actors

```
> add_actor 3
name> "Robert Downey Jr."
Robert Downey Jr. was added to the list of actors of "The Avengers" (2012)

>list_actors
[1] Robert Downey Jr.

> add_movie
title> "Iron Man"
year> 2008
rating> 6
"Iron Man" (2008) was added to your catalog!

> add_actor 3 1
Robert Downey Jr. was added to the list of actors of "Iron Man" (2008)
```
Note that the actor_id (the second id provided in the second example) is optional but the movie_id is not. You can't be an actor if you have not taken part in at least one movie.

### Lising actors

```
>list_actors
[1] Robert Downey Jr.

add_actor 1
name> "Henry Fonda"
Henry Fonda was added to the list of actors of "12 Angry Men" (1957)

>list_actors
[1] Robert Downey Jr.
[2] Henry Fonda
```

### Actor info

```
>list_actors
[1] Robert Downey Jr.
[2] Henry Fonda

> actor_info 1
Robert Downey Jr. stars in:
[3] "The Avengers" (2012)
[5] "Iron Man" (2008)

> actor_info 2
Henry Fonda stars in:
[1] "12 Angry Men" (1957)
```

### Movie info
```
> movie_info 1
Title: "12 Angry Men"
Year: (1957)
Cast: Henry Fonda
Rating: 5

> movie_info 5
Title: "Iron Man"
Year: (2008)
Cast: Robert Downey Jr.
Rating: 5

```

### Rating movies
You can change the rating of the movie corresponding to the movie_id you provide. Here's how this should go:
```
> list_movies
[1] "12 Angry Men" (1957)
[2] "12 Angry Men" (1997)
[3] "The Avengers" (2012)
[4] "The Avengers" (1998)
[5] "Iron Man" (2008)

> rate_movie 1
rating> 8

> movie_info 1
Title: "12 Angry Men"
Year: (1957)
Cast: Henry Fonda
Rating: 8

> rate_movie 1
rating> 10

> movie_info 1
Title: "12 Angry Men"
Year: (1957)
Cast: Henry Fonda
Rating: 10

```

### Finding movies

The program prints a list of all movies with rating equal to the rating provided by the user.
```
> rate_movie 2
rating> 6

> rate_movie 3
rating> 7

> find_movies 10
[1] "12 Angry Men" (1957)

> find_movies 7
[3] "The Avengers" (2012)

```

## Pointers and additional information

Let's remind ourselves how the actor and the movie list looked like in the examples above:
```
[1] Robert Downey Jr.
[2] Henry Fonda
```
```
[1] "12 Angry Men" (1957)
[2] "12 Angry Men" (1997)
[3] "The Avengers" (2012)
[4] "The Avengers" (1998)
[5] "Iron Man" (2008)
```

In this example we have a *many-to-many relationship* between the tables "Movies" and "Actors" of our database. A many-to-many relationship is when one or more rows in a table are associated with one or more rows in another table. We have a table of movies that have casts of many different actors and a table of actors who can star in many different movies.

It might be useful to create an additional third table that keeps track of the relationship between movies and actors. It might look like this:

movie_id | actor_id
---------|---------
1 | 2
3 | 1
5 | 1

The table shows that actor with unique actor_id [2] - in our example that is Henry Fonda - stars in movie with unique movie_id [1] which is "12 Angry Men" (1957). Actor with actor_id [1] - Robert Downey Jr. - stars in movies with movie_ids [3] and [5] a.k.a. "The Avengers" (2012) and "Iron Man" (2008)

**Useful Links**:

[SQLite Documentation](http://www.sqlite.org/docs.html)

[Creating tables and info about INTEGER PRIMARY KEY](http://www.sqlite.org/lang_createtable.html)

[SQLite Problem from Monday with SQL basic commands]
(https://github.com/HackBulgaria/Programming101/blob/master/week4/problems.md)

[Video that shows how INTEGER PRIMARY KEY is used](https://www.youtube.com/watch?v=wWBXV8oNcJ0)

## Bonus Round

If you want to, you can add the functions ```<remove_movie>``` and ```<remove_actor>``` which, surprisingly enough, *remove* actors and movies from the database. Note that if you remove a movie some of the actors who star in it might become jobless and have to be removed from the list of actors. You're not an actor if you haven't played in a single movie.
