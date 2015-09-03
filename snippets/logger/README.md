# Kivy Logger 사용하기

Kivy에서는 파이썬 기본 로깅 모듈 비슷한 Kivy 로거를 제공한다.

참고: [Kivy Logger](http://kivy.org/docs/api-kivy.logger.html)


기본적으로 Kivy 로그는 `KIVY_HOME` 폴더 아래의 `logs/` 폴더에 `Kivy_~.txt` 형식의 파일명으로 남는데, 이래서는 여러 가지 앱을 한 컴퓨터에서 만드는 경우 구분이 잘 안되어 불편하다. 바람직한 것은 현재 프로젝트 폴더 아래에 남는 것이겠다.

이를 위해 프로젝트 별 로그 셋팅이 필요한데, Kivy에서는 현재 폴더에서 config.ini를 읽어오는 것을 지원하지 않기에, 코드에서 `Config` 객체를 임포트해서 설정해야 한다.

```python

# Kivy Config에서 로그 설정을 먼저하고
from kivy.config import Config
log_dir = os.path.join(os.getcwd(), 'logs')
Config.set('kivy', 'log_dir', log_dir)

# 이후에 다른 Kivy 모듈을 임포트해야 현재 폴더에 로그가 제대로 남는다.
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
```

Kivy 로거는 다음과 같이 임포트해서 사용한다.

```python
from kivy import Logger

Logger.info('title: This is a info message')

# 출력
[INFO    ] [title] This is a info message
```

Kivy 로거는 임포트 시 파이썬 기본 로거의 root 로거로 등록이 되기에, 임포트가 제대로 되었다면 기본 로거처럼 사용해도 된다.

```python
import logging

logging.debug("Debug message")
```

`trace`라는 로그 레벨이 따로 있는 것이 좀 특이하다.

기본적으로 `KIVY_HOME`에 생기는 config.ini에서 `log_enable = 1` 설정이 있기에 Kivy 로거는 활성화되어 있다. (별도로 `from kivy import Logger` 를 해주지 않아도 된다.)
