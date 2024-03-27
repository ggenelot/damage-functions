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
             'https://www.iamconsortium.org/resources/model-resources/dsk-the-dystopian-schumpeter-meeting-keynes-climate-economy-agent-based-model/', 
             'https://www.iamconsortium.org/resources/model-resources/e3me-ftt/', 
             'https://www.iamconsortium.org/resources/model-resources/e3mg/', 
             'https://www.iamconsortium.org/resources/model-resources/elena-ecuador-land-use-and-energy-network-analysis-model/', 
             'https://www.iamconsortium.org/resources/model-resources/empire-european-model-for-power-system-investment-with-renewable-energy/', 
             'https://www.iamconsortium.org/news-from-the-community/news-f-the-community/en-roads/', 
             'https://www.iamconsortium.org/resources/model-resources/env-linkages-moodel/', 
             'https://www.iamconsortium.org/resources/model-resources/envisage-environmental-impact-and-sustainability-applied-general-equilibrium-model/', 
             'https://www.iamconsortium.org/resources/model-resources/eppa/', 

             'https://www.iamconsortium.org/resources/model-resources/eucalc-european-calculator/', 
             'https://www.iamconsortium.org/resources/model-resources/exiomod-2-0-extended-input-output-model/', 
             'https://www.iamconsortium.org/resources/model-resources/fairv2-0-0-finite-amplitude-impulse-response-v2-0-0/',
             'https://www.iamconsortium.org/resources/model-resources/fasom-ghg-forestry-and-agricultural-sector-optimization-model-with-greenhouse-gases/', 
             'https://www.iamconsortium.org/resources/model-resources/felix/', 
             'https://www.iamconsortium.org/resources/model-resources/fund-climate-framework-for-uncertainty-negotiation-and-distribution/', 
             'https://www.iamconsortium.org/resources/model-resources/gains-model/', 
             'https://www.iamconsortium.org/resources/model-resources/gcam/', 
             'https://www.iamconsortium.org/resources/model-resources/gem-e3/', 
             'https://www.iamconsortium.org/resources/model-resources/gemini-e3-eu/', 

             'https://www.iamconsortium.org/resources/model-resources/get-global-energy-system-model/', 
             'https://www.iamconsortium.org/resources/model-resources/globio-global-biodiversity-model-for-policy-support/', 
             'https://www.iamconsortium.org/resources/model-resources/globiom-global-biosphere-management-model/', 
             'https://www.iamconsortium.org/resources/model-resources/glucose/', 
             'https://www.iamconsortium.org/resources/model-resources/grace/', 
             'https://www.iamconsortium.org/resources/model-resources/ices/', 
             'https://www.iamconsortium.org/resources/model-resources/ifs/', 
             'https://www.iamconsortium.org/resources/model-resources/igsm-integrated-global-system-model/', 
             'https://www.iamconsortium.org/resources/model-resources/imaclim-r/', 

             'https://www.iamconsortium.org/resources/model-resources/nemesis-world/', 
             'https://www.iamconsortium.org/resources/model-resources/omnia/', 
             'https://www.iamconsortium.org/resources/model-resources/open-prom/', 
             'https://www.iamconsortium.org/news-from-the-community/news-f-the-community/osemosys-open-source-energy-modelling-system/', 
             'https://www.iamconsortium.org/resources/model-resources/oxford-global/', 
             'https://www.iamconsortium.org/resources/model-resources/page2002-policy-analysis-of-the-greenhouse-effect/', 
             'https://www.iamconsortium.org/news-from-the-community/news-f-the-community/plaia-plastics-integrated-assessment-model/', 
             'https://www.iamconsortium.org/resources/model-resources/plan4res/', 
             'https://www.iamconsortium.org/resources/model-resources/poles-prospective-outlook-on-long-term-energy-systems/', 
             'https://www.iamconsortium.org/resources/model-resources/prometheus/', 

             'https://www.iamconsortium.org/resources/model-resources/remes/', 
             'https://www.iamconsortium.org/resources/model-resources/remind/', 
             'https://www.iamconsortium.org/resources/model-resources/rev-the-renewable-energy-potential-model/', 
             'https://www.iamconsortium.org/resources/rice50-a-multi-regional-integrated-assessment-model/', 
             'https://www.iamconsortium.org/resources/model-resources/stem-swiss-times-energy-systems-model/', 
             'https://www.iamconsortium.org/resources/model-resources/tempest-technological-economic-political-energy-systems-transition/', 
             'https://www.iamconsortium.org/resources/model-resources/us-regen-u-s-regional-economy-greenhouse-gas-and-energy/', 
             'https://www.iamconsortium.org/resources/model-resources/witch/'



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

    # Find page title
    title = soup.find_all('div', class='page-title-txt')[0]

    # Trouver les éléments contenant les informations sur les modèles intégrés
    details = soup.find_all('div', class_='project-details')
    modele_elements = details[0].find_all('li')


    info = {'Page title': title}

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

