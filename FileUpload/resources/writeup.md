```
going through the web application there is a feature to upload jpg images to the server on this path : http://localhost:8080/index.php?page=upload

lets check the request with our friend Burp , going through the server headers  

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7

i found the  "*/*" a little bit squichy , does it mean that the server accept every other mime type ? lol , what about a php file .

i struggled making the upload work using burp alone so went googling how to use curl to upload files and found this :

curl -X POST -F "uploaded=@file.php;type=image/jpg" -F Upload=upload "http://localhost:8080/index.php?page=upload" | grep "The flag is :"


resource : https://curl.se/docs/manpage.html#-F

```

***Prevention***

### Only allow specific file types:
```
By limiting the list of allowed file types, you can avoid executables, scripts and other potentially malicious content from being uploaded to your application.
```

### Verify file types:
```
In addition to restricting the file types, it is important to ensure that no files are ‘masking’ as allowed file types. For instance, if an attacker were to rename an .exe to .docx, and your solution relies entirely on the file extension, it would bypass your check as a Word document which in fact it is not. Therefore, it is important to verify file types before allowing them to be uploaded.
```

### Store uploaded files outside the web root folder: 
```
The directory to which files are uploaded should be outside of the website’s public directory so that the attackers cannot execute the file via the assigned path URL.
```