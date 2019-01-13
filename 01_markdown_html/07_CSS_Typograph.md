# CSS Typography



##### Font-family

* 적용된 font를 user의 컴퓨터에서 보기 위해선 user의 컴퓨터에 해당하는 font가 설치되어 있어야 한다.

* 대부분의 browsers의 default값은 `Times New Roman`font이다.

* font 종류를 하나의 web page에서 2~3개정도로 제한하는것이 좋다. (연습할 때)

* font의 이름이 두개 이상의 단어로 구성되어 있는 경우 " " 안에 font의 이름을 적어야 한다.

  ```css
  h1 {
    font-family: "Courier New";
  }
  ```


##### Font-weight

* header와 같은 몇몇 element를 제외하고는 default값이 normal로 설정되어 있다.
  * header같은 경우는 bold가 default값이다.
* Font weight는 100 ~ 900 사이의 숫자(100의 배수)로 value값을 정할 수도 있다.
  * default는 400이다.
  * bold font weight는 700이다.
  * light font weight는 300이다.



##### Font-style

*  default 값은 normal이다.
* italic 스타일을 적용할 수 있다.

```css
h3 {
  font-style: italic;
}
```



##### Word spacing

* 단어 사이의 space 길이를 조절할 수 있다.
* value의 단위는 em이다.
* default값은 0.25em이다.
* spacing를 늘리는 작업은 흔하지 않지만, bolded거나 enlarged된 text의 경우는 가독성을 늘리기 위해 사용될 수 있다.

```css
h1 {
  word-spacing: 0.3em;
}
```



##### Letter spacing

* 문자 하나하나 사이의 거리를 조절할 수 있다.(자간)
* value의 단위는 em이다.
* letter spacing역시 흔하진 않지만 대문자로 이루어진 text의 가독성을 높이기 위해 조절하기도 한다.

```css
h1 {
  letter-spacing: 0.3em;
}
```



##### Text transform

* 모든 text를 대문자 혹은 소문자로 변경할 수 있다.

  * ```css
    text-transform: uppercase;
    ```

  * ```css
    text-transform: lowercase;
    ```



##### Text alignment

* text의 위치를 정렬시킬 수 있다.
  * left : 왼쪽 정렬
  * center : 가운데 정렬
  * right : 오른쪽 정렬



##### Line height

![1547363784143](C:\Users\조성규\AppData\Roaming\Typora\typora-user-images\1547363784143.png)

* 줄간 간격을 조절할 수 있다.
* line height는 font size와 줄 간 사이 공간인 leading의 합계를 의미한다.
* value는 그냥 숫자와 px과 같은 unit단위로 사용할 수 있다.
  * 그냥 숫자 ( like 1.2 )는 line height의 길이가 font size의 몇배로 나타날지를 의미한다.
    * 1.2면 leading의 크기가 font size의 1/5가 되는것을 의미한다.
  * unit단위는 pixels, percents, ems, rems 등 css에서 사용할 수 있는 모든 unit이 적용된다.
* 그냥 unit없이 숫자로만 표기하여 비율로 계산하는 방식이 선호되는 방식이다.
  * 현재 font size를 실시간으로 수용하여 적용하기 때문에 더 사용하기 편하다.



##### Serif / Sans-serif

![1547364278134](C:\Users\조성규\AppData\Roaming\Typora\typora-user-images\1547364278134.png)

* serif 는 문자의 끝이 detail하게 꾸며진 font종류를 의미한다.
  * Times New Roman이나 Georgia같은 font가 serif에 속한다.
* sans-serif는 문자의 끝부분이 아무런 꾸밈 없이 단조로운 font 종류를 의미한다.
  * Arial이나 Helvetica같은 font가 sans serif에 속한다.



#####  Fallback Fonts

* user의 컴퓨터에 설치되어 있지 않은 font의 경우에는 사용자의 컴퓨터에 설치된 기본 font로 적용받게 된다.

  * 보통 serif font인 Times New Roman이나 sans-serif font인 Arial같은 font로 fallback된다.
* fallback font를 설정하기 위해선 다음과 같이 적용하면 된다.

```css
h1 {
  font-family: "Garamond", "Times", serif;
}
```

 위와 같이 적용하면 `Garamond`로 font가 적용되지만 user의 컴퓨터에 `Garamond` font가 없을 경우 `Times` font로 적용하고, 이도 없으면 user의 컴퓨터에 있는 아무 serif 계열 font를 적용하게 된다.



##### Linking font

* google font같이 무료로 공개된 font를 사용할 수 있는데 이를 non-user fonts라고 부른다.

* fonts.google.com -> 우측 상단의 search에서 검색 (Droid serif) -> +버튼을 누르면 font가 선택된다. (여러개 중복 체크 가능, Droid serif는 왜 체크가 안될까...) -> customize할 수 있음. -> 링크를  복사해와서 가져올 수 있다.

  * single linked font (ex. Droid Serif)

  ```css
  <head>
    <link href="https://fonts.googleapis.com/css?family=Droid+Serif" type="text/css" rel="stylesheet">
  </head>
  ```

  * miltiple linked font (ex. Droid Serif + Playfair Display)

  ```css
  <head>
    <link href="https://fonts.googleapis.com/css?family=Droid+Serif|Playfair+Display" type="text/css" rel="stylesheet">
  </head>
  ```



##### Font face ( @ font-face )

* link 를 하는 다른 방법이다.

* url을 html 파일에 link하는 대신에 browser의 url바에 입력한다.

  -> `/* latin */`로 표기된 부분을 찾는다.( 분리된 line에 존재할 수도 있는데 다 찾아야 한다.)

  -> 적혀있는 css rules를 복사해와서 css 파일의 최상단에 붙여넣기 한다.

  ```css
  /* latin */
  @font-face {
    font-family: 'Space Mono';
    font-style: normal;
    font-weight: 400;
    src: local('Space Mono'), local('SpaceMono-Regular'), url(https://fonts.gstatic.com/s/spacemono/v4/i7dPIFZifjKcF5UAWdDRYEF8RQ.woff2) format('woff2');
    unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
  }
  ```

* 같은 작업 환경에 있는 directory ( ex. fonts/ )에서 font를 받아와서 @font-face를 만들 수도 있다.

  ```css
  @font-face {
    font-family: "Roboto";
    src: url(fonts/Roboto.woff2) format('woff2'),
         url(fonts/Roboto.woff) format('woff'),
         url(fonts/Roboto.tff) format('truetype');
  }
  ```
