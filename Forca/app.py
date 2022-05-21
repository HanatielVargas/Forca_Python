'''
Jogo Da Forca by Hanatiel Vargas
Jogo clássico da forca com letras e boneco sendo enforcado caso erre a letra e a palavra.
Criando o jogo para aprender tkinter, web scrape e data storage com xlsx e sql. 
'''

from kivy.app import App
from kivy.lang import Builder
import pandas as pd


def preencherlista(*args):
    lista = list()
    palavras = pd.read_excel('Forca/database/palavras.xlsx')
    for c in palavras['Palavras']:
        lista.append(str(c))


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


tema = {'Branco':{'Letra': '#000000', 
                  'Fundo': '#FFFFFF',
                  'Fback': '#777777'}, 
        'Preto': {'Letra': '#FFFFFF', 
                  'Fundo': '#000000',
                  'Fback': '#777777'}, 
        'Roxo':  {'Letra': '#000000', 
                  'Fundo': '#E396FF',
                  'Fback': '#777777'},
        'Rosa':  {'Letra': '#361133',
                  'Fundo': '#FF7975',
                  'Fback': '#777777'},
        'padrao':{'Letra': '#000000',
                  'Fundo': '#F0F0F0',
                  'Fback': '#E396FF'}} 

lista_palavras = preencherlista()


class Forca(App):
    def build(self):
        self.icon = 'Forca/images/favicon.ico'
        self.title = 'Jogo da Forca'
        return Builder.load_file('Forca/forca.kv')


if __name__ == '__main__':
    Forca().run()
