```
in the robots.txt file we have also a  /.hidden path as we saw earlier, well lets try and chek it 

it seems like and an index for multiple directories that contains multiple directories and some README files but a lot of directories into a lot of subdirectories 

well at first i tried to write a python script to  fetch all the possible paths and then extract all the README files from them then download all thos readme files  and   use either grep or find  on them to search for my flag  but apparently i didnt succed to complete the script and unstead  a used wget to download everything then used gred recursively on those sub-directories to find th flag




wget -r -e robots=off -np -nH http://localhost:8080/.hidden/
grep -ri "flag" ./.hidden
```


***Prevention***