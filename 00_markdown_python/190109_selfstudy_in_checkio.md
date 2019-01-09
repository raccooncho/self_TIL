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



