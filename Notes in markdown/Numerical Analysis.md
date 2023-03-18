# 目录

1. [引论](#1-引论)
2. [解方程](#2-解方程)



# 1. 引论

## 1.1 数值计算的误差

数值计算总是会存在误差的。这样的误差主要来源有两个：**固有误差**（来自模型、观测）、**计算误差**（来自截断，舍入）
因此，我们需要定量分析误差：

绝对误差
: 即数值解和真实解的距离的上界\[e^* = |x-x^*|\]

相对误差
: 我们对**相对误差**$e^*_r$有如下定义：\[e^*_r = \left|\frac{x-x^*}{x^*}\right|\]

有效数字
: 若$x^*$是某一位的半个单位，该位到$x^*$的第一个非零数字共有$n$个，则称$x^*$具有$n$个**有效数字**

* 例子：3.15作为$\pi$的估计具有2位有效数字，因为：\[0.5\times 10^{-2}<|3.15-\pi|<0.5\times 10^{-1}\]故3.15的有效位从$10^{-1}$开始算起

**Theorem**
有近似$x^* = 10^m\sum_{k=1}^n a_n\times 10^{-(n-1)}$,则：
1. 若$x^*$有$n$个有效数字，则\[e^*_r \leq \frac{1}{2a_1}\times 10^{-(n-1)}\]
2. 反之，若\[e^*_r \leq \frac{1}{2(a_1+1)}\times 10^{-(n-1)}\]则$x^*$至少有$n$个有效数字。

### 误差的四则运算

设$x_i^*$为$x_i$的误差，则：
1. 令$x_3 = x_1 \plusmn x_2$, 则$|x_3 - x_3^*| \leq |x_1-x_1^*| + |x_2-x_2^*|$
2. 令$x_3 = x_1 x_2$, 则$|x_3 - x_3^*| \leq |x_2^*||x_1-x_1^*| + |x_1^*||x_2-x_2^*|$
3. 令$x_3 = \frac{x_1}{x_2}$, 则\[|x_3 - x_3^*| \leq \frac{|x_2^*||x_1-x_1^*| + |x_1^*||x_2-x_2^*|}{|x_2||x_2^*|}\]

### 注意事项

1. 避免大数与小数直接相加
2. 避免大数除小数
3. 避免相近数相减（如$\sqrt{n+1} - \sqrt{n}$）
4. 减少运算次数

## 1.2 算法的评价指标

* **精确性**
* **可靠性**：误差是否可以由理论或数学证明。
* **复杂度**：一般来说分时间复杂度（计算次数）与空间复杂度（内存）。
* **稳定性**：若输入数据的微小变化会导致输出剧烈变化，那么这样的算法是不稳定的。

# 2. 解方程

## 2.1 二分法

“二分法”，顾名思义，是一个迭代的过程。通过测度不断缩小的开区间套逼近待求解。因此，该方法的关键是一个在每一次迭代确定新区间的方法。注意到：
> For an continuous function f on subset $E$ of $\mathbb{R}$, if there exists $a,b \in E$ with 
> \[f(a)f(b) < 0\] then there exists an $x$ with $f(x) = 0$.

因此，我们每次只需要在已有区间取中点即可。在区间长度达到终止条件后，解即为终止时所得区间的终点。

同时，对于一个定义在$[a,b]$的连续函数，我们的求解误差为：
\[\lVert x_c - r\rVert < \frac{b-a}{2^{n+1}}\] 其中$x_c$为事实解，$r$为数值解，$n$为迭代次数。

## 2.2 不动点迭代

望文生义，不动点即为满足$g(x)=x$的实数$x$。一般而言，我们采用不动点迭代来寻找不动点：
\[x_{n+1} = f(x_n)\]但这样的迭代并不总是收敛。
可以绘制**cobweb图**来直观地说明这一点。因此我们需要找到确保不动点迭代可行的前提。

### 2.1.1 敛散性

注意到：
> ***压缩映像原理***
> 设$f$在$E \subset \mathbb{R}$上可微，且数列$\{x_n\}_{n=1}^\infty$由$x_{n+1} = f(x_n)$定义，若
> \[\sup |f'(x)| \leq r < 1\]则数列收敛。

# 3. 插值法

## 3.1 为什么需要插值法

> For a continuous function f defined on a section $[a,b]$, we have $n+1$ points satisfying 
> \[a=x_0<x_1 < \ldots < x_n = b\] and $y_i = f(x_i)$ for each $i$. Then we need a function $g$ which is close to $f$ and is easy to manipulate.

一般地来说，我们要求$g$至少满足$(f-g)(x_i) = 0$

## 3.2 多项式插值

我们在此记$F[x]_n$为以$x$为文字的，次数小于n的多项式全体。（或以$P_n$表示$<1,x,x^2,\ldots, x^n>$）

我们首先有以下定理：
> ***Theorem 3.2.1***
> 对于给定的$n+1$个不同的点$x_i,\quad i=0,1,\ldots,n$和$y_i = f(x_i)$， 其插值多项式存在且唯一。

在说明多项式插值的存在性后，我们就可以着手考虑这样的多项式的具体形式了。于是我们接下来会介绍一个简洁的插值多项式。

### 3.2.1 拉格朗日插值函数

其思想是通过**基函数**来构造整个$n$阶插值函数。首先考虑其形式：
> 假定已知$n$个点：$y_i = f(x_i)$, $i=0,1,\ldots,n$, 那么
> $$
> \begin{align*}
>    & L_nf(x) = \sum_{i=1}^n \frac{y_i\,F(x)}{(x-x_i)F'(x_i)}\\
>    & F(x) = \prod_{i=1}^n (x-x_i)
> \end{align*}
> $$

接下来，我们将阐述写出这样的式子的想法：
我们希望这样的式子会有如下形式：
\[L_nf(x) = \sum_{i=1}^n y_il_i\]其中$l_i$是一个关于$x$的函数，满足
\[ l_i(x_j) = 
    \left\{
    \begin{align*}
    1,\quad & i=j \\
    0,\quad & i \not = j
    \end{align*}
    \right.
    \]
在这里，为了易于操控，我们将$l_i$设定为$n$次多项式。将任一$x_i$带入，可以发现$n+1$个零点，从而确定$l_i$的形式。再乘上某个常数，就可以满足$l_i$的定义。而接下来的步骤便是显然的。

> 注：这样的$l_i$显然是与$f$无关的，同理，$L_nf(x)$也与$f$自身的性质无关，只与$f$的采样点有关。

#### 误差分析

> ***Theorem 3.2.2***
> 设$f$在$[a,b]$上$n+1$阶连续可导，那么
> \[ f(x) - L_nf(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}F(x),\quad\xi\in(a,b)\]其中$F(x)$定义见*Lagrange插值多项式*定义。
>

> ***Corollary***
> 令$M_{n+1} := \max_{a\leq x\leq b} \left| f^{(n+1)}(x)\right|$， 则
> \[ \left|f(x) - L_nf(x)\right| \leq \frac{M_{n+1}}{(n+1)!}\left|F(x)\right|\]
> 令$h := \max_{1\leq j\leq n}\left|x_j-x_{j-1}\right|$, 则
> \[ \left|f(x) - L_nf(x)\right| \leq \frac{h^{n+1}}{4(n+1)}M_{n+1}\]
>

我们还发现一个基函数的重要性质：

多项式再生性
: \[\forall p(x) \in P_n,\quad\sum_{i=0}^n p(x_i)l_i(x) \equiv p(x)\]

### 3.2.2 牛顿插值法

这是一个动态的过程，核心思想是：**在添加新项时，保证原有项不发生变化**。
以下，我们将列出这样的一个过程：

> 假定已知$n$个点：$y_i = f(x_i)$, $i=0,1,\ldots,n$, 记$f_i(x)= \prod_{k=0}^i (x-x_k)$那么
> $$
\begin{align*}
    p_0(x) & = y_0\\
    p_1(x) & = p_0(x) + u_1f_0(x)\\
    p_2(x) & = p_1(x) + u_2f_1(x)\\
    & \ldots\\
    p_n(x) & = p_{n-1}(x) + u_nf_{n-1}(x)
\end{align*}
> $$
> 其中每个$u_i$都是保证$f(x_i) = p(x_i)$的一个待解常数。

然而，待解常数的求解是一个比较麻烦的过程，所以接下来我们将会探讨这个问题。

#### 均差

均差
: 我们记$f$在$x_0,x_k$处的一阶均差为$$f[x_0,x_k]:=\frac{y_k-y_0}{x_k-x_0}$$继而可以定义$f$在$x_{k_0},x_{k_1},\ldots,x_{k_n}$的$n$阶均差$$f[x_{k_0},x_{k_1},\ldots,x_{k_n}] := \frac{f[x_{k_0},\ldots,x_{k_{n-2}},x_{k_n}]-f[x_{k_0},x_{k_1},\ldots,x_{k_{n-1}}]}{x_{k_n}-x_{k_{n-1}}}$$

而我们有以下推断：

> ***Theorem 3.2.3***
> $$u_k = f[x_0,x_1,\ldots,x_k],\quad k=1,2,\ldots,n$$
> 即k阶多项式的系数为$f$的$k$阶均差。

因此，需要了解一些均差的性质：
* $$f[x_0,x_1,\ldots,x_k] =\sum_{j=0}^k \frac{f(x_j)}{\prod_{i\not ={j}}(x_j-x_i)}$$
* 对称性：均差的值与括号内点的顺序无关。
* $$R_n(x)=f[x,x_0,\ldots,x_n]\,F(x)$$
* $$f[x_0,x_1,\ldots,x_k] = \frac{f^{(k)}(\xi)}{k!},\quad \xi\in (x_0,x_k)$$

### 3.2.3 Hermite插值

一言以蔽之，插值导数的插值。

重节点均差
: $$f[x_0,x_0] \colonequals \lim_{x_1\rightarrow x_0} f[x_1,x_0]$$
类似地，$$f[x_0,x_0,x_0]\colonequals\lim_{(x_1,x_2)\rightarrow(0,0)}f[x_0,x_1,x_2]$$

显然由均差性质可得，$f[x_0,x_0,\ldots,x_0] = \frac{f^{(k)}(x_0)}{k!}$

从而，我们得以定义Hermitee插值。
> 假设已知点$x_0,x_1,\ldots,x_n$，并分别给出了其中$x_{k_1},x_{k_2},\ldots,x_{k_m}$的$s_1,s_2,\ldots,s_m$阶导数，那么：
> 我们称关于$x_1,x_2,\ldots,x_n$的牛顿插值为*Hermitee插值*，其中$x_{k_i}$重复了$s_i$次

举例说明：已知$f(x_0),f(x_1),f(x_2),f'(x_1)$，那么该式的Hermitee插值即为关于$x_0,x_1,x_1,x_2$的牛顿插值。

### 3.2.4 分段低次插值

龙格现象
: 插值多项式的次数越高，误差未必越好
例子：设$f(x)=\frac{1}{1+x^2}$, $x_i:-5,-4,\ldots,4,5$, 那么其Lagrange插值$L_{10}f(x)$在边缘会出现无法忍受的误差。

正因这种情况，我们提出了新的插值方法。这个方法来自于一个非常简单的想法：为什么我们不将已知点用直线连起来呢？
把这种想法变成严谨的表述，就变成了：
> 插值函数$I_h(x)\quad(h = \max\left|x_k-x_{k+1}\right| )$满足
> \[I(x_k)=y_k\\ I_h(x) \text{ is linear on } [x_k, x_{k+1}] \]
> 
但我们不想止步于此。进一步地，不妨认为$I_h(x)$在区间$[x_k,x_{k+1}]$是一个非线性函数，例如二次、三次函数，或三角、指数函数。同样地，我们可以在每个小分段上进行*Newton*,*Lagrange*,*Hermitee*插值。这样的插值至少保证了其插值函数的连续性。

### 3.2.5 三次样条插值

三次样条函数
: 若$S(x)\in \mathcal{C}^2[a,b]$在每个$[a,b]$都是三次多项式，那么就称$S(x)$是一个三次样条函数。
若同时满足$S(x_k) = f(x_k)$，那么称$S(x)$为三次样条插值函数。

#### 自由度分析

每一个三次函数有四个系数，那么对于$n+1$个点，便具有$n$个区间，即有$4n$个未知系数。
而我们已知的限制有：
* $n+1$个已知点
* $n-1$个中间点的连续性、一阶导连续性和二阶导连续性（$3n-3$个已知限制）
* 边界条件，根据实际情况的不同，常见的有：
  * $S'(x_0) = f'(x_0)$, $S'(x_n) = f'(x_n)$（第一种边界条件）
  * $S''(x_0) = f''(x_0)$, $S''(x_n) = f''(x_n)$（第二种边界条件）
  * $S(x_0^+) = S(x_n^-)$，$S'(x_0^+) = S'(x_n^-)$，$S''(x_0^+) = S''(x_n^-)$

#### 构造

* 第一类边界条件：
  > 假设$S''(x_j)=M_j$，其中$M_j$未知。
  > 因为$S''(x)$在$[x_k,x_{k+1}]$上是一次的，故可以轻易求出$S''(x)$的表达式
  > $$S''(x) = M_j\frac{x-x_{j+1}}{x_j-x_{j+1}}+M_{j+1}\frac{x-x_{j}}{x_{j+1}-x_j}$$ 利用两次不定积分，结合区间的边界条件，可以确定两次积分中产生的两个常数项。接下来，考虑利用一阶导连续可得一个非齐次线性方程式。这样，插值函数便得解了。
* 第二类边界条件：
  > 根据定义对线性方程组中变量取特殊值即可。

上面所说的线性方程组为：
记
$$
A = \left(\begin{array}{ccccccc}
      2 & \lambda_0 & 0 & \ldots & 0 & 0 & 0\\
      \mu_1 & 2 & \lambda_1 & \ldots & 0 & 0 & 0\\
      \vdots & \vdots & \vdots & & \vdots & \vdots & \vdots\\
      0 & 0 & 0 & \ldots & \mu_{n-1} & 2 & \lambda_{n-1} \\
      0 & 0 & 0 & \ldots & 0 & \mu_n & 2 \\
    \end{array}\right) \\
    M = (M_0,M_1,\ldots,M_n)^T, D=(d_0,d_1,\ldots,d_n)^T
$$
其中
$$
\begin{align*}
  h_i = & \,x_{i+1} - x_i\\
  \mu_i = & \,\displaystyle\frac{h_{i-1}}{h_{i-1}+h_i},\quad \lambda_i = \displaystyle\frac{h_{i}}{h_{i-1}+h_i}\\
  d_i =& \,6f[x_{i-1},x_i,x_{i+1}]
\end{align*}
$$

注：$\lambda_0$与$\mu_n$的具体取值取决于初值条件。

#### 误差分析

> ***Theorem 3.2.4***
> 设$f\in\mathcal{C}^4[a,b]$，$S(x)$为满足第一类或第二类边界条件的三次样条插值函数。令$h\colonequals \max\left|x_k-x_{k+1}\right| $，则：
> $$\left|f^{(k)}(x)-S^{(k)}(x)\right| \leq C_k\max \left|f^{(4)}(x)\right|\, h^{4-k},\quad k=0,1,2$$ 其中$C_0=\frac{5}{384},\: C_1=\frac{1}{24},\: C_2=\frac{3}{8}$


# 3. 函数逼近

我们的主要目的，就是找一个简单的，已于计算的$p(x)$和一个metric，使得在该metric下，$f(x)$与$p(x)$的距离最小。

## 3.1 线性空间

### 3.1.1 赋范线性空间

设$V$为一个定义在$F$上的线性空间，若存在函数$f: V \rightarrow \mathbb{R}$，满足：
1. 正定性
2. $f(ax)=f(a)f(x)$
3. 三角不等式
4. $f^{-1}(0)={0}$
则记$f(a)$为$\lVert a \rVert$，称其为定义在$V$上的**范数**，并称定义了范数的$V$为**赋范空间**

从而可以在$\mathbb{R}^n$上定义一个平凡的范数：
> for all $x = (x_1,x_2,\ldots,x_n)$, the $\text{norm}^n$ of $x$ is $$\lVert x\rVert = (\sum_{i=1}^n \left|x\right|^n)^{1/n}$$
> for all integrable $f$, the $\text{norm}^n$ of $f$ is $$\lVert f\rVert _n = (\int \left|f\right|^n)^{1/n}$$

进而有加权范以及无穷范：
> 设$w(x) > 0$则 $$\lVert f\rVert _{w.n} = (\int \left|f\right|^n w)^{1/n}$$ 且 $$
>  \lVert x\rVert _{\infin} = \max \left|x_i\right| \\
>  \lVert f\rVert _{\infin} = \max \left|f\right|
>$$

注：可以定义加权内积，即在度量矩阵中，对原有定义加权。例如，设$\varepsilon_1,\varepsilon_2,\ldots,\varepsilon_n$为$\mathbb{R}^n$的一组基，那么可以将原有的$(\varepsilon_i,\varepsilon_j)=a$变为$(\varepsilon_i,\varepsilon_j)=aw_{ij}$；设$\varepsilon_1,\varepsilon_2,\ldots,\varepsilon_n$为$\mathbb{R}^{\mathbb{R}^n}$的一组基，那么可以将原有的$(\varepsilon_i,\varepsilon_j)=\int\varepsilon_i\varepsilon_j $变为$(\varepsilon_i,\varepsilon_j)=\int\varepsilon_i\varepsilon_jw$

### 3.1.2 最佳逼近

最佳逼近
: 设$f\in \mathcal{C}[a,b]$，$H_n$是由实值函数张成的维度为$n$的赋范空间。若有$p^*\in H_n$使\[\lVert f-p^*\rVert=\min_{p\in H_n} \lVert f-p\rVert\]则称$p^*$是$f$在赋范空间$H_n$上的**最佳逼近**
特别地，若范数为$\lVert x\rVert_{\infin}$，则称其为**最佳一致逼近**；若范数为$\lVert x\rVert_2$，则称其为**最佳平方逼近**；若范数为$\lVert x\rVert_w$，则称其为**最佳加权逼近**

于是
> **Theorem 3.1.1(Weierstrass)**
> Suppose f is continuous on $[a,b]$. Then for any $\varepsilon > 0$, there exists a polonomial $p(x)\in P_\infin$,such that\[\lVert f-p\rVert_\infin < \varepsilon\]

最小二乘拟合
: 设$f\in\mathcal{C}[a,b]$, $y_i=f(x_i),\, i\in[0,m]$，那么$p^*\in H_n$是$f$的最小二乘拟合当且仅当：
$$ \lVert f-p^*\rVert_{w.2} = \min_{p\in H_n}\lVert f-p\rVert_{w.2}$$
在此，我们将范数定义为
$$ \lVert f-p\rVert_{w.2} = \sqrt{\sum_{i=0}^m (f(x_i)-p(x_i))^2w(x_i)}$$

## 3.2 正交多项式

显然地，多项式空间是由$1,x,x^2,\ldots$张成的。根据施密特正交化，可以得到一个多项式空间的正交基。也就是说：正交多项式由内积决定（原因参考施密特正交化的步骤）。

正交族
: 设函数$\varphi_1,v\varphi_2,\ldots,\varphi_n$为内积空间$V$的一组基，若$(\phi_i,\phi_j) = \delta_{ij}$，那么称其为一个正交族；
若内积$(*,*)$（$<*,*>$）还使用了权重定义，那么称其为加权正交族。