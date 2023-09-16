```
going through the web app there is a feedback section at this path : http://localhost:8080/index.php?page=feedback


the feedback section have  2 fields : name which is mandatory and a message to leave which is optionnal 

it is probably vulnerable to stored xss 

after trying the keyword  <script> .
in the name field i got prompted with the flag  
```


*** Prevention ***

### Secure handling of user input 
```
you must never implicitly trust input submitted by a user. Inspect all user-submitted input to ensure it doesn’t include risky characters that may affect how a user’s browser interprets the data on your website. Implement thorough input validation and ensure characters are output-escaped.
```

### escaping and encoding
```
encode any special characters to ensure the program interprets them literally (and not as special characters) before you allow them to render on your webpage. You might, for example, replace angle brackets < > in HTML with alternative characters, like &lt and &gt, to prevent the characters contained in them from forming a tag. You should also escape characters that convey special meanings in HTML. 
```