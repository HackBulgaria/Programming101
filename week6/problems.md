# Money In The Bank

## 1. Setup the project 
Project URL: https://github.com/HackBulgaria/money-in-the-bank

Your first task is to set up the project!

__Make a virtual environment__ and install all requirements in ```requirements.txt``` file. 

Then run the program from ```start.py```. __Try to run the tests.__ If everything is OK you are ready to continue.

## 2. SQL injection 

Take a look at the code. You may recognize that is not secure at all. Your second task is to protect your that program from SQL injections using prepared statements. 

You can try to login and give the following username:

```
' OR 1 = 1 --
```

and give anything for the password. You will login successfuly!


__Make some unit tests to proof your security.__

## 3. Strong passwords
 
In this program you can register people and there are no any requirements for the password. 

To increase the level of security of your clients, they all must have a STRONG password. By strong we mean:

* More then 8 symbols
* Must have capital letters, and numbers and a special symbol
* Username is not in the password (as a substring)

Implement that requirements in the register and change password function and test them.

## 4. Hash them passwords!

__All the passwords of your users are in plain text.__ 

You know that this is not good for security reasons. You have to store the passwords in a hash. Use the `SHA1` hashing algorithm. Make some research on that topic. 

Write some tests to proof your work.

## 5. Hide passwords while typing 

As a UI (User Interface)  of your application you are using the console. 

If you are typing your password in a web form, it appears as `***`. Sadly, this is not the case in our console.

__Make some research and fix that problem.__

No, you can not test that at all. :D

## 6. Bruteforce protection 

You can catch if a user tries to login too many times within a minute. If he tries 10 or 20 times, it can be a signal for a brute-force attack! You have to protect the bank software from that.

__If someone enters 5 wrong passwords in a row, block him from trying for the next 5 minutes.__

This should work even if the user exits the bank software and tries to login again. 

It is a good idea to use the help of the database, to achieve that!
__As always, don't forget the tests.__ 

## 7. Reset password email

Your customers need a reset password function. Add an email field in the client module and in the database.
Your command must look like this:

```send-reset-password Ivaylo```

It sends an email to the user, with a unique random hash code.


```reset-password Ivaylo```

That will ask you for the hash code, that was send to the user. If you know the hash it will led you to change your passwords. That proofs that you are the owner of that email.

Try sending emails by using a gmail SMTP. GOOGLE IT!
