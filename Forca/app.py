'''
Jogo Da Forca by Hanatiel Vargas
Jogo clássico da forca com letras e boneco sendo enforcado caso erre a letra e a palavra.
Criando o jogo para aprender kivy e data storage com xlsx. 
'''

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition
from random import choice
import pandas as pd


class Main(Screen):

    temas = {'Branco':{'Letra': (0, 0, 0, 1), 
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
    lista_temas = list(temas.keys())
    lista_palavras = list()
    tentativas = ''

    palavras = pd.read_excel('Forca/database/palavras.xlsx')
    for c in palavras['Palavras']:
        if c not in lista_palavras and c != '':
            lista_palavras.append(str(c))

    palavra = choice(lista_palavras)
    tema_atual = lista_temas[-1]
    imagem_atual = 'Forca/images/forca_6vidas.png'
    palavra_adv = ('_ ' * len(palavra))[:-1]


    def atualizar(self):
        self.atua_tent()
        self.atua_pala()
        self.atua_imag()
        self.ids.wrongs.text = self.tentativas
        


    def atua_pala(self):
        self.palavra_adv = ''
        for c in self.palavra:
            if c not in self.tentativas:
                self.palavra_adv += '_ '
            else:
                self.palavra_adv += f'{c} '
        self.ids.output.text = self.palavra_adv


    def atua_imag(self):
        pass


    def atua_tent(self):
        tent = self.ids.input.text
        if tent not in self.tentativas and len(tent) == 1:
            self.tentativas += tent.upper()
            if len(self.tentativas) % 10 == 0:
                self.tentativas += '\n'
            else: 
                self.tentativas += ' '

    
    def novo_jogo(self):
        pass


    def mudar_tema(self):
        atual = self.lista_temas.index(self.tema_atual)
        tamanho = len(self.lista_temas)
        print(atual)
        if atual+1 != tamanho:
            self.tema_atual = self.lista_temas[atual+1]
        else:
            self.tema_atual = self.lista_temas[0]


    def adicionar_palavra(self):
        
        from urllib3 import PoolManager, exceptions

        word = self.ids.input.text

        try:
            site = PoolManager().request('GET', f'https://www.dicio.com.br/{word.lower()}/')
            if 'Ops' in str(site.data) or word == '' or word.capitalize() in self.lista_palavras or word.isalnum():
                raise exceptions.SSLError
        except exceptions.SSLError:
            pass
        else:
            self.lista_palavras.append(word.capitalize())
            self.lista_palavras.sort()
            palavras = pd.Series(self.lista_palavras, name='Palavras')
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
