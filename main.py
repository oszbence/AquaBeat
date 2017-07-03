import kivy
kivy.require('1.0.6')

from kivy.app import App
from kivy.config import Config

from MainScreen import *

class MainApp(App):

    def build(self):
        return Main()


if __name__ == '__main__':
    # to run on opengl 1.1 as well
    Config.set('graphics', 'multisamples', '0')
    # set window size
    Config.set('graphics', 'width', 480)
    Config.set('graphics', 'height', 320)
    # apply config settings
    Config.write()
    # run app
    MainApp().run()
