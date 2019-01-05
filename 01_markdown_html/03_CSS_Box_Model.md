# CSS Box Model



#### Box model

![1546668429872](C:\Users\조성규\AppData\Roaming\Typora\typora-user-images\1546668429872.png)

* Width and height : content의 높이와 넓이를 조절한다.
* Padding : content와 border사이의 공간이다.
* Border : content와 padding를 둘러싸고 있는 border의 굵기와 스타일을 조절한다.
* Margin : border과 이 요소 바깥 사이의 공간이다.



#### Width and height

* px단위로 조절하면 된다.



#### Border

* width : thin, medium, thick 로 border의 두께를 조절한다. 
  * px단위로 설정할 수도 있다
* style : none, dotted, solid 로 border의 모양을 조절한다.
* color : border의 색을 조절한다.
* default값은 medium none color이다.
  * color의 의미는 해당 요소의 현재 색을 의미한다. (아마 글자 색이랑 같아지는듯)
* border의 코너는 border-radius로 모양을 변경할 수 있다.
  * 설정값을 높일수록 둥글둥글해진다.
  * px로 값을 지정하는데 해당 px만큼의 반지름을 가진 원이 코너에 잘리는 듯 하다.
  * 100%로 설정하면 원이 된다. -> 설정값이 box의 height값과 동일해 진다.



#### Padding

* px단위로 content와 border사이 공간을 지정한다.
* 4방위의 padding를 개별 조절할 수 있다.
  * padding-top
  * padding-right
  * padding-bottom
  * padding-left
* padding값에 px값 4개를 나열하면 각각 순서대로 top right bottom left의 값이 된다.
  * 아래 예시는 위 6px 오른쪽 11px 아래 4px 왼쪽 9px로 설정된다.

```css
padding: 6px 11px 4px 9px;
```

* padding값에 px값 2개를 나열하면 앞의 값은 top과 bottom의 값이 되고,
  뒤의 값은 right와 left의 값이 된다.
  * 아래 예시는 위 아래 5px과 좌 우 10px로 설정된다.

```css
padding: 5px 10px;
```



#### Margin

* 기본적으로는 padding와 같다.
* auto값을 설정할 수 있다. (자동으로 중앙으로 배열이 됨)
  * 아래 예시는 위 아래 margin 값은 0이고, 좌 우 값이 동일하게 설정되어 가운데 정렬됨을 의미한다.

```css
  margin: 0 auto;
```

* 효과적인 margin값은 옆의 요소와 20px간격, 아래 요소와 30px간격이다.

  ![1546669457365](C:\Users\조성규\AppData\Roaming\Typora\typora-user-images\1546669457365.png)





#### Min and Max for contents

* 웹의 크기가 제각각이므로 content의 width 와 height 의 min 값과 max값을 지정할 수 있다.
  * min-width
  * max-width
  * min-height
  * max-height



#### Overflow

* 설정된 요소의 크기가 (content + padding + border + margin) 표시할 수 있는 구역(containing area)의 크기보다 클 경우를 overflow라고 한다.
* 이럴 때를 대비해서overflow를 설정해 놓아야 한다.
* hidden : overflow된 content를 보이지 않게 한다.
* scroll : scroll을 생성해서 overflow된 content를 볼 수 있게 한다.
* visible : overflow된 content를 표시할수 있는 구역을 벗어나서 볼 수 있게 설정한다. 기본값이다.



#### Reset defaults

* 원활한 작업을 위해서 defaults값을 reset해야 할 수도 있다.
* *{}는 모든 요소에 적용되는 값이므로 defaults값을 reset할 때 이용한다.
  * 아래 예시는 margin과 padding의 defaults값을 reset하는 코드 이다.

```css
* {
  margin: 0;
  padding: 0;
}
```



#### Visibility

* 원하는 경우 element를 화면에서 사라지게 할 수 도 있다.
* hidden : element를 가린다.
* visible : element를 화면에 나타낸다.
* display: none의 경우 화면에서 아예 삭제하지만,
  visibility: hidden의 경우에는 화면에 보이지 않을 뿐 해당하는 공간은 빈공간으로 남아있게 됨으로 사용에 유의하면 된다.

