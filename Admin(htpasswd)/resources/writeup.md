```
when browsing the web application we can access the robots.txt file

and it contains two paths 

/whatever and /.hidden

cheking the /whatever path we find an htpasswd file that we can download .  it contain a  user and and encrypted password

the user is "root" and after decrypting the string using md5 algorithm we get the password "qwerty123@"


after a while i found a path in the web application  /admin where i can use those credentials to login and it works we get the flag.
```

*** Prevention ***
### access control
```
The presence of the robots.txt does not in itself present any kind of security vulnerability. However, it is often used to identify restricted or private areas of a site's contents. The information in the file may therefore help an attacker to map out the site's contents, especially if some of the locations identified are not linked from elsewhere in the site. If the application relies on robots.txt to protect access to these areas, and does not enforce proper access control over them, then this presents a serious vulnerability.
```