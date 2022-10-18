from kivy.app import App
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.button import  Button


class CustomBtn(Widget):
    pressed = ListProperty([0, 0])

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.pressed = touch.pos
            return True
        return super(CustomBtn, self).on_touch_down(touch)

    def on_pressed(self, instance, pos):
        print('pressed at {pos}'.format(pos=pos))


class RootWidget(BoxLayout):

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.add_widget(Button(text='btn 1'))
        cb = CustomBtn()

        def _local_func(instance, pos):
            print('pos: printed from root widget: {pos}'.format(pos=pos))

        cb.bind(pressed=_local_func)
        self.add_widget(cb)


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text='Password'))
        self.password = TextInput(multiline=False, password=True)
        self.add_widget(self.password)

        self.add_widget(Label(text='Additional info'))
        self.addinfo = TextInput(multiline=True)
        self.add_widget(self.addinfo)

        self.add_widget(Label(text='Custom button'))
        self.custombutton = CustomBtn()
        self.add_widget(self.custombutton)

        self.add_widget(Label(text='Custom buttons 2'))
        self.custombutton2 = RootWidget()
        self.add_widget(self.custombutton2)


class UserPage(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    UserPage().run()
