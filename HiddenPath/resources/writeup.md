
wget -r -e robots=off -np -nH http://localhost:8080/.hidden/
grep -ri "flag" ./.hidden