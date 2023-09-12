from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.config import Config

Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')

Builder.load_file("home.kv")

class HomeScreen(MDScreen):
    pass

class MyApp(MDApp):
    def build(self):
        return HomeScreen()

if __name__ == '__main__':
    MyApp().run()
