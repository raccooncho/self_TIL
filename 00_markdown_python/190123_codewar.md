## 1. Pyramid Slide Down

##### 피라미드를 내려오면서 지나온 수들의 합 중 가장 큰수를 찾으시오

```python
def longest_slide_down(pyramid):
    for i in range(len(pyramid)):
        if i > 1:
            for j in range(1, i):
                pyramid[i][j] += max(pyramid[i-1][j], pyramid[i-1][j-1])
            pyramid[i][0] += pyramid[i-1][0]
            pyramid[i][-1] += pyramid[i-1][-1]
        elif i == 1:
            pyramid[i][0] += pyramid[0][0]
            pyramid[i][-1] += pyramid[0][-1]
    return max(pyramid[-1])
```



## 2. Rot13

##### 알파벳 순서에서 13번 다음순서에 있는 알파벳으로 변환하시오

```python
import string
from codecs import encode as _dont_use_this_

def rot13(message):
    alpa = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    alpac = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    message = [x for x in message]
    for i in range(len(message)):
        if message[i].isalpha():
            if message[i].isupper(): 
                message[i] = alpac[alpac.index(message[i])+13]
            else:
                b = message[i]
                a = alpa.index(message[i]) + 13
                message[i] = alpa[a]
    message = ''.join(message)
    return message
```



## 3. Memorized Fibonacci

##### 피보나치 수열을 푸세요 (타임아웃 극혐..)

```python
fib = [0, 1]
def fibonacci(n):
    if n < 2:
        return n
    if len(fib) > n:
        return fib[n]
    fib.insert(n, fibonacci(n-1) + fibonacci(n-2))
    return fib[n]
```



## 4. Next smaller number with the same digits

##### 주어진 수의 배열을 바꿀 경우 그 다음으로 작은수를 return하시오.(주어진 수가 최소면 -1)

```python
def next_smaller(n):
    num = [str(i) for i in str(n)]
    num.reverse()
    for i in range(len(num)):
        if i > 0:
            num_list = []
            for j in range(i):
                num_list.append(int(num[j]))
            if min(num_list) < int(num[i]):
                num_list.append(int(num[i]))
                num[i] = str(max([x for x in num_list if int(x) < int(num[i])]))
                num_list.remove(int(num[i]))
                num_list.sort()
                num[:i] = [str(x) for x in num_list]
                num.reverse()
                num = ''.join(num)
                if num[0] == '0':
                    return -1
                return int(num)
    return -1
```



## 5. Calculating the function

##### 읽어지는대로 계산되게 함수를 만드세요

```python
def answer(a, b):
    if b >= 10 and b < 20:
        return a + b -10
    elif b >= 20 and b < 30:
            return a - (b-20)
    elif b >= 30 and b < 40:
        return a * (b - 30)
    elif b >= 40:
        hh = round(a / (b - 40), 1)
        if int(str(hh)[-1]) >= 5:
            if hh > 1:
                return round(a / (b - 40)) - 1
            else:
                return 0
        else:
            return round(a / (b - 40))
    else:
        return a

def zero(a=0):
    return answer(0, a)
def one(a=1):
    return answer(1, a)
def two(a=2):
    return answer(2, a)
def three(a=3):
    return answer(3, a)
def four(a=4): 
    return answer(4, a)
def five(a=5): 
    return answer(5, a)
def six(a=6): 
    return answer(6, a)
def seven(a=7): 
    return answer(7, a)
def eight(a=8): 
    return answer(8, a)
def nine(a=9): 
    return answer(9, a)
def plus(a): 
    return a + 10
def minus(a):
    return a + 20
def times(a): 
    return a + 30
def divided_by(a):
    return a + 40
```



## 6. Sudoku Solution Validator

##### 스도쿠가 맞는지 확인하세요 (0이 있으면 False임)

```python
def validSolution(board):
    row = []
    sqare = []
    for i in range(9):
        count = 0
        if len(set(board[i])) < 9:
            return False
        for j in range(9):
            if board[i][j] == 0:
                return False
            row.append(board[j][i])
            if i < 3 and count < 3:
                sqare.append(board[3*i][j])
                sqare.append(board[3*i + 1][j])
                sqare.append(board[3*i + 2][j])
                count += 1
            elif i < 3 and count >= 3:
                if len(set(sqare)) < 9:
                    return False
                count = 1
                sqare = []
                sqare.append(board[3*i][j])
                sqare.append(board[3*i + 1][j])
                sqare.append(board[3*i + 2][j])
        if len(set(row)) < 9:
            return False
        else:
            row = []
    return True
```

