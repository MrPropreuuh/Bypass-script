import os
import shutil
import subprocess
import sys
from colorama import Fore
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from PIL import Image, ImageChops
import msvcrt

# Fonction pour comparer les images


def are_images_similar(image_path1, image_path2, threshold=0):
    if os.path.exists(image_path1) and os.path.exists(image_path2):
        image1 = Image.open(image_path1)
        image2 = Image.open(image_path2)
        diff = ImageChops.difference(image1, image2)
        diff_ratio = diff.getbbox()
        return diff_ratio is None or diff_ratio[2] < threshold
    else:
        return False


# Identifiant de l'utilisateur
utilisateur = input("Identifiant : ")
# Utilisez flush pour forcer l'affichage immédiat de "Mot de passe :"
print("Mot de passe :", end=" ", flush=True)

mot_de_passe = ""
while True:
    key = msvcrt.getch()
    key = key.decode("utf-8")

    # Si l'utilisateur appuie sur la touche Entrée, terminez la boucle
    if key == '\r':
        break
    # Si l'utilisateur appuie sur la touche de retour arrière (Backspace)
    elif key == '\x08':
        if len(mot_de_passe) > 0:
            # Effacez le dernier caractère du mot de passe et de l'affichage
            mot_de_passe = mot_de_passe[:-1]
            print("\b \b", end='', flush=True)
    else:
        # Ajoutez le caractère à la chaîne du mot de passe et affichez un astérisque (*)
        mot_de_passe += key
        print("*", end='', flush=True)

print()  # Aller à la ligne suivante


# Masquer le mot de passe en utilisant des astérisques (*)
mot_de_passe_masque = '*' * len(mot_de_passe)

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

vote_url = 'https://top-metin2.org/in/335-gloria/'
login_url = 'https://gloria-mt2.fr/login'
valide_url = 'https://gloria-mt2.fr/vote'

# Chemin du dossier des images
images_folder = "images"

# Chemin vers les dossiers [1, 2, ..., 9]
folders_path = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
folder_values = {
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9"
}

# Répétez le script indéfiniment
while True:
    # Connectez-vous au site pour vous connecter
    # Remplacez par votre chemin réel du driver
    driver_path = "C:\\Program Files (x86)\\chromedriver.exe"
    service = ChromeService(driver_path)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    # Désactiver les logs de l'infobulle
    chrome_options.add_argument("--disable-logging")
    # Désactiver les infos de débogage
    chrome_options.add_argument("--log-level=3")
    # Désactiver l'accélération GPU pour le mode sans tête
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(login_url)

    # Ajoutez un délai pour vous assurer que la page est chargée
    time.sleep(1)

    # Remplissez les informations de connexion
    wait = WebDriverWait(driver, 10)
    username_input = wait.until(
        EC.presence_of_element_located((By.NAME, 'login')))
    password_input = wait.until(
        EC.presence_of_element_located((By.NAME, 'password')))

    # Ajoutez les identifiants de connexion de l'utilisateur
    username_input.send_keys(utilisateur)
    password_input.send_keys(mot_de_passe)

    # Soumettez le formulaire
    password_input.send_keys(Keys.RETURN)

    # Ajoutez un délai pour vous assurer que la page est chargée
    time.sleep(1)

    # Vérifiez si la connexion a réussi
    if "Déconnexion" in driver.page_source:
        print("Connexion réussie.")
        # Ouvrez la page de vote
        driver.get(vote_url)
        time.sleep(1)
        driver.refresh()

        # Analysez le code source avec Beautiful Soup
        soup = BeautifulSoup(driver.page_source, "html.parser")

        # Sélectionnez la balise img à l'intérieur de la div spécifiée
        div_with_image = soup.find(
            'div', class_='d-flex f-d-column ai-center jc-center bg-info br-9-px p-16-px mt-16-px')
        if div_with_image:
            image_tag = div_with_image.find('img')
            if image_tag and 'src' in image_tag.attrs:
                image_url = image_tag['src']
                # Extraction du nom de l'image à partir de l'URL
                image_name = image_url.split("/")[-1]
                image_path = os.path.join(images_folder, image_name)

                # Vérifiez si l'image existe déjà dans le dossier 'images'
                if not os.path.exists(image_path):
                    print(
                        "Téléchargement de l'images captcha...")
                    # Téléchargez et enregistrez l'image
                    response = requests.get(image_url, stream=True)
                    with open(image_path, 'wb') as out_file:
                        shutil.copyfileobj(response.raw, out_file)
                    del response
                    print("Image enregistrée avec succès.")

                    # Comparez l'image téléchargée avec les images dans les dossiers [1, 2, ..., 9]
                    for folder in folders_path:
                        folder_path = os.path.join(images_folder, folder)
                        for filename in os.listdir(folder_path):
                            if are_images_similar(os.path.join(folder_path, filename), image_path, threshold=10):
                                print(
                                    f"Image similaire trouvée dans le dossier {folder}.")
                                # Récupérez la valeur associée au dossier
                                folder_value = folder_values.get(folder, "?")

                                # Remplissez l'élément input avec la valeur du dossier
                                captcha_password_input = driver.find_element(
                                    By.NAME, "captcha-password")
                                captcha_password_input.clear()
                                captcha_password_input.send_keys(folder_value)

                                # Cliquez sur le bouton "Voter"
                                vote_button = driver.find_element(
                                    By.ID, "vote-button")
                                vote_button.click()
                                print("Captcha réussit.")
                                time.sleep(2)
                                # Basculez vers la nouvelle fenêtre (le dernier onglet)
                                driver.switch_to.window(
                                    driver.window_handles[-1])

                                # Ouvrez la page valide_url
                                driver.get(valide_url)

                                # Attendez que le bouton "Valider" soit présent et cliquez dessus
                                valider_button = wait.until(EC.presence_of_element_located(
                                    (By.CSS_SELECTOR, 'button.btn.btn-primary.d-block.mx-auto.mb-3')))
                                valider_button.click()
                                print("Vote validé avec succès.")
                                time.sleep(1.5)

                                # Supprimez l'image téléchargée
                                if os.path.exists(image_path):
                                    os.remove(image_path)
                                    break

            else:
                print(
                    "Aucune balise img trouvée ou pas d'attribut 'src' dans la balise img.")
        else:
            print("Div spécifiée introuvable.")
            continue
    else:
        print("Échec de la connexion. Vérifiez vos identifiants.")

    # Fermez le pilote
    driver.quit()

    # Enregistrez l'heure du vote
    heure_vote = datetime.datetime.now().strftime("%H:%M")
    heure_prochain_vote = (datetime.datetime.now(
    ) + datetime.timedelta(hours=1, minutes=31)).strftime("%H:%M")
    print(
        f"Heure du vote réalisé : {heure_vote} - Heure du prochain vote : {heure_prochain_vote}")
    # Calculez le temps restant avant le prochain vote (1 heure et 31 minutes)
    temps_restant = datetime.timedelta(hours=1, minutes=30)

    # Affichez le temps restant à chaque seconde
    while temps_restant.total_seconds() > 0:
        heures, reste = divmod(temps_restant.total_seconds(), 3600)
        minutes, secondes = divmod(reste, 60)
        print(
            f"Il reste : {int(heures):02d}:{int(minutes):02d}:{int(secondes):02d} avant le prochain vote", end='\r')
        time.sleep(1)
        temps_restant -= datetime.timedelta(seconds=1)
    print()
