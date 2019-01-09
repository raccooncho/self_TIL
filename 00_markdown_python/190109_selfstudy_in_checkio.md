## 1.  Even the last

##### index가 짝수인 수를 더하고 index가 가장 큰 수를 거기에 곱해라.

```python
def checkio(array):
    if array == False:
        return 0
    sum_number = 0
    multi = 0
    for index, number in enumerate(array):
        if index % 2 == 0:
            sum_number += number
        if index == (len(array) - 1):
            multi = number
    return sum_number * multi
```



## 2. Secret Message

##### str 안에 있는 대문자만 추출해서 표출하시오. 없으면 None/

```python
def find_message(text: str) -> str:
    result = []
    s_message = ''
    capital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in range(len(text)):
        if text[i] in capital:
            result.append(text[i])
    for s in result:
        s_message += s
    return s_message
```

```python
def find_message(text: str) -> str:
    return ''.join(c for c in text if c.isupper())
```



## 3. Three Words

##### space 한칸 간격으로 str과 int가 나열되어 있는 str이 주어진다. str이 연속 3개 이상 존재하면 True 아니면 False를 return 하라.

```python
def checkio(words: str) -> bool:
    word = words.split()
    count = 0
    num = list(range(0, 10))
    for w in word:
        for i in num:
            if str(i) in w:
                count = 0
                break
        else:
            count += 1
            if count == 3:
                return True
    return False
```



## 4. Index Power

##### 숫자의 list와 number이 하나씩 주어진다. number를 index로 가지는 수의 number제곱을 return 한다. 단, index가 범위를 벗어나면 -1을 return 한다.

```python
def index_power(array: list, n: int) -> int:
    if len(array) > n:
        result = int(array[n] ** n)
    else:
        result = -1
    return result

```

