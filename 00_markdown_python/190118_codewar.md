## 1.  Good vs Evil

##### Good 진영은 순서대로 [1, 2, 3, 3, 4, 10]점이고, evil진영은 순서대로 [1, 2, 2, 2, 3, 5, 10]점이다. 주어진 리스트와 각 자릿수의 점수를 곱해서 더 큰 결과를 출력하시오

```python
def goodVsEvil(good, evil):
    good_worth = [1, 2, 3, 3, 4, 10]
    evil_worth = [1, 2, 2, 2, 3, 5, 10]
    good = good.split()
    evil = evil.split()
    p_good = [good_worth[i] * int(good[i]) for i in range(6)]
    p_evil = [evil_worth[i] * int(evil[i]) for i in range(7)]
    if sum(p_good) > sum(p_evil):
        return 'Battle Result: Good triumphs over Evil'
    elif sum(p_good) == sum(p_evil):
        return 'Battle Result: No victor on this battle field'
    else:
        return 'Battle Result: Evil eradicates all trace of Good'
```



## 2. Valid Braces

##### 괄호가 잘 닫혔는지 확인하고 맞으면 True, 아니면 False를 출력하시오.

```python
def validBraces(string):
    for i in range(len(string) * 3):
        if string == '':
            return True
        else:
            if '()' in string:
                string = string.replace('()', '')
            if '[]' in string:
                string = string.replace('[]', '')
            if '{}' in string:
                string = string.replace('{}', '')  
    if string == None:
        return True
    else:
        return False
```



