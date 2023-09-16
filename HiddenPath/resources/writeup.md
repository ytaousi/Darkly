```
in the robots.txt file we have also a  /.hidden path as we saw earlier, well lets try and chek it 

it seems like and an index for multiple directories that contains multiple directories and some README files but a lot of directories into a lot of subdirectories 

well at first i tried to write a python script to  fetch all the possible paths and then extract all the README files from them then download all thos readme files  and   use either grep or find  on them to search for my flag  but apparently i didnt succed to complete the script and unstead  a used wget to download everything then used gred recursively on those sub-directories to find th flag




wget -r -e robots=off -np -nH http://localhost:8080/.hidden/
grep -ri "flag" ./.hidden
```


*** Prevention ***
### access control
```
The presence of the robots.txt does not in itself present any kind of security vulnerability. However, it is often used to identify restricted or private areas of a site's contents. The information in the file may therefore help an attacker to map out the site's contents, especially if some of the locations identified are not linked from elsewhere in the site. If the application relies on robots.txt to protect access to these areas, and does not enforce proper access control over them, then this presents a serious vulnerability.
```