# %%

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import json
import time
# %%
url = 'https://www.vivareal.com.br/venda/minas-gerais/juiz-de-fora/apartamento_residencial/?pagina={}'
# %%
i = 1
ret = requests.get(url.format(i))
soup = bs(ret.text)
# %%
houses = soup.find_all(
    'a', {'class': 'property-card__content-link js-card-title'}
)

qte_imoveis = float(soup.find(
    'strong', {'class': 'results-summary__count'}).text.replace('.', '')
)
# %%
# Quantidade de Páginas
qte_pagina = qte_imoveis/len(houses)
house = houses[0]
# %%
house
# %%
df = pd.DataFrame(
    columns=[
        'descricao', 'endereco', 'area', 'quartos', 'banheiro', 'vagas', 'valor', 'condominio', 'site'
    ]
)
# %%
i = 0
while len(houses) > 0:
    i += 1
    ret = requests.get(url.format(i))
    soup = bs(ret.text)
    houses = soup.find_all(
        'a', {'class': 'property-card__content-link js-card-title'}
    )
    print(f'Tamanho Data Frama: {df.shape[0]} \t\t Página Atual: {i}')
    for house in houses:
        try:
            descricao = house.find(
                'span', {'class': 'property-card__title'}).text.strip()
        except:
            descricao = None

        try:
            endereco = house.find(
                'span', {'class': 'property-card__address-container'}).text.strip()
        except:
            endereco = None

        try:
            area = house.find(
                'span', {'class': 'property-card__detail-value'}).text.strip()
        except:
            area = None

        try:
            quartos = house.find('li', class_="property-card__detail-item property-card__detail-room js-property-detail-rooms").find(
                'span', class_="property-card__detail-value js-property-card-value").text.strip()
        except:
            quartos = None

        try:
            banheiro = house.find('li', class_="property-card__detail-item property-card__detail-bathroom js-property-detail-bathroom").find(
                'span', class_="property-card__detail-value js-property-card-value").text.strip()
        except:
            banheiro = None

        try:
            vagas = house.find('li', class_="property-card__detail-item property-card__detail-garage js-property-detail-garages").find(
                'span', class_="property-card__detail-value js-property-card-value").text.strip()
        except:
            vagas = None

        try:
            valor = house.find(
                'div', class_="property-card__price js-property-card-prices js-property-card__price-small").p.text.strip()
        except:
            valor = None

        try:
            condominio = house.find(
                'div', class_="property-card__price-details--condo").strong.text.strip()
        except:
            condominio = None

        try:
            site = 'https://www.vivareal.com.br/' + house['href']

        except:
            site = None

        df.loc[df.shape[0]] = [
            descricao, endereco, area, quartos, banheiro, vagas, valor, condominio, site
        ]
# %%
df.to_csv('imoveisJuizDeForaRaspagem.csv', sep="|", index=False)
