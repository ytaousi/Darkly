```
wherever we go in the webapplication if we check the request sent to the webserver it has the header : Cookie: I_am_admin=68934a3e9455fa72420237eb05902327



after decrypting  this md5 string it is "false"

what if we can encrypt the string "true" using md5 and use it as our cookie . fortunatly it worked and got our flag
```


***Prevention***