# Selalu membuat 2 class, satu utk interface, satu utk APP
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class Interface(FloatLayout):
    def display_information(self):
        data1 = self.ids.textInput1.text
        self.ids.label1.text = data1

class PojectApp(App):
    pass


PojectApp().run()