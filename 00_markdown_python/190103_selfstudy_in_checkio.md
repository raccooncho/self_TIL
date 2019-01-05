# 1. 대문자전환

#### 1) 스트링의 첫 단어의 첫 글자만 대문자로 바꾸는 경우

```python
mystr = "john, they're bill's friends from the UK"
print mystr.capitalize()
# John, they're bill's friends from the uk
```

* [str.capitalize()](https://docs.python.org/2/library/stdtypes.html?highlight=title#str.capitalize)는 str의 첫 글자만을 대문자로, 나머지는 전부 소문자로 바꾼 str을 return해 준다.

#### 2) 문장의 모든 단어의 첫 글자를 대문자로 바꾸는 경우

```python
mystr = "john, they're bill's friends from the UK"
print mystr.title()
# John, They'Re Bill'S Friends From The Uk
```

* str.title()는 모든 단어의 첫 글자를 대문자로, 나머지 글자는 소문자로 변환한 str을 return한다.

* 단어를 나누는 기준에 공백 뿐 아니라 '나 ''도 포함되어 있다.

#### 3) str.title()을 보완한 string.capwords()

```python
import string
mystr = "john, they're bill's friends from the UK"
print string.capwords(mystr)
# John. They're Bill's Friends From The Uk
```

#### 4) 모든 문자를 바꾸고 싶을경우

```python
mystr = "john, they're bill's friends from the UK"
print(mystr.upper())
# JOHN, THEY'RE BILL'S FRIENDS FROM THE UK
print(mystr.lower())
# john, they're bill's firends from the uk
```

#### 예제)

```python
# 첫 글자만 대문자로 바꾸고, 맨 뒤에는 . 을 출력하세요.
def correct_sentence(text: str) -> str:
    if text[-1] == '.':
        return text[0].upper() + text[1:]
    else:
        return f'{text[0].upper()}{text[1:]}.'

```



## 2.  .과 , 을 삭제하고 첫번째 단어 추출하기

```python
def first_word(text: str) -> str:
    text = text.replace('.', ' ').replace(',', ' ')  # .replace()로 .과 ,을 space로 변경
    text = text.strip()  # space을 제거
    text = text.split()  # 아무 값을 입력하지 않으면 공백을 기준으로 단어를 구분한다.
    return text[0]
```

* split 메소드

```python
>>> a = "Life is too short"
>>> a.split()  # 아무것도 입력되지 않으면 공백을 기준으로 단어를 구분한다.
['Life', 'is', 'too', 'short']
>>> a = "a:b:c:d"
>>> a.split(':')  # 입력한 값을 기준으로 단어를 구분한다.
['a', 'b', 'c', 'd']
```

