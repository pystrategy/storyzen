
## 스플래쉬 구현하기 
스플래쉬 화면을 단체 로고 + 앱 로고로 생각하겠다.

### PC
키비 코드로 짜주면 될 듯. 단체 로고 -> 앱 로고 순으로 표시. `main.py` 참고

### 안드로이드
- 키비로 만들 모바일 앱에는 **presplash**로 불리는 로딩화면이 존재한다. 기본적으로 여기에 Kivy 로고가 표시된다.
- presplash는 모바일 앱 실행시 초기 화면으로 생각하면 된다. 여기에 단체 로고를 표시하고,
- 이후에 앱 로고를 코드로 구현.

buildozer.spec 파일에 다음 부분을 필요에 따라 수정하고,

```ini
  # (str) Presplash of the application
  presplash.filename = %(source.dir)s/data/presplash.png
```

해당 위치에 `presplash.png` 을 복사해두면 될 듯.

- presplash에 사용되는 이미지는 제약이 존재한다:
  
  http://cheparev.com/kivy-presplash-screen/

### iOS
- iOS에서는 Default(Launch) image를 이용하면 presplash 효과가 날 듯. 여기에 단체 로그 표시하고,
- 마찬가지로 앱 로고는 코드로 구현.

http://www.ios-developer.net/iphone-ipad-programmer/icons_and_graphics/default-image
