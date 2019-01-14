## 1.  Absolute sorting

##### tuple형식으로 구성된 숫자의 묶음이 주어진다. 절대값을 기준으로 정렬하세요.

```python
def checkio(numbers_array: tuple) -> list:
    numbers = list(numbers_array)
    result = []
    while numbers:
        number = numbers[0]
        for j in numbers:
            if j**2 < number ** 2:
                number = j
        result.append(number)
        numbers.remove(number)
    return result
```



## 2. The Most Frequent

##### 문자열의 리스트 중에서 가장 빈도수가 높은 str을 출력하시오.

```python
def most_frequent(data: list) -> str:
    most_s = data[0]
    for s in data:
        if data.count(s) > data.count(most_s):
            most_s = s
    return most_s
```



## 3. Easy Unpack

##### 주어진 튜플 중에서 첫번째, 세번째, 뒤에서 두번째 element를 튜플로 묶어서 추출하세요.

```python
def easy_unpack(elements: tuple) -> tuple:
    easy = list(elements)
    result = (easy[0], easy[2], easy[-2])
    return result
```



