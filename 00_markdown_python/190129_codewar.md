## 1. String Mix

##### 주어진 두개의 스트링들의 소문자들 중에서 많이 있는 것을 표기하고 정렬하세요.(많은순, 1>2>=, 알파벳순)

```python
def mix(s1, s2):
    s1_list = {}
    for s in s1:
        s1_list[s] = s1.count(s)
    s2_list = {}
    for s in s2:
        s2_list[s] = s2.count(s)
    answer = []
    for key1, value1 in s1_list.items():
        for key2, value2 in s2_list.items():
            if key1 == key2 and key1.isalpha() and key1.islower():
                if value1 > value2 and value1 > 1:
                    a = '1:' + key1 * value1
                    answer.append(a)
                elif value2 > value1 and value2 > 1:
                    a = '2:' + key2 * value2
                    answer.append(a)
                elif value1 == value2 and value1 > 1:
                    a = '=:' + key1 * value1
                    answer.append(a)
            elif key1 not in s2_list.keys() and value1 > 1 and key1.isalpha() and key1.islower():
                a = '1:' + key1 * value1
                if a not in answer:
                    answer.append(a)
            elif key2 not in s1_list.keys() and value2 > 1 and key2.isalpha() and key2.islower():
                a = '2:' + key2 * value2
                if a not in answer:
                    answer.append(a)
    answer = sorted(answer, key=None, reverse=True)
    answer = sorted(answer, key=len)
    answer.reverse()
    answer = '/'.join(answer)
    return answer
```



## 2. One Line Task: Squirrel And Tree

##### 한줄코딩 하세요..

```python
squirrel=lambda h,H,S:round((1+(S/h)**2)**0.5*H,4)
```





