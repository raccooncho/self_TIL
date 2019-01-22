## 1. Common Denominators

##### Set 안의 Set 혹은 list안의 list 혹은 list안의 tuple이 주어진다. 

```python
def convertFracts(lst):
    gcd = lambda a, b: a if not b else gcd(b, a%b)
    lcm = lambda a, b: a * b / gcd(a, b) if a > b else a * b / gcd(b, a)
    if type(lst) == list:
        D = lst[0][1]
        for i in range(len(lst)-1):
            D = lcm(D, lst[i+1][1])
        if type(lst[0]) == list:
            for i in range(len(lst)):
                lst[i][0] = round(D / (lst[i][1] / lst[i][0]))
                lst[i][1] = round(D)
        else:
            for i in range(len(lst)):
                lst[i] = list(lst[i])
                lst[i][0] = round(D / (lst[i][1] / lst[i][0]))
                lst[i][1] = round(D)
                lst[i] = tuple(lst[i])
    else:
        lst = list(lst)
        for i in range(lst):
            lst[i] = list(lst[i])
        D = lst[0][1]
        for i in range(len(lst)-1):
            D = lcm(D, lst[i+1][1])
        for i in range(len(lst)):
            lst[i][0] = round(D / (lst[i][1] / lst[i][0]))
            lst[i][1] = round(D)
            lst[i] = set(lst[i])
        lst = set(lst)
    return lst
```



## 2. Double Cola

##### 맨 앞사람이 콜라를 마시고 뒤로간다. 대신 두배로 마신다! n번째 콜라를 마시는 사람은?

```python
def whoIsNext(names, r):
    n = len(names)
    count = 0
    while r >= n:
        r -= n
        n *= 2
        count += 1
    for i in range(len(names)):
        if (i + 1)*2**count < r:
            continue
        else:
            return names[i]
```



## 3. Pyramid Slide Down

##### 피라미드를 내려오면서 지나온 수들의 합 중 가장 큰 수는?

```python

```



