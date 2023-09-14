from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget

Window.size = (370,670)

Builder.load_file("home.kv")

class MyScreenManager(ScreenManager):
	pass

class FirstScreen(Screen):
	pass

class MyButton(Widget):
	pass

class SecondScreen(Screen):
	pass

class MyApp(MDApp):
    def build(self):
        return MyScreenManager()

if __name__ == '__main__':
    MyApp().run()
