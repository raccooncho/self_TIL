## 1. Pick peaks

##### 다음 수의 lists들 중에서 peak를 찍는 value의 인덱스와 value값을 딕셔너리 형태로 출력하세요. 단 평평한 고원의 경우에는 첫번째 value의 index와 value만 출력한다.

```python
def pick_peaks(arr):
    pos = []
    peaks = []
    answer = {}
    for i in range(len(arr)):
        if i >= 1 and (arr[i-1]-arr[i]) < 0:
            if i < len(arr) - 1 and (arr[i]-arr[i+1]) > 0:
                pos.append(i)
                peaks.append(arr[i])
            elif i < len(arr) - 2:
                if (arr[i]-arr[i+1]) == 0 :
                    k = i
                    while arr[k] == arr[k+1]:
                        if k < len(arr) - 2:
                            k += 1
                        else:
                            break
                    if arr[k]-arr[k+1] > 0:
                        pos.append(i)
                        peaks.append(arr[i])
    answer["pos"] = pos
    answer["peaks"] = peaks
    return answer
```



## 2. Bit Counting

##### 주어진 수를 2진법으로 전환한 후 2진법 에서 1의 수를 세시오

```python
def countBits(n):
    n = bin(n)
    n = str(n).count('1')
    return n
```



## 3. Did I Finish my Sudoku?

##### 스도쿠가 맞았는지 확인하고, 스도쿠가 맞으면 Finished!를 틀리면 Try again!을 return 하시오

```python
def done_or_not(board): #board[i][j]
    for i in range(9):
        if len(set(board[i])) != 9:
            return 'Try again!'

        if len(set([board[x][i] for x in range(9)])) != 9:
            return 'Try again!'
    for i in range(3):
        square = [board[3*i], board[3*i + 1], board[3*i + 2]]
        for j in range(3):
            K = [3*j, 3*j+1, 3*j+2]
            haha =[square[l][k] for l in range(3) for k in K]
            if len(set(haha)) != len(haha):
                return 'Try again!'
    return 'Finished!'
```



## 4. Find the odd int

##### 주어진 리스트 중 홀수개 존재하는 int는 단 한개이다. 그 int를 찾아서 출력하시오

```python
def find_it(seq):
    for i in seq:
        if seq.count(i) % 2:
            return i
```



## 5. CamelCase Method

##### 주어진 str의 단어 첫 글자들을 전부 대문자로 변경한 후 공백을 제거하여 출력하시오

```python
def camel_case(string):
    string = string.title().replace(' ','')
    return string
```

