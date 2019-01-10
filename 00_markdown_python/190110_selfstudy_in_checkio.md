## 1.  Right to Left

##### list안의 단어들을 ','을 기준으로 하나의 str로 합치고, 모든 right를 left로 바꾸세요.

```python
def left_join(phrases):
    left = ','.join(phrases).replace('right', 'left')
    return left
```



## 2. Digits Multiplication

##### 주어진 숫자의 각 자릿수를 모두 곱하시오. 단, 0은 곱하지 말것!

```python
def checkio(number: int) -> int:
    num = [i for i in str(number)]  # for문으로 한번에 나누려면 str로 변경해야함.
    result = 1
    for i in num:
        if int(i) != 0:
            result *= int(i)
    return result
```



## 3. Number Base

##### str과 숫자n이 주어진다. str은 n진법으로 표현된 숫자이다. 이를 10진법의 정수로 바꾸어라. 만약 n의 범위를 넘어간 수가 주어진다면 (ex 2진법에 2) -1을 리턴하라.

```python
def checkio(str_number: str, radix: int) -> int:
    numbers = [i for i in str_number.lower()]
    list_number = '0123456789abcdefghijklmnopqrstuvwxyz'
    result = 0
    for i in numbers:
        decinum = list_number.index(i)
        if decinum >= radix:
            return -1
        i_ind = numbers.index(i)
        ind_num = len(numbers) - i_ind -1
        result += decinum * (radix ** ind_num)
        numbers.remove(i)
        numbers.insert(i_ind, '.')
    return result
```



