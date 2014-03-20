This is a problem, designed to be coded in teams, for GitHub multiplayer exercise!

## The Command Line Mailist

We are going to create a command-line tool, that will help us manage different mailing lists!

We are going to store information for our users (Name and Email) and put them into different mail lists.

We are going to implement some operations like:

* CRUD of Lists and People (Create Read Update Delete)
* Checking if we have already added the given email to the given list
* Searching in all lists for a given email
* Merging two lists into a new one
* Exporting a list into JSON format

The idea is to think how you can approach this problem as a team and work together, using GitHub, as your main tool!

We are not going to be clear on the specifications, so you will have a room for creativity and taking your own design decisions.

__There are three important things:__

* Use OOP
* Use TDD
* Code in Python 3.*

### Basic interaction with the program

So lets imagine, our program is in the file ```mail.py```. Lets run the program:

```
$ python mail.py
Hello Stranger! This is a cutting-edge, console-based mail-list!
Type help, to see a list of commands.
>help
Here is a full list of commands:
* show_lists - Prints all lists to the screen. Each list is assigned with a unique identifier
* show_list <unique_list_identifier> - Prints all people, one person at a line, that are subscribed for the list. The format is: <Name> - <Email>
* add <unique_list_identifier> - Starts the procedure for adding a person to a mail list. The program prompts for name and email.
* remove_subscriber <unique_list_identifier> <unique_name_identifier> - Removes the given subscriber from the given list
* create <list_name> - Creates a new empty list, with the given name.
* search_email <email> - Performs a search into all lists to see if the given email is present. Shows all lists, where the email was found.
* merge_lists <list_identifier_1> <list_identifier_2> <new_list_name> - merges list1 and list2 into a new list, with the given name.
* export <unique_list_identifier> - Exports the given list into JSON file, named just like the list. All white spaces are replaced by underscores.
* exit - this will quit the program
```

### Listing lists and Listing users

Lets imagine we have two mailing lists - ```Hack Bulgaria``` and ```HackFMI```
Our program should do the following:

```
>show_lists
[1] Hack Bulgaria
[2] HackFMI
```

Now, if we want to check all subscribers for list 1:

```
>show_list 1
[1] Radoslav Georgeiv - radorado@hackbulgaria.com
[2] Ivaylo Bachvaroff - ivo@hackbulgaria.com
[3] Daniel Taskoff - dani@dani.com
[4] .. and so on ..
```

And all subscribers for list 2:

```
>show_list 2
[1] Radoslav Georgiev - radorado@hackbulgaria.com
```

If we want to show a list, that is not created:

```
> show_list 3
List with unique identifier 3 was not found!
```

### Adding subscribers to a given list:

Now, if we want to add more subscribers to the HackFMI list, we can do so:

```
>add 2
name>Ivaylo Bachvaroff
email>ivo@hackbulgaria.com
Ivaylo Bachvaroff <ivo@hackbulgaria.com> was added to HackFMI!
>add 2
name> RadoRado
email>radorado@hackbulgaria.com
A person with the given email <radorado@hackbulgaria.com> is already in the list!
>show_list 2
[1] Radoslav Georgiev - radorado@hackbulgaria.com
[2] Ivaylo Bachvaroff - ivo@hackbulgaria.com
```

### Removing subscribers from a given list:

We should have a way to delete subscribers from a given list.

This is done with the ```remove_subscriber <unique_list_identifier> <unique_name_identifier>``` command:

```
>add 2
name>Ivan Ivanov
email>ivan@ivanov.com
>show_list 2
[1] Radoslav Georgiev - radorado@hackbulgaria.com
[2] Ivaylo Bachvaroff - ivo@hackbulgaria.com
[3] Ivan Ivanov - ivan@ivanov.com
>remove_subscriber 2 3
<Ivan Ivanov> was removed from the list <HackFMI>
>remove_subscriber 2 3
Subscriber with identifider <3> was not found in the list <HackFMI>
>remove subscriber 10 1
List with unique identifier <10> was not found.
```

### Creating new lists

This is very simple:

```
>create HackBulgaria - Java
New list <HackBulgaria - Java> was created
>show_lists
[1] Hack Bulgaria
[2] HackFMI
[3] HackBulgaria - Java
```

If we try to create an existing list, we get an error:

```
>create Hack Bulgaria
A list with name <Hack Bulgaria> already exists!
```

### Searching emails

We are going to have functionality to search our lists for a given email.

We want to find all lists, where the given email is occurring as a subscriber!

```
>search_email dani@dani.com
<dani@dani.com> was found in:
[1] Hack Bulgaria
>search_email ivo@hackbulgaria.com
<ivo@hackbulgaria.com> was found in:
[1] Hack Bulgaria
[2] HackFMI
>search_email anton@antonov.com
<anton@antonov.com> was not found in the current mailing lists.
```

### Merging lists

This one is a bit tricky - we should be able to merge to existing mail lists into a new one:

```
>merge_lists 1 2 HACK_LIST
Merged lists <Hack Bulgaria> and <HackFMI> into <HACK_LIST>
>show_lists
[1] Hack Bulgaria
[2] HackFMI
[3] HackBulgaria - Java
[4] HACK_LIST
>show_list 4
[1] Radoslav Georgeiv - radorado@hackbulgaria.com
[2] Ivaylo Bachvaroff - ivo@hackbulgaria.com
[3] Daniel Taskoff - dani@dani.com
[4] .. and so on ..
```

There should be no duplicate entries in the new lists (One email, repeating two times)

### Exporting lists into JSON file

We should be able to export a list into a JSON file.

```
>export 1
Exported <Hack Bulgaria> to <Hack_Bulgaria.json>
```

If we take a look at our JSON file:

```json
[
    {
        "name" : "Radoslav Georgiev",
        "email" : "radorado@hackbulgaria.com"
    },
    {
        "name" : "Ivaylo Bachvaroff",
        "email" : "ivo@hackbulgaria.com"
    },
    {
        "name" : "Daniel Taskoff",
        "email" : "dani@dani.com"
    }
]
```

### The program should be persistent

Check this magic:

```
$ python mail.py
Hello Stranger! This is a cutting-edge, console-based mail-list!
Type help, to see a list of commands.
>show_lists
[1] Hack Bulgaria
[2] HackFMI
[3] HackBulgaria - Java
[4] HACK_LIST
>create Test for Persistence
New list <Test for Persistence> was created
>exit
$ python mail.py
Hello Stranger! This is a cutting-edge, console-based mail-list!
Type help, to see a list of commands.
>show_lists
[1] Hack Bulgaria
[2] HackFMI
[3] HackBulgaria - Java
[4] HACK_LIST
[5] Test for Persistence
```

We should be able to save everything! You can use files for storage.
