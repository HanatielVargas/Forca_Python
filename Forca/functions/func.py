import pandas as pd

def limparlista():
    lista = []
    palavras = pd.Series(lista, name='Palavras')
    palavras.to_excel('Forca/database/palavras.xlsx')


def novojogo(*args):
    pass


def preencherlista(*args):
    lista = list()
    palavras = pd.read_excel('Forca/database/palavras.xlsx')
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
        palavras.to_excel('Forca/database/palavras.xlsx')


def trocartema(temaatual, temas):
    for i, c in enumerate(temas):
        if temas[i-1] == temaatual:
            temaatual = c
            break
