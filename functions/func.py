import pandas as pd


def limparlista():
    lista = []
    palavras = pd.Series(lista, name='Palavras')
    palavras.to_excel('palavras.xlsx')


def novojogo(*args):
    pass


def preencherlista():
    lista = list()
    palavras = pd.read_excel('palavras.xlsx')
    for c in palavras['Palavras']:
        lista.append(str(c))
    return lista


def adicionarpalavra(lista, word):
    from urllib3 import PoolManager, exceptions

    try:
        site = PoolManager().request('GET', f'https://www.dicio.com.br/{word.lower()}/')
        if 'Ops' in str(site.data):
            raise exceptions.SSLError
    except exceptions.SSLError:
        pass
    else:
        lista.append(word.capitalize())
        palavras = pd.Series(lista, name='Palavras')
        palavras.to_excel('.palavras.xlsx')


def trocartema(*args):
    global temaatual, temas 
    for i, c in enumerate(temas):
        if temas[i-1] == temaatual:
            temaatual = c
            break
