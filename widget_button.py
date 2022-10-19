from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout


class RootWidget(RelativeLayout):

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)

        # self.cols = 6  # GridLayout

        self.button1 = Button(text='Button 1', width=100, size_hint=(1, 1))
        self.add_widget(self.button1)

        self.button2 = Button(text='Button 2', width=100, size_hint=(1, 0.75))
        self.add_widget(self.button2)

        self.button3 = Button(text='Button 3', width=100, size_hint=(0.5, 0.5))
        self.add_widget(self.button3)

        self.button4 = Button(text='Button 4', width=100, size_hint=(1, None))
        self.add_widget(self.button4)

        self.button5 = Button(text='Button 5', width=100, size_hint=(None, 1))
        self.add_widget(self.button5)

        self.button6 = Button(text='Button 6', width=100, size_hint=(None, None))
        self.add_widget(self.button6)


class TestApp(App):

    def build(self):
        return RootWidget()


if __name__ == '__main__':
    TestApp().run()
