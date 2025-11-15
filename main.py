from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class TestApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        label = Label(text='Привет от Kivy!', font_size=30)
        btn = Button(text='Нажми меня!', font_size=25)
        layout.add_widget(label)
        layout.add_widget(btn)
        return layout

TestApp().run()