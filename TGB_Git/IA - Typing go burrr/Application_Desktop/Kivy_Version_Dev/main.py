import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(True)

Builder.load_file('tgb.kv')


class mainClass(Widget):
    pass



class TypingGoBurr(App):
    def build(self):
        Window.clearcolor = (34/255, 40/255, 49/255)
        return mainClass()

if __name__ == '__main__':
    TypingGoBurr().run()