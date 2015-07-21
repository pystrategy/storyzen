# 드랍 다운 구현하기

Kivy의 DropDown 객체는 자식 위젯을 품는 컨테이너 역할이다. 여기에는 버튼뿐만 아니라 이미지 같은 다양한 위젯도 등록될 수 있다.

참고: [Kivy 도큐먼트 예제](http://kivy.org/docs/api-kivy.uix.dropdown.html)

## 코드로 만들기

- DropDown 인스턴스에 자식 위벳을 등록하고 있다.
- 자식 위젯의 on_relase 이벤트를 DropDown의 select 이벤트로 연결해준다.
- `runTouchApp` 을 사용하는 것이 특이하다.

```python
# -*- coding: utf8 -*-

from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp

# create a dropdown with 10 buttons
dropdown = DropDown()
for index in range(10):
    # when adding widgets, we need to specify the height manually (disabling
    # the size_hint_y) so the dropdown can calculate the area it needs.
    btn = Button(text='Value %d' % index, size_hint_y=None, height=44)

    # for each button, attach a callback that will call the select() method
    # on the dropdown. We'll pass the text of the button as the data of the
    # selection.
    # 릴리즈될 때 dropdown의 select 이벤트 호출
    btn.bind(on_release=lambda btn: dropdown.select(btn.text))

    # then add the button inside the dropdown
    dropdown.add_widget(btn)

# create a big main button
mainbutton = Button(text='Hello', size_hint=(None, None))

# show the dropdown menu when the main button is released
# note: all the bind() calls pass the instance of the caller (here, the
# mainbutton instance) as the first argument of the callback (here,
# dropdown.open.).
mainbutton.bind(on_release=dropdown.open)

# one last thing, listen for the selection in the dropdown list and
# assign the data to the button text.
# 드랍다운의 select 이벤트에 핸들러 연결
dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

# App 인스턴스 만들지 않고 어플리케이션 실행
runTouchApp(mainbutton)
```


## KV 파일로 만들기

- `DropDown` 을 상속받아 CustomDropDown 을 만들고
- 자식 위벳은 KV 파일에서 등록한다

```
Widget:

<CustomDropDown>:
    Button:
        text: 'My first Item'
        size_hint_y: None
        height: 44
        # 릴리즈시 select 이벤트를 호출
        on_release: root.select('item1')
    Label:
        text: 'Unselectable item'
        size_hint_y: None
        height: 44
        # Label에는 on_release가 없다
    Button:
        text: 'My second Item'
        size_hint_y: None
        height: 44
        # 릴리즈시 select 이벤트를 호출
        on_release: root.select('item2')
```

```python
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.app import App


class CustomDropDown(DropDown):
    pass


class DropDownApp(App):
    def build(self):
        dropdown = CustomDropDown()
        mainbutton = Button(text='Hello', size_hint=(None, None))
        mainbutton.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton,
                      'text', x))
        self.root.add_widget(mainbutton)


if __name__ == "__main__":
    DropDownApp().run()
```
