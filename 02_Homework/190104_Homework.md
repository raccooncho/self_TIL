# 190104_Homework

### 1) True / False

* windows 와 unix 계열 운영체제는 CLI(Command Line Interface) 에서 같은 명령어를 사용한다. [F]
* 우리가 사용하는 컴퓨터는 windows 이므로, unix 계열 운영체제 명령어를 학습할 필요가 없다. [F]
* CLI 는 결국 컴퓨터를 조작하기 위해 사용하는 것이다. [T]
* CLI 를 통해서 바탕화면에 새로운 파이썬 파일(.py)을 생성할 수 있다.[T]



### 2) 다음 unix 명령어들에 대하여 간략하게 기술하세요

* ls
  * 현재 디렉토리에 존재하는 파일 목록을 나열합니다.
* cd
  * 뒤에 입력하는 디렉토리로 이동합니다.
* mkdir
  * 새로운 디렉토리를 생성합니다.
* touch
  * 새로운 파일을 생성합니다.



### 3) CLI 와 익숙해지게 되면, Tab키를 매우 빈번하게 사용하게 됩니다. 그 이유는 무엇일까요?

#### (git bash를 켜고 cd Desk까지만 입력 후 탭 키를 눌러 봅시다!)

* 원하는 문구를 자동 완성 시켜 줍니다.!





#### * 달력만들기

```python
for i in range(1, 13):
    print(f'{i} 월\n 일 월 화 수 목 금 토 ')
    if i in [1, 3, 5, 7, 8, 10, 12]:  # list로 만들어서 안에 있는 값을 찾으니까 됨.
        n = 31
    elif i in [2]:    
        n = 28
    else:
        n = 30
    for d in range(1, n + 1):
        if d < 10:
            if d == 7:
                print(f' {d}  ')
            else:
                print(f' {d} ', end='')
        elif d == n:
            print(f'{d} \n')
        elif d % 7:
            print(f'{d} ', end='')
        else:
            print(f'{d}  ')
```

