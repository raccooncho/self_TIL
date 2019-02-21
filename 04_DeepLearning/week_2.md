## 복습

### Entropy Loss

#### Kullback-Leiber divergence

정보이론(information theory)의 엔트로피(entropy) 손실값 공식들의 기반

실제로 거리함수는 아니나, 거리(distance, 혹은 metric)의 성질 4가지 중 3가지를 만족하는 준거리공식(semi-distance)

```
함수 d(x,y)가 metric이 되기 위한 4가지 성질

d(x,y) >=0
d(x,y) = 0 iff x==y
d(x,y) = d(y,x)
d(x,z) <= d(x,y) + d(y,z)

KL은 위 4가지 성질 중 3번 성질 대칭성(symmetry)을 만족하지 못함
```

KL-divergence는 두 확률분포 사이의 거리를 측정하는 도구이며, 이산확률변수의 경우에 대한 식은 아래와 같습니다.

![D_{KL}(P, Q) = D_{KL}(P || Q) = \sum_{i} p_i log \frac{p_i}{q_i} ](http://s0.wp.com/latex.php?latex=D_%7BKL%7D%28P%2C+Q%29+%3D+D_%7BKL%7D%28P+%7C%7C+Q%29+%3D+%5Csum_%7Bi%7D+p_i+log+%5Cfrac%7Bp_i%7D%7Bq_i%7D+&bg=ffffff&fg=000&s=1)

머신러닝에선 p를 실제 정답인 라벨로, q를 예측한 확률분포로 사용합니다. 예측이 지수 정규화(softmax) 활성함수(activation function)의 결과물이라면 q가 0이 될 일은 없습니다. 안정성을 위해서는 각 라이브러리마다 제공하는 내부 함수(built-in function)를 사용하는 것이 좋습니다.

KL divergence 또한 q에 대한 볼록 함수(convex function)이기 때문에 SGD([Stochastic Gradient Descent](http://www.khshim.com/archives/455)) 알고리즘을 적용하기 좋습니다. p는 고정값이라는 것을 생각하면, KL 거리를 줄인다는 것은 다음과 같이 바꿀 수 있습니다.

![minimize (D_{KL}) = minimize ( \sum_i p_i log p_i - \sum_i p_i log q_i) = maximize (\sum_i p_i log q_i) \\ = minimize (- \sum_i p_i log q_i) ](http://s0.wp.com/latex.php?latex=minimize+%28D_%7BKL%7D%29+%3D+minimize+%28+%5Csum_i+p_i+log+p_i+-+%5Csum_i+p_i+log+q_i%29+%3D+maximize+%28%5Csum_i+p_i+log+q_i%29+%5C%5C+%3D+minimize+%28-+%5Csum_i+p_i+log+q_i%29+&bg=ffffff&fg=000&s=1)

가장 마지막 식은 교차 엔트로피(cross-entropy)라고 하며, 요즘 대부분의 손실 공식으로는 이 값을 사용합니다. 교차 엔트로피는 음수 로그 유사도(negative log-likelihood) 라고도 하며 이 경우 다른 방법으로 유도한 같은 식입니다.

y가 0 혹은 1만 되는 경우(즉, 최종 확률분포가 1차원인 경우) 위 교차 엔트로피 식은 다음과 같이 바꿀 수 있습니다.

![L = - y_t log \hat y - (1-y_t) log (1-\hat y) ](http://s0.wp.com/latex.php?latex=L+%3D+-+y_t+log+%5Chat+y+-+%281-y_t%29+log+%281-%5Chat+y%29+&bg=ffffff&fg=000&s=1)

y가 여러 class를 갖는 경우(대부분의 경우), 위 교차 엔트로피 식은 다음과 같습니다.

![L = - \sum_i y_{ti} log \hat y_i ](http://s0.wp.com/latex.php?latex=L+%3D+-+%5Csum_i+y_%7Bti%7D+log+%5Chat+y_i+&bg=ffffff&fg=000&s=1)

### Activation Function

#### ReLU

NN의 중간에 조건문이 들어가기 때문에 backprop하는 것이 좀 더 까다로워질 수는 있지만(Theano같은 그래프 구조를 사용하는 경우 큰 문제는 없습니다.) 대신 미분하는 것도 훨씬 쉽습니다.

ReLU의 문제는 음수 부분의 정보가 완전히 사라진다는 점과 값이 무한히 커질 수 있다는 점인데, 이를 해결하기 위해 ReLU의 여러 변종들이 많이 나왔습니다. 그 중 하나는 leaky ReLU입니다. 음수 부분의 기울기 알파를 주어 음수 쪽으로도 약간의 정보를 갖고 있도록 합니다. 보통 알파 = 0.01 정도를 사용합니다.

#### Sigmoid

Sigmoid는 결과값이 0부터 1 사이의 값으로 나오기 때문에 같은 크기의 다른 벡터에 element-wise 곱을 해 일종의 mask처럼 사용하기도 합니다.

#### Softmax

Softmax는 보통 activation으로 구현되어 있습니다. 이 함수는 입력 각각에 지수를 취한 뒤 전체 합 중 지수를 취한 값이 얼마나 되는지를 계산합니다. 즉, 입력 벡터를 확률분포로 만들어 줍니다.

[Futher study](http://www.khshim.com/archives/629)



## 공부

It’s a Python-based scientific computing package targeted at two sets of audiences:

- A replacement for NumPy to use the power of GPUs
- a deep learning research platform that provides maximum flexibility and speed



torch.randn(*sizes, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False) → Tensor`

Returns a tensor filled with random numbers from a normal distribution with mean 0 and variance 1 (also called the standard normal distribution).

$\text{out}_{i} \sim \mathcal{N}(0, 1)​$

- **sizes** (*int...*) – a sequence of integers defining the shape of the output tensor. Can be a variable number of arguments or a collection like a list or tuple.
- **out** ([*Tensor*](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)*,* *optional*) – the output tensor
- **dtype** ([`torch.dtype`](https://pytorch.org/docs/stable/tensor_attributes.html#torch.torch.dtype), optional) – the desired data type of returned tensor. Default: if `None`, uses a global default (see [`torch.set_default_tensor_type()`](https://pytorch.org/docs/stable/torch.html#torch.set_default_tensor_type)).
- **layout** ([`torch.layout`](https://pytorch.org/docs/stable/tensor_attributes.html#torch.torch.layout), optional) – the desired layout of returned Tensor. Default: `torch.strided`.
- **device** ([`torch.device`](https://pytorch.org/docs/stable/tensor_attributes.html#torch.torch.device), optional) – the desired device of returned tensor. Default: if `None`, uses the current device for the default tensor type (see [`torch.set_default_tensor_type()`](https://pytorch.org/docs/stable/torch.html#torch.set_default_tensor_type)). `device` will be the CPU for CPU tensor types and the current CUDA device for CUDA tensor types.
- **requires_grad** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,* *optional*) – If autograd should record operations on the returned tensor. Default: `False`.

Talk

* sizes: the shape of output tensor
* dtype: initial default for floating point is torch.float32
* layout: Strides are a list of integers: the k-th stride represents the jump in the memory necessary to go from one element to the next one in the k-th dimension of the Tensor. This concept makes it possible to perform many tensor operations efficiently.
* required_grad: autograd(automatic differentiation package)



`torch.sum()`

`torch.sum(input, dtype=None) → Tensor`

`torch.sum(input, dim, keepdim=False, dtype=None) → Tensor`

`torch.mm(mat1, mat2, out=None) → Tensor`

Performs a matrix multiplication of the matrices `mat1` and `mat2`.

If `mat1` is a $(n \times m)$ tensor, `mat2` is a $(m \times p)$ tensor, `out` will be a $(n \times p)$ tensor.

Futher study, This function does not broadcast, For broadcasting matrix products, see [`torch.matmul()`](https://pytorch.org/docs/stable/torch.html#torch.matmul).

,lm

`torch.Tensor.view(shape) → Tensor`

Returns a new tensor with the same data as the `self` tensor but of a different `shape`.

The returned tensor shares the same data and must have the same number of elements, but may have a different size. For a tensor to be viewed, the new view size must be compatible with its original size and stride, i.e., each new view dimension must either be a subspace of an original dimension, or only span across original dimensions d, d+1, \dots, d+k*d*,*d*+1,…,*d*+*k* that satisfy the following contiguity-like condition that \forall i = 0, \dots, k-1∀*i*=0,…,*k*−1,

$\text{stride}[i] = \text{stride}[i+1] \times \text{size}[i+1]$

Contigous? An instance of class [`ndarray`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.html#numpy.ndarray) consists of a contiguous one-dimensional segment of computer memory (owned by the array, or by some other object), combined with an indexing scheme that maps *N* integers into the location of an item in the block

Further study, `.reshape()`, `resize_()`



`torch.nn.Linear(in_features, out_features, bias=True)`

- **weight** – the learnable weights of the module of shape $(\text{out_features}, \text{in_features})​$. The values are initialized from $\mathcal{U}(-\sqrt{k}, \sqrt{k})​$, where $k = \frac{1}{\text{in_features}}​$
- **bias** – the learnable bias of the module of shape $(\text{out_features})(\text{out_features})$. If `bias` is `True`, the values are initialized from $\mathcal{U}(-\sqrt{k}, \sqrt{k})$ where $k = \frac{1}{\text{in_features}}$
- Kaiming Uniform (more commonly called He initialization)



### Initialization

어떻게 가중치와 편향치를 잡는게 좋은지는 아직도 밝혀지지 않았으나 symmetry를 깨는 방향으로 초기화를 해야 합니다. 같은 입력에 대해 동일하거나 대칭적인 가중치로 초기화를 하면 그 방향으로 집중될 수 밖에 없고 이는 표현할 수 있는 범위가 줄어듭니다. 제일 좋은 방법은 모든 가중치가 orthogonal하게 만드는 것입니다. 하지만, 그러지 않아도 무작위로 잘 뽑으면 높은 확률로 서로 독립적인 값을 얻을 것입니다.

훈련된 모델의 평균이 얼마나 정답에서 멀리 떨어져 있는지가 bias(편향), 모델의 값들이 모델의 평균에서 얼마나 떨어져 있는지가 variance(분산)입니다.

![1100-image-1](https://i1.wp.com/khshim.files.wordpress.com/2016/10/1100-image-1.png?resize=561%2C557&ssl=1)

즉, 우리는 bias와 variance 둘 모두를 줄이면 좋습니다. 이는 식으로도 확인할 수 있습니다. 아래 식에서 시그마는 원래 데이터에 있던 분산을 의미합니다.

![E[(y_t - \hat y)^2] = E[y_t^2 + \hat y ^2 - 2y_t \hat y] \\ = E[y_t^2] + E[\hat y ^2] - 2E[y_t \hat y] \\ = Var(y_t) + E[y_t]^2 + Var(\hat y) + E[\hat y]^2 - 2y_t E[\hat y] \\ = Var(y_t) + Var(\hat y) + E[(y_t - \hat y)^2] \\ = \sigma^2 + Var(\hat y) + Bias(\hat y)^2 \\ ](http://s0.wp.com/latex.php?latex=E%5B%28y_t+-+%5Chat+y%29%5E2%5D+%3D+E%5By_t%5E2+%2B+%5Chat+y+%5E2+-+2y_t+%5Chat+y%5D+%5C%5C+%3D+E%5By_t%5E2%5D+%2B+E%5B%5Chat+y+%5E2%5D+-+2E%5By_t+%5Chat+y%5D+%5C%5C+%3D+Var%28y_t%29+%2B+E%5By_t%5D%5E2+%2B+Var%28%5Chat+y%29+%2B+E%5B%5Chat+y%5D%5E2+-+2y_t+E%5B%5Chat+y%5D+%5C%5C+%3D+Var%28y_t%29+%2B+Var%28%5Chat+y%29+%2B+E%5B%28y_t+-+%5Chat+y%29%5E2%5D+%5C%5C+%3D+%5Csigma%5E2+%2B+Var%28%5Chat+y%29+%2B+Bias%28%5Chat+y%29%5E2+%5C%5C+&bg=ffffff&fg=000&s=1)

보통 다음과 같은 관계가 성립합니다.

![1100-image-2](https://i0.wp.com/khshim.files.wordpress.com/2016/10/1100-image-2.png?resize=503%2C265&ssl=1)

Generalization error: 훈련 데이터 외의 데이터(테스트 데이터)에서 발생하는 에러

Underfitting vs Overfitting

| Underfitting                                       | Overfitting                                                  |
| -------------------------------------------------- | ------------------------------------------------------------ |
| Kill Godzilla using a flyswatter                   | Kill a fly using a bazooka                                   |
| Not Animals vs Animals<br>Instead Not Dogs vs Dogs | Anything but Dogs that are yellow, orange or gray<br> vs <br>Dogs that are yellow, orange or gray |
| as error due to bias, high bias                    | as error due to variance, high variance                      |

|            | Var large   | Var small    |
| ---------- | ----------- | ------------ |
| Bias large | Fail        | Underfitting |
| Bias small | Overfitting | Very Good    |

딥러닝의 어마어마한 표현 공간을 모두 사용할 수 있다는 점 때문에, 적절한 훈련이 이루어지면 딥러닝은 보통 과적합이 됩니다. 이 경우 분산만 조금 끌어내리면 아주 좋은 결과를 얻을 수 있습니다. 문제는 Bias-Variance 사이에는 보통 Tradeoff(교환)이 있기 때문에, 얼마나 끌어내려야 하는지, 어느 정도까지 끌어내려야 하는지는 아직까지는 heuristic(시행착오를 통한 지식)의 영역입니다.

[Futher study](http://www.khshim.com/archives/641)