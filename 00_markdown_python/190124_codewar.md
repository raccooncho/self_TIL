## 1. Strip Comments

##### 주어진 마커 뒤에 있는 문자를 모두 제거하여 출력하시오.

```python
Python:
def solution(string,markers):
    answer = string.split('\n')
    for i in range(len(answer)):
        for mk in markers:
            if type(answer[i]) == list:
                answer[i] = answer[i][0].split(mk)
            else:
                answer[i] = answer[i].split(mk)
        if type(answer[i]) == list:
            answer[i] = answer[i][0].strip()
        else:
            answer[i] = answer[i].strip()
    answer = '\n'.join(answer)
    return answer
```


