from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

# Gives Location of Kivy Design File
Builder.load_file('my.kv')


class myBox(Widget):
    pass


# Main Application Builder
class main(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return myBox() # Add all classes here
			

if __name__ == '__main__':
    main().run()