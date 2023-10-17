import os
import shutil
from selenium.webdriver.chrome.options import Options
import time
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

# Ajouter les cookies à la session
cookies = {
    'cookie_name1': 'cookie_value1',
    'cookie_name2': 'cookie_value2',
    # Ajoutez d'autres cookies si nécessaire
}

# Headers (optionnel, peut être nécessaire pour simuler un navigateur)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

url = 'https://top-metin2.org/in/335-gloria/'

# Path to the images folder
images_folder = "images"

# Repeat the script 10 times
for i in range(1000000):
    # Effectuer une requête GET avec les cookies
    session = requests.Session()
    session.cookies.update(cookies)
    response = session.get(url)

    # Vérifier le statut de la requête
    if response.status_code == 200:
        print("Requête réussie avec les cookies.")
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode
        chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration for headless mode
        driver_path = "C:\\Program Files (x86)\\chromedriver.exe"  # Replace with your actual driver path
        service = ChromeService(driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get(url)
        driver.refresh()

        page_source = driver.page_source    
        # Fermez le navigateur
        driver.quit()

        # Analyze the code source with Beautiful Soup
        soup = BeautifulSoup(page_source, "html.parser")

        # Select the img tag inside the specified div
        div_with_image = soup.find('div', class_='d-flex f-d-column ai-center jc-center bg-info br-9-px p-16-px mt-16-px')
        if div_with_image:
            image_tag = div_with_image.find('img')
            if image_tag and 'src' in image_tag.attrs:
                image_url = image_tag['src']
                image_name = image_url.split("/")[-1]  # Extracting image name from the URL
                image_path = os.path.join(images_folder, image_name)

                # Check if the image already exists in the 'images' folder
                if not os.path.exists(image_path):
                    print("Image not found in 'images' folder. Downloading...")
                    # Download and save the image
                    response = requests.get(image_url, stream=True)
                    with open(image_path, 'wb') as out_file:
                        shutil.copyfileobj(response.raw, out_file)
                    del response
                    print("Image saved successfully.")
                else:
                    print("Image already exists in 'images' folder. Not saving.")

            else:
                print("No img tag found or no 'src' attribute in img tag.")
        else:
            print("Specified div not found.")
    else:
        print("La requête a échoué. Code de statut:", response.status_code)

    # Add a delay before repeating the loop
    time.sleep(2)

# Print a message when the script completes 10 repetitions
print("Script completed 10 repetitions.")
