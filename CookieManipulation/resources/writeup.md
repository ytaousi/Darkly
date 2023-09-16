```
wherever we go in the webapplication if we check the request sent to the webserver it has the header : Cookie: I_am_admin=68934a3e9455fa72420237eb05902327



after decrypting  this md5 string it is "false"

what if we can encrypt the string "true" using md5 and use it as our cookie . fortunatly it worked and got our flag
```


*** Prevention ***

### Use the right cookie flags and attributes
```
There are several ways to make cookies less accessible to attackers. By setting the httpOnly flag, you can make a cookie inaccessible to scripts. This is recommended especially for session cookies, as is setting the secure flag to ensure that the cookie is only sent over HTTPS. Carefully selecting values for the domain attribute can also minimize cookie abuse – see our cookie security white paper for more information.
```