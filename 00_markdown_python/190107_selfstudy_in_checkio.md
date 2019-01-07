## 1.  Best stock

##### 주어진 dict에서 가장 value값이 큰 key를 출력하시오

```python
def best_stock(data):    
    max_price = 0
    answer = ''
    for s in data:
        if data[s] > max_price:
            max_price = data[s]
            answer = s
    return answer
```



## 2. Popular_words

##### 워드가 사용된 횟수를 구하시오 (dict형식으로)

```python
def popular_words(text: str, words: list) -> dict:
    # your code here
    answer = {}
    for word in words:
        count = text.lower().count(f'{word} ')
        answer[word] = count
    return answer 
```

* 문제점 1 : 대 소문자 구분안하고 모두 포함시켜야 함 ( lower을 포함시킴)
* 문제점 2:  nearly 안에 있는 near도 near로 인식함. 
  * 앞 뒤에 공백을 넣어주어서 완성도를 높이려 했으나, 맨 앞에 나와있는 문자는 앞에 공백이 없으므로 뒤에만 공백을 포함.
  * thing을 찾을때 something를 같이 인식시킬 위험이 높음
  * if문을 삽입해서 수정할 필요 있음.
* 는 역시나 check가 실패한다

```python
def popular_words(text: str, words: list) -> dict:
    answer = {}
    text = text.lower().split()
    for word in words:
        count = text.count(word)
        answer[word] = count
    return answer

```

