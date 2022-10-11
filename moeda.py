# %%
# imports
import requests
import json
import backoff
import logging
# %%


@backoff.on_exception(backoff.expo, (), max_tries=1)
def checarErroFuncao(func):
    def inner_func(*args, **kargs):
        try:
            func(*args, **kargs)
        except Exception as e:
            print(f"Falhou na Função : {func.__name__} , no Argumento: {e}  ")
    return inner_func
# %%
@checarErroFuncao
def cotacao(valor, parmoeda):
    url = f'https://economia.awesomeapi.com.br/json/last/{parmoeda}'
    ret = requests.get(url).text
    cotacao = json.loads(ret)[parmoeda.replace('-', '')]
    bid = float(cotacao['bid'])
    print(
        f"{valor} {parmoeda[:3]} hoje equivalem a {valor*bid} {parmoeda[-3:]}")
# %%
cotacao(100, 'BRL-USD')
cotacao(200, 'BRL-USD')
cotacao(300, 'BRL-USD')
cotacao(400, 'BRL-USD')
cotacao(500, 'BRL-USD')
cotacao(600, 'BRLUSD')
cotacao(700, 'BRL-USD')

# %%
log = logging.getLogger()
log.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
log.addHandler(ch)

# %%
@backoff.on_exception(backoff.expo, (), max_tries=1)
def checarErroFuncao(func):
    def inner_func(*args, **kargs):
        try:
            #           log.info('Passei no Try')
            #           log.debug('Passei no Try')
            log.error('{func(*args, **kargs)}}')
            func(*args, **kargs)
        except Exception as e:
            log.error(
                f"Falhou na Função : {func.__name__} , no Argumento: {e}  ")
 #          log.debug('Passei no Try')
 #           log.error('Passei no Try')
            print(f"Falhou na Função : {func.__name__} , no Argumento: {e}  ")
    return inner_func


# %%
cotacao(100, 'BRL-USD')
cotacao(200, 'BRL-USD')
cotacao(300, 'BRL-USD')
cotacao(400, 'BRL-USD')
cotacao(500, 'BRL-USD')
cotacao(600, 'BRLUSD')
cotacao(700, 'BRL-USD')
