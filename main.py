from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock


SHOW_SPLASH = True
SPLASH_TIME = 1.5


class Splash(Widget):
    source = StringProperty(None)


class Main(BoxLayout):
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
