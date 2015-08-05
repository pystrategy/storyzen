# -*- coding: utf8 -*-

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button


SHOW_SPLASH = False
SPLASH_TIME = 1.5

FIELDS = [u'돈', u'사랑', u'영생', u'명예', u'권력']


class Splash(Widget):
    source = StringProperty(None)


class FieldMainButton(Button):
    def on_release(self):
        print '----------'
        print self.children


class FieldMainButton(Button):
    def __init__(self, **kwargs):
        super(FieldMainButton, self).__init__(**kwargs)


class FieldButton(Button):
    def __init__(self, **kwargs):
        super(FieldButton, self).__init__(**kwargs)


class FieldDropDown(DropDown):
    def __init__(self, **kwargs):
        super(FieldDropDown, self).__init__(**kwargs)
        mainbtn = FieldMainButton()
        self.add_widget(mainbtn)


class Main(BoxLayout):
    def build(self):
        pass


class StoryZenApp(App):
    def build(self):
        if SHOW_SPLASH:
            self.splash = Splash(source='images/title.png')
            self.root.add_widget(self.splash)
            Clock.schedule_once(self.show_main, SPLASH_TIME)
        else:
            self.root.add_widget(Main())

    def show_main(self, dt):
        self.root.remove_widget(self.splash)
        self.root.add_widget(Main())


if __name__ == "__main__":
    StoryZenApp().run()
