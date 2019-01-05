## 1. 문자에서 두번째 index찾기

#### ( 두번째 index가 없으면 None 출력하기)

```python
def second_index(text: str, symbol: str) -> [int, None]:
    result =[]
    for index, symbols in enumerate(text):  
        # for 문 안에 result =[]를 넣었더니 리스트가 자꾸 초기화 되었다. 빈 리스트는 for문 밖에 빼놓자.
        if symbols == symbol:
            result.append(index)
    if len(result) >= 2:
        return result[1]
    else:
        return None
```



## 2. str에서 주어진 두개의 str사이에 있는 문자만 출력하기

* begin 만 있으면 begin 뒤가 전부 출력
* end 만 있으면 end 앞이 전부 출력
* begin과 end 둘다 없으면 전체 문장 출력
* end 가 begin보다 앞에 있으면 ' ' 출력

```python
def between_markers(text: str, begin: str, end: str) -> str:
    if begin in text and end in text and text.find(begin) >= text.find(end):
        text =''
    elif begin in text:
        indexf = text.find(begin) + len(begin)
        text = text[indexf:]
        if end in text:
            indexl = text.find(end)
            text = text[:indexl]
    elif end in text:
        indexl = text.find(end)
        text = text[:indexl]
    return text
```

