 #Money in the bank:#

#### 1. Setup the project ####
Project URL: https://github.com/HackBulgaria/money-in-the-bank
Your first task is to set up the project. Make a virtual environment and install all requirements in requirements.txt file. Then run the program with start.py. Try to run the tests. If everything is OK you are ready to continue.

#### 2. SQL injection ####
Take a look at the code. You may recognize that is not secure at all. Your second task is to protect your that program from SQL injections using prepared statements. Make some unit tests to proof your security.

#### 3. Strong passwords ####
In this program you can register people. There are no any requirements for the password. To increase the level of security of your clients, they all must have a STRONG password. By strong we mean:

* More then 8 symbols
* Must have capital letters, and numbers and special symbol
* Username is not in the password

Implement that requirements in the register and change password function and test them.

#### 4. Hash passwords ####
All the passwords of your users are in plain text. You know that this is not good for security reasons. You have to store the passwords in hashed way. Use the sha1 algorithm for your hashing algorithm. Make some research on that topic. 

Yes, you have to change some code. Write some tests to proof your work.

#### 5. Hide passwords while typing ####
As a UI of your application you are using the console. You know how in web forms while you are typing your password it does not appear on the screen. There is a way to do this with the console too. Make some research and fix that problem.

No, you can not test that at all. :D

#### 6. Bruteforce protection ####
You may see, that your users can try to login unlimited times a minute. That may cause a bruteforce attack. You have to protect the bank software from that.

If you enter 5 wrong passwords you have to be blocked for 5 minutes. It is up to you how to implement that feature. You can change database structure if you want. As always dont forget the tests.  