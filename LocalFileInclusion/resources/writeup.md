```
whenver browsing to a page in the web application the request is made in this form :

GET http://localhost:8080/index.php?page=NameOfPage


lets try then to include a path that takes us outside of the webserver  for example lets try to reach /etc/password

after a few tries we got access to the flag using :
http://localhost:8080/index.php?page=../../../../../../../etc/passwd
```


*** Prevention ***
```
The most effective solution to eliminate file inclusion vulnerabilities is to avoid passing user-submitted input to any filesystem/framework API. 

If this is not possible the application can maintain an allow list of files, that may be included by the page, and then use an identifier (for example the index number) to access to the selected file.

Any request containing an invalid identifier has to be rejected, in this way there is no attack surface for malicious users to manipulate the path.
```