```
when browsing the web application we can access the robots.txt file

and it contains two paths 

/whatever and /.hidden

cheking the /whatever path we find an htpasswd file that we can download .  it contain a  user and and encrypted password

the user is "root" and after decrypting the string using md5 algorithm we get the password "qwerty123@"


after a while i found a path in the web application  /admin where i can use those credentials to login and it works we get the flag.
```