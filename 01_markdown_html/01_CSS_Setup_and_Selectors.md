# CSS setup and selectors



####  html파일에서 스타일 적용

* css를 이용하지 않고 html 자체적으로도 스타일을 조정할 수 있다.

```html
<p style="color: red; font-size: 20px; font-family: Arial;">I'm learning to code!</p>
```

* 또 뭉텅이로 스타일을 적용할 수도 있다.

```html
<head>
  <style>
    p {
      color: red;
      font-size: 20px;
    }
  </style>
</head>
```

* 하지만 비효율적이다.

#### 

#### CSS link 걸어주기

- css를 적용하려면 html 파일의 head부분에 link를 걸어줘야 한다.

```html
<link href="style.css" type="text/css" rel="stylesheet">
```

- href : css 파일에 대한 경로다.
- type : 링크된 파일의 형식이다.
- rel : html파일과 연결되는 css파일 사이의 관계이다.



#### CSS 파일에서 태그걸기

```css
p {
    font-family: Arial;
}
h1 {
    color: maroon;
}
```

* 이렇게 태그를 걸고싶은 카테고리에 원하는 스타일을 적용할 수 있다.



#### Class 적용하기

* html파일에서 class를 지정해서 좀 더 세분화하는 스타일을 적용할 수 있다.

```html
<p class="brand">Sole Shoe Company</p>
```

* class에 대한 css 스타일 적용은 .class를 이용하면 된다.

```css
.brand {
    color: teal;
}
```

* class는 여러개 동시 적용이 가능하다.

```css
.green {
    color: green;
}

.bold {
    font-weight: bold;
}
```

```html
<h1 class="green bold"> ... </h1>
```

* 위와 같이 두개의 클래스를 동시에 적용하면 color: green과 font-weight: bold가 동시에 적용됨을 확인할 수 있다.



#### ID 적용하기

* 더 세분화한 스타일 적용을 원한다면 id를 이용할 수 있다.

```html
<h1 id="large-title"> ... </h1>
```

* id에 대한 css 적용은 # id{}를 이용하면 된다.

```css
#large-title {
    font-family: cursive;
	text-transform: capitalize;
}
```

* 스타일 적용 우선순위는 id -> class -> tag



#### Chaining Selectors

* 원하는 태그에만 클래스를 적용하고 싶을 떄 chaining를 할 수 있다.

```css
h1.special {
	font-family: cursive;
}
```

* 위와 같이 chaining를 하면 h1요소에 있는 special 클래스만 cursive 폰트가 적용된다.
* 즉, p나 h2 등의 다른 태그에 있는 special 클래스는 위 스타일이 적용되지 않는다.



#### Nested Elements

```html
<ul class='main-list'>
  <li> ... </li>
  <li> ... </li>
  <li> ... </li>
</ul>
```

* 위의 li와 같이 nested된 요소는 상위 요소에 class를 지정함으로써 한번에 스타일 적용이 가능하다.
* 적용은 .mail-list li {}로 하면 된다.

```css
.main-list li {
	color: teal;
}
```

```css
p {
  color: blue;
}

.main p {
  color: red;
}
```

* 위 처럼 적용하면 보통의 p요소는 blue color로 출력되지만, main 클래스의 하위 p요소는 red color로 출력된다.



#### 중요할땐 !important

* class 나 ID 등으로 세분화 시키더라도 !important로 강조한 항목은 class, ID를 무시하고 적용된다.

```css
p {
  color: blue !important;
}

.main p {
  color: red;
}
```

* 이렇게 p요소의 blue color에 !important를 이용해 강조한다면 main 클래스의 하위에 존재하는 p요소도 blue color을 적용받게 된다.



#### 두가지 이상의 태그를 한번에 적용!!

* 다른 태그, 스타일 등의 contents라도 같은 스타일을 적용할 경우에는 동시적용이 가능하다.

```css
h1, 
.menu {
  font-family: Georgia;
}
```

* 이렇게 동시에 font를 입력하면 h1요소와 menu class는 모두 Georgia 폰트를 적용한다.



