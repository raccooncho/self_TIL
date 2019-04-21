### Django & Sqlite3



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

  