import os
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0'}

def download_file(url, directory):
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        content = response.content
        file_extension = os.path.splitext(url)[1]  # Get the file extension
        file_name = os.path.basename(url).replace(file_extension, "")  # Remove extension from original filename
        index = 1
        new_file_name = os.path.join(directory, f"{file_name}_{index}{file_extension}")
        
        # Find a unique filename
        while os.path.exists(new_file_name):
            index += 1
            new_file_name = os.path.join(directory, f"{file_name}_{index}{file_extension}")

        with open(new_file_name, "wb") as file:
            file.write(content)


def process_links(url):
    request = requests.get(url, headers=header)
    html = request.text
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup.find_all('a')
    tags = [tag for tag in tags if tag.has_attr('href')]
    links = [tag['href'] for tag in tags]

    return links

initial_url = "http://localhost:8080/.hidden/"
output_directory = "downloaded_readme_files"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

while True:
    initial_links = process_links(initial_url)

    if len(initial_links) < 3:
        print("Reached size less than 1.")
        break
    for link in initial_links[1:]:
        new_url = urljoin(initial_url, link)
        new_links = process_links(new_url)
        if len(new_links) < 3:
            print("Reached size less than 1.")
            break
        for new_link in new_links[1:-1]:
            full_new_link = urljoin(new_url, new_link)
            #if new_link.endswith("README"):
            print(full_new_link)
            #    download_file(full_new_link, output_directory)
    initial_url = new_url  # Update the initial URL for the next iteration


