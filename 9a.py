import os 
import requests 
from bs4 import BeautifulSoup 

# Set the initial URL and create the comics folder 
url = 'https://xkcd.com/1/' 
comics_folder = 'xkcd_comics' 
if not os.path.exists(comics_folder): 
    os.makedirs(comics_folder) 

# Function to download and save a comic 
def download_comic(url): 
    response = requests.get(url) 
    response.raise_for_status() 
    soup = BeautifulSoup(response.text, 'html.parser') 
    comic_elem = soup.select('#comic img') 
    if comic_elem: 
        comic_url = 'https:' + comic_elem[0].get('src') 
        image_response = requests.get(comic_url) 
        image_response.raise_for_status() 
        image_filename = os.path.basename(comic_url) 
        image_path = os.path.join(comics_folder, image_filename) 
        with open(image_path, 'wb') as image_file: 
            for chunk in image_response.iter_content(100000): 
                image_file.write(chunk) 
        print(f'Downloaded: {image_filename}') 
    else: 
        print('Comic image not found.') 

# Loop through all comics 
while url: 
    download_comic(url) 
    response = requests.get(url) 
    response.raise_for_status() 
    soup = BeautifulSoup(response.text, 'html.parser') 
    prev_link = soup.select('a[rel="prev"]') 
    if prev_link: 
        url = 'https://xkcd.com' + prev_link[0].get('href') 
    else: 
        url = None 

print('All comics downloaded.')
