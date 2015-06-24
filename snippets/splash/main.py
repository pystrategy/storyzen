from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.clock import Clock

SPLASH_TIME = 3


class Splash(Widget):
    source = StringProperty(None)


class SplashApp(App):
    def build(self):
        self.presplash = Splash(source='data/presplash.png')
        self.splash = Splash(source='data/splash.png')
        self.root.add_widget(self.presplash)
        Clock.schedule_once(self.show_splash, SPLASH_TIME)

    def show_splash(self, dt):
        self.root.remove_widget(self.presplash)
        self.root.add_widget(self.splash)
        Clock.schedule_once(self.clear_splash, SPLASH_TIME)

    def clear_splash(self, dt):
        self.root.remove_widget(self.splash)
        self.presplash = self.splash = None


if __name__ == '__main__':
    SplashApp().run()
