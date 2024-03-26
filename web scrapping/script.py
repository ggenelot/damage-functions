import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de la page à scraper
liste_url = ['https://www.iamconsortium.org/resources/model-resources/aim-hub/', 
             'https://www.iamconsortium.org/resources/model-resources/bet-glue/', 
             'https://www.iamconsortium.org/resources/model-resources/brazilian-land-use-and-energy-system-blues/',
             'https://www.iamconsortium.org/resources/model-resources/c3iam-chinas-climate-change-integrated-assessment-model/', 
             'https://www.iamconsortium.org/resources/model-resources/capri-model-common-agricultural-policy-regional-impact-analysis/', 
             'https://www.iamconsortium.org/resources/model-resources/china-times/', 
             'https://www.iamconsortium.org/resources/model-resources/cias-community-integrated-assessment-system/', 
             'https://www.iamconsortium.org/resources/model-resources/clews-models-assess-how-production-and-use-of-resources-affect-climate-change/', 
             'https://www.iamconsortium.org/resources/model-resources/computable-framework-for-energy-and-the-environment-model-coffee/', 
             'https://www.iamconsortium.org/resources/model-resources/dne21/', 
             ]

def metadonnees(url):


    # En-têtes de l'agent utilisateur pour simuler un navigateur
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }

    # Obtenir le contenu de la page
    response = requests.get(url, headers=headers)
    html_content = response.text

    # Analyser le contenu HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Trouver les éléments contenant les informations sur les modèles intégrés
    details = soup.find_all('div', class_='project-details')
    modele_elements = details[0].find_all('li')


    info = {}

    # Parcourir les éléments et extraire les étiquettes et les valeurs
    for item in modele_elements:
        label = item.find('span', class_='detail-label').text.strip()
        value = item.find('span', class_='detail-value').text.strip()
        info[label]=value
    

    return info

extraction = []

for url in liste_url: 
    info = metadonnees(url)
    extraction.append({'URL': url, **info})

# Créer un DataFrame pandas
df = pd.DataFrame(extraction)

# Écrire le DataFrame dans un fichier Excel
df.to_csv('extraction.csv')

print(df)

