import kivy

kivy.require('2.1.0')  # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock

count = 0


class MyApp(App):

    def build(self):
        return Label(text='Hello Twitch')

    # def my_callback(dt):
    #     print('My callback is called', dt)
    #
    # event = Clock.schedule_interval(my_callback, 1 / 30.)

    # def my_callback(dt):
    #     global count
    #     count += 1
    #     if count == 10:
    #         print('Last call of my callback, bye bye !')
    #         return False
    #     print('My callback is called')
    #
    # Clock.schedule_interval(my_callback, 1 / 30.)

    def my_callback(dt):
        print("My callback is called!")

    # Clock.schedule_once(my_callback, 5)

    # First, schedule once.
    # event = Clock.schedule_once(my_callback, 0)
    #
    # # Then, in another place you will have to unschedule first
    # # to avoid duplicate call. Then you can schedule again.
    # Clock.unschedule(event)
    # event = Clock.schedule_once(my_callback, 0)

    trigger = Clock.create_trigger(my_callback)
    # later
    trigger()


if __name__ == '__main__':
    MyApp().run()
