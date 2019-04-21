# Django & Sqlite3

### SQL Basic

* 데이터베이스 : 체계화된 데이터의 모임
* RDBMS(관계형 데이터베이스 관리 시스템) 
* 스키마(scheme) : 자료의 구조, 표현방법, 관계 등을 정의한 구조
  * 데이터베이스의 구조와 제약조건에 관련한 전반적인 명세를 기술한 것
* SQL(Structured Query Language) : RDBMS의 데이터를 관리하기 위해 설계된 특수목적의 프로그래밍 언어이다.
  * DDL(데이터 정의 언어) : 데이터를 정의하기 위한 언어 ( CREATE, DROP, ALTRE )
  * DML(데이터 조작 언어) : 데이터를 저장, 수정, 삭제, 조회하기 위한 언어 ( INSERT, UPDATE, DELETE, SELECT )
  * DCL(데이터 제어 언어) : :데이터베이스 사용자의 권한제어를 위해 사용되는 언아 ( GRANT, REVOKE, COMMIT, ROLLBACK )

```sqlite
.mode csv
.import hellodb.csv examples
```

* 전체 선택 하기

```sqlite
SELECT * FROM examples;
```

* 예쁘게 보려면

```sqlite
.headers on
.mode column
```

* table 생성하기

```sqlite
CREATE TABLE classmates (
id INT PRIMARY KEY, name TEXT);
```

* 테이블 목록 조회 및 특정 테이블 스키마 조회

```sqlite
.table
.schema classmates
```

* 특정 table 삭제

```sqlite
DROP TABLE classmates;
```

* data 추가 (INSERT)

```sqlite
INSERT INTO classmates (name, age)
VALUES ('홍길동', 23);
```

* 모든 열에 데이터를 추가할 경우에는 column을 명시할 필요가 없다.

```sqlite
INSERT INTO classmates VALUES ('홍길동', 23);
```

* id같이 필수적이고 중복되면 안되는 값에 AUTOINCREMENT를 사용할 수 있다 (INTEGER에서만 사용 가능)

```sqlite
CREATE TABEL classmates (
id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INT NOT NULL,
    address TEXT NOT NULL
);
```

* data 가져오기 (SELECT)

```sqlite
SELECT * FROM classmates;
SELCET name, age FROM classmates;
```

* 정해진 숫자만 가져오기 (LIMIT)

```sqlite
SELECT id, name FROM classmates LIMIT 3;
```

* 가져오는 값의 인덱스를 정하기 (OFFSET)

```sqlite
SELECT id, name FROM classmates LIMIT 3 OFFSET 2;
```

* 조건을 부여하기 (WHERE)

```sqlite
SELECT id, name FROM classmates WHERE address="서울";
```

* data 삭제 (DELETE)

```sqlite
DELETE FROM classmates WHERE id=3;
```

* data 수정 (UPDATE)

```sqlite
UPDATE classmates SET name="홍길동", address="제주도" WHERE id=4;
```

* 갯수 세기 (COUNT)

```sqlite
SELECT COUNT(*) FROM users;
```

* 표현식 
  * AVG, SUM, MIN, MAX :숫자 일때만 사용 가능하다

  ```sqlite
  SELECT first_name, MAX(balance) FROM users;
  SELECT AVG(balance) FROM users WHERE age >= 30;
  ```
  * LIKE  : 패턴을 비교한다.

  ```sqlite
  SELECT * FROM users WHERE age LIKE '2%';
  ```

| %    | 2%      | 2로 시작하는 값                               |
| ---- | ------- | --------------------------------------------- |
|      | %2      | 2로 끝나는 값                                 |
|      | %2%     | 2가 들어가는 값                               |
| _    | _2%     | 아무 값이나 들어가고 두번째가 2로 시작하는 값 |
|      | 1___    | 1로 시작하고 4자리인 값                       |
|      | `2_%_%` | 2로 시작하고 적어도 3자리인 값                |

* 정렬(ORDER)

```sqlite
# 나이순으로 오름차순 정렬하여 상위 10개만 출력
SELECT * FROM users ORDER BY age ASC LIMIT 10;
# 나이순, 성 순 으로 오름차순 정렬하여 상위 10개만 출력
SELECT * FROM users ORDER BY age, last_name ASC LIMIT 10;
# 계좌잔액순으로 내림차순 정렬하여 이름만 10개 출력
SELECT first_name, last_name FROM users ORDER BY balance DESC LIMIT 10;
```



### Django

* pip install django_extensions
* python manage.py shell_plus



* data 생성 : 

  ```sqlite
  user1 = User.objects.create(name-'cho')
  post1 = Post.objects.create(title='aa', user = user1)
  content1 = Content.objects.create(content='aa', post=post1, user=user1)
  ```

  

* data 얻기

  ```sqlite
  User.objects.get(id=1)
  or
  User.objects.get(pk=1)
  # id가 1인 user
  ```

  ```splite
  user1 = User.objects.get(id=1)
  
  user1.post_set.all()
  # 1번 유저의 모든post
  ```

  ```sqlite
  for post in user1.post_set.all():
  	for comment in post.comment_set.all():
  	    print(comment.content)
  # 1번 유저가 쓴 글의 모든 comment
  ```

  ```sqlite
  comment1.user.name
  # 1번 댓글 단 사람 이름
  comment1.user.post_set.all()
  # 1번 댓글 단 사람이 쓴 모든 글
  ```

  ```sqlite
  post1.comment_set.first().user.name
  post1.comment_set.all()[0].user.name
  # post1의 첫번째 댓글 단 사람
  ```

  ```sqlite
  post1.comment_set.all()[1:4]
  # 1번 글의 2~4번째 댓글
  ```

  ```sqlite
  Comment.objects.value('user').get(id=1)
  # 1번 댓글의 user정보만
  ```

  ```sqlite
  user1.comment_set.order_by('-content')
  # 1번 사람이 작성한 댓글을 content의 내림차순으로
  ```

  ```sqlite
  Post.objects.filter(title='1글')
  # 제목이 1글인 모든 게시물
  ```

  ```sqlite
  Post.objects.filter(title__contains='글')
  # 제목에 '글'이 포함된 모든 게시물
  ```

  ```sqlite
  Comment.objects.filtre(post__title='1글')
  # 제목이 '1글'인 게시물에 쓰여진 모든 댓글
  ```

  ```sqlite
  Comment.objects.filter(post__title__contains='1')
  # 제목에 '1'이 포함된 글에 쓰여진 모든 댓글
  ```

  

* one to one field

  ```python
  class Profile(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE)
      nickname = models.CharField(max_length=20)
  ```



* many to many field

  * 1 : N으로 만들기

  ```python
  class Doctor(models.Model):
      name = models.CharField(max_length=20)
      
  class Patient(models.Model):
      name = models.CharField(max_length=20)
      
  class Reservations(models.Model):
      doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
      patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  ```

  * 간단하게 바꾸기

  ```python
  class Doctor(models.Model):
      name = models.CharField(max_length=20)
      
  class Patient(models.Model):
      name = models.CharField(max_length=20)
      doctors = models.ManyToManyField(Doctor, related_name='patients')
  ```

  