import kivy
kivy.require('1.0.6')

from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Config app
# to run on opengl 1.1 as well
Config.set('graphics', 'multisamples', '0')
# set window size
Config.set('graphics', 'width', 480)
Config.set('graphics', 'height', 320)
# apply config settings
Config.write()

# Load UI declarations
Builder.load_file('AquaScreen.kv')
Builder.load_file('Layouts.kv')
Builder.load_file('Widgets.kv')
Builder.load_file('MainScreen.kv')
Builder.load_file('StorageScreen.kv')

# Declare all screens
class MainScreen(Screen):
    pass

class StorageScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.add_widget(StorageScreen(name='storage'))

class MainApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    MainApp().run()
