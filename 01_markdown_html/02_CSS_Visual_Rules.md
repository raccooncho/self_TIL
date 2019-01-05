# CSS Visual Rules



#### CSS structure

* property : 변경하고 싶은 스타일 요소 (ex. size, color)

* value : property의 값 (ex. 18px for size, blue for color)

* property 와 value는 : 으로 구분한다.
* 항상 ; 으로 끝을 표시해준다.



#### font-family

* 원하는 font는 반드시 사용자의 pc에 설치되어 있어야 한다.
* HTML의 기본 font는 Times New Roman이다.
* 한 페이지에 2~3개의 font를 사용하는 것이 가장 적절하다.
* font-family의 이름이 두 단어 이상일 경우에는 value값에 " "을 이용해서 표기해 준다.

```CSS
font-family: "Courier New";
```



#### font-size & font-weight

* font size는 px단위로 센다.
* font weight로 폰트의 무게감을 조절한다.
  * 기본값은 normal이다.
  * 진한 글씨를 보고 싶으면 bold로 설정하면 된다.



#### text-align

* text의 위치를 조정하기 위해선 text-align을 통해서 조절한다.
* right / center / left를 이용해서 오른쪽 중앙 왼쪽 배치를 할 수 있다.



#### color

* color에는 두가지 property가 있다.
* color : 글자의 색을 변경한다.
* background-color : 글자의 배경 색을 변경한다.



#### opacity

* 0 ~ 1 사이의 투명도를 조절할 수 있다.
* 1에 가까워 질 수록 불투명해진다.



#### background-image

* background-image를 통해서 배경화면을 지정할 수 있다.
* background-image의 value값은 url로 입력한다.
* url은 인터넷 주소가 되기도 하고 파일 경로가 될 수 도 있다.

```css
background-image: url("https://www.example.com/image.jpg");
					or
background-image: url("images/mountains.jpg");
```



