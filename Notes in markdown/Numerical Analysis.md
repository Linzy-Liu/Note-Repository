# 目录

1. [引论](#1-引论)
2. [解方程](#2-解方程)
3. [插值](#3-插值法)
4. [函数逼近](#4-函数逼近)
5. [积分](#5-数值积分)



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
\[\lVert x_c - r\rVert < \frac{b-a}{2^{n+1}}\] 其中$x_c$为事实解，$r$为数值解，$n$为迭代次数。但该方法的缺点十分显著：收敛太慢。所以我们接下来将介绍更好的一些方法。

## 2.2 不动点迭代

首先注意到，对于任一须求根的方程$f(x)=0$，总存在有限的变换使其转化为$x=g(x)$的形式。这样的存在性是易于说明的，比如：$x=x+f(x)$就是一类。从而我们现在可以转而研究不动点迭代的问题。
望文生义，不动点即为满足$g(x)=x$的实数$x$。一般而言，我们采用不动点迭代来寻找不动点：
\[x_{n+1} = f(x_n)\]但这样的迭代并不总是收敛。
可以绘制**cobweb图**来直观地说明这一点。因此我们需要找到确保不动点迭代可行的前提，即确保这个迭代过程收敛的条件。

### 2.2.1 敛散性

注意到：
$\textbf{Theorem 2.2.1}\left(压缩映像原理\right)$设$f$在$E \subset \mathbb{R}$上可微，且数列$\{x_n\}_{n=1}^\infty$由$x_{n+1} = f(x_n)$定义，若
 \[\sup |f'(x)| \leq r < 1\]则数列收敛。

注：若$f'$在收敛点$x^*$的邻域上连续且在$x^*$处绝对值小于1，那么存在一个邻域使其上的任意一个点都会迭代至$x^*$

这一定理的离散版本是：
$\textbf{Theorem 2.2.1*}\left(压缩映像原理\right)$ 设对于数列$\{x_n\}$，存在正数$L<1$，使得\[\left|x_{n+1}-x_n\right| < L\left|x_n-x_{n-1}\right|\]则数列收敛。

从而我们的敛散性是可以得到保证的。同时，我们为了收敛序列的唯一性，考虑以下定理：
$\textbf{Theorem 2.2.2}$ 设$\varphi\in\mathcal{C}[a,b]$，且：
  1. 对于任一$x\in [a,b]$，有$a\leq \varphi(x)\leq b$
  2. 存在正数$L<1$，对于任意$a\leq x,y \leq b$， 有$$\left|\varphi(x)-\varphi(y)\right|\leq L\left|x-y\right|$$
  则$\varphi$在$[a,b]$上存在唯一的不动点。
并且，由这一定理可以立马得到以下推论：
$\textbf{Corollary}$ 设$\varphi\in\mathcal{C}[a,b]$满足定理2.2.2中的两个条件，记该唯一的不动点为$x^*$，那么对于任意的由初始点$x_0\in[a,b]$产生的数列$\{x_n\}_{n=1}^\infty$，有上界估计
  $$\left|x^*-x_k\right|\leq \frac{L^k}{1-L}\left|x_1-x_0\right|$$

收敛阶
: 设由$x_{n+1}=\varphi(x_n)$收敛于$\varphi$的不动点$x^*$，记$e_k=x_k-x^*$ 。若当$k\rightarrow\infty$时，满足：
$$\frac{e_{k+1}}{e_k^p}\rightarrow C$$其中$C\not ={0}$，那么称该迭代过程是$\textbf{p}$**阶收敛**的。

$\textbf{Theorem 2.2.3}$ 设$p$为正整数，且迭代过程为$x_{n+1}=\varphi(x_n)$。若$\varphi^{(p)}$在所求解$x^*$的一个领域中连续，且满足
$$ \varphi(x^*)=\varphi'(x^*)=\ldots=\varphi^{(p-1)}(x^*)=0\\ \varphi^{(p)}(x^*)\not ={0}$$ 那么该迭代过程在$x^*$邻域是$p$阶收敛的。

由上可见，为了寻求一个收敛且速度极快的序列，选取一个好的迭代函数是必要的。

### 2.2.2 迭代收敛的加速方法

首先介绍Aitken(埃特金)加速收敛法的思想。现已知迭代公式$x_1=\varphi(x_0)$，而后我们*自然*地认为$\varphi'$在我们想要探究的区域上变化不大，那么就有：
$$
\begin{aligned}
  x_1-x^* &= \varphi'(\xi)(x_0-x^*) \approx L(x_0-x^*)\\
  x_2 - x^* &\approx  L(x_1-x^*)
\end{aligned}
$$
联立得解：$$x^*\approx x_0 - \frac{(x_1-x_0)^2}{x_2-2x_1+x_0}$$
那么便有迭代式：$$\bar{x}_{k+1} = x_0 - \frac{(x_{k+1}-x_k)^2}{x_{k+2}-2x_{k+1}+x_k}$$

可以证明，$\frac{\bar{x}_{k+1}-x^*}{x_k - x^*} \rightarrow 0$，这说明${\bar{x}_{k+1}}$的收敛是快于原迭代式的。
接下来，我们考虑将二者结合起来：因为注意到单凭埃特金加速法是基于一个现有的收敛序列进行的加速计算，而我们需要一个可自迭代的递推式，故我们考虑如下递推式：
$$
\begin{aligned}
  y_k &= \varphi(x_k),& z_k = \varphi(y)\\
  x_{k+1} &= x_k - \frac{(x_k-y_k)^2}{z_k-2y_k+x_k}
\end{aligned}
$$
在几何上，我们可以理解为，我们对原迭代中的两个误差$\varepsilon(x_k),\varepsilon(y_k)$进行了一次线性插值，然后令$x_{k+1}$取其零点。
最终可以整合得迭代式
$$x_{k+1} = x_k - \frac{(\varphi(x)-x)^2}{\varphi(\varphi(x))-2\varphi(x)+x}$$

$\textbf{Theorem 2.2.4}$ 设$x^*$为上式定义的迭代过程的不动点，则$x^*$为$\varphi(x)$的不动点；若$x^*$为$\varphi(x)$的不动点，且$\varphi''$存在，$\varphi'(x^*)\not ={1}$，那么上述迭代过程二阶收敛。

同时也可以说明，我们可以将不收敛的迭代式加速为收敛的；将$p$阶收敛的迭代式加速为$p+1$阶收敛的迭代式。

## 2.3 牛顿法

这一方法事实上是来自于对可微函数的线性近似。即，$f(x) = f(x_0) + f'(\xi)(x-x_0)$。在下面，我们将给出一般的牛顿法的迭代公式：
$$ x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}$$由压缩映像定理与$\textbf{Theorem 2.2.3}$可知，这一方法在求方程的单根的时候是平方收敛的，对于复根则降低至线性收敛。

这一迭代过程往往经历以下步骤：确定初值——迭代产生下一个数——计算差距——迭代...通常我们会采用一个常数$C$来控制采用绝对误差还是相对误差，即：当$|x_{k+1}|\leq C$时，采用绝对误差$|x_{k+1} - x_k|$，否则选择相对误差$|x_{k+1} - x_k|/|x_k|$

一般来说，微分计算是比较复杂，有时候对于一些函数是难以实现的。因此有一些改进型的牛顿法：

### 简化牛顿法

我们出于简便计算和直觉上，可以考虑将$1/f'(x_n)$替换为$C = 1/f'(x_0)$，这样，迭代公式就变为了$$x_{n+1} = x_n - Cf(x_n)$$而这一方法的问题在于，随着精度的降低，其收敛界将会更小，该方法是适用范围将会更局部。

### 牛顿下山法

注意到，牛顿法不总是收敛的，
### 割线法

为了回避导数值的计算，我们还可以考虑使用差商来代替。当我们准备求$x_{k+1}$时，我们已经知道$x_j(j=1,2,\ldots,k)$的值，从而根据前面所提出的想法，可以将$f'(x_k)$以$x_k$与$x_{k-1}$的差商替代。从而有迭代公式：
$$x_{k+1} = x_k - \frac{(x_k-x_{k-1})f(x_k)}{f(x_k) - f(x_{k-1})}$$

$\textbf{Theorem 2.3.1}$ 设$f(x)$在根的的邻域内二阶连续可导，且在此邻域内$f'(x) \not ={0}$，且初值$x_0,x_1$均在此邻域内。那么当此邻域足够小时，割线法的收敛阶为$\frac{1+\sqrt{5}}{2}$

### 抛物线法

从另一个角度解释，可以认为割线法是通过求$x_k,x_{k-1}$的线性插值函数的零点来得到迭代公式的。因此可以进一步想，是否可以使用高次多项式呢？当然，鉴于高于五次的多项式就没有解析解了，且三、四次的求根公式也比较复杂，故在此采用二次插值。即令$x_{k+1}$为$x_k,x_{k-1},x_{k-2}$的插值多项式的零点。一般地来说由于方程存在两个根，故我们倾向于选择距$x_k$最近的根。由于方程本身形状虽易于计算但形式复杂，故在此不列出。

### 解非线性方程组

设待解方程为$F(x) = 0$，在此不加证明地指出，在形式上，$F$同样适用于本章的大部分敛散性有关的定理和定义，除了一个，我们将此定理书写如下：

$\textbf{Theorem 2.3.2}$ 设$F$在$E\subset\mathbb{R}^n$上有不动点$x^*$，且$F$的Jacobi矩阵$J_F$存在，那么若$$\rho(J_F(x^*))<1$$，则存在一个$x^*$的邻域$S$，使得以$x_0\in S$为初值的迭代序列均收敛。

在这里，我们依然考虑采用牛顿法：
$$x_{k+1} =x_k - J_F^{-1}(x_k)F(x_k)$$在这里，逆符号仅作为形式记号，在计算中并不会求逆。同时也指出，我们所求的非线性方程组的因变量数量和自变量数量不一定一致。于是，我们给出事实上的迭代公式
$$
\begin{aligned}
  & x_{k+1} = x_k - \Delta x
  & s.t.\quad J_F(x_k)\Delta x = F(x_k)
\end{aligned}
$$
这一方法中，若$J_F$在$x^*$的一个开邻域$S$上存在且连续，且$J_F$可逆，那么这一方法的迭代序列在闭邻域$S_0\subset S$上超线性收敛。更多地，若$F$在$S$上满足$L<1$的Lipschitz条件，那么该迭代法二阶收敛。


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


# 4. 函数逼近

我们的主要目的，就是找一个简单的，已于计算的$p(x)$和一个metric，使得在该metric下，$f(x)$与$p(x)$的距离最小。

## 4.1 线性空间

### 4.1.1 赋范线性空间

设$V$为一个定义在$F$上的线性空间，若存在函数$f: V \rightarrow \mathbb{R}$，满足：
1. 正定性
2. $f(ax)=\left|a\right|f(x)$
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

### 4.1.2 最佳逼近

最佳逼近
: 设$f\in \mathcal{C}[a,b]$，$H_n$是由实值函数张成的维度为$n$的赋范空间。若有$p^*\in H_n$使\[\lVert f-p^*\rVert=\min_{p\in H_n} \lVert f-p\rVert\]则称$p^*$是$f$在赋范空间$H_n$上的**最佳逼近**
特别地，若范数为$\lVert x\rVert_{\infin}$，则称其为**最佳一致逼近**；若范数为$\lVert x\rVert_2$，则称其为**最佳平方逼近**；若范数为$\lVert x\rVert_w$，则称其为**最佳加权逼近**

于是
> **Theorem 4.1.1(Weierstrass)**
> Suppose f is continuous on $[a,b]$. Then for any $\varepsilon > 0$, there exists a polonomial $p(x)\in P_\infin$,such that\[\lVert f-p\rVert_\infin < \varepsilon\]

最小二乘拟合
: 设$f\in\mathcal{C}[a,b]$, $y_i=f(x_i),\, i\in[0,m]$，那么$p^*\in H_n$是$f$的最小二乘拟合当且仅当：
$$ \lVert f-p^*\rVert_{w.2} = \min_{p\in H_n}\lVert f-p\rVert_{w.2}$$
在此，我们将范数定义为
$$ \lVert f-p\rVert_{w.2} = \sqrt{\sum_{i=0}^m (f(x_i)-p(x_i))^2w(x_i)}$$

## 4.2 正交多项式

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

> **Theorem 4.2.1**
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

> **Theorem 4.2.2**
> 设$\left\{\varphi_n(x)\right\}_{n=0}^\infty$是$[a,b]$上带权$\rho(x)$的正交多项式,则$\varphi_n$在$[a,b]$上有不同的$n$个零点。

（上述$\left\{\varphi_n(x)\right\}_{n=0}^\infty$都是由$1,x,\ldots,x^n$经施密特正交化依次得到的, 而一般实践中，可以有$T^TATx$一样的变换，但注意各个定理推导时的前提条件。）

### 4.2.1 勒让德多项式

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

### 4.2.2 切比雪夫多项式

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

> **Theorem 4.2.3**
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

## 4.3 最佳平方逼近

### 4.3.1 讨论域

我们在本节，主要想解决这样的一个问题：
对于$\mathcal{C}[a,b]$上的函数$f$和函数组$\left\{\varphi_k\right\}_{k=0}^n$，是否存在一个$\left\{\varphi_k\right\}_{k=0}^n$的线性组合$S^*(x)$，使得对于任一一个线性组合$S(x)$：
\[\lVert f(x)-S^*(x)\rVert_2^2 = \min \lVert f(x)-S(x)\rVert_2^2\]
如果存在，它的具体形式如何？

### 4.3.2 最佳平方逼近

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

### 4.3.3 正交函数族的最佳平方逼近

显而易见的是，度量阵需要计算$(n+1)(n+2)$次积分，且还涉及解线性方程组，这样的计算是较为繁杂的。而我们希望得到一个较为简洁的计算方式。不难发现，对于一个正交基，
其度量阵是一个对角阵，这使得得到矩阵和解矩阵所需的计算量大大减少。

这样的解是：
$$S^*(x)=\sum_{k=0}^n \frac{(f,\varphi_k)}{(\varphi_k,\varphi_k)}\varphi_k(x)$$

同时，我们称按此形式展开的函数为$f$的**广义傅里叶级数**。

由其误差可得*Bessel不等式*
$$\sum_{k=0}^n (a_k^*\lVert \varphi_k(x)\rVert_2)^2 \leq \lVert f(x)\rVert_2^2$$

> **Theorem 4.3.1**
> 设$f\in \mathcal{C}[a,b]$，$S_n^*(x)$是$f(x)$在正交多项式族$\left\{\varphi_k\right\}_{k=0}^n$上的最佳平方逼近多项式。那么：
> $$\lim_{n\rightarrow\infty}\lVert f(x)-S_n^*(x)\rVert_2 = 0$$

> **Theorem 4.3.2**
> 设$f\in \mathcal{C}^2[a,b]$，$S_n^*(x)$是$f(x)$在勒让德正交多项式族$\left\{p_k\right\}_{k=0}^n$上的最佳平方逼近多项式。那么:$\forall \epsilon > 0,\exists N=N(\epsilon)$，当$n>N$时，
> $$\sup_{x\in[-1,1]} \left|f(x)-S^*(x)\right|\leq \frac{\epsilon}{\sqrt{n}}$$

> **Theorem 4.3.3**
> 在所有首一$n$次多项式中，勒让德多项式$\hat{P}_n(x)$在$[-1,1]$上的(不带权)平方范数最小，即：
> $$\lVert\hat{P}_n(x)\rVert_2\leq\lVert p_n(x)\rVert_2$$
>（由证明过程可知，这里实际上对于任一度量矩阵正定的正交多项式族中的$n$次项均成立。但显然勒让德多项式是易于计算的。）

### 4.3.4 切比雪夫级数

事实上即为当正交基为切比雪夫多项式的时候所得的广义傅里叶级数。鉴于切比雪夫多项式可以由变量代换$x=\cos\theta$变换成三角函数，且此时$f(x)$的切比雪夫级数恰为$f(\cos\theta)$的傅里叶级数。故可以引入傅里叶级数的原理来研究。

其形式：
$$\frac{C_0^*}{2}+\sum_{n=1}^\infty C_n^*T_n(x)$$
其中：
$$C_n^*(x)=\frac{2}{\pi}\int_{-1}^1 \frac{f(x)T_n(x)}{\sqrt{1-x^2}}\,dx$$


## 4.4 曲线拟合的最小二乘法

在这里，已知有数个已知的点值。我们希望找到一个多项式$\hat{p}(x)$使得在这些点上，均方误最小。若采用离散内积，那么可以表示为：
\[\lVert f(x)-\hat{p}(x)\rVert_2^2 = \min \lVert f(x)-p(x)\rVert_2^2\]可以很容易地发现，这个表达式和我们在上文讨论的最佳平方逼近的目标没有什么差别。
再结合现在所采用的离散内积和连续内积在对参数求偏导时，行为是类似的这一事实，我们完全可以在重定义内积为离散内积后，应用前面所讨论的定理。

当然，在此处与“函数线性无关”所对应的条件是“*Harr条件*”
例如：对[一般基底的最小二乘逼近](#432-最佳平方逼近)和[正交基的最小二乘逼近](#433-正交函数族的最佳平方逼近)


# 5. 数值积分

## 5.1 牛顿-柯斯特公式

当我们利用多项式对待积函数插值，并使用插值函数的积分代表待积函数的积分时，我们称之为**插值积分**。特别地，如果采用待求区间的等距点插值，这样的插值积分是相对易于求出的，公式如下：
$$ \int_a^b f(x)\, dx = (b-a)\sum_{k=0}^n C_k^{(n)}f(x_k)$$
其中$C_k^{(n)}$被称为**柯斯特系数**，这是一个由$f(x)$确定的值。在经过代换$x=a+t(b-a)/n$后，就有
$$C_k^{(n)} = \frac{1}{n}\int_0^{n}\prod_{j=0,j\not ={k}}\frac{t-j}{k-j}\, dt = \frac{(-1)^{(n-k)}}{nk!(n-k)!}\int_0^{n}\prod_{j=0,j\not ={k}}(t-j)\, dt$$
特别地，当$n=2$时，我们称之为**辛普森公式**：
$$S = \frac{b-a}{6}\left[f(a)+4f(\frac{a+b}{2})+f(b)\right]$$
当$n=4$时，我们称之为**柯斯特公式**
$$S = \frac{b-a}{90}\left[7f(x_0)+32f(x_1)+12f(x_2)+32f(x_3)+7f(x_4)\right]$$

## 5.2 积分精度

### 5.2.1 代数精度

首先，要谈谈什么是精度：我们认为，如果对于给定函数$f$,已知的一个积分公式所求出的数值积分值与函数$f$的积分值严格相等，那么称该积分公式对于$f$可以精确积分

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

> **Theorem 5.2.1**
> 机械公式（形如$\sum_{k=0}^n f(x_k)A_k$的积分公式）具有至少$n$阶代数精度的充要条件是，它是插值型的。

> **Theorem 5.2.2**
> 偶数$n$阶牛顿-柯斯特多项式的代数精度至少为$n+1$

### 5.2.2 积分误差

1. 若$I_n(f)$是插值积分公式，那么$$\int_a^b f(x)\,dx - I_n(f)=\int_a^b \frac{f^{(n+1)}(\xi)}{(n+1)!}F(x)\,dx$$
2. 若$I_n(f)$具有$m$阶代数精度，那么$$\int_a^b f(x)\,dx - I_n(f)=\frac{f^{(m+1)}(\xi)}{(m+1)!}R[x^{m+1}]$$，其中$$R[x^{m+1}] = \int_a^b x^{m+1}\,dx - I_n(x^{m+1})$$
   * *Corollary* $R[f]=K(b-a)^{m+2}f^{(m+1)}(\xi)$，在这里，积分公式的代数精度为$m$

## 5.3 复合求积公式

简而言之，就是为了避免龙格现象的出现，我们尝试将待积区域分段，而后对每段运用前面讲到的梯形、中点等牛顿-斯科特类公式，以及一些最佳一致逼近/平方逼近的积分公式。

思考：
1. 复合梯形公式有什么形状？误差如何？
2. 复合辛普森公式的形状如何？误差如何？

### 5.3.1 外推方法

在这里，我们特别提到这个概念是因为它采用了**外推**技巧。这样的技巧来自一种信念：每一次计算和推导都消耗了资源，因此我们需要在推导出新式子之后充分利用旧资源，使得计算资源利用最大化。
首先，我们有定理如下：
> **Theorem 5.3.1**
> 设$f\in \mathcal{C}^\infty[a,b]$，$T_n(h)$代表将区间分为$n=\frac{1}{h}$等分后所得的复合梯形积分公式。那么有：
> $$T_n(h)=\int_a^b f(x)\,dx + \alpha_1 h^2+\alpha_2 h^4 +\ldots$$

这个定理可由$f(x+h)$，$f(x-h)$结合积分误差的估计式可得。
有了这个定理，就可以保证外推的精度递增速度了。我们接下来尝试说明外推的具体操作。
首先，我们由上有：
$$
\begin{align*}
  T_n(h) &=\int_a^b f(x)\,dx + \alpha_1 h^2+\alpha_2 h^4 +\ldots\\
  T_n(h/2) &=\int_a^b f(x)\,dx + \frac{\alpha_1}{4} h^2+ \frac{\alpha_2}{16} h^4 +\ldots
\end{align*}
$$
从而可知，令$S(h):=\frac{1}{3}(4T_n(h/2)-T_n(h))$，则
$$ S(h) - \int_a^b f(x)\,dx = O(h^4)$$
同理，记$T^{(0)} = T_n(h)$，$T^{(1)}=S(h)$，则可由上述过程得到函数列$\{T^{(k)}\}_{k=0}^\infty$，在每一次迭代后，精度都会提高二次。
> 注：在整个过程中，$h$并未换元，也就是说，$h$的值是一致的。因而想要控制精度，至少要保证$h<1$。

### 5.3.2 *Romberg*算法

上文中提到的函数列$\{T^{(k)}\}_{k=0}^\infty$，在这里我们给出统一的一个递推公式。
$$T^{(m)}(h)=\frac{4^m}{4^m-1}T^{(m-1)}(h/2)-\frac{1}{4^m-1}T^{(m-1)}(h)$$
回忆$Hermitee$插值法，同样地，我们也可以给出一个$T$值表。限定好终止条件，我们便可以得到任意精确的数值积分。

我们尝试规范化这一过程：
1. 令$k=0$，$h=b-a$，$T_0^{(0)}=h(f(a)+f(b))/2$
2. 按复合梯形公式计算区间经$m$次二分的积分值$T_0^{(m)}$，事实上，我们有：$T_0^{(n)} = 1/2\,T_0^{(n-1)} + h/2\sum_k f(x_k)$，其中$x_k$代表在上一次二分中新产生的点
3. 根据公式$$T_m^{(n)} = \frac{4^n}{4^n-1}T_{m-1}^{(n)} - \frac{1}{4^n-1}T_{m-1}^{(n-1)}$$
4. 根据精度$\varepsilon$，当$\left|T_{n+1}^{(n+1)}-T_n^{(n)}\right|<\varepsilon时成立。$

## 5.4 自适应积分

由上面的外推公式，我们很容易可以知道，当我们对区间二分时，误差会下降，但会使计算量上升。在实际应用中，我们仅需找到一个固定精度的值，而对于不同函数的不同段上，达到固定精度所需二分的次数是不同的，因此需要有选择地二分。
记在$[a,b]$上的积分公式为$S(a,b)$，以辛普森公式为例，则有：
\[\int_a^b f(x)\,dx - S(a,b) = -\frac{b-a}{180}\left(\frac{h}{2}\right)^4f^{(4)}(\xi)\]其中$h=b-a$，将其二分，有：
$$
\begin{align*}
  \left|\int_a^b f(x)\,dx - S_2(a,b)\right| &= \left|\int_a^b f(x)\,dx - \left(S\left(a,\frac{a+b}{2}\right)+ S\left(\frac{a+b}{2},b\right)\right)\right|\\
                                            &= \frac{b-a}{180}\left(\frac{h}{4}\right)^4\left|f^{(4)}(\psi)\right|
\end{align*}
$$
可以认为，$\left|f^{(4)}(\psi)\right| \approx \left|f^{(4)}(\xi)\right|$，从而可以得到一个上界估计:
\[\left|\int_a^b f(x)\,dx - S_2(a,b)\right| \leq M\left|S(a,b)-S_2(a,b)\right|\]
因而在程序执行中，只需计算二分前后的精度差便可知道当前精度，从而实现自适应。

## 5.5 高斯积分

对于一个$n$阶机械公式$\int f(x)\rho(x)\,dx=\sum_{k=0}^n f(x_k)A_k$，我们知道它们至多在其为等距插值公式时，可以有代数精度$n+1$。那么，这个精度是否能更高？注意到，我们之前一直试图在采样点固定的前提下积分，这样的话，可变系数只有$n$个参数$A_i$。现在，我们尝试将采样点也作为待优化参数，并试着使这样的积分公式的代数精度达到$2n+1$（~~当然不是靠定义实现的~~）。

高斯型求积公式
: 若机械公式$\int f(x)\rho(x)\,dx=\sum_{k=0}^n f(x_k)A_k$有$2n+1$次代数精度，那么称其节点$x_k$为**高斯点**，称这样的机械公式为高斯型求积公式。

在推导这样的机械公式中，我们可以得到这样的定理，它揭示了高斯点可由$n+1$阶正交多项式的零点求出。
> **Theorem 5.5.1**
> 插值型求积公式的节点$x_k$是高斯点的充要条件是，以这些节点为零点的多项式$w_{n+1}(x) = \prod (x-x_k)$和任意不超过$n$的多项式带权$\rho$正交。

那么$2n+1$是否是最高的代数精度呢？不幸的是，答案是肯定的。首先，$2n+1$的代数精度实际上意味着$2n+2$个方程，已经满足了机械公式的$2n+2$个自由度，再多的话可能会出现无解的情况。其次，这样高的精度要求，就意味着这一定是个插值型积分公式。

利用$f(x_k)$和$f'(x_k)$，就可以得到一个Hermitee插值多项式$H_{2n+1}$，这样的多项式有：
$$f(x)=H_{2n+1}+\frac{f^{(2n+2)}(\xi)}{(2n+2)!}w_{n+1}^2(x)$$从而可得误差的表达式：
$$R_n[f] = \frac{f^{(2n+2)}(\eta)}{(2n+2)!}\int_a^bw_{n+1}^2(x)\rho(x)\,dx$$
注：式中的$\eta$与$\xi$是不同的，其是由积分中值公式产生的。

还可以知道高斯求积公式的两个性质
1. 稳定性：高斯求积公式的所有求积系数$A_k$都是正数。
2. 高斯求积公式是收敛的，即\[\int_a^bf(x)\rho(x)\,dx=\lim_{n\rightarrow\infty}\sum_{k=0}^n f(x_k)A_k\]

# 6 解线性方程

## 6.1 LU分解

> 鉴于高斯消元是高代的基础操作，在此不做赘述。但易得，该过程的乘除法次数约为$\frac{n^3}{3}$,加减法次数为$\frac{n^3}{3}$

我们还有这样的定理：
$\textbf{Theorem 6.1.1}\quad$ 矩阵$A$主对角线上的所有元素$a_{ii}$非零当且仅当$A$的各阶顺序主子式非零。


$\textbf{Theorem 6.1.2}\left(LU分解\right)\quad$ 设$A$为$n$阶矩阵，若$A$的各阶顺序主子式$D_i$非零，那么$A$可以分解为一个单位下三角矩阵$L$和上三角矩阵$U$，且这样的分解是唯一的
\[A=LU\]

注：单位下三角矩阵即主对角线上都是$1$的三角阵

那么，在$LU$分解下求逆的复杂度为$n^3$，同时$LU$分解对于解$Ax=b_k$这样的一系列的非齐次线性方程组的情况十分友好，可以将复杂度由$M\frac{n^3}{3}$减为$\frac{n^3}{3}+Mn^2$
但鉴于对于数值计算，存在一种情况：主对角线上的元素过小，导致明显的精度折损。为了避免这种情况，我们需要事先将合适的元素换至对角线上。这样，我们就有改进版的$LU$分解：
$\textbf{Theorem 6.1.3}\left(LU分解\right)\quad$ 设$A$为$n$阶矩阵，若$A$的各阶顺序主子式$D_i$非零，那么经过合适的调换顺序后$A$可以分解为一个单位下三角矩阵$L$和上三角矩阵$U$，且这样的分解是唯一的
\[PA=LU\]其对应的消元法叫*列主元素消元法*

从而由以上两种消元法得到两种解方程的方式：**直接三角分解法**（*Doolittle算法*）和**选主元的三角分解法**
一般而言，需要解方程：
$$
\left\{
\begin{align*}
  Ly &= \beta\\
  Ux &= y
\end{align*}\right.$$
对于选主元的三角分解法，将$\beta$换为$P\beta$即可。而在算法实践中，可以根据这些消元过程推导得到对应的公式，有需要可以手推或看书。

### 6.1.1 平方根法

由合同变换的过程可以很容易地得到以下结论：

$\textbf{Theorem 6.1.4}$ 设$A$为$n$阶对称阵，且$A$的各阶顺序主子式非零，那么$A$存在唯一的分解：
\[A=L^TDL\]其中$L$为单位上三角阵，$D$为对称阵。

进一步地，若$A$正定，则$D$存在分解$\sqrt{D}\,\sqrt{D}$，进而可以得到推论：
$\textbf{Corollary}$ 设$A$为$n$阶正定阵，那么存在一个实可逆上三角矩阵$L_1$，使得：
\[A=L_1^TL_1\]这样的$L_1$在不管对角线正负号的前提下是唯一的。

对于这一分解，其所需的乘除次数约为$n^3/6$。鉴于这一计算涉及开平方根，我们尝试改进平方根法：即利用定理2.3.4的分解$A=L^TDL$，令$T=L^TD$，那么可以采用相似的算法计算得$T$与$L$。在这里相较于前者仅仅是多了一个额外计算
对角线元素$d_i$的步骤。和$LU$分解一样，两者都可以写在同一个矩阵里。

### 6.1.2 追赶法

我们在一些特殊情况会解这样的线性方程组：（比如三次样条插值）
\[Ax=f\]其中
$$
A = \left[
  \begin{array}{ccccc}
    b_1 & c_1 & & & \\
    a_2 & b_2 & c_2 & & \\
     & \ddots & \ddots & \ddots & & \\
     & &  a_{n-1} & b_{n-1} & c_{n-1}\\
     & & & a_n & b_n 
  \end{array}
\right]\\
f = (f_1,f_2,\ldots,f_n)^T
$$
且这样的矩阵$A$满足：
1. $\left|b_1\right|>\left|c_1\right|>0$，$\left|b_n\right|>\left|a_n\right|>0$
2. $\left|b_i\right|\geq \left|a_i\right|+\left|c_i\right|$

显然，这样的矩阵$A$是可以分解为$A=LU$的
$$
A = \left[
  \begin{array}{ccccc}
    b_1 & c_1 & & & \\
    a_2 & b_2 & c_2 & & \\
     & \ddots & \ddots & \ddots & & \\
     & &  a_{n-1} & b_{n-1} & c_{n-1}\\
     & & & a_n & b_n 
  \end{array}
\right] = \left[
  \begin{array}{cccc}
    \alpha_1 & & &\\
    \gamma_2 & \alpha_2 & &\\ 
     & \ddots & \ddots & \\
     & & \gamma_n & \alpha_n 
  \end{array}
\right]
\left[
  \begin{array}{cccc}
    1 & \beta_1 & & \\
    & 1 & \ddots & \\
    & & \ddots  & \beta_{n-1}\\
    & & & 1
  \end{array}
\right]
$$
从而有方程组：
$$
\left\{
\begin{align*}
  b_1 &= \alpha_1, & c_1 &= \alpha_1\beta_1\\
  a_i &= \gamma_i, & b_i &= \gamma_i\beta_{i-1}+\alpha_i\\
  c_i &= \alpha_i\beta_i
\end{align*}
\right.
$$
化简得
$$
\left\{
\begin{align*}
  \alpha_i &= b_i - a_i\beta_{i-1}\\
  \beta_i &= c_i/(a_i\beta_{i-1})\\
  \gamma_i &= a_i
\end{align*}
\right.
$$
我们发现，只需要一个额外的可以自迭代的变量$\beta$即可求解。于是求解步骤变为：求出$\{\beta_i\}$——求解$Ly=f$——求解$Ux=y$。总共仅需$5n-4$次乘除法。后续若更换$f$也仅需额外的$3n-2$次乘除计算。
最后，还有定理：
$\textbf{Theorem 6.1.5}$ 设有线性方程组$Ax=f$，$A$满足本小节开头的三对角线矩阵条件，那么$A$可逆且：
1. $0<\left|\beta_i\right|<1, i=1,2,\ldots,n$
2. $0<\left|b_i\right|-\left|a_i\right|<\left|\alpha_i\right|<\left|b_i\right|+\left|a_i\right|,\quad i=2,3\ldots,n$
3. 这样的定理保证了一个已知的边界估计，让计算中不至于因极端值而损失精度

## 6.2 向量范数

范数的定义将会在[4.1.1](#411-赋范线性空间)介绍，这里阐述一下内积的定义：
内积
: 若函数$(*,*):\,\mathbb{C}^n\times\mathbb{C}^n\rightarrow\mathbb{R}$满足：$\forall a,b \in \mathbb{R}, f,g,h\in \mathbb{C}^n$
  1. $(af+bg,h)=a(f,h)+b(g,h)$
  2. $(f,g) = \bar{(g,f)}$
  3. $(a,a)=0 \lrArr a=0$

同时，我们给出以下定理：
$\textbf{Theorem 6.2.1}(范数的连续性)$ $\mathbb{R}^n$上的范数是$\mathbb{R}^n$上的连续函数。

$\textbf{Theorem 6.2.2}(范数的等价性)$  对于$\mathbb{R}^n$上的两种范数$\lVert x\rVert_s,\lVert x\rVert_r$，总存在$c_1,c_2>0$，使得
\[c_1\lVert x\rVert_s\leq \lVert x\rVert_r \leq c_2\lVert x\rVert_s\]

$\textbf{Theorem 6.2.3}(范数的收敛性)$ 对于任意一种向量范数，都有下式成立：
$$\lim_{k\rightarrow\infty}x^{(k)}=x^* \lrArr \lim_{k\rightarrow\infty} \lVert x^{(k)}-x^*\rVert=0$$

矩阵范数
: 设函数$\lVert X\rVert : \mathbb{R}^{n\times n}\rightarrow\mathbb{R}$若满足：
    1. 正规性
    2. $\forall c\in \mathbb{R}$，$\lVert cA\rVert=\left|c\right|\lVert A\rVert$
    3. $\lVert AB\rVert\leq \lVert A\rVert\lVert B\rVert$
    4. $\lVert A+B\rVert\leq \lVert A\rVert+\lVert B\rVert$
  那么称$\lVert X\rVert$为一个**矩阵范数**

很容易可以验证**Frobenius范数**$$\lVert A\rVert_F:=\left(\sum a_{ij}^2\right)^\frac{1}{2}$$是矩阵范数
为了免去范数的验证并利用已经构建的范数，我们尝试使用向量范数诱导产生矩阵范数：

算子范数
: 设$x\in \mathbb{R}^n,\, A\in\mathbb{R}^{n\times n}$, 对于一个给定的向量范数$\lVert x\rVert_v$，我们相应地定义一个矩阵范数：
$$\lVert A\rVert_v = \max_{x \not ={0}}\frac{\lVert Ax\rVert_v}{\lVert x\rVert_v}$$
由这样定义的矩阵范数被称为**算子范数**或**从属范数**

从实际操作上，我们也可以认为这样的算子范数是由$\lVert x\rVert_v$诱导的范数。但出于严谨性，需要证明这个式子所定义的函数是一个矩阵范数。
接下来，就可以由此产生一些常用矩阵范数了：
1. \[\lVert A\rVert_\infty = \max_{i}\sum_{j=1}^n \left|a_{ij}\right|\]
2. \[\lVert A\rVert_1 = \max_{j}\sum_{i=1}^n \left|a_{ij}\right|\]
3. \[\lVert A\rVert_2 = \sqrt{\lambda_{max}(A^TA)}\]其中$\lambda_{max}(A)$表示$A$的绝对值的最大特征值。

$\textbf{Theorem 6.2.4}(范数与谱半径)$ 我们定义**谱半径**为方阵$A$的特征值的绝对值的最大值$\rho(A):=\lambda_{max}(A)$，则有：
$$\rho(A)\leq \lVert A\rVert$$且对于任意$\epsilon > 0$，总存在一个算子范数$\lVert A\rVert_\epsilon$，使得
$$\lVert A\rVert_\epsilon \leq \rho(A) + \epsilon$$
即\[\rho(A)=\inf_v \lVert A\rVert_v\]

同时，由此可证对于一个$n$阶对称阵$A$，有$\rho(A)=\lVert A\rVert_2$

## 6.3 误差与残差

一般来说，实际测量的数据总会存在误差，因而我们不希望测量数据的微小扰动显著地影响到解。
$\textbf{Theorem 6.3.1}(扰动定理)$ 若$\lVert B\rVert < 1$，则$I\plusmn B$可逆，且
$$(I\plusmn B)^{-1}\leq \frac{1}{1-\lVert B\rVert}$$

$\textbf{Theorem 6.3.2}(右项扰动)$ 设矩阵$A$可逆，向量$b$不为0，若$b$有个小扰动$\delta b$，设$A(x+\delta x)=b+\delta b$，则
$$\frac{\lVert\delta x\rVert}{\lVert x\rVert} \leq \lVert A\rVert \lVert A^{-1}\rVert\frac{\lVert\delta b\rVert}{\lVert b\rVert}$$

$\textbf{Theorem 6.3.3}(系数扰动)$ 设矩阵$A$可逆，向量$b$不为0，若$A$存在扰动$\delta A$，设$(A+\delta A)(x+\delta x)=b$，且$\lVert A\rVert\lVert\delta A\rVert\leq 1$，则
$$\frac{\lVert \delta x\rVert}{\lVert x\rVert}\leq \frac{\lVert A\rVert \lVert A^{-1}\rVert\frac{\lVert\delta A\rVert}{\lVert A\rVert}}{1-\lVert A\rVert \lVert A^{-1}\rVert\frac{\lVert\delta A\rVert}{\lVert A\rVert}}$$

同时，注意到这些上界都有共同项$\lVert A\rVert_n \lVert A^{-1}\rVert_n$，我们称这些共同项为$A$的**条件数**，记作$cond(A)_n$。可以发现，条件数对扰动的放大作用是十分显著的。因此，我们考虑找出一些条件数的特点。
对于任意可逆矩阵$A$，
1. $cond(A)_v\geq 1$
2. $\forall c\in \mathbb{R},\quad cond(cA)_v=cond(A)_v$
3. 设$R$为正交阵，则$cond(R)_2=1$，且\[cond(AR)_2=cond(RA)_2=cond(A)_2\]

且我们知道，\[cond(A)_2=\sqrt{\frac{\lambda_{max} (A^TA)}{\lambda_{min}(AA^T)}}\]
特别地，当$A$为对称阵时，$$cond(A)_2=\frac{\max \Lambda}{\min \Lambda}$$其中$\Lambda$代表$A$的所有特征值的集合。

以下为几种条件数特别大的情形：
1. $A$的规模很大
2. $detA$与0的距离很近
3. $A$有两行的值十分接近
4. $A$的元素之间数量级相差过大

$\textbf{Theorem 6.3.4}(事后误差估计)$ 设$A$为可逆阵，$x$为$Ax=b$的精确解，$\bar{x}$为其近似解。那么有：
$$\frac{\lVert x -\bar{x}\rVert}{\lVert x\rVert} \leq cond(A)\,\frac{\lVert  b-A\bar{x}\rVert}{\lVert x\rVert}$$

## 6.4 解线性方程组的迭代法

### 6.4.1 迭代法思路

虽然我们已经得到了相对好用的直接解线性方程的方法，但在实际应用中，面对稀疏矩阵，存在着一些更好的解方程方法——迭代法。对于稀疏矩阵来说，矩阵相乘所需的计算花销是低于矩阵分解后逐行求解的。因此，我们产生了一个问题：能否通过不断自相乘的方式得到线性方程$Ax=b$的解。进一步地，我们提出问题：对于精确解$x^*$所满足的式子$x^*=Bx^*+f$，是否可以利用其将一个初始值$x^{(0)}$经过迭代$x^{(k+1)}=Bx^{(k)}+f$不断逼近精确解？答案是肯定的。记$\varepsilon_k = x_k-x^*$，那么
$$ \lVert\varepsilon_k\rVert \leq B^k \lVert\varepsilon_0\rVert $$此时若$B^k\rightarrow 0$，则可以保证这样的想法得到实现。

### 6.4.2 迭代法的敛散性

$\textbf{Theorem 6.4.1}$ 设$A$为一个实矩阵，$\left\{A^{(k)}\right\}$为一个实矩阵列，则以下命题等价
   1. $$\lim_{k\rightarrow\infty} A^{(k)}=A$$
   2. $$\lVert A^{(k)}-A\rVert_\infty \rightarrow 0$$
   3. 对任一矩阵范数$\lVert A \rVert_t$ $$\lVert A^{(k)}-A\rVert_t \rightarrow 0$$
   4. $$\forall x \in \mathbb{R}^n,\quad A^{(k)}x\rightarrow Ax$$

$\textbf{Theorem 6.4.2}$ 以下命题等价：
   1. $\lim_{k\rightarrow\infty} B^k = 0$
   2. $\rho(B) < 1$
   3. 存在一个算子范数使$\lVert B\rVert < 1$

从而我们可以得到一个**推论**：$x^{(k+1)}=Bx^{(k)}+f$对任一初值$x^{(0)}$收敛的充要条件是$\rho(B)<1$

$\textbf{Theorem 6.4.3}$ 设$x=Bx+f$，且找到满足$\lVert B\rVert = q < 1$的算子范数，则
   1. $x^{(k+1)}=Bx^{(k)}+f$ 在任一初值$x^{(0)}$下均收敛至$x^*$
   2. $\lVert x^{(k)}-x^*\rVert \leq q^k \lVert x^{(0)}-x^*\rVert$
   3. $$\lVert x^{(k)}-x^*\rVert \leq \frac{q}{1-q} \lVert x^{(k)}-x^{(k-1)}\rVert$$
   4. $$\lVert x^{(k)}-x^*\rVert \leq \frac{q^k}{1-q} \lVert x^{(1)}-x^{(0)}\rVert $$

$\textbf{Theorem 6.4.3}$ 对于任一算子范数，
$$\lim_{k\rightarrow\infty} \lVert B^k\rVert^{1/k} = \rho(B)$$

### 6.4.3 收敛速度

已知等式$\epsilon^{(k)}= B^k\epsilon^{(0)}$，一般地，我们希望$\epsilon^{(k)}$尽快趋于0，因而产生了一种评价收敛速度的方式：

收敛速度
: 我们称$R_k=-\ln \lVert B^k\rVert^{1/k}$为平均收敛速度，$R=-\ln\rho(B)$为渐进收敛速度。

这样的式子是由下式推出的：
$$\frac{\lVert\epsilon^{(k)}\rVert}{\lVert\epsilon^{(0)}\rVert} \leq \lVert B^k\rVert < \sigma$$

### 6.4.4 迭代法的设计

如果需要实现这样的迭代法，我们需要设计一些满足$x=Bx+f$的矩阵$B$和向量$f$，使得我们的计算过程具有一些良好的性质。

#### 矩阵分裂法

注意到$A=D-L-U$，其中$D$为$A$的主对角线，$L$为$A$的除主对角线的下三角部分，$U$为$A$的除主对角线的上三角部分。

那么对于$Ax=b$，稍作变换后有
\[x=D^{-1}(L+U)x+D^{-1}b\]这种构造被称为**Jacobi迭代法**
而构造\[x=(D-L)^{-1}Ux+(D-L)^{-1}b\]被称为**Gauss-Seidel迭代法**

可以认为，后者是前者的改进版本。在这里我们不会将它们在实际中的具体迭代公式写出，但会解释这一点。上面二者在实际中采用的迭代步骤分别为：
$$
\begin{align*}
  Dx^{(k+1)} &= (L+U)x^{(k)}+b\\
  Dx^{(k+1)} &= Lx^{(k+1)} + Ux^{(k)} + b
\end{align*}
$$
可以发现，虽然事实上二者做的是同一分解，但后者的每一分量的更新都会利用前面刚刚更新的分量，从而减少所需存储量和计算量。

接下来，我们需要了解其敛散性。

对角占优矩阵
: 若对任一$i=1,2,\ldots,n$，均有\[\left|a_{ii}\right|>\sum_{j\not ={i}}\left|a_{ij}\right|\]则称其为**严格对角占优矩阵**
  若对任一$i=1,2,\ldots,n$，均有\[\left|a_{ii}\right|\geq\sum_{j\not ={i}}\left|a_{ij}\right|\]且至少有一个等式严格成立，那么称其为**弱对角占优矩阵**

可约矩阵
: 对于$A\in \mathbb{R}^{n\times n}$，如果存在置换矩阵$P$使得
  $$P^TAP=\left(\begin{array}{cc}
    A_{11} & A_{12}\\
    0 & A_{22}
  \end{array}\right)$$
  其中$A_{11}$为方阵，那么称$A$为**可约矩阵**。反之则为**不可约矩阵**

$\textbf{Theorem 2.6.4}(对角占优定理)$ 若$A$为严格对角占优矩阵或不可约弱对角占优矩阵，则$Ax=b$存在唯一解，且Jacobi迭代法、Gauss-Seidel迭代法均收敛。

$\textbf{Theorem 2.6.5}$ 设矩阵$A$对称，且主对角元均为正数，则：
  1. Jacobi法收敛的充要条件是$A$和$2D-A$正定。
  2. Gauss-Seidel法收敛的充要条件是$A$正定。

#### 超松弛迭代法(SOR)

考虑将分裂矩阵设置为$M=(D-\omega L)/\omega$，那么有分解
$$A=\frac{1}{\omega}(D-\omega L) + \frac{1}{\omega}[(\omega-1)D-\omega U]$$从而有
$$x = (D-\omega L)^{-1}[(1-\omega)D+\omega U]x+\omega(D-\omega L)^{-1}b$$令
$$
\begin{align*}
  L_\omega &= (D-\omega L)^{-1}[(1-\omega)D+\omega U]\\
  f &= \omega(D-\omega L)^{-1}b 
\end{align*}
$$可见迭代矩阵$B=L_\omega$。当$\omega<1$时，被称为低松弛法；当$\omega>1$时，被称为超松弛法。

实际上，我们的迭代公式都由下面的式子产生：
$$ Dx^{(k+1)} = Dx^{(k)} + \omega \left(b + Lx^{(k+1)} + Ux^{(k)} - Dx^{(k)}\right) $$ 这一方法可被视为是对 Gauss-Seidel迭代法的一种修正。即，当我们迭代至$x^{(k)}$时，首先利用Gauss-Seidel迭代法得到分量 $\hat{x}^{(k+1)}_j$，而后SOR的这一分量将由 $x^{(k+1)}_j = x_j^{(k)} + \omega(\hat{x}^{(k+1)}_j-x_j^{(k)})$ 计算得到。

在下面，我们将讨论敛散性。我们引入SOR的动机是加快迭代法收敛的速度，但这并不代表SOR迭代法内的所有矩阵均能收敛。首先，存在这样的必要条件：

$\textbf{Theorem 2.6.6}$ 若解线性方程组$Ax=b$的SOR迭代法收敛，则$0<\omega<2$

$\textbf{Theorem 2.6.7}$ 设$Ax=b$，若：
1. $A$为正定阵，且$0<\omega<2$，则解$Ax=b$的SOR迭代法收敛。
2. $A$为严格对角占优矩阵或不可约弱对角占优矩阵，且$0<\omega\leq 1$
则解$Ax=b$的SOR迭代法收敛。

由上，我们知道有渐进收敛速度$-\ln\rho B$，因此让SOR收敛最快的$\omega_0$应当满足$\rho(L_{\omega_0}) = \min_{0<\omega<2}\rho(L_\omega)$，那么记$$J=D^{-1}(L+U)$$则让迭代过程最快的$\omega$为
\[\omega_{opt} = \frac{2}{1+\sqrt{1-\rho^2(J)}}\]这样的$\omega$被称为最佳松弛因子公式。

## 6.5 共轭梯度法

### 6.5.1 最速下降法

对于线性方程组$Ax=b$，令$\varphi(x)=\frac{1}{2}(Ax,x)-(b,x)$。当$A$为正定阵的时候，有以下定理：

$\textbf{Theorem 2.7.1}$ $Ax^*=b$当且仅当$\varphi(x^*)=\min\varphi(x)$

从而我们开始考虑构造一个点列$\left\{x_{(k)}\right\}$使得$\lim_{k\rightarrow\infty}\varphi(x_{(k)})=\varphi(x^*)$
不妨找一个方向$p^{(k)}$，让更新法则变为$x^{(k+1)} = x^{(k)} + \alpha_kp^{(k)}$，但为了保证迭代速度，我们需要选取合适的步长与方向。按先优化步长，后优化方向的步骤，可以得到：
$$
\begin{aligned}
  p^{(k)} &= -\nabla \varphi(x^{}) = r^{(k)} := b - Ax^{(k)}\\
  \alpha_k &= \frac{(r^{(k)},r^{(k)})}{(Ar^{(k)},r^{(k)})}
\end{aligned}
$$ 还可以证明，$r^{(k)}$与$r^{(k+1)}$正交，

其收敛速度为
$$\lVert x^{(k)}-x^*\rVert_A \leq \left(\frac{cond(A)_2 - 1}{cond(A)_2 + 1}\right)^k\lVert x^{(0)}-x^*\rVert_A$$ 其中$\lVert u\rVert_A := \sqrt{(Au,u)}$

### 6.5.2 共轭梯度法*

\*待补充*\

# 7 常微分方程


