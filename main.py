import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.config import Config

from MainScreen import *

class MainApp(App):

    def build(self):
        return Main()


if __name__ == '__main__':
    Config.set('graphics', 'width', 480)
    Config.set('graphics', 'height', 320)
    Config.write()
    MainApp().run()
