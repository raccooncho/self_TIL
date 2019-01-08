# CSS Changing the box model



#### box model의 default

![1546943429812](C:\Users\조성규\AppData\Roaming\Typora\typora-user-images\1546943429812.png)



#### default값을 다른 타입으로 바꿀 수 있다.(border-box)

![1546943501854](C:\Users\조성규\AppData\Roaming\Typora\typora-user-images\1546943501854.png)

```css
* {
  box-sizing: border-box;
}
```

* css에서 위와 같이 입력하면 box model의 default 값이 border-box로 변경된다.
* *은 웹 페이지의 모든 요소에 적용되는 universal selector이다.

