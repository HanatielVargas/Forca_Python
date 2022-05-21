from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition 
from kivy.lang import Builder


class Forca(App):
    def build(self):
        return Builder.load_file('Forca/forca.kv')


if __name__ == '__main__':
    Forca().run()
