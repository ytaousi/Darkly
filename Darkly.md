## OWAP TOP 10


Local File Inclusion
```
http://localhost:8080/?page=../../../../../../../etc/passwd

flag : b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0
```

Cookie Manipulation
```
every request made to the server comes with a cookie header key "I_am_admin" , its value is md5 encrypted after decypting it using crackstation it has the value "false".
after encrypting the value "true" and sending it back to the server .

flag : df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3
```

No idea input invalidation (feedBack Section)
```
flag: 0FBB54BBF7D099713CA4BE297E1BC7DA0173D8B3C21C1811B916A3A86652724E
```

Insecure Direct Object Reference (survey section)
```
flag: 03A944B434D5BAFF05F46C4BEDE5792551A2595574BCAFC9A6E25F67C382CCAA
```

Cryptographic Failure
```
robots.txt  expose a path  /whatever if visited we get a file htpasswd  that contains a login "root" and an md5 hashed passswd "437394baff5aa33daa618be47b75cb49" after decrypting it we get the password for the root login

those credentials can be used to authenticate to http://<ip>:<port>/admin

flag : d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff

```

Redirection
```
flag : B9E775A0291FED784A2D9680FCFAD7EDD6B8CDF87648DA647AAF4BBA288BCAB3
```