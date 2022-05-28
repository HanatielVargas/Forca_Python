'''
Jogo Da Forca by Hanatiel Vargas
Jogo clássico da forca com letras e boneco sendo enforcado caso erre a letra e a palavra.
Criando o jogo para aprender kivy, web scrape e data storage com xlsx e sql. 
'''

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition
from random import choice
import pandas as pd


class Main(Screen):

    TEMAS = {'Branco':{'Letra': (0, 0, 0, 1), 
                       'Fundo': (255, 255, 255, 1),
                       'Fback': (119, 119, 119, 1)}, 
             'Preto': {'Letra': (255, 255, 255, 1), 
                       'Fundo': (0, 0, 0, 1),
                       'Fback': (119, 119, 119, 1)}, 
             'Roxo':  {'Letra': (0, 0, 0, 1), 
                       'Fundo': (227, 150, 255, 1),
                       'Fback': (119, 119, 119, 1)},
             'Rosa':  {'Letra': (54, 17, 51, 1),
                       'Fundo': (255, 121, 117, 1),
                       'Fback': (119, 119, 119, 1)},
             'padrao':{'Letra': (0, 0, 0, 1),
                       'Fundo': (240, 240, 240, 1),  
                       'Fback': (227, 150, 255, 1)}} 
    LISTA_TEMAS = list(TEMAS.keys())
    LISTA_PALAVRAS = list()
    TENTATIVAS = ''

    palavras = pd.read_excel('Forca/database/palavras.xlsx')
    for c in palavras['Palavras']:
        LISTA_PALAVRAS.append(str(c))

    palavra = choice(LISTA_PALAVRAS)
    tema_atual = LISTA_TEMAS[-1]
    imagem_atual = 'Forca/images/forca_6vidas.png'
    palavra_adv = ('_ ' * len(palavra))[:-1]


    def atualizar(self):    
        self.ids.output.text = self.palavra_adv
        self.ids.wrongs.text = 'erros'

    
    def novo_jogo(self):
        pass


    def mudar_tema(self):
        atual = self.LISTA_TEMAS.index(self.tema_atual)
        tamanho = len(self.LISTA_TEMAS)
        print(atual)
        if atual+1 != tamanho:
            self.tema_atual = self.LISTA_TEMAS[atual+1]
        else:
            self.tema_atual = self.LISTA_TEMAS[0]


    def adicionar_palavra(self):
        global LISTA_PALAVRAS
        from urllib3 import PoolManager, exceptions

        word = self.ids.input.text

        try:
            site = PoolManager().request('GET', f'https://www.dicio.com.br/{word.lower()}/')
            if 'Ops' in str(site.data) or word == '':
                raise exceptions.SSLError
        except exceptions.SSLError:
            pass
        else:
            LISTA_PALAVRAS.append(word.capitalize())
            LISTA_PALAVRAS.sort()
            palavras = pd.Series(LISTA_PALAVRAS, name='Palavras')
            palavras.to_excel('Forca/database/palavras.xlsx')



class Forca(App):
    def build(self):
        self.icon = 'Forca/images/favicon.ico'
        self.title = 'Jogo da Forca'
        self.jogo_da_forca = ScreenManager(transition=NoTransition(duration=0))
        self.jogo_da_forca.add_widget(Main(name='main'))
        return self.jogo_da_forca


if __name__ == '__main__':
    Forca().run()

'''
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
'''
