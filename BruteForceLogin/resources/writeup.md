```
after fetching a lot of data from the database using the sql vulnerability  i cam accross a username : GetThe

and going to the signin page , it might only need to brute force the password to gain access, let's write a python script to bypass the login page.

the login request is made in this form :

GET /index.php?page=signin&username=GetThe&password=&Login=Login 
HTTP/1.1

i will be using the wordlist rockyou.txt to bruteforce the login
```


***Prevention***
```

```