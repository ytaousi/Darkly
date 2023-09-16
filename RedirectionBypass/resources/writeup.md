```
at the bottom of the web page we have link to social media's 

facebook , twitter , instagram

the request is made like this :


GET http://localhost:8080/index.php?page=redirect&site=facebook HTTP/1.1


if we can modify it so that it redirect us to any other malicious website we might get a flag lets try to

GET http://localhost:8080/index.php?page=redirect&site=http://maliciousWebSite HTTP/1.1


and we got our flag
```

*** Prevention ***

### Whitelist Url's
```
If you don’t need to take the redirect via a query parameter then don’t take it, maybe you can put hard coded url values where any other input is rejected
```

### Regex Expression's
```
For applications where whitelisting is simply not feasible, we recommend at minimum filtering based on protocol handler. A regex such as "^https?://" can ensure you redirect only to websites (and not javascript: handlers).

If your application is a secure authenticated application it is recommended that a “speed bump” is put in place. This would show a warning on screen that users are leaving to an external URL.
```