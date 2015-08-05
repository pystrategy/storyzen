
`Slide` 인스턴스를 사용하면 됨.

참고: [Kivy 도큐먼트 예제](http://kivy.org/docs/api-kivy.uix.slider.html?highlight=slider#kivy.uix.slider)

아래의 예제는 슬라이드를 코드에서 하나, KV에서 하나를 만듦

```python
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
        slider.bind(value=root.on_value)  # 슬라이더의 value에 바인드
        root.add_widget(slider)
        return root


if __name__ == "__main__":
    SliderApp().run()
```

```
#:kivy 1.4

<Root>:
    progress: bar
    orientation: 'vertical'
    padding: 50

    ProgressBar:
        id: bar
        value: 100
        max: 200

    Slider:
        id: slider
        max: 200
        value: 100
        step: 50
        on_value: bar.value = self.value  # on_value 이용
```
