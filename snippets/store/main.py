from random import random
from copy import deepcopy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Ellipse, Color
from kivy.storage.jsonstore import JsonStore

RAD = 20
HALF_R = 10

store = JsonStore('draw.json')


class MyCanvas(BoxLayout):
    def __init__(self, **kwargs):
        super(MyCanvas, self).__init__(**kwargs)
        self.load()

    def ellipse(self, pos, hue):
        Color(hue, 1, 1, mode='hsv')
        Ellipse(pos=pos, size=(RAD, RAD))

    def render(self):
        with self.canvas:
            for draw in self.draws:
                pos, hue = draw
                self.ellipse(pos, hue)

    def on_touch_down(self, touch):
        with self.canvas:
            if touch.pos[1] < self.height - HALF_R:
                pos = (touch.pos[0] - HALF_R, touch.pos[1] - HALF_R)
                hue = random()
                self.ellipse(pos, hue)
                self.draws.append((pos, hue))

    def load(self):
        self.clear()
        if store.exists('draws'):
            self.draws = deepcopy(store.get('draws')['data'])
        self.render()

    def clear(self):
        self.draws = []
        self.canvas.clear()

    def save(self):
        store.put('draws', data=self.draws)


class StoreApp(App):
    pass

if __name__ == "__main__":
    StoreApp().run()
