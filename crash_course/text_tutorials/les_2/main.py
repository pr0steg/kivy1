from kivy.app import App
from kivy.uix.label import Label


class HelloApp(App):
    def build(self):
        root_widget = Label(font_size=100,
                            italic=True,
                            markup=True)
        root_widget.text = '[color=#ff0000]Hello[/color] [color=#00ff00]world![/color]'

        return root_widget


if __name__ == '__main__':
    HelloApp().run()
