### week2

* `torch.randn()` : 정규분포 함수를 랜덤 추출

* `torch.sum()` : 행렬을 더해줌
  * torch.sum(input, dtype=None)
  * torch.sum(input, dim, keepdim=False, dtype=None)
* `torch.mm(mat1, mat2)` : 곱해줌
  * 단 행렬 곱에 맞는 규격으로 맞춰줘야 함
* `torch.tensor.shape()`
* `torch.tensor.view()`
  * torch.tensor.view(a, b) : 행렬의 모양을 (a, b)의 형태로 변경해줌



* `torch.nn.Linear()`
* `torch.nn.Sigmoid()`
* `torch.nn.Softmax()`







### week3

```python
torch.nn.Sequential
torch.nn.CrossEntropyLoss
torch.nn.LogSoftmax
torch.nn.NLLLoss

.backward()
# 일반적으로 loss.backward()로 씀

torch.optim.SGD

.step()
# 일반적으로 optimizer.step()으로 씀

# backward와 step은 많이 보실 거에요.
# 어느 함수에서 많이 쓰이는지 각 역할이 무엇인지 위주로 보시면 되요
```

