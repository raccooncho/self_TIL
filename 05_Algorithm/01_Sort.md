# 01_Sort



### 1. 버블 소트 (bubble sort)

```python
arr = [55, 7, 78, 12, 42]

for j in range(len(arr), 0, -1): # range == [5, 4, 3, 2, 1]
    for i in range(1, j): # range = [1, 2, 3, 4] [1, 2, 3] [1, 2] [1] []
        if arr[i - 1] > arr[i]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1] # 앞과 뒤를 비교해서 큰걸 뒤로 옮김

```

* 숫자 두개씩 비교해서 큰 수를 뒤로 (혹은 앞으로)  옮기는 식으로 정렬하는 방법
* O(n^2)의 복잡도를 가진다(for문 두번)



### 2. 카운팅 소트 (counting sort)

```python
K = 4  # 가장 큰 수 ( 수의 범위, 해당 예시에선 0부터 시작하기 때문에 4로 설정)
A = [0, 4, 1, 3, 1, 2, 4, 1] # len(A) == 8
B = [0] * len(A) # B == [0, 0, 0, 0, 0, 0, 0, 0]
cnt = [0] * (K + 1)  # 0 ~ 4까지의 범위 는 K+1( == 5)개 이므로 cnt를 해주기 위해 크기가 5인 list를 만들어준다.

for val in A: # 각 A의 숫자들에 대해서 cnt(인덱스)를 추가해준다.
    cnt[val] += 1 # [1, 3, 1, 1, 2] ==> [0은 1개, 1은 3개, 2는 1개, 3은 1개, 4는 2개]

for i in range(1, K + 1): # range = [1, 2, 3, 4]
    cnt[i] += cnt[i - 1] # 누적 카운팅을 해준다. -> 최종 결과물인 B에서의 인덱스를 위함

for i in range(len(A) - 1, -1, -1): # range == [7, 6, 5, 4, 3, 2, 1, 0]
    cnt[A[i]] -= 1  # A의 i번째에 위치한 숫자의 누적카운트를 1 빼고
    B[cnt[A[i]]] = A[i]  # 누적 카운트에 해당하는 B의 숫자를 A의 i번째 숫자로 변경한다.

```

* 먼저, 정렬을 할 리스트( 길이가 같고 모든 items가 0인 리스트 == 위의 예시에서 B)를 생성한다.
* 주어진 숫자의 범위만큼 카운팅 해주는 리스트를 만들어 준다.
* 맨 처음 리스트의 숫자들을 카운팅 리스트에서 카운트 해준다. (인덱스 값을 일치시켜주는데, 잘 계산 해야한다. 가장 작은 숫자가 0번 인덱스에 해당하도록!)
* 카운트를 누적카운트로 변경시켜 준다.
* 누적 카운트를 1씩 빼주면서 맨 처음에 만든 정렬 리스트에 추가해 준다.



### 3. 선택 정렬 (selection sort)

```python
arr = [64, 25, 10, 22, 11]

for i in range(len(arr) - 1): # range = [0, 1, 2, 3]
    minIdx = i
    for j in range(i + 1, len(arr)): # range = [1, 2, 3, 4] [2, 3, 4] [3, 4] [4]
        if arr[minIdx] > arr[j]: # 최솟값을 찾아서 최솟값에 해당하는 인덱스를 변경해준다.
            minIdx = j

    arr[i], arr[minIdx] = arr[minIdx], arr[i]  # 최솟값을 앞으로 보낸다.
```

* 전체 범위에서 최솟값의 인덱스를 찾는다. 
* 0번 과 최솟값을 교환한다.
* 전체 범위에서 1씩 뺀다(방금 들어간 0번인덱스를..)
* 끝까지 반복한다.



### 4. 퀵 소트 (quick sort)

```python
def qsort(nums):
    if len(nums) <= 1: # 길이가 1이 되면 구분이 의미가 없으므로 현재 값을 리턴하고 함수(재귀)를 종료한다.
        return nums
    pivot = nums[len(nums) // 2] # 임의의 값을 pivot(기준점)으로 잡는다. 아무 값이나 상관 없지만, 편의상 가운데 인덱스에 자리잡은 값을 기준으로 잡는다.
    less = [] # 기준점보다 작은 값을 less 리스트에 포함시킨다.
    more = [] # 기준점보다 큰 값을 more 리스트에 포함시킨다.
    equal = [] # 기준점과 동일한 값을 equal 리스트에 포함시킨다.
    for a in nums:
        if a < pivot:
            less.append(a) # 기준점보다 작은 값을 less 리스트에 포함시킨다.
        elif a > pivot:
            more.append(a) # 기준점보다 큰 값을 more 리스트에 포함시킨다.
        else:
            equal.append(a) # 기준점과 동일한 값을 equal 리스트에 포함시킨다.
    return qsort(less) + equal + qsort(more) # less와 more를 다시 quick sort 시킨다.
```

* 주어진 리스트가 1일 경우에 리턴한다.
* 기준점(pivot)을 잡는다.  (0번 인덱스, -1인덱스, 혹은 중간 인덱스 -> 편의상 중간에 위치한 인덱스로 잡는게 좋은듯...)

* 비교한 값을 포함시키기 위해 less, more, equal이라는 이름의 빈 리스트를 생성시킨다.
* 기준점보다 작은것은 less, 큰 것은 more, 같은 것은 equal리스트에 포함시킨다.
* less와 more리스트는 qsort로 재귀시킨다.



### 5. 삽입정렬 (Insert sort)

```python
def isort(A):
    lena = len(A)
    for i in range(1, len(A)):
        I = A.pop(i)
        for j in range(i):
            if I < A[j]:
                A.insert(j, I)
                break
        if len(A) != lena:
            A.insert(i, I)
    return A
```

* 주어진 리스트의 크기가 적당히 작을 경우 효율적이다.
* 사실 퀵소트의 가짓수를 줄이기 위해서 작은 범위의 리스트에 대해선 삽입정렬을 하는 것이 효율적이다.

```python
def qsort(nums):
    if len(nums) <= 5: 
        return isort(nums)
    pivot = nums[len(nums) // 2] 
    less = []
    more = []
    equal = []
    for a in nums:
        if a < pivot:
            less.append(a)
        elif a > pivot:
            more.append(a)
        else:
            equal.append(a) 
    return qsort(less) + equal + qsort(more) 
```



### 6. 병합정렬 (Merge sort)

```python
def merge_sort(A):
    if len(A) <= 1:  # 길이가 1이 되면 리턴한다.
        return A
    M = len(A) >> 1    # 위치상 중간을 기준으로
    L = merge_sort(A[M:])   # 반으로 쪼개서 왼쪽 오른쪽을 각각 다시 머지 소트 한다.
    R = merge_sort(A[:M])
    return merge(L, R)  # 각각 머지소트한 왼쪽 오른쪽 리스트를 머지로 합병한다.

def merge(l, r):
    result = []
    while len(l) > 0 and len(r) > 0:  # 둘중 하나의 리스트가 다 빌때까지
        if l[0] <= r[0]:  # 0번 인덱스가 작은 것을 result에 append시킨다.
            result.append(l.pop(0))
        else:
            result.append(r.pop(0))
    if len(l) > 0:   # 남은 리스트를 result 에 합병시킨다.
        result += l
    else:
        result += r
    return result
```

* 가운데 인덱스를 중심으로 계속 반으로 나눈 뒤
* 크기순으로 정렬해가며 정렬하는 방법이다.
* n log n의 속도를 보장하지만 파이썬에서는 잦은 슬라이싱 때문에 효율이 좋지 못할 수 있다.