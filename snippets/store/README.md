# Store 사용하기

Kivy에는 기본으로 `DictStore`, `JsonStore`, `RedisSotre`의 세가지 스토리지가 있다.

참고: [Kivy Storage](http://kivy.org/docs/api-kivy.storage.html)

예제에서는 JsonStore를 사용한다.

주의할 점은, **리스트를 저장하고 읽어올 때의 참조관계**이다.

```python
# mylist에 1, 2가 저장된 경우
mylist = store.get('data', 'mylist')
mylist.append(3)
print store.get('data', 'mylist')
# 1, 2, 3이 출력됨
```

`main.py`

```python
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
```


`store.kv`

```
#:kivy 1.4

BoxLayout:
    orientation: 'vertical'

    BoxLayout:
        size_hint_y: 1
        Button:
            text: 'Save'
            on_press: my_canvas.save()

        Button:
            text: 'Load'
            on_press: my_canvas.load()

        Button:
            text: 'Clear'
            on_press: my_canvas.clear()

    MyCanvas:
        id: my_canvas
        size_hint_y: 9
```
