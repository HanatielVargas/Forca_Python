'''
Jogo Da Forca by Hanatiel Vargas
Jogo clássico da forca com letras e boneco sendo enforcado caso erre a letra e a palavra.
Criando o jogo para aprender kivy, web scrape e data storage com xlsx e sql. 
'''

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition
from random import choice
import pandas as pd


def preencherlista(*args):
    lista = list()
    palavras = pd.read_excel('Forca/database/palavras.xlsx')
    for c in palavras['Palavras']:
        lista.append(str(c))
    print(lista)
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


TEMAS = {'Branco':{'Letra': '#000000', 
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
LISTA_TEMAS = list(TEMAS.keys())
LISTA_PALAVRAS = preencherlista()
TENTATIVAS = ''

palavra = choice(LISTA_PALAVRAS)
tema_atual = LISTA_TEMAS[-1]
imagem_atual = 'Forca/images/forca_6vidas.png'
palavra_adv = ('_ ' * len(palavra))[:-1]

    
class Main(Screen):
    def refresh(self):
        self.ids.output.text = palavra_adv
        self.ids.wrongs.text = 'erros'


class Forca(App):
    def build(self):
        self.icon = 'Forca/images/favicon.ico'
        self.title = 'Jogo da Forca'
        self.jogo_da_forca = ScreenManager(transition=NoTransition(duration=0))
        self.jogo_da_forca.add_widget(Main(name='main'))
        return self.jogo_da_forca


if __name__ == '__main__':
    Forca().run()
