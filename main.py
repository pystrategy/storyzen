# -*- coding: utf8 -*-

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.dropdown import DropDown
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button as Button


SHOW_SPLASH = False
SPLASH_TIME = 1.5


class Splash(Widget):
    source = StringProperty(None)


class HButton(Button):
    pass


class DropDownBtn(HButton):
    pass


class DropDownSet(Widget):
    def __init__(self, **kwargs):
        super(DropDownSet, self).__init__(**kwargs)
        # dropdown main button
        self.mainbtn = HButton(text='---')
        self.mainbtn.bind(on_release=self.main_click)
        self.add_widget(self.mainbtn)

        # dropdown
        self.dropdown = DropDown()
        self.dropdown.bind(on_select=lambda instance, x: setattr(self.mainbtn,
                           'text', x))
        items = kwargs['items']

        # dropdown item buttons
        for item in items:
            btn = DropDownBtn(text=item)
            btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
            self.dropdown.add_widget(btn)

    def main_click(self, btn):
        self.dropdown.open(btn)


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
