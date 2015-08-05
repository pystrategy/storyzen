from functools import partial

from kivy.app import App
from kivy.uix.slider import Slider
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout


class Root(BoxLayout):
    progress = ObjectProperty()

    def on_value(self, slider, value):
        self.progress.value = value


class SliderApp(App):
    def build(self):
        root = Root()
        slider = Slider(orientation='vertical', min=0, max=200, value=100)
        slider.bind(value=root.on_value)
        root.add_widget(slider)
        return root


if __name__ == "__main__":
    SliderApp().run()
