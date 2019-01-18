## 1. file write

#### 파일 생성하기

* 파일열기

```python
f = open("새파일.txt", "w")
```

* 파일 객채 = open (파일 이름, 파일 열기 모드)를 이용해서 호출할 수 있다.

  | 파일열기모드 | r(읽기모드)              | w(쓰기모드)              | a(추가모드)                                    |
  | ------------ | ------------------------ | ------------------------ | ---------------------------------------------- |
  | 설명         | 파일을 읽기만 할 때 사용 | 파일에 내용을 쓸 때 사용 | 파일의 마지막에 새로운 내용을 추가시킬 때 사용 |

* 파일 쓰기 모드로 열었을 때 파일이 이미 존재할 경우 -> 원래 있던 내용이 모두 사라짐

  * 없는 파일일 경우 -> 새로운 파일이 생성됨

* 다른 디렉토리에 파일을 생성하고 싶다면

  ```python
  f = open("C:/doit/새파일.txt", 'w')
  ```

  이렇게 디렉토리의 경로를 지정해 주면 된다.

* 쓰기모드로 열었던 파일을 닫지 않고 다시 사용하려고 하면 오류가 발생할 수 있기 때문에 `f.close()`를 통해서 파일을 닫아주는 것이 좋다.



##### 파일을 쓰기모드로 열어 출력값 적기

* 프로그램의 출력값을 파일에 써 볼 수 있다.

```python
f = open("C:/doit/새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
```

* .wirte() 메서드를 이용해서 데이터를 파일에 추가할 수 있다.



#### 프로그램의 외부에 저장된 파일을 읽는 여러가지 방법

##### readline()함수 이용하기

* `.readline()`메서드는 파일의 첫번째 줄을 읽어서 출력하는 함수이다.

```python
f = open("C:/doit/새파일.txt", 'r')
line = f.readline()
print(line)
f.close()
```

* 만약 모든 라인을 출력하고 싶으면 while문을 이용해서 읽을 수 있다.

```python
f = open("C:/doit/새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()
```

* 이렇게 된다면 한 줄씩 파일을 계속해서 읽어들이게 된다.
  * readline()함수는 더 이상 읽을 라인이 없을 경우 None을 출력한다.



##### readlines()함수 이용하기

* `readlines()`메서드를 이용하면 한번에 여러줄을 출력할 수 있다.(리스트로)

```python
f = open("C:/doit/새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()
```

위 예시에서는 `["1 번째 줄입니다.\n","2 번째 줄입니다.\n",..., "10 번째 줄입니다.\n"]`라는 리스트가 생성되게 된다.(한줄을 하나의 element로 여기는 list이다.)



##### read()함수 이용하기

* `.read()`메서드는 파일의 내용 전체를 문자열로 리턴한다.

```python
f = open("C:/doit/새파일.txt", 'r')
data = f.read()
print(data)
f.close()
```



#### 파일에 새로운 내용 추가하기

* 파일에 새로운 내용을 추가하기 위해서는 a모드로 파일을 열어야 한다.

​	(w모드로 열었을 경우에는, 파일 내용이 모두 초기화 되기 때문이다.)



#### with문과 함께 사용하기

* with문을 이용하면 with블록을 벗어나는 순간 자동으로 파일이 close되어 편리하게 사용할 수 있다. 

  (with 문은 python 2.5 버전부터 지원되는 기능임)

  ```python
  with open("foo.txt", "w") as f:
      f.write("Life is too short, you need python")
  ```

  