# CSS Grid Essential



##### Grid 란

* html에 있는 item 들을 수평 혹은 수직으로 이동하는 방법이다.
* 지원하지 않는 browser 버전이 있을 수도 있으니 확인을 꼭! 해야 한다.



##### Creating Grid

* Grid를 사용하기 위해서는 초기 설정을 할 필요가 있다.
* Grid container과 Grid items가 필요하고 서로 부모 자식 관계의 상속관계이다.
* Grid container에서 display property의 value를 grid 혹은 inline-grid로 설정해 주어야 한다.
  * grid : 블럭 단위로 움직이는 grid이다.
  * inline-grid : 라인 위에서만 움직이는 grid이다.



##### Creating Columns

* Grid의 default column값은 1개이다.
* 더 많은 column을 원한다면 grid-template-columns property를 조절해야 한다.

```css
.grid {
  display: grid;
  width: 500px;
  grid-template-columns: 100px 200px;
}
```

 * 이렇게 설정하면 width가 500px인 column이 두개 생성된다.
 * 혹은 %로 사용할 수도 있는데, %는 width값을 기준으로 값을 적용한다.
 * 각 columns 값의 합이 width보다 큰 경우 overflow될 수 있다.



##### Creating rows

* Grid의 rows 갯수를 조절하기 위해서는 grid-template-rows property를 조절한다.
* column의 갯수를 조절하는 방법과 동일하지만, width 대신 height값을 설정해야 하며 height값이 기준값이 된다.



##### Grid template

* Grid-template property의 값을 조절하면 한번에 column과 row를 조절할 수 있다.
* column과 row값 사이에 `/`를 입력하여 구분하는데 앞이 row값이고 뒤가 column값이다.

```css
.grid {
  display: grid;
  width: 1000px;
  height: 500px;
  grid-template: 200px 300px / 20% 10% 70%;
}
```



##### Fraction

* overflow를 방지하기 위해서 px이나 % 대신에 fr이라는 fraction단위를 사용할 수 있다.

```css
grid-template: 2fr 1fr 1fr / 1fr 3fr 1fr;
```

​	이렇게 모든 값을 fr값으로 사용해서 적용할 수도 있지만,

```css
grid-template-columns: 1fr 60px 1fr;
```

​	위 예시처럼 60px을 적용하고 남은 부분을 fr단위로 쪼개는 방식으로 사용할 수도 있다.



##### Repeat

* 입력하는 grid의 value값이 중복될 경우 repeat를 사용할 수 있다.

```css
.grid {
  display: grid;
  width: 300px;
  grid-template-columns: repeat(3, 100px);
}
```

​	위 처럼 입력하면 100px의 column이 3개 생성된다.

* 또한 다른 값을 중복해서 생성할 수도 있다.

```css
grid-template-columns: repeat(2, 20px 50px)
```



##### MinMax

* browser의 사이즈에 따라서 grid의 값이 유동적으로 변해야 할 경우도 있다.
* 이 때 grid의 값이 너무 커지거나 작아지지 않게 하기 위해 minmax값을 설정한다.

```css
grid-template-columns: 100px minmax(100px, 500px) 100px;
```



##### Grid Gap

* Grid 사이에 빈 공간을 삽입하기 위해선 Gird gap 기능을 활용하면 된다.

```css
grid-column-gap: 10px;
grid-row-gap: 10px;
```

* 한번에 row와 column의 grid gap을 설정할 수도 있다.

```css
grid-gap: 20px 10px;
```

​	앞의 값(20px)이 row에 해당하는 gap크기이고, 뒤의 값(10px)이 column의 gap크기이다.



##### Multiple Row Items

* 여러줄을 차지한 element를 만들기 위해선 grid-row-start와 grid-row-end property를 설정해야 한다. 
* grid-row-start의 값은 시작하려는 줄의 번호를 적으면 되고, grid-row-end는 끝내려는 줄의 번호보다 1 큰 수를 적으면 된다.
  * `grid-row-start: 2` 와 `grid-row-end: 5`를 적게 된다면 해당 element는 2, 3, 4 row의 영역을 차지하게 된다.
  * grid-row-start가 grid-row-end보다 큰 수인 경우도 가능하다.
    * 이 경우에는 음수로 계산하게 된다.
* 간단하게 grid-row를 이용하면 한번에 적용할 수 있다.

```css
.item {
  grid-row: 4 / 6;
}
```

* column에서도 마찬가지로 `grid-column-start`와 `grid-column-end`를 이용하거나 `grid-column`을 활용하여 다수의 column영역을 차지한 items를 생성할 수 있다.
* span을 사용하면 더 편하다.

```css
.item {
  grid-column: 4 / span 2;
}
```

​	위처럼 span을 사용하면 그만큼 영역을 차지한다는 의미로 
​	column 4, 5에 해당하는 영역을 차지하게 된다.

* span을 사용하면 overflow를 하지 않으므로 범위를 계산하기 어려울 경우 사용하면 **매우** 유용하다

* grid-area property를 사용하면 row와 column을 한번에 설정할 수 있다.
  * `/`로 구분되는 4개의 values를 가지는데 순서대로 row-start / column-start / row-end / column-end 이다.