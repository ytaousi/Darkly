```
browsing the web application at bottom of the page we have a clickable link  @bornToSec  going there a wierd soundtrack is played  and there is an image of a bird after clicking it we get redirected to the played soundtrack on youtube.

inspecting the source code of the web page we have an unreasonnable ammount of new lines  and sometimes unredable texts and at some point i 
found this -> we must come from : https://www.nsa.gov/ 
then a few minutes of scrolling i found this -> lets use this browser : ft_bornToSec

so i started thinking about the referrer and user-agent when talking to server that hosts the webapplication

then lets use our friend  Burp :D catching the request 

GET /index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f HTTP/1.1
Host: localhost:8080
sec-ch-ua: 
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: ""
Upgrade-Insecure-Requests: 1
User-Agent: ft_bornToSec    <---- 
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://www.nsa.gov/   <------
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: I_am_admin=68934a3e9455fa72420237eb05902327
Connection: close
```


***Prevention***

### Referer Policy
```
Up until recently it was not possible for a web site to remove the referer header from requests that it caused, but this changed with the introduction of referrer policy. This specification is meant to solve another security problem: the leaking of URLs. If you are on a secret page and click a link to another web site, the URL of the secret page is sent in the referer header. To prevent leaking of any secrets in the URL, referrer policy makes it possible to limit the information in the referer header, or to disable the referer header at all.
```