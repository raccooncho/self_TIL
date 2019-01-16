## 1.  Stressful Subject

##### 모두 대문자로 되어 있거나, 뒤에 연속한 3개의 !가 표기되어 있거나, ['help', 'asap','urgent']중 한 단어가 대소문자, 반복된 알파벳, 가운데 낀 다른 기호 등에 상관없이 존재한다면 True를, 아니면 False를 출력하시오.

```python
def is_stressful(subj):
    for s in subj:
        if s.islower():
            if subj[-1] != '!' or subj[-2] != '!' or subj[-3] != '!':
                my_list = []
                for i in range(len(subj) - 1):
                    if subj[i] != subj[i + 1]:
                        my_list.append(subj[i])
                if subj[-1] != subj[-2]:
                    my_list.append(subj[-1])
                my_list = ''.join(my_list).split('!')
                my_list = ''.join(my_list).split('.')
                my_list = ''.join(my_list).split('-')
                my_list = ''.join(my_list)
                red = ['help', 'asap', 'urgent']
                for t in red:
                    if t in my_list.lower():
                        return True
                else:
                    return False     
    return True    
```



## 2. Printer Errors

##### 프린터 색은 a 부터 m까지 있다. 가끔 오류가 발생해서 다른 알파벳이 찍히는데 오류가 발생하는 비율을 구하시오.

```python
def printer_error(s):
    colors = 'abcdefghijklm'
    count = 0
    for letter in s:
        if letter not in colors:
            count += 1
    return str(count) + '/' + str(len(s)) 
```



## 3. Breaking chocolate problem

##### n * m 사이즈의 초콜릿 바가 있다. 모두 1*1 사이즈의 초콜릿으로 쪼개기 위해 최소 몇번 쪼개야 하는가?

```python
def breakChocolate(n, m):
    if n*m:
        return n * m -1
    else:
        return 0
```



## 4. Jaden Casing Strings

##### 공백 이후 첫글자를 대문자로 전환하기.

```python
def toJadenCase(string):
    string = string.split()
    result = []
    for s in string:
        result.append(s.capitalize())
    result = ' '.join(result)
    return result
```



## 5. Duplicate Encoder

##### str에서 한번만 나타나는 문자에 대해서는 (, 여러번 나타나는 문자에 대해서는 )로 변형해서 출력하시오.

```python
def duplicate_encode(word):
    word = word.lower()
    lists = []
    list_d = []
    for s in word:
        if s not in lists:
            lists.append(s)
        else:
            list_d.append(s)
    result = []
    for s in word:
        if s in list_d:
            result.append(')')
        else:
            result.append('(')
    return ''.join(result)
```

