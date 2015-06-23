
### 스플래쉬 구현하기 

- 키비로 만들 모바일 앱에는 스플래쉬(splash) 화면전에 **presplash**가 존재한다. 기본적으로 여기에 Kivy 로고가 표시된다.
- presplash는 모바일 앱 실행시 초기 화면으로 생각하면 된다. 여기에 단체 로고를 표시하고,
- 이후에 본격적인 splash 화면이 나온다. 여기에 앱 로고를 표시하자.

### presplash 설정
buildozer.spec 파일에 다음 부분을 필요에 따라 수정하고,

```ini
  # (str) Presplash of the application
  presplash.filename = %(source.dir)s/data/presplash.png
```

해당 위치에 `presplash.png` 을 복사해두면 될 듯.

### 만약 PC라면?
- PC에는 별도의 presplash 단계가 없는 듯. 결국 App내에서 presplash + splash 를 만들어야 할 것.

- presplash에 사용되는 이미지는 제약이 존재한다:
  
  http://cheparev.com/kivy-presplash-screen/
