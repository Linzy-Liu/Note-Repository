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
: 设函数$\varphi_1,\varphi_2,\ldots,\varphi_n$为内积空间$V$的一组基，若$(\varphi_i,\varphi_j) = \delta_{ij}$，那么称其为一个正交族；
若内积$(*,*)$（$<*,*>$）还使用了权重定义，那么称其为加权正交族。

假设$\varphi_n$是$[a,b]$上$n$次多项式，$\rho(x)$为权函数。若$\left\{\varphi_n(x)\right\} _{n=0}^\infty$在$(*,*)_\rho$正交族中，那么称$\varphi_n$为$[a,b]$上带权$\rho(x)$的**正交多项式**。

**性质**
假设$\left\{\varphi_n(x)\right\}_{n=0}^N$是由$1,x,\ldots,x^n$经施密特正交化依次得到的一组正交多项式
1. $\left\{\varphi_n(x)\right\}_{n=0}^N$线性无关。
2. 任一不超过$N$次的多项式可由$\left\{\varphi_n(x)\right\}_{n=0}^N$线性表出。
3. $\varphi_n$与任一次数小于$n$的多项式正交。

> **Theorem 3.2.1**
> 设$\left\{\varphi_n(x)\right\}_{n=0}^\infty$是$[a,b]$上带权$\rho(x)$的首一正交多项式，那么下式成立：
> $$
\varphi_{n+1}=(x-\alpha_n)\varphi_n - \beta_n\varphi_{n-1},\quad n=0,1,\ldots\\
> $$其中
> $$
> \begin{align*}
>   \varphi_0 &= 1,&\varphi_{-1}&=0\\
>   \alpha_n &= \frac{(x\varphi_n,\varphi_n)_\rho}{(\varphi_n,\varphi_n)_\rho},&\beta_n &= \frac{(\varphi_n,\varphi_n)_\rho}{(\varphi_{n-1},\varphi_{n-1})_\rho}
> \end{align*}
> $$

> **Theorem 3.2.2**
> 设$\left\{\varphi_n(x)\right\}_{n=0}^\infty$是$[a,b]$上带权$\rho(x)$的正交多项式,则$\varphi_n$在$[a,b]$上有不同的$n$个零点。

（上述$\left\{\varphi_n(x)\right\}_{n=0}^\infty$都是由$1,x,\ldots,x^n$经施密特正交化依次得到的, 而一般实践中，可以有$T^TATx$一样的变换，但注意各个定理推导时的前提条件。）

### 3.2.1 勒让德多项式

勒让德多项式
: 我们称在$[-1,1]$上，权函数为$\rho(x)\equiv 1$的，由$1,x,x^2,\ldots$经施密特正交化得到的正交多项式为勒让德多项式。

表达式：
\[P_0(x)=1,\quad P_n(x) = \frac{n!}{(2n)!}\frac{d^n}{d\,x^n}\left((x^2-1)^n\right)\:(n=1,2,\ldots)\]

性质:
* $$\int_{-1}^1P_n(x)P_m(x) = \left\{
  \begin{align*}
    0&,& m &\not ={n}\\
    \frac{2}{2n+1}&,& m &= n
  \end{align*}
  \right.$$
* $$P_n(-x) = (-1)^nP_n(x)$$
* $$(n+1)P_{n+1}(x)=(2n+1)xP_n(x)-nP_{n-1}(x)$$

### 3.2.2 切比雪夫多项式

切比雪夫多项式
: 我们称在$[-1,1]$上，权函数为$\rho(x) = (1-x^2)^{-1/2}$的，由$1,x,x^2,\ldots$经施密特正交化得到的正交多项式为切比雪夫多项式。

表达式：
$$T_n(x)=\cos(n\arccos x), \left|x\right|\leq 1$$

性质：
* $$T_{n+1}(x) = 2xT_n(x)-T_{n-1}(x)$$
* $$\int_{-1}^1T_n(x)T_m(x)\rho(x) = \left\{
  \begin{align*}
    0&,& m &\not ={n}\\
    \frac{\pi}{2}&,& m &= n \not ={0}\\
    \pi &,& m &= n = 0
  \end{align*}
  \right.$$
* $T_{2k}$仅含偶数项，$T_{2k-1}$仅含奇数项
* $T_n(x)$在$[-1,1]$上有$n$个零点。（具体值可由通用表达式推得）
* $T_n(x)$的首项系数为$2^{n-1}$

那么我们记$\hat{T}_n(x) = 2^{1-n}T_n(x)$,可得定理如下：

> **Theorem 3.2.3**
> $$ \max_{-1\leq x\leq 1} \left|\hat{T}_n(x)\right|\leq \max_{-1\leq x\leq 1} \left|\hat{p}_n(x)\right|$$ 其中$\hat{p}_n(x)$为首一$n$次多项式
>

鉴于切比雪夫多项式良好的性质，我们考虑将其应用于插值多项式中。在$[-1,1]$上，我们称多项式$T_n(x)$的所有零点为切比雪夫点，利用这些点进行插值，可以让误差最小：
> **Corollary**
> 设已知函数$f\in\mathcal{C}^{n+1}[-1,1]$在$n$个切比雪夫点上的点值，得到了插值函数$L_n(x)$，那么：
> $$ \max_{-1\leq x\leq 1} \left|f(x)-L_n(x)\right|\leq \frac{1}{2^n(n+1)!}\lVert f^{(n+1)}(x)\rVert_\infty$$

对于一般的**闭区间**，考虑变换：（应该没有人想对着任意闭集做变换吧）
$$t = [(b-a)x+a+b]/2,\quad x\in[-1,1]$$
上面的引理的形式在此时会变成：
$$\max_{a\leq x\leq b} \left|f(x)-L_n(x)\right|\leq \frac{(b-a)^{n+1}}{2^{2n+1}}\,\frac{\lVert f^{(n+1)}(x)\rVert_\infty}{(n+1)!}$$

## 3.3 最佳平方逼近

### 3.3.1 讨论域

我们在本节，主要想解决这样的一个问题：
对于$\mathcal{C}[a,b]$上的函数$f$和函数组$\left\{\varphi_k\right\}_{k=0}^n$，是否存在一个$\left\{\varphi_k\right\}_{k=0}^n$的线性组合$S^*(x)$，使得对于任一一个线性组合$S(x)$：
\[\lVert f(x)-S^*(x)\rVert_2^2 = \min \lVert f(x)-S(x)\rVert_2^2\]
如果存在，它的具体形式如何？

### 3.3.2 最佳平方逼近

由上可知，该问题的等价形式为：
$$I(a_0,a_1,\ldots,a_n)=\int_a^b \rho(x)\left[\sum_{k=0}^na_k\varphi_k(x) - f(x)\right]^2\,dx$$
求其驻点：
$$
\begin{align*}
  & \frac{\partial I}{\partial a_j} = 2\int_a^b \rho(x)\left[\sum_{k=0}^na_k\varphi_k(x) - f(x)\right]\varphi_j(x) \,dx = 0, \quad j=0,1,\ldots,n\\
  \iff & \sum_{k=0}^n (\varphi_k,\varphi_j)_\rho\,a_k = (f,\varphi_j)_\rho, \quad j=0,1,\ldots,n
\end{align*}
$$

记度量矩阵$\left[(\varphi_i,\varphi_j)\right]$为$T$，记向量$\beta=\left[ (f,\varphi_0),\ldots,(f,\varphi_n)\right]^T$, 则驻点$a=(a_0,a_1,\ldots,a_n)^T$即为
\[Ta=\beta\]的解。因为该度量阵是由线性无关组生成的，该方程组仅有唯一解。从而可得解$a^*$

易于验证，该解是使$S^*(x):=\sum_{k=0}^n a^*_k\varphi_k(x)$成为$f(x)$的最佳平方逼近的解。

**性质**
1. $(f,\varphi_i)_\rho=(S^*,\varphi_i)_\rho,\quad i=0,1,\ldots,n$
   $\rArr (f-S^*,S)=0$，$S$是任意$\left\{\varphi_k\right\}_{k=0}^n$的线性组合
2. $\lVert f(x)-S^*(x)\rVert_{\rho.2}^2 \leq \lVert f(x)-S(x)\rVert_{\rho.2}^2$

> 可以这样理解：所求的$S^*$实际上是$f$在线性空间$<\varphi_0,\varphi_1,\ldots,\varphi_n>$上的正交投影，它的余项是与整个空间正交的。

从而其误差为：
$$
\begin{align*}
  \lVert\delta(x)\rVert _2^2 &= (f(x)-S^*(x),f(x)-S^*(x))\\
  &= (f,f)-(S^*,f)\\
  &= \lVert f(x)\rVert _2^2 - \beta^Ta^*
\end{align*}
$$

### 3.3.3 正交函数族的最佳平方逼近

显而易见的是，度量阵需要计算$(n+1)(n+2)$次积分，且还涉及解线性方程组，这样的计算是较为繁杂的。而我们希望得到一个较为简洁的计算方式。不难发现，对于一个正交基，
其度量阵是一个对角阵，这使得得到矩阵和解矩阵所需的计算量大大减少。

这样的解是：
$$S^*(x)=\sum_{k=0}^n \frac{(f,\varphi_k)}{(\varphi_k,\varphi_k)}\varphi_k(x)$$

同时，我们称按此形式展开的函数为$f$的**广义傅里叶级数**。

由其误差可得*Bessel不等式*
$$\sum_{k=0}^n (a_k^*\lVert \varphi_k(x)\rVert_2)^2 \leq \lVert f(x)\rVert_2^2$$

> **Theorem 3.3.1**
> 设$f\in \mathcal{C}[a,b]$，$S_n^*(x)$是$f(x)$在正交多项式族$\left\{\varphi_k\right\}_{k=0}^n$上的最佳平方逼近多项式。那么：
> $$\lim_{n\rightarrow\infty}\lVert f(x)-S_n^*(x)\rVert_2 = 0$$

> **Theorem 3.3.2**
> 设$f\in \mathcal{C}^2[a,b]$，$S_n^*(x)$是$f(x)$在勒让德正交多项式族$\left\{p_k\right\}_{k=0}^n$上的最佳平方逼近多项式。那么:$\forall \epsilon > 0,\exists N=N(\epsilon)$，当$n>N$时，
> $$\sup_{x\in[-1,1]} \left|f(x)-S^*(x)\right|\leq \frac{\epsilon}{\sqrt{n}}$$

> **Theorem 3.3.3**
> 在所有首一$n$次多项式中，勒让德多项式$\hat{P}_n(x)$在$[-1,1]$上的(不带权)平方范数最小，即：
> $$\lVert\hat{P}_n(x)\rVert_2\leq\lVert p_n(x)\rVert_2$$
>（由证明过程可知，这里实际上对于任一度量矩阵正定的正交多项式族中的$n$次项均成立。但显然勒让德多项式是易于计算的。）

### 3.3.4 切比雪夫级数

事实上即为当正交基为切比雪夫多项式的时候所得的广义傅里叶级数。鉴于切比雪夫多项式可以由变量代换$x=\cos\theta$变换成三角函数，且此时$f(x)$的切比雪夫级数恰为$f(\cos\theta)$的傅里叶级数。故可以引入傅里叶级数的原理来研究。

其形式：
$$\frac{C_0^*}{2}+\sum_{n=1}^\infty C_n^*T_n(x)$$
其中：
$$C_n^*(x)=\frac{2}{\pi}\int_{-1}^1 \frac{f(x)T_n(x)}{\sqrt{1-x^2}}\,dx$$


## 3.4 曲线拟合的最小二乘法

在这里，已知有数个已知的点值。我们希望找到一个多项式$\hat{p}(x)$使得在这些点上，均方误最小。若采用离散内积，那么可以表示为：
\[\lVert f(x)-\hat{p}(x)\rVert_2^2 = \min \lVert f(x)-p(x)\rVert_2^2\]可以很容易地发现，这个表达式和我们在上文讨论的最佳平方逼近的目标没有什么差别。
再结合现在所采用的离散内积和连续内积在对参数求偏导时，行为是类似的这一事实，我们完全可以在重定义内积为离散内积后，应用前面所讨论的定理。

当然，在此处与“函数线性无关”所对应的条件是“*Harr条件*”
例如：对[一般基底的最小二乘逼近](#332-最佳平方逼近)和[正交基的最小二乘逼近](#333-正交函数族的最佳平方逼近)


# 4. 数值积分

## 4.1 牛顿-柯斯特公式

当我们利用多项式对待积函数插值，并使用插值函数的积分代表待积函数的积分时，我们称之为**插值积分**。特别地，如果采用待求区间的等距点插值，这样的插值积分是相对易于求出的，公式如下：
$$ \int_a^b f(x)\, dx = (b-a)\sum_{k=0}^n C_k^{(n)}f(x_k)$$
其中$C_k^{(n)}$被称为**柯斯特系数**，这是一个由$f(x)$确定的值。在经过代换$x=a+t(b-a)/n$后，就有
$$C_k^{(n)} = \frac{1}{n}\int_0^{n}\prod_{j=0,j\not ={k}}\frac{t-j}{k-j}\, dt = \frac{(-1)^{(n-k)}}{nk!(n-k)!}\int_0^{n}\prod_{j=0,j\not ={k}}(t-j)\, dt$$
特别地，当$n=2$时，我们称之为**辛普森公式**：
$$S = \frac{b-a}{6}\left[f(a)+4f(\frac{a+b}{2})+f(b)\right]$$
当$n=4$时，我们称之为**柯斯特公式**
$$S = \frac{b-a}{90}\left[7f(x_0)+32f(x_1)+12f(x_2)+32f(x_3)+7f(x_4)\right]$$

## 4.2 积分精度

### 4.2.1 代数精度

首先，要谈谈什么是精度：我们认为，如果对于给定函数$f$,已知的一个积分公式所求出的数值积分值与函数$f$的积分值严格 相等，那么称该积分公式对于$f$可以精确积分

代数精度
: 若某个积分公式对于不超过$m$次的多项式可以精确积分，但对于$m+1$次多项式不能精确积分，那么称该积分公式代数精度为$m$

换言之，记积分公式为$I(f)$，则可以表达为
$$\int_a^b f(x)\,dx - I(f) = 0$$特别地，若积分公式是由某个函数$g$在$[a,b]$上生成的，那么有：
$$\int_a^b (f(x)-g(x))\,dx = 0$$

从而可计算：
| 公式 | 精度 |
| --- | --- |
| 梯形公式 | 1 |
| 中点式 | 1 |
| 辛普森公式 | 3 |
| 柯斯特公式 | 5 |

> *Instance*:
> 给定形如$\int_0^1 f(x)\, dx = A_0f(0)+A_1f(1)+B_0f'(0)$的积分公式，确定$A_0,A_1,B_0$使得其具有尽可能高的代数精度。

> **Theorem 4.2.1**
> 机械公式（形如$\sum_{k=0}^n f(x_k)A_k$的积分公式）具有至少$n$阶代数精度的充要条件是，它是插值型的。

> **Theorem 4.2.2**
> 偶数$n$阶牛顿-柯斯特多项式的代数精度至少为$n+1$

### 4.2.2 积分误差

1. 若$I_n(f)$是插值积分公式，那么$$\int_a^b f(x)\,dx - I_n(f)=\int_a^b \frac{f^{(n+1)}(\xi)}{(n+1)!}F(x)\,dx$$
2. 若$I_n(f)$具有$m$阶代数精度，那么$$\int_a^b f(x)\,dx - I_n(f)=\frac{f^{(m+1)(\xi)}}{(m+1)!}R[x^{m+1}]$$，其中$$R[x^{m+1}] = \int_a^b f(x)\,dx - I_n(x^{m+1})$$