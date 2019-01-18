# CSS Display and Positioning



#### position

* static : default
* relative
  * position: relative를 선택하면 4가지 값을 더 설정할 수 있다.
  * top : top에서 설정 값만큼 멀어진다.
  * bottom : bottom에서 설정 값만큼 멀어진다.
  * left : left에서 설정 값만큼 멀어진다.
  * right : right에서 설정 값만큼 멀어진다.
  * 설정 값의 단위는 px단위이다.
* absolute
  * position: absolute에서도 마찬가지로 top, bottom, left, right값을 설정할 수 있다.
  * 이 때 다른 요소는 무시하고 이동한다. ( 가려지게 덮어버릴 수 있다. )
* fixed
  * position: fixed에서도 마찬가지로 top, bottom, left, right 값을 설정할 수 있다.
  * page의 스크롤을 이동해도 화면에 고정되어서 스크롤과 같이 움직이지 않는다.



#### Z-index

* 해당 요소가 얼마나 앞에 있고 뒤에 있는지를 나타내는 property이다.
* 숫자가 클 수록 앞에 나온다.
* position: static에서는 작동하지 않는다.



#### Display

* inline
  * <em>, <strong>, <a>와 같은 tag들에 default로 주어지는 값이다.
  * inline element는 주변 text와 동일한 크기를 가지며 height나 width 등을 조절할 수 없다.
* block
  * default width는 화면 전체다.(100%) 다만 width를 설정할 수 있다.
  * default height는 주변 text와 동일하다.
  * / <h1> ~ <h6>, <p>, <div>, <footer>같은 element는 block를 default로 가진다.
* inline-block
  * inline과 block의 혼합형이다.
  * inline처럼 주변 다른 요소와 나란히 나타날 수 있지만, block처럼 width와 height를 조절할 수 있다.
  * image가 대표적인 예시다.



#### Float

* left 혹은 right로 요소를 이동시키고 싶을 때 사용한다.
* left : 가능한 만큼 left로 element를 이동시킨다.
* right : 가능한 만큼 right로 element를 이동시킨다.
* float를 적용하는 element는 반드시 width값이 정해져 있어야 한다.



#### Clear

* float 한 element들이 충돌하는걸 방지하기 위해서 필요하다.
* left : left쪽에 있는 element가 같은 containing안에 있는 다른 element를 건들지 않는다.
* right : right쪽에 있는 element가 같은 containing안에 있는 다른 element를 건들지 않는다.
* both : 양쪽에 있는 element들이 같은 containing안에 있는 다른 element를 건들지 않는다.
* none : element가 양쪽 element를 모두 건들 수 있다.