## 1.  Bigger Price

##### name과 price가 각각 dict형태로 묶인 list가 있다. 가장 비싼 물건을 출력하라.

```python
def bigger_price(limit: int, data: list) -> list:

    count = 0
    true_result = []
    result = []
    while count != limit:
        result = data[0]  # sample값은 가능하면 주어진 list안의 것으로 하자.
        for lists in data:
            if lists["price"] >= result["price"]:
                result = lists
        data.remove(result)
        count += 1
        true_result.append(result)
    
            
    return true_result
```



## 2. Fizz Buzz

##### 3의 배수이면 Fizz, 5의 배수이면 Buzz, 15의 배수이면 Fizz Buzz, 아니면 주어진 값을 str로 전환하여 출력하시오 ( 이미 풀어본 문제 )

```python
def checkio(number: int) -> str:
    if number % 5 == 0:
        if number % 3 == 0:
            return "Fizz Buzz"
        else:
            return "Buzz"
    elif number % 3 == 0:
        return "Fizz"
    else:
        return str(number)
```



## 3. The Most Numbers

##### 주어진 다수의 수 중에서 가장 큰수와 가장 작은 수의 차이를 출력하세요. ( 단, 수가 주어지지 않을 경우에는 0을 출력합니다. )

```python
def checkio(*args):
    if len(args) == False:
        return 0
    else:
        maxn = args[0]
        minn = args[0]
        for num in args:
            if num >= maxn:
                maxn = num
            elif num <= minn:
                minn = num
        return maxn - minn
```

