* 참고자료
  * [미분표](https://ko.wikipedia.org/wiki/%EB%AF%B8%EB%B6%84%ED%91%9C)(문서)
  * [선형대수](https://youtu.be/kjBOesZCoqc)(동영상)



* History

![deep_learning_intro](/Users/hwang-eunseok/TIL/Summary/study/image/deep_learning_intro.png)



* Perceptron & Neuron

![singleneuron_update](/Users/hwang-eunseok/TIL/Summary/study/image/singleneuron_update.png)

Question) XOR을 어떻게 풀 것인가?

-> MLP(Mulitlayer Perceprtron)



* Activation Function

  * $Wx+b​$ to $\hat{y}=\delta(Wx+b)​$, discrete(step) to **continuous**(sigmoid)

  * Example)

    * Single-Class(Sigmoid Function): $\sigma{(x)} = \frac{1}{1+e^{-x}}​$

      Also, easy to be **differentiable**, Try) Calculate!

    * Multi-Class(Softmax Function): P(class i) = $\frac{e^{Z_i}}{e^{Z_1} + ... + e^{Z_n}}​$

    * These restrict the results between 0 and 1: Probabilitis

  Question) Is Softmax for n=2 values the same as the sigmoid function?



* Logistic Regression
  * Take your data
  * Pick a random model
  * Calculate the **error**
  * Minimize the **error**, and obtain a better model



* To calculate error function, we need cost function.

* 용어 정리
  * The **error function** is the difference between the values computed by model and the real values.
    * Mean Squared Error $𝑀𝑆𝐸(𝜃)=\frac{1}{𝑁}∑^𝑁_𝑖(𝑓(𝑥_𝑖|𝜃)−𝑦_𝑖)^2​$
  * The **objective function** is the function you want to maximize or minimize. When they call it "**cost function**" (again, it's the objective function) it's because they want to only minimize it.
    * The **loss function** is usually a function defined on a data point, prediction and label, and measures the penalty.
      * 0/1 loss function: $𝑙(𝑓(𝑥_𝑖|𝜃),𝑦_𝑖)=1⟺𝑓(𝑥_𝑖|𝜃)≠𝑦_𝑖​$
    * The **cost function** is a sum of loss functions over your training set plus some model complexity penalty (regularization).
      * Cross-Entropy $-\sum_{i=1}^m y_i ln(p_i) + (1 - y_i)ln(1 - p_i)​$ 
  * The **criterion** is the rule for stopping the algorithm which is using. Stop it "near" to the optimum with a particular stopping criterion.



* Cost Function

  * Cross-Entropy

    ![cross_entropy_1](/Users/hwang-eunseok/TIL/Summary/study/image/cross_entropy_1.svg)

    ![cross_entropy_1_1](/Users/hwang-eunseok/TIL/Summary/study/image/cross_entropy_1_1.svg)

    ![cross_entropy_2](/Users/hwang-eunseok/TIL/Summary/study/image/cross_entropy_2.svg)

    ![cross_entropy_3](/Users/hwang-eunseok/TIL/Summary/study/image/cross_entropy_3.svg)



@Logistic Regression

* Error Function

  * Cross-Entropy Error

    $-\frac{1}{m}\sum_{i=1}^m y_i ln(p_i) + (1 - y_i)ln(1 - p_i)​$

    * $y \in {0, 1}​$

    * $p=\hat{y}=\sigma(Wx+b)​$

      ​	$= \sigma(w_1x_1 + ... + w_nx_n + b)​$



* Algorithm

1. Start with random weights:

   $w_1, ..., w_n, b​$

2. For every point($x_1, ..., x_2​$):

   1. For i = 1 ... n
      1. Update $w_i\prime \leftarrow w_i - \alpha (\hat y - y)x_i​$
      2. Update $b\prime \leftarrow b - \alpha(\hat y - y)​$

3. Repeat until error is small



* Caculate!

$E=-\frac{1}{m}\sum_{i=1}^{m}(y_iln(\hat{y_i})+(1-y_i)ln(1-\hat{y_i}))​$

where $\hat{y_i}=\sigma(Wx^{(i)} + b)​$, $Wx^{(i)}=(w_1x^{(i)}_1 + ... + w_nx^{(i)}_n)​$

$\bigtriangledown E = (\frac{\partial}{\partial{w_1}}E, ..., \frac{\partial}{\partial{w_n}}E, \frac{\partial}{\partial{b}}E)​$

To simplify calculations

1. *think the error* that **each point produces**, *calculate the derivative* of **this error**
2. the total error is **the average of the errors** at all the points.

* $E=−yln(\hat{y})−(1−y)ln(1−\hat{y})​$
  * $\frac{\partial}{\partial{w_j}} \hat{y} =​$
  * $\frac{\partial}{\partial{w_j}}E=​$
  * $\frac{\partial}{\partial b}E =​$

* $\bigtriangledown{E} =​$

  **That is , the gradient is actually a scalar times the coordinates of the point!**



* Backpropagation(reverse of Feedback)
  * Doing a feedforward operation.
  * Comparing the output of the model with the desired output.
  * Calculating the error.
  * Running the feedforward operation backwards (backpropagation) to **spread the error to each of the weights**.
  * Use this to update the weights, and get a better model.
  * Continue this until we have a model that is good.



* Example

* $\hat y = \sigma\begin{pmatrix} W^{(2)}_{11} \\ W^{(2)}_{21} \\ W^{(2)}_{31}\end{pmatrix}\sigma\begin{pmatrix} W^{(1)}_{11} && W^{(1)}_{12} \\ W^{(1)}_{21} && W^{(1)}_{22} \\ W^{(1)}_{31} && W^{(1)}_{32}\end{pmatrix} \begin{pmatrix}x_1 \\ x_2 \\ 1\end{pmatrix}$

  In simple, $\hat y = \sigma \circ W^{(2)} \circ \sigma \circ W^{(1)}(x) $

  * Feedforward

  $h_1=W^{(1)}_{11}x_1+W^{(1)}_{21}x_2+W^{(1)}_{31}$

  $h_2=W^{(1)}_{12}x_1+W^{(1)}_{22}x_2+W^{(1)}_{32}$

  $h=W^{(2)}_{11}\sigma{(h_1)}+W^{(2)}_{21}\sigma{(h_2)}+W^{(2)}_{31}​$

  $\hat y =\sigma (h)$

  $\hat y = \sigma \circ W^{(2)} \circ \sigma \circ W^{(1)}(x) $

  * Backpropagation

  $E(W)=-\frac{1}{m}\sum^m_{i=1}y_i ln(\hat{y_i})+(1-y_i)ln(1-\hat y_i)​$

  $E(W) = E(W^{(1)}_{11}, W^{(1)}_{12}, ..., W^{(2)}_{31})$

  $\bigtriangledown E = (\frac{\partial E}{\partial W^{(1)}_{11}}, ..., \frac{\partial E}{\partial W^{(2)}_{31}})$ 

  $\bigtriangledown E = \begin{pmatrix} \frac{\partial E}{\partial W^{(1)}_{11}} && \frac{\partial E}{\partial W^{(1)}_{12}} && \frac{\partial E}{\partial W^{(2)}_{11}} \\ \frac{\partial E}{\partial W^{(1)}_{21}} && \frac{\partial E}{\partial W^{(1)}_{22}} && \frac{\partial E}{\partial W^{(2)}_{21}} \\ \frac{\partial E}{\partial W^{(1)}_{31}} && \frac{\partial E}{\partial W^{(1)}_{32}} && \frac{\partial E}{\partial W^{(2)}_{31}} \end{pmatrix}​$

  $\frac{\partial E}{\partial W^{(1)}_{11}}=\frac{\partial E}{\partial \hat y}\frac{\partial \hat y}{\partial h}\frac{\partial h}{\partial h_1}\frac{\partial h_1}{\partial W^{(1)}_{11}}$

  Because, $h=W^{(2)}_{11}\sigma{(h_1)}+W^{(2)}_{21}\sigma{(h_2)}+W^{(2)}_{31}​$, we can calculate $\frac{\partial h}{\partial h_1} = W^{(2)}_{11} \sigma(h_1)[1-\sigma(h_1)]​$.

  * At last, $W^{\prime (k)}_{ij} {\leftarrow} W^{(k)}_{ij} - \alpha \frac{\partial E}{\partial W^{(k)}_{ij}}​$ ($\alpha​$ = learning rate​)



* Code!

  * About Error

    ```python
    # use np.exp(), np.log()
    
    def sigmoid(x):
        return 1 / (np.exp(-x) + 1)
    def sigmoid_prime(x):
        return sigmoid(x) * (1 - sigmoid(x))
    def error_formula(y, output):
        return y * np.log(output) + (1 - y) * np.log(1 - output)
    def error_term_formula(x, y, output):
        return (y - output) * sigmoid_prime(x)
    ```

  * Overall

    ```python
    for e in range(epochs):
            del_w = np.zeros(weights.shape)
            # Loop through all records, x is the input, y is the target
            for x, y in zip(features.values, targets):
                # Activation of the output unit
                #   Notice we multiply the inputs and the weights here 
                #   rather than storing h as a separate variable
                # use np.dot()
                output = sigmoid(np.dot(x, weights))
    
                # The error, the target minus the network output
                error = error_formula(y, output)
    
                # The error term
                error_term = error_term_formula(x, y, output)
    
                # The gradient descent step, the error times the gradient times the inputs
                del_w += error_term * x
    
            # Update the weights here. The learning rate times the 
            # change in weights, divided by the number of records to average
            weights += learnrate * del_w / n_records
    ```

* 용어정리
  * Size of Steps took in any direction = Learning rate
  * Gadget tells you height = Cost function
  * The direction of your steps = Gradients