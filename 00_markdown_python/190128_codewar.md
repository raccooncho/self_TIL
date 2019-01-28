## 1. snail

##### 달팽이가 n*n의 리스트를 바깥부터 돈다. 도는 경로를 return하시오

```python
def road(lists, num):
    answer = []
    if len(lists) == 0:
        return []
    for i in range(num):
        answer += lists[i][i:-i-1]
        for j in range(i, len(lists)-i):
            answer.append(lists[j][-i-1])
        for j in range(i+1, len(lists)-i):
            answer.append(lists[-i-1][-j-1])
        if 2 *i < len(lists) - 2:
            for j in range(i+1, len(lists)-i-1):
                answer.append(lists[-j-1][i])
    return answer
def snail(array):
    answer = []
    if len(array) == 0:
        return []
    elif len(array) == 1:
        return array[0]
    num = len(array) // 2 
    if len(array) % 2:
        a = road(array, num)
        answer += a
        answer.append(array[num][num])
    else:
        a = road(array, num)
        answer += a
    return answer
```



## 2. Next bigger number with the same digits

##### 같은 숫자의 배열을 가지는 수중에서 다음으로 큰 수를 찾으세요. 주어진 수가 가장 큰 수면 -1을 리턴합니다.

```python
def next_bigger(n):
    num = [str(i) for i in str(n)]
    num.reverse()
    for i in range(len(num)):
        if i > 0:
            num_list = []
            for j in range(i):
                num_list.append(int(num[j]))
            if max(num_list) > int(num[i]):
                num_list.append(int(num[i]))
                num[i] = str(min([x for x in num_list if int(x) > int(num[i])]))
                num_list.remove(int(num[i]))
                num_list.sort()
                num_list.reverse()
                num[:i] = [str(x) for x in num_list]
                num.reverse()
                num = ''.join(num)
                if num[0] == '0':
                    return -1
                return int(num)
    return -1
```



