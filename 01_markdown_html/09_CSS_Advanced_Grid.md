# CSS Advanced Grid



##### Grid Template Areas

* 각 grid의 이름을 정해줄 수 있다.

  ```css
  .container {
    display: grid;
    max-width: 900px;
    position: relative;
    margin: auto;
    grid-template-areas: "head head"
                         "nav nav" 
                         "info services"
                         "footer footer";
    grid-template-rows: 300px 120px 800px 120px;
    grid-template-columns: 1fr 3fr; 
  }
  header {
    grid-area: head;
  } 
  nav {
    grid-area: nav;
  } 
  .info {
    grid-area: info;
  } 
  .services {
    grid-area: services;
  }
  footer {
    grid-area: footer;
  }
  ```

  위 처럼 gird area를 나누게 된다면 header가 위 두칸, nav가 그 다음 두칸, info와 services가 3번째 줄을 각각 나눠 가지고 마지막 줄은 footer가 차지하도록 설정할수 있게 된다.



##### Overlapping Elements

* grid가 overlap된 경우에는 z-index를 사용할 수 있다.
* z-index의 value가 높을 경우 높은 우선순위를 갖게 되어 더 위에 표시되게 된다.



##### Justify Items

* grid의 items를 gird area에서 정렬하는 property이다.
  * start : 왼쪽 정렬을 한다.
  * end : 오른쪽 정렬을 한다.
  * center : 가운데 정렬을 한다.
  * stretch : grid area를 꽉 채우도록 늘인다.



##### Justify Content

* 화면이 넓어지면 grid가 한쪽으로 쏠리게 된다.
* 이때 화면에 정렬하기 위해 justify-content property의 value를 정해줄 수 있다.
  * start : grid area 를 화면 전체에서 왼쪽 정렬 한다.
  * end : grid area 를 화면 전체에서 오른쪽 정렬 한다.
  * center : grid area 를 화면 중앙에 정렬한다.
  * stretch : grid area 를 화면 크기에 맞춰 늘인다.
  * space-around : 각 elements 사이의 공간을 동일하게 맞춘다.
    * 양 side의 공간보다 elements사이의 공간이 두배크기이다.
  * space-between : 각 elements 사이의 공간을 동일하게 맞춘다.
    * 양 side의 공간이 없다.
  * space-evenly : 각 elements 사이의 공간과 양 side의 공간이 동일하게 맞춘다.



##### Align Items

* grid의 items를 grid area내에서 위아래로 정렬하는 property이다.
  * start : 위쪽으로 정렬한다.
  * end : 아래쪽으로 정렬한다.
  * center : 가운데로 정렬한다.
  * stretch : grid area를 가득 채우도록 gird items를 늘인다.



##### Align Content

* grid area를 전체 화면에서 위아래로 정렬하는 property이다.
  * start : grid container를 위쪽으로 정렬한다.
  * end : grid container를 아래쪽으로 정렬한다.
  * center : grid container를 가운데로 정렬한다.
  * stretch : grid container가 화면을 가득 채우게 늘인다.
  * space-around : 각 elements 사이의 공간을 동일하게 맞춘다.
    * 위 아래의 여백보다 각 elements 사이의 공간이 두배 크기이다.
  * space-between : 각 elements 사이의 공간을 동일하게 맞춘다.
    * 위 아래의 여백이 없다.
  * space-evenly : 각 elements 사이의 공간과 위 아래의 여백이 동일한 크기이다.



##### Justify Self and Align Self

* justify self와 align self property는 justify items와 align items property보다 우선되어 적용되며, 단일 item에 적용되는 property이다.
* start, end, center, stretch의 4가지 value를 가진다.



##### Implicit vs. Explicit Grid

* 화면에 표시해야 하는 내용의 갯수와 출력할 수 있는 grid 갯수의  차이가 발생할 수도 있다.
* 이 때 발생하는 상황에 대해 implicit grid가 해결해준다.
* default값은 새로운 rows를 생성해서 초과되는 contents를 출력하는 것이다.



##### Grid Auto Rows and Grid Auto Columns

* implicit grid의 상황에 맞춰서 생성되는 grid의 사이즈는 `grid-auto-rows` property와 `grid-auto-columns` property로 설정할 수 있다.
* grid-auto-rows는 새로 생성되는 grid rows의 height를 설정한다.
* grid-auto-columns는 새로 생성되는 grid columns의 width 를 설정한다.
  * grid-auto-rows와 grid-auto-columns둘다 px, %, fr, repeat()를 모두 받을 수 있다.



##### Grid Auto Flow

* grid-auto-flow property는 새로 추가된 grid가 row인지 column인지 정해주는 property이다.
  * row : 새로 추가되는 elements는 row의 왼쪽부터 채워지며, 너무 많은 elements가 있을 경우 새로운 row를 생성한다.
  * column : 새로 추가되는 elements는 columns의 위쪽부터 채워지며, 너무 많은 elements가 있을 경우 새로운 column을 생성한다.
  * dense : 작은 elements가 추가될 경우 빈 공간에 먼저 채워 넣는다.