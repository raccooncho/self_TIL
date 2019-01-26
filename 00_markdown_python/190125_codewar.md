## 1. Detect Pangram

##### 주어진 str이 모든 알파벳을 포함하고 있는지 확인하는 함수를 만들어 주세요.

```python
import string

def is_pangram(s):
    answer = []
    s = s.lower()
    for a in s:
        if a not in answer and a.isalpha():
            answer.append(a)
    if len(answer) == 26:
        return True
    else:
        return False
```


