import kivy
kivy.require('1.0.6')

from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader

import os


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
Builder.load_file('MediaPlayerScreen.kv')
Builder.load_file('BluetoothScreen.kv')

# Declare all screens
class MainScreen(Screen):
    pass

class StorageScreen(Screen):
    pass

class MediaPlayerScreen(Screen):
    pass

class BluetoothScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.add_widget(StorageScreen(name='storage'))
sm.add_widget(MediaPlayerScreen(name='mediaPlayer'))
sm.add_widget(BluetoothScreen(name='bluetooth'))


class MainApp(App):
    # Current music
    sound = None

    def build(self):
        return sm

    def setScreen(self, name):
        sm.current = name

    # Called from MediaPlayerScreen.FileChooserListView when a file is selected
    def onListItemSelected(self, selectedFilePaths):
        try:
            # Check file type
            (name, extension) = os.path.splitext(selectedFilePaths[0])
            if extension == '.mp3':
                # Stop previous track if present
                if self.sound:
                    self.sound.stop()
                # Play new track
                print 'Playing file:', selectedFilePaths[0]
                self.sound = SoundLoader.load(selectedFilePaths[0])
                self.sound.play()
            else:
                print 'File type', extension, 'is not supported!'

        # IndexError can occur from selectedFilePaths[0]
        except IndexError as detail:
            print 'IndexError:', detail


if __name__ == '__main__':
    MainApp().run()
