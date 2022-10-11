# Café Brasil
# %%
import pandas as pd
import requests
import logging
from bs4 import BeautifulSoup as bs
# %%
url = 'https://portalcafebrasil.com.br/todos/podcasts/'
ret = requests.get(url)
ret.text
soup = bs(ret.text)
soup
soup.find('h5')
soup.find('h5').text
soup.find('h5').a['href']

# %%
for item in soup.find_all('h5'):
    print(f'''Nome Podecast: {item.text}  link: {item.a['href']}''')
# %%
log = logging.getLogger()
log.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
log.addHandler(ch)
# %%
url = 'https://portalcafebrasil.com.br/todos/podcasts/page/{}/?ajax=true'
# %%
def get_podcast(url):
    ret = requests.get(url)
    soup = bs(ret.text)
    return soup.find_all('h5')


# %%
i = 1
listTotal = []
listInicial = get_podcast(url.format(i))
# %%
#log.debug(f'Coletados {len(listInicial)} do link : {url.format(i)}')
while len(listInicial) != 0:
    listInicial = get_podcast(url.format(i))
    listTotal += listInicial
    print(i)
    # print(url.format(i))
    i += 1
    #log.debug(f'Coletados {len(listInicial)} do link : {url.format(i)}')
# %%
len(listTotal)
# %%
df = pd.DataFrame(columns=['nome','link'])
# %%
for item in listTotal:
    df.loc[df.shape[0]] = [item.text,item.a['href']]
# %%
df.to_csv('tabela_podcast.csv', sep="|" , index=False)
# %%
