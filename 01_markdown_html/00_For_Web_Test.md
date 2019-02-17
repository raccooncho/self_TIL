# 1. HTML ( Hyper Text Markup Language )

HTTP(s) : Hyper Text Transfer Protocol



### 1) Semantic Tags

 * `header` : 문서 전체나 섹션의 헤더
 * `nav`: 내비게이션
 * `aside` : 사이드에 위치한 공간으로, 메인 콘텐츠와 관련성이 적은 콘텐츠에 사용
 * `section` : 문서의 일반적인 구분으로 콘텐츠의 그룹을 표현하며, 일반적으로 h1 ~ h6 요소를 가짐
 * `article` : 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역 (포럼 / 신문 등의 글 또는 기사)
 * `footer` : 문서 전체나 섹션의 풋터
 * non semantic element :  `div`, `span`, etc...



### 2) Units

css에 같은 내용 포함..



### 3) Box model

* Width and Height : `content`의 높이와 넓이를 조절한다.
* `Padding` : content와 border사이의 공간이다.
  * px단위로 content와 border사이 공간을 지정한다.
  * `padding-top` `padding-right` `padding-right` `padding-left`로 각 방위의 padding를 조절할 수 있다.
  * `padding`값에 4개의 px값을 나열하면 순서대로 top right bottom left가 된다.
  * `padding`값에 2개의 px값을 나열하면, 앞의 값은 top과 bottom에 적용되고 뒤의 값은 right와 left에 적용된다.
* `Border` : content와 padding를 둘러싸고 있는 border의 굵기와 스타일을 조절한다.
  * width : thin, medium, thick로 두께를 조절한다. px과 같은 단위로도 조절할 수 있다.
  * style : none, dotted, solid등으로 border의 모양을 조절한다.
  * color : border의 색을 조절한다.
  * default값은 medium none color이다.
    * color는 해당 box의 현재 색을 의미한다. (글자색..)
  * border의 코너는 border-radius로 모양을 변경할 수 있다.
* `Margin` : border와 box 바깥 사이의 공간이다
  * 기본적으로 padding과 같다.
  * auto를 설정할 수 있다. (중앙 정렬..)
  * 효과적인 margin은 옆 box와 20px, 아래 box와 30px이다.
* 웹의 크기가 제각각 다르므로 width 와 height의 min, max값을 지정할 수 있다.
  * `min-width`
  * `max-width`
  * `min-height`
  * `max-height`
* `Overflow` : 설정된 box의 크기(content + padding + border + margin)가 표시할 수 있는 구역 (containing area)의 크기보다 클 경우를 overflow라고 한다.
  * hidden : overflow된 content를 보이지 않게 한다.
  * scroll : scroll을 생성해서 overflow된 content를 볼 수 있게 한다.
  * visible : overflow된 content를 표시할 수 있는 구역을 벗어나서 볼 수 있게 설정한다. default 값 이다.
* `Visibility` : 원하는 element를 화면에서 사라제기 할 수 있다.
  * hidden : element를 가린다.
  * visible : element를 화면에 나타낸다.
  * display: none의 경우 화면에서 완전 삭제 하지만, 
    visibility: hidden의 경우에는 화면에 보이지 않을 뿐 해당하는 공간은 공백으로 남아있게 된다.



### 4) Inline - block

css에 같은 내용 포함..



# 2. CSS ( Cascading Style Sheet )

### *) css 적용 방법

* html파일에서 적용

  * 각 tag에서 바로 적용

  ```html
  <p style="color: red; font-size: 20px; font-family: Arial;">I'm learning to code!</p>
  ```

  * head에서 뭉텅이로 적용하기

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

* css link걸어주기

  ```html
  <link href="style.css" type="text/css" rel="stylesheet">
  ```

  * css 파일에서 tag 걸기

  ```css
  p {
      font-family: Arial;
  }
  h1 {
      color: maroon;
  }
  ```

  

### 1) px, em, rem, vw, vh 등 단위 길이

 * `px` : 화소단위이다. 대부분의 브라우저는 1/96인치를 1px로 설정.
 * `%` :  기본글꼴의 크기(상속 및 기본값 기준)에 대하여 상대적인 값을 가진다.
 * `em` : 부모 element의 폰트사이즈를 상속받는다. (1em == 1배)
 * `rem` : 최상위 tag의 폰트사이즈를 상속받는다. (보통 html)
 * `vw` : 너비의 1/100
 * `vh` : 높이의 1/100
 * `vmin` : 너비 또는 높이 중 작은 쪽의 1/100
 * `vmax`: 너비 또는 높이 중 큰 쪽의 1/100



### 2) 선택자(selector)

* 기본 셀렉터 

  * `*` : 모든 요소에 적용된다.

  * `.container` : container class에 적용된다.

  * `#main` : id=main에 적용된다.

  * `!important`

    * `!important`로 강조한 항목은 class, ID를 무시하고 적용된다.

    ```css
    p { color: blue !important;}
    
    .main p { color: red;}
    ```

    위 경우 main class의 하위에 존재하는 p element도 blue color을 적용받게 된다.

 * 어트리뷰트 셀렉터
    * `a[href]` : a tag elements 중에 href 어트리뷰트를 갖는 모든 elements에 적용된다.
    * `a[target="_blank"]` : a tag elements 중에 target의 값을 _blank로 갖는 모든 elements에 적용된다.
    * `p[title~="first"]` : p tag elements 중에 title 어트리뷰트의 값으로 first를 갖는 모든 elements에 적용된다. 단 first의 앞 뒤는 공백으로 구분되어 있어야 한다.
    * `p[title|="second"]` : p tag elements 중에 title 어트리뷰트의 값이 seond이거나 second뒤에 "-"로 이어지는 모든 elements에 적용된다.
    * `p[title^="second"]` : p tag elements 중에 title 어트리뷰트의 값이 second로 시작하는 모든 elements에 적용된다.
    * `a[href$=".net"]` : a tag elements 중에 href 어트리뷰트의 값이 .net로 끝나는 모든 element에 적용된다.
    * `p[title*="first"]` : p tag elements 중에 title어트리뷰트의 값에 first가 포함되어 있는 모든 elements에 적용된다.
* combinator 셀렉터
  * `div p` : div요소의 후손 (n level)요소 중 p tag 전체에 적용된다.
  * `div > p` : div요소의 자손 (1 level)요소 중 p tag 전체에 적용된다.
  * `p + ul` : p의 sibling(형제) 요소 중에 바로 뒤에 오는 ul 요소에 적용된다.
  * `div ~ p` : div의 sibling 요소 중에 뒤에 오는 모든 p 요소에 적용된다.
  * `h1.special` : h1 element의 special class에만 적용된다.
  * `h1, .menu` : h1 element와 menu class에 동시에 적용된다.
* pseudo 셀렉터
  * `a:hover` : a 태그에 마우스를 올리면 적용된다.
  * `input:focus` : input에 포커스가 가면 적용된다.
  * `a:link` : a link를 방문하지 않았을 때 적용된다.
  * `a:visited` : a link를 방문했을 때 적용된다.
  * `a:active` : a link를 클릭하고 있을 때 적용된다.
  * `input:enabled + span` : input이 사용 가능할 때, input element 바로 뒤에 오는 형제 span을 선택하여 적용한다.
  * `input:disabled + span` : input이 사용 불가능할 때, input element 바로 뒤에 오는 형제 span을 선택하여 적용한다.
  * `input:checked + span` : input이 checked상태일 때, input element 바로 뒤에 오는 형제 span을 선택하여 적용한다.
  * `p:first-child` : 전체 자식 중 첫번째 element가 p element일 경우 선택하여 적용한다.
  * `p:last-child` : 전체 자식 중에서 마지막 element가 p element일 경우 선택하여 적용한다.
  * `ol>li:nth-child(2n)` : ol element의 자식 중 짝수번째 element가 li element일 경우 선택하여 적용한다.
  * `ol>li:nth-child(4)` : ol element의 자식 중 4번째 element가 li element일 경우 선택하여 적용한다.
  * `ul> :nth-last-child(2n+1)` : ul element의 자식 중 뒤에서 홀수번째 element를 선택하여 적용한다.
  * `p:first-of-type` : p element의 자식 중 첫번째인 p element를 선택하여 적용한다.
  * `p:last-of-type` : p element의 자식 중 마지막 p element를 선택하여 적용한다.
  * `p:nth-of-type(2)` : p element의 자식 중 두번째 p element를 선택하여 적용한다.
  * `p:nth-last-of-type(2)` : p element의 자식 중 뒤에서 두번째 p element를 선택하여 적용한다.
  * `input:not([type="password"])` : input element중 type이 password가 아닌 것을 선택하여 적용한다.
  * `p::first-letter` : p의 첫 글자를 선택하여 적용한다.
  * `p::first-line` : p의 첫 줄을 선택하여 적용한다.
  * `h1::before { content: "HTML5!"; }` : h1 element 앞에 content가 붙음, content는 드래그로 선택되지 않음
  * `h1::after { content: "CSS3!"; }` : h1 element 뒤에 content가 붙음, content 는 드래그로 선택되지 않음
  * `::selection` : 선택된 경우(마우스 클릭 or drag)에 적용됨. (color, background, cursor, outline)



### 3) inline / block

 * `block`
    * 항상 새로운 라인에서 시작한다.
    * 화면 크기 전체의 가로폭을 차지한다. (width : 100%)
    * block레벨 요소 내에 inline레벨 요소를 포함할 수 있다.
    * div, h1 ~ h6, p, ol, ul, li, hr, table, form, etc...
    * div element
       * 여러 element의 스타일을 한 번에 적용하기 위해 사용한다.
 * `inline`
    * 새로운 라인에서 시작하지 않으며 문장의 중간에 들어갈 수 있다.
    * content의 너비만큼만 가로폭을 차지한다.
    * width, height, margin-top, margin-bottom property를 지정할 수 없다.
    * 상, 하 여백은 line-height 로 지정한다.
    * span, a, strong, img, br, input, select, textarea, button
    * span element
       * text의 특정 부분에 따로 스타일을 적용하기 위해 사용한다.
 * `inline-block`
    * block과 inline레벨 요소의 특징을 모두 갖는다.
    * inline레벨 요소처럼 한 줄에 표시되면서, block에서의 width, height, margin(top, bottom) 속성을 모두 지정할 수 있다.
 * `None`
    * 해당 요소를 화면에 표시하지 않는다.(공간조차 사라진다.)



### *) Float

* left 혹은 right로 element를 이동시킬 때 사용한다.
* left : 가능한 만큼 left로 element를 이동시킨다.
* right : 가능한 만큼 right로 element를 이동시킨다.
* float를 적용하는 element는 반드시 width값이 정해져 있어야 한다.
* Clear : float한 element들이 충돌하는걸 방지하기 위해서 필요하다.
  * left :  left쪽에 있는 element가 같은 containing안에 있는 다른 element를 건들지 않는다.
  * right : right쪽에 있는 element가 같은 containing안에 있는 다른 element를 건들지 않는다.
  * both : 양쪽에 있는 element들이 같은 containing안에 있는 다른 element를 건들지 않는다.
  * none : element가 양쪽 element를 모두 건들 수 있다.



### *) Position

* static : default값이다.
* relative : `position:relative`에서는 `top`, `bottom`, `left`, `right`값을 설정하여 기준점에서 멀어지게 설정할 수 있다.
* fixed : `position:fixed`에서도 relative와 같이 `top`, `bottom`, `left`, `right`을 설정할 수 있다.
  * page의 스크롤을 이동해도 화면에 고정되어 스크롤과 같이 움직이지 않는다.
* absolute : `position:absolute`에서도 relative와 같이 `top`, `bottom`, `left`, `right`을 설정할 수 있다.
  * 다른 요소의 위치를 무시하고 움직인다.(겹치게 할 수 있다.)
  * 그래서 z-index를 설정하여서 우선순위를 정해주어야 한다.



# 3. Bootstrap

### 1) Text

* `Text alignment`
  * .text-left : 왼쪽 정렬
  * .text-center : 가운데 정렬
  * .text-right : 오른쪽 정렬
  * .text-sm-left, .text-md-left, .text-lg-left, .text-xl-left 등 특정 브라우저 크기에서 적용되는 정렬도 설정할 수 있다.
* `Text wrapping and overflow`
  * .text-nowrap : `style="width: 8rem"`과 같이 너비를 같이 지정해 주면 그만큼 wraping하는 블럭이 글씨를 감싼다..
  * .text-truncate : 긴 글의 앞부분만 표기해준다.
    * `display: inline-block` or `display: block`이 요구된다.
* `Text transform`
  * .text-lowercase : 모두 소문자로 바꾼다.
  * .text-uppercase: 모두 대문자로 바꾼다.
  * .text-capitalize : 공백 이후 첫 글자를 대문자로 바꾼다.
* `Font weight and italics`
  * .font-weight-bold : bold weight로 바꾼다.
  * .font-weight-normal : normal weight로 바꾼다.
  * .font-weight-light : light weight로 바꾼다.
  * .font-italic : italic font로 바꾼다.



### 2) Color

* `Text color`
  * .text-primary  : 파란색
  * .text-secondary : 회색
  * .text-success : 녹색
  * .text-danger : 빨간색
  * .text-warning : 노란색
  * .text-info : 청록색
  * .text-dark : 검정색
  * .text-muted : 회색, link styling(링크 tag에 해당 클래스가 부여됬을 경우 hover, focus상태에 부여되는 styling)이 존재하지 않음.
  * .text-light : 흰색(보다 약간 어두운..)
  * .text-white : 흰색, link styling이 존재하지 않음.
* `Background color`
  * .bg-primary : 파란색
  * .bg-secondary : 회색
  * .bg-success : 녹색
  * .bg-danger : 빨간색
  * .bg-warning : 노란색
  * .bg-info : 청록색
  * .bg-light : 흰색(보다 약간 어두운 색)
  * .bg-dark : 검정색
  * .bg-white : 흰색



### 3) Spacing

* `breakpoint`

  |                     | Extra small <576px | Small ≥576px | Medium ≥768px | Large ≥992px | Extra large ≥1200px |
  | ------------------- | ------------------ | ------------ | ------------- | ------------ | ------------------- |
  | Max container width | None (auto)        | 540px        | 720px         | 960px        | 1140px              |
  | Class prefix        | `.col-`            | `.col-sm-`   | `.col-md-`    | `.col-lg-`   | `.col-xl-`          |

* margin과 padding을 지정할 수 있다. 
  * default ($spacing)값은 Sass map에 의해 정해진다. (range 0.25rem ~ 3rem)
  * $spacing의 default는 1rem이다.
* xs의 경우 {property}{sides}-{size}, 
  sm, md, lg, xl의 경우 {property}{sides}-{breakpoint}-{size}로 클래스 이름을 정의한다.
* `property`
  * m : margin
  * p : padding
* `sides`
  * t : top
  * b : bottom
  * l : left
  * r : right
  * x : x축(left, right)
  * y : y축(top, bottom)
  * blank : all sides
* `size`
  * 0 : set 0
  * 1 : $spacer * 0.25
  * 2 : $spacer * 0.5
  * 3 : $spacer
  * 4 : $spacer * 1.5
  * 5 : $spacer * 3
  * auto : set margin auto
    * display:block과 width값이 존재할 경우 .mx-auto를 하면 horizontal center로 align할 수 있다.



### 4) 컴포넌트들 이름과 요소 매칭

(참고하면 좋은 사이트 - https://hackerthemes.com/bootstrap-cheatsheet/)

* Alerts
* Badge
* Breadcrumb : text로 현재 위치만 inactive한 link group같은..거?
* Buttons / Button group
  * 버튼 하나하나는 button, 버튼 여러개가 같은 스타일로 묶여있으면 group..
* Card
* Carousel : 이미지 슬라이드
* Collapse / Dropdowns
  * 화면이 작아지거나 할 때 내용을 숨겨주는게 collapse / button에 목록을 숨겨주는게 dropdowns
* Forms / Input group
  * id/password login form, 여러 선택지 중에 선택하는 form 등등..
  * input그룹은 라벨, 버튼 등으로 꾸며진 인풋
* Jumbotron : 중요한 메세지를 미리보기용으로 보여주기 위한 서머리 창.....(연한 회색 배경)
* List group : 리스트 그룹..(링크나 버튼도 가능)
* Modal : 눌렀을때 뜨는 팝업창
* Navs / Navbar
  * navbar로 nav가 들어갈 수 있는 bar를 형성 
* Pagination : page를 이동할 수 있는 bar를 생성
* Popovers : 버튼을 클릭했을 때 안내 메세지를 생성
* Progress / Scrollspy
  * 진행상태를 올려주는 progress bar
  * 스크롤 이동에 따라 현재 위치를 표시해주는 scrollpy
* Tooltips : 버튼에 마우스를 올렸을 때 안내 메세지를 생성



### 5) flex 기초(flexboxfroggy.com)

* `justify-content`
  * flex-start : 요소들을 컨테이너의 왼쪽으로 정렬한다.
  * flex-end : 요소들을 컨테이너의 오른쪽으로 정렬한다.
  * center : 요소들을 컨테이너의 가운데로 정렬한다.
  * space-between : 요소들 사이에 동일한 간격을 둔다. ( 양 끝에 달라붙음 )
  * space-around : 요소들 주위에 동일한 간격을 둔다. ( 양 끝에서 떨어짐 )
  * **bootstrap** 에서는 `.justify-content-start` / `.justify-content-end` / `.justify-content-center` / `.justify-content-between` / `.justify-content-around`로 사용한다.
    * 특정 사이즈의 브라우저에서 적용을 하기 위해선 content뒤에 breakpoint를 입력해주면 된다.
    * ex ) `.justify-content-md-end`
* `align-items`
  * flex-start : 요소들을 컨테이너의 꼭대기로 정렬한다.
  * flex-end : 요소들을 컨테이너의 바닥으로 정렬한다.
  * center : 요소들을 컨테이너의 세로선 상의 가운데로 정렬한다.
  * baseline : 요소들을 컨테이너의 시작위치에 정렬한다.
  * stretch : 요소들을 컨테이너에 맞도록 늘린다.
  * **bootstrap** 에서는 `.align-items-start`/ `.align-items-end` / `.align-items-center` / `.align-items-baseline` / `.align-items-stretch`로 사용한다.
    * 특정 사이즈의 브라우저에서 적용을 하기 위해선 items 뒤에 breakpoint를 입력해 주면 된다.
    * ex ) `.align-items-sm-end`
* `flex-direction`
  * row: 요소들을 텍스트의 방향과 동일하게 정렬한다.
  * row-reverse : 요소들을 텍스트의 반대방향으로 정렬한다.
  * column : 요소들을 위에서 아래로 정렬한다.
  * column-reverse : 요소들을 아래에서 위로 정렬한다.
  * **bootstrap**에서는 `.flex-row` / `.flex-row-reverse` / `.flex-column` / `.flex-column-reverse` 로 사용한다.
    * 특정 사이즈의 브라우저에서 적용하기 위해서느flex뒤에 breakpoint를 입력해 주면 된다.
    * ex ) `.flex-md-row`



# 4. Django

### *)Django-admin

* $django-admin startproject MYMODEL
  * MYMODEL project를 생성한다.
* $django-admin startapp mymodel
  * mymodel app을 생성한다.



### *) manage.py

* $python manage.py runserver $IP:$PORT
  * (C9에서) 서버를 실행시킨다.
* $python manage.py makemigrations mymodel
  * mymodel 의 model을 migration한다.
* $python manage.py migrate
  * migration한 model을 적용한다.
* $python manage.py migrate mymodel zero
  * mymodel model을 초기화 한다.
* python manage.py createsuperuser
  * 관리자계정을 생성한다.



### 1) views

* import

  ```python
  from django.shortcuts import render, get_object_or_404, redirect
  from .models import Mymodel
  ```

* index page

  ```python
  def index(request):
      mymodels = Mymodel.objects.all()
      return render(request, 'mymodel/index.html', { 'mymodels':mymodels })
  ```

  index.html 의 경로와 모든 마이모델의 정보를 render로 넘겨준다.

* detail page

  ```python
  def detail(request, id):
      mymodel = get_object_or_404(Mymodel, id=id)
      return render(request, 'mymodel/detail.html', { 'mymodel': mymodel })
  ```

  get_object_or_404로 없으면 404error을 발생시키고 존재하면 받아온다.

  나머지는 index와 유사하다.

* create page

  ```python
  def create(request):
      if request.method == 'GET':
          return render(request, 'mymodel/create.html')
      else:
          mymodel = Mymodel()
          mymodel.title = request.POST.get('title')
          mymodel.save()
          return redirect('mymodel:detail', mymodel.id)
  ```

  GET 이면 create.html의 경로를 render한다.

  POST이면 mymodel을 입력하고 저장한 후 detail page로 redirect시킨다.

* update page

  ```python
  def update(request, id):
      mymodel = get_object_or_404(Mymodel, id=id)
      if request.method == 'GET':
          return render(request, 'mymodel/update.html', { 'mymodel': mymodel })
      else: 
          mymodel.title = request.POST.get('title')
          mymodel.save()
          return redirect('mymodel:detail', id)
  ```

  해당하는 id의 mymodel을 받아오고 (없으면 404 error를 발생), GET이면 update.html의 경로와 mymodel을 render한다.

  POST면 입력된 값으로 기존 값을 덮어 씌우고 저장한 다음 detail page로 redirect시킨다.

* detele page

  ```python
  def delete(request, id):
      if request.method == 'POST':
          mymodel = Mymodel.objects.get(id=id)
          mymodel.delete()
      return redirect('mymodel:index')
  ```

  POST를 받으면 해당하는 id의 mymodel을 불러온 후 삭제한다.

  index page로 redirect한다.



### 2) 템플릿(dtl)

* mkdir -p mymodel/templates/mymodel 로 새 폴더를 생성한다.

* base.html을 만들어 기본적인 세팅(css, javascripy 등)을 해준다

  * {% block body %}, {% endblock %}을 활용한다.

* index.html / create.html / detail.html / update.html을 생성한다.(detelete.html은 만들 필요가 없다.)

* 각 페이지 마다 base.html을 불러오기 위해 최상단에 {% extends 'mymodel/base.html' %}을 입력한 후 {% block body %} {% endblock %}을 통해 base.html을 불러와야 한다.

* 정보를 불러오는 것은 {{ mymodel }}처럼 render할때 넘겨준 model이나 값을 처리하면 된다.

* {% for mymodel in mymodels %} {% endfor %}처럼 for문을 활용할 수 있다.

* {% if mymodel %} 처럼 if문을 활용할 수 있다.

* 링크를 걸 때는 a tag를 사용하는데 

  ```html
  <a href="{% url 'mymodel:create' %}">create</a>
  <a href="{% url 'mymodel:detail' mymodel.id %}">detail</a>
  ```

  처럼 app_name과 urlname을 사용하면 편하게 입력할 수 있다. (id는 순서대로 적용된다.)

* POST로 정보를 전송하기 위해선 form tag를 활용한다.

  ```html
  <form action="{% url 'mymodel:delete' mymodel.id %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="delete"/>
  </form>
  ```

  하지만 보안을 위해 {% csrf_token %}은 필수적으로 입력해야만 한다.



### 3) urls

* import

  ```python
  from django.urls import path
  from . import views
  ```

  path modul과 현재 app의 views를 import한다.

* app_name

  ```python
  app_name = 'mymodel'
  ```

  app_name 을 설정해 준다.

* urlpatterns

  ```python
  urlpatterns = [
      path('', views.index, name='index'),
      path('<int:id>/', views.detail, name='detail'),
      path('create/', views.create, name='create'),
      path('<int:id>/update/', views.update, name='update'),
      path('<int:id>/delete/', views.delete, name='delete'),
  ]
  ```

  url 경로와 views에서 적용할 함수, 그리고 경로가 가질 이름까지 적용한다.