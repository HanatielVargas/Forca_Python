from kivy.app import App
from kivy.lang import Builder
import pandas as pd


def preencherlista(self, *args):
    self.lista = list()
    self.palavras = pd.read_excel('Forca/database/palavras.xlsx')
    for c in self.palavras['Palavras']:
        self.lista.append(str(c))


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

lista = preencherlista()


class Forca(App):
    def build(self):
        return Builder.load_file('Forca/forca.kv')


if __name__ == '__main__':
    Forca().run()
