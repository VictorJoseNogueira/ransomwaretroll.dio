import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue = [0, 0, 1, 1]
purple = [1, 0, 1, 1]

class HBoxLayoutExample(App):
    def build(self):
        layout = BoxLayout(padding=10)
        collors = [red, blue, green, purple]
        for c in range(1, 5):
            btn = Button(text=f'esse é o botao#{c}', background_color=random.choice(collors))
        layout.add_widget(btn)
        return layout

if __name__ == '__main__':
    app = HBoxLayoutExample()
    app.run()