# CSS Color



#### 들어가기 전에..

* color
  * foreground color이라고 말한다.
  * 글자같은 element의 색을 결정한다.
* background-color
  * 배경 색을 변경한다.



##### Hexadecimal

* 색을 표현할 때 `#`으로 시작한다.
* `#` 뒤에 3개 혹은 6개의 문자가 온다.

```css
DarkSeaGreen: #8FBC8F
Sienna:       #A0522D
SaddleBrown:  #8B4513
Brown:        #A52A2A
Black:        #000000 or #000
White:        #FFFFFF or #FFF
Aqua:         #00FFFF or #0FF
```

* 위 예시는 대표적으로 사용되는 색의 hexadecimal 표기법이다.
* 이는 16진법을 의미한다.
* 영어는 대문자 소문자 상관 없다. (소문자로 해도 원하는 대로 나온다.)



##### RGB colors

* rgb colors는 0~ 255 사이의 숫자로 값을 정할 수 있다.
* 순서대로 각각 red green blue색의 양을 정한다.

```css
.green {
  background-color: rgb(143, 188, 143);
}
```

* 위와 같이 색상을 조절할 수 있다.



##### Hue, Saturation, and Lightness

* 합쳐서 HSL이라고 부른다.
* 3가지 값을 모두 입력한다.

```css
color: hsl(120, 60%, 70%);
```

* hsl은 360도의 각도로 표현되는 수치인데, 0 혹은 360에 가까울 수록 red에 가까운 색, 120에 가까울 수록 green에 가까운 색, 240에 가까울 수록 blue에 가까운 색이다.

![1547118990171](C:\Users\조성규\AppData\Roaming\Typora\typora-user-images\1547118990171.png)

* saturation은 채도를 의미한다.
  * 100%에 가까울 수록 선명해진다.
* lightness는 명도를 의미한다.
  * 100%에 가까울 수록 밝은 색이다.(흰색에 가까워 진다.)



##### Opacity and Alpha

* hsl에서 opacity 즉, 투명도를 조절할 수 있다.

  * hsl 대신 hsla를 쓰고 lightness 뒤에 0 ~ 1사이의 숫자를 입력하면 된다.
  * 이 숫자는 alpha라고 불린다.

  ```css
  color: hsla(34, 100%, 50%, 0.1);
  ```

* rgb에서도 rgba 를 사용하면 alpha값을 적용할 수 있다.

* 그냥 transparent를 적용하면 완전 투명상태가 되며 이는 `color: rgba(0, 0, 0, 0);`와 같은 상태 이다.

```css
color: transparent;
```

* 1에 가까울수록 불투명이다.