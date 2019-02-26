# 1. HTML / CSS

```
- HTML 파일 제공.
- 예시 결과를 보고 CSS를 직접 작성해서 HTML Tag에 적용하는 형식. (주로 텍스트를 꾸미는 형식, 수업시간 및 프로젝트에서 자주 사용했던 속성들 위주로 출제)
- tag 선택자, class 선택자, id 선택자만 사용해도 되도록 출제.
- position, display, background-image 같은 속성들은 출제 안됨.
- class 선택자, id 선택자를 이용하여 작성한 CSS를 HTML Tag에 적용하는 방법 숙지 필요.
```



### 1) css linking

```html
<link href="style.css" type="text/css" rel="stylesheet">
```



### 2) 완전 basic

* `font-family`

  * font-family 의 이름이 두 당너 이상일 경우에는 " "안에 font 이름을 적어준다.

  ```css
  font-family: "Courier New";
  ```

* `font-size`

* `font-weight`

  * 100 ~ 900의 100단위 숫자이다.
  * default 는 400, light 는 300, bold 는 700

* `font-style` : default는 normal / italic을 적용할 수 있음

* `text-align` : right / center / left

* `text-transform` : uppercase / lowercase

* `line-height` : 줄간 간격을 조절할 수 있다.

  * 그냥 숫자나 unit단위를 사용할 수 있다.
  * 1.2는 font size의 1/5가 줄 사이 공간(leading)이 된다

* `color`

  * color : 글자 색 변경
  * background-color : 배경 색 변경

* `opacity`

  * 0 ~ 1 사이의 투명도 조절
  * 1에 가까울 수록 불투명 (0이 완전 투명)

### 3) Box model

* width : 너비 조절
* height : 높이 조절
* Padding : content와 border사이 공간
  * `paddig-top` `padding-right` `padding-left` `padding-bottom`
  * `padding` : 0 0 0 0 (top, right, bottom, left)
  * `padding` : 0 0 (top bottom / right left)
* Border : 경계선
  * width : thin, medium, thick(px단위 등도 가능)
  * style : none, dotted, solid
  * color
  * default : medium none color
  * `border-radius` : 15% 75% -> ↘  ↙
* Margin : 바깥공간
  * padding과 동일
  * auto가능 ( 정렬됨)
* Overflow : hidden, scroll, visible(default)
* Visibility : hidden, visible







# 2. Bootstrap

```
- Grid System에 관한 문제를 출제.
- 미리 작성된 HTML 파일 제공. (CDN을 통하여 Bootstrap도 추가되어 있음)
- 예시 결과를 보고 알맞는 클래스를 채워 넣는 형식.
- Bootstrap 사이트 접속 불가능.
- Responsive Grid를 위한 Breakpoint 관련 내용은 문제에서 주어짐.
- 공식문서를 반드시 볼 것. (최소한 Grid의 Offsetting columns까지, 세로 정렬은 출제 안됨.)
```



### 1) 

# 3. Django

```
- [R]ead(List, Detail), [D]elete(Delete) 중에 하나를 작성하는 문제 출제.
- Django 프로젝트 코드 제공. (runserver를 통한 서버 실행은 불가능)
- `views.py`에 새로운 함수 작성하여 페이지 만드는 법, template(html) 파일 만드는 법 숙지 필요.
- Django Template Language의 기본적인 사용법, '반복문', '조건문', '템플릿 상속(extends)', '페이지 출력(render)' 숙지 필요.
- 부분 점수를 위해서 최대한 많이 작성할 것.
```



### 1) 