import kivy

kivy.require('2.1.0')  # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.app import EventDispatcher


class MyEventDispatcher(EventDispatcher):

    def __init__(self, **kwargs):
        self.register_event_type('on_test')
        super(MyEventDispatcher, self).__init__(**kwargs)

    def do_something(self, value):
        self.dispatch('on_test', value)

    def on_test(self, *args):
        print("I am dispatched", args)


class MyApp(App):

    def build(self):
        return Label(text='Hello Twitch')

    def my_callback(value, *args):
        print("Hello, I got an event", args)

    ev = MyEventDispatcher()
    ev.bind(on_test=my_callback)
    ev.do_something('test')


if __name__ == '__main__':
    MyApp().run()
