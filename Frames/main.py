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

class MyButton(Widget):
	pass

class FirstScreen(Screen):
	pass
class SecondScreen(Screen):
	pass
class ThirdScreen(Screen):
	pass
class FourthScreen(Screen):
	pass
class FifthScreen(Screen):
	pass
class SixthScreen(Screen):
	pass


class MyApp(MDApp):
    def build(self):
       	sm = ScreenManager()
        sm.add_widget(FirstScreen(name='first_screen'))
        sm.add_widget(SecondScreen(name='second_screen'))
        return sm

    def change_screen(self, screen_name):
      	self.root.current = screen_name

if __name__ == '__main__':
    MyApp().run()
