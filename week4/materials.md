# The materials for Week 4

## Databases, SQL and sqlite

We are going to scratch the surface of the following topics:

* Databases & Storing data in a structured way
* What is Structured Query Language?
* How to use sqlite with Python?

### Databases and SQL

Of course, to get the definition straight, check Wikipedia - http://en.wikipedia.org/wiki/Database

We are going to use Relational Databases for our purposes.

RDBMS (Relational Database Management System) is a software, that handles few very important topics for us:

* It has a server, that listens at a given port for open connections
* It manages the concurency access to the data, removing race conditions
* The data is stored in optimal data structures, which makes accessing the data very fas.
* Usually, the RDBMS supports a query language, called SQL (Structured Query Language)

We are going to use the most simple RDBMS - sqlite! It stores the entire data in a single file, located in the same directory as our scripts.

__Few good materials for getting a grasp of SQL:__

* First, we will need some SQL syntax. This is a very good SQL tutorial - http://www.w3schools.com/sql/sql_intro.asp for learning the syntax!
* Learn what is an SQL Injection (This will help you understand SQL) - https://www.youtube.com/watch?v=_jKylhJtPmI
* SQL vs NoSQL is a good way to understand SQL :) - https://www.youtube.com/watch?v=rRoy6I4gKWU

### sqlite

We are going to tackle with sqlite:

* Check the Python documentation for sqlite - http://docs.python.org/2/library/sqlite3.html
* You can check the web page for sqlite for better understanding it - https://sqlite.org/
* A very good tutorial on sqlite - http://www.pythoncentral.io/series/python-sqlite-database-tutorial/
