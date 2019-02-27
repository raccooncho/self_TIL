# 1. HTML / CSS

```
- HTML 파일 제공.
- 예시 결과를 보고 CSS를 직접 작성해서 HTML Tag에 적용하는 형식. (주로 텍스트를 꾸미는 형식, 수업시간 및 프로젝트에서 자주 사용했던 속성들 위주로 출제)
- tag 선택자, class 선택자, id 선택자만 사용해도 되도록 출제.
- position, display, background-image 같은 속성들은 출제 안됨.
- class 선택자, id 선택자를 이용하여 작성한 CSS를 HTML Tag에 적용하는 방법 숙지 필요.
```



### 1) css linking

```html
<link href="style.css" type="text/css" rel="stylesheet">
```



#### %) inline에서 특정 부분만 class를 부여하려면 span tag를 사용!



### 2) 완전 basic

* `font-family`

  * font-family 의 이름이 두 당너 이상일 경우에는 " "안에 font 이름을 적어준다.

  ```css
  font-family: "Courier New";
  ```

  * linking font-family

  ```html
  <head>
    <link href="https://fonts.googleapis.com/css?family=Droid+Serif|Playfair+Display" type="text/css" rel="stylesheet">
  </head>
  ```

  ​	( Droid Serif 와 Playfair Display 가 사용 가능해진다. font-family에서 사용하면 된다. - '|'로 각 폰트가 구분되고 폰트 이름에서 띄어쓰기는 '+'로 표현됨 )

* `font-size`

* `font-weight`

  * 100 ~ 900의 100단위 숫자이다.
  * default 는 400, light 는 300, bold 는 700

* `font-style` : default는 normal / italic을 적용할 수 있음

* `text-align` : right / center / left

* `text-transform` : uppercase / lowercase

* `line-height` : 줄간 간격을 조절할 수 있다.

  * 그냥 숫자나 unit단위를 사용할 수 있다.
  * 1.2는 font size의 1/5가 줄 사이 공간(leading)이 된다

* `color`

  * color : 글자 색 변경
  * background-color : 배경 색 변경

* `opacity`

  * 0 ~ 1 사이의 투명도 조절
  * 1에 가까울 수록 불투명 (0이 완전 투명)

* _나올리없는 그것_  : word-spacing (default == 0.25em) [단어간] / letter-spacing [자간]

### 3) Box model

* width : 너비 조절
  * max-width
  * min-width
* height : 높이 조절
* Padding : content와 border사이 공간
  * `paddig-top` `padding-right` `padding-left` `padding-bottom`
  * `padding` : 0 0 0 0 (top, right, bottom, left)
  * `padding` : 0 0 (top bottom / right left)
* Border : 경계선
  * width : thin, medium, thick(px단위 등도 가능)
  * style : none, dotted, solid ( + dashed, double, groove, ridge, inset, outset, hidden)
  * color
  * default : medium none color
  * `border-radius` : 15% 75% -> ↘  ↙
* Margin : 바깥공간
  * padding과 동일
  * auto가능 ( 정렬됨)
* Overflow : hidden, scroll, visible(default)
* Visibility : hidden, visible

* z-index : 1~10 (클수록 우선순위 큼)

### 4) visibility

* visibility : { hidden / visible / collapse }
  * display: none은 공간이 사라짐 visibility: hidden은 내용만 안보임
* transition -> 애니메이션;;
  * transition-property : width, background-color;등으로 trasition을 하는 property를 지정한다.
  * transition-duration: 1.2s, 3s; 으로 지연 시간을 지정 가능



# 2. Bootstrap

```
- Grid System에 관한 문제를 출제.
- 미리 작성된 HTML 파일 제공. (CDN을 통하여 Bootstrap도 추가되어 있음)
- 예시 결과를 보고 알맞는 클래스를 채워 넣는 형식.
- Bootstrap 사이트 접속 불가능.
- Responsive Grid를 위한 Breakpoint 관련 내용은 문제에서 주어짐.
- 공식문서를 반드시 볼 것. (최소한 Grid의 Offsetting columns까지, 세로 정렬은 출제 안됨.)
```



### 1) grid system

* 기본 12칸의 column을 구성

  * 각 column사이엔 padding이 숨어져 있어서 없애기 위해선 `.no-gutters`를 추가하면 된다.

* 기본 단계

  * .container -> .row -> col
    * .container-fluid를 사용하면 좌우 margin이 사라져서 화면이 꽉 찬다.

  ```html
  <div class="container">
      <div class="row">
          <div class="col">
              <h1>
                  말이 안되는 시험이다;;
              </h1>
          </div>
      </div>
  </div>
  ```

* .align-items-{start / center / end} : 세로정렬 (.row에 같이 쓰는 클래스)

  * .align-self-{start / center / end} : 각자 돌게 할 수 있따(.col에 같이 쓰는 클래스)

* .justify-content-{start / center / end / around / between(양끝에 딱 붙음)} : 가로정렬 (.row에 같이 쓰는 클래스)

* .order-{1 ~ 12}로 순서를 정할 수 있음 (밑에 있어도 같은 .row에 있으면 .order-1이 .order-12보다 왼쪽에 출력됨) ( col에 같이 쓰는 클래스)

  * .order-first / .order-last도 가능

* .offset-{breakpoint}-{0~} : 마지막에 적힌 숫자의 column만큼 앞에 빈 column을 생성 (.col과 같이 쓰는 클래스)

  * breakpoint마다 초기화를 위해 .offset-md-0같이 0을 입력해 주어야 한다.
  * 비슷하게 왼쪽 오른쪽에 자동으로 빈 column을 생성하기 위해
    ml-{breakpoint}-auto / mr-{breakpoint}-auto 등을 사용할 수 있다.

* Nesting (.col안에 다시 .row > .col을 생성해주면 12칸의 column을 가진 row를 사용할 수 있다.)



### 2) Card

* 카드 생성 : .card ( style="width: 18rem;"과 같이 너비를 같이 줄 수 있다.)

```html
<div class="card" style="width: 18rem;">
```

* 카드 이미지: .card > img (class="card-img-top") (보통 카드 바디보다 이미지가 위에 있으므로 카드바디보다 먼저 작성해준다.)
  * card-img를 주면 body와 이미지가 overlap된다.
* 카드 바디 : .card > .card-body 안에 h1~h6, p, a tag등 을 활용해서 내용을 채우면 된다.
  * .card-title : 카드 타이틀(h5태그정도..)
  * .card-subtitle :카드 부제목 (h6태그정도..)
  * .card-text : 카드 내용 (p태그..)
  * .card-link : 링크 (a태그..)

* 카드 헤더 : .card > .card-header





# 3. Django ( 귀차나서 comment같이있는거 복붙)

```
- [R]ead(List, Detail), [D]elete(Delete) 중에 하나를 작성하는 문제 출제.
- Django 프로젝트 코드 제공. (runserver를 통한 서버 실행은 불가능)
- `views.py`에 새로운 함수 작성하여 페이지 만드는 법, template(html) 파일 만드는 법 숙지 필요.
- Django Template Language의 기본적인 사용법, '반복문', '조건문', '템플릿 상속(extends)', '페이지 출력(render)' 숙지 필요.
- 부분 점수를 위해서 최대한 많이 작성할 것.
```



### 0) import in views.py

```python
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Comment  # model import
```



### 1) base.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    {% load static %}
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="{% static 'simple_board/css/bootstrap.css' %}" type="text/css" />
    <link rel="stylesheet" href="{% static 'simple_board/css/index.css' %}" type="text/css" />
    <title>Simple Board</title>
</head>
<body>
    {% include 'simple_board/_navbar.html' %}
    <div class="container">
        {% block body %}
        {% endblock %}
    </div>
    {% include 'simple_board/_footer.html' %}
    <script type="text/javascript" src="{% static 'simple_board/js/bootstrap.js' %}"></script>
    <script type="text/javascript" src="{% static 'simple_board/js/index.js' %}"></script>
</body>
</html>
```



### 2) Read

####  list

* html

  ```html
  {% extends 'simple_board/base.html' %}
  {% load static %}
  
  {% block body %}
  <h1>All Articles</h1>
  <img src="{% static 'simple_board/images/header.jpg' %}" alt="header"></img>
  {% if articles %}
  <ol>
      {% for article in articles %}
          <li><a href="{% url 'simple_board:article_detail' article.id %}"> {{ article.title }} </a> </li>
      {% endfor %}
  </ol>
  <a href="{% url 'simple_board:article_create' %}"><button>새로 만들기</button></a>
  {% endif %}
  {% endblock %}
  ```

  

* view

  ```python
  def article_list(request):
      articles = Article.objects.all()
      context = { 'articles': articles }
      return render(request, 'simple_board/list.html', context)
  ```

  

#### detail

* html

  ```html
  {% extends 'simple_board/base.html' %}
  
  {% block body %}
  <h1>{{ article.title }}</h1>
  <p>
      {{ article.content }}
  </p>
  <hr />
  <div>
      <a href="{% url 'simple_board:article_list' %}">
          <button>목록으로 가기</button>
      </a>
  </div>
  <div>   
      <a href="{% url 'simple_board:article_update' article.id %}">
          <button>수정하기</button>
      </a>
  </div>
  <form action="{% url 'simple_board:article_delete' article.id %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="삭제하기" onclick="return confirm('정말로 삭제 하시겠습니까?')">   
  </form>
  <hr />
  
  {% include 'simple_board/_comment.html' with title=article.title %}
  
  {% endblock %}
  ```

  

* view

  ```python
  def article_detail(request, article_id):
      article = get_object_or_404(Article, id=article_id)
      comments = reversed(article.comment_set.all())
      context = { 'article': article, 'comments': comments }
      return render(request, 'simple_board/detail.html', context)
  ```

  

### 3) Delete

* html

```html
<form action="{% url 'simple_board:article_delete' article.id %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="삭제하기" onclick="return confirm('정말로 삭제 하시겠습니까?')">   
</form>
```



* view

```python
def article_delete(request, article_id):
    if request.method == 'POST':
        article = Article.objects.get(id=article_id)
        article.delete()
    return redirect('simple_board:article_list')
```





### 4) urls.py

* import

```python
from django.urls import path
from . import views
```



* urlpatterns

```python
app_name = 'simple_board'

urlpatterns = [
# URL about articles
    path('', views.article_list, name='article_list'),
    path('<int:article_id>/', views.article_detail, name='article_detail'),
    path('create/', views.article_create, name='article_create'),
    path('<int:article_id>/update/', views.article_update, name='article_update'),
    path('<int:article_id>/delete/', views.article_delete, name='article_delete'),
# URL about comments
    path('<int:article_id>/comments/create/', views.comment_create, name='comment_create'),
    path('<int:article_id>/comments/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),
    path('<int:article_id>/comments/<int:comment_id>/edit/', views.comment_update, name='comment_update'),
    ]
```





### 5) models.py

* import

```python
from django.db import models
```



* class 지정

```python
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default='')
    like = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.id}: {self.title}'
    
    
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    like = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.article.title}: {self.content}'
```

