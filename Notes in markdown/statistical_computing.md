# 目录


# Chapter1 一维非均匀随机数的产生

随机数
: 设$\mathit{X}$为具有分布函数$F(x)$的随机变量，从分布$F(x)$中随机抽样得到的序列$\{x_i\}_{i\in\mathbb{N}}$被称为该分布的**随机数**

## 1.1 逆变换抽样法

> $\mathbf{Theorem 1.1}$ 设连续型r.v. $\eta$的分布函数$F(x)$是连续且严格单增的分布函数，其记反函数为$F^{-1}(x)$，则：
> 1. 随机变量$F(\eta)$满足：$F(\eta)\sim U(0, 1)$
> 2. 对于$U\sim U(0,1)$，$F^{-1}(U)$的分布函数为$F(x)$

注：证明方法为By definition

> $\mathbf{Corollary}$ 已知连续型r.v. $\xi \sim G(x)$，若$\xi$的cdf $F(x)$的反函数存在，则r.v. $(F^{-1}\circ G)(\xi) \sim F(x)$

逆变换抽样法缺点：这一方法是为数值计算而生的，故计算时应当力求快捷、简便（指应用中动不动就是`stats.uniform.rv(0,1,size=1000)`）。而在cdf $F(x)$的逆变换非初等的情况下，这一方法的计算开销是比较大的。

## 1.2 舍选抽样法

> $\mathbf{Theorem 1.2}$ 设$f,g$分别为pdf，$h$为任意函数。若按以下步骤生成随机数：
> 1. 按$f(x)$生成$\mathit{X}$，按$g(x)$生成$\mathit{Y}$
> 2. 当$\mathit{X},\mathit{Y}$满足$Y \leq h(X)$时，令$\eta = \mathit{X}$且输出$\eta$，否则回到上一步
> 
> 那么记r.v.$\mathit{Y}$的分布函数为$G(x)$，则$\eta$的pdf为：
> $$p(z) = \frac{f(z)(G\circ h)(z)}{\int_{-\infin}^{+\infin}f(x)(G\circ h)(x)\, dx}$$


> $\mathbf{Corollary}$ 设r.v. $\eta$的pdf为$p(z) \leq M(z)$，且$M(z)$在$\mathbb{R}$上的积分有界，为$C$，那么：令$f(x) = M(x)/C$且$g(x)$为$U(0,1)$的pdf，若按以下步骤生成r.v. $\eta$：
> 1. 按$f(x)$生成$\mathit{X}$，按$g(x)$生成$\mathit{Y}$
> 2. 直到$\mathit{X},\mathit{Y}$满足$Y \leq p(\mathit{X})/M(\mathit{X})$，那么令$\eta=\mathit{X}$
> 
> 则$\eta$的pdf为$p(z)$

> $\mathbf{Corollary}$ 设$\eta$在有限区间$I=(a,b)$上取值，具有密度函数$p(z)$满足$\sup_{z\in I} p(z) = M < \infin$，那么若按以下步骤进行：
> 1. 独立生成$\textit{X}\sim U(a,b)$与$Y\sim U(0,1)$
> 2. 直到$\textit{X}$，$\textit{Y}$满足$\textit{Y}\leq p(\textit{X})/M$时，令$\eta = \textit{X}$
> 
> 则$\eta$的pdf为$p(z)$

> $\mathbf{Corollary}$ 设随机变量$\eta$的概率密度$p(z)$可表为如下形式：$$p(z) = Lh(z)f(z)$$其中$L > 1$，$h(z) \in [0,1]$，$f(z)$为概率密度函数，那么：
> 1. 独立生成$\textit{X}\sim f(x)$与$Y\sim U(0,1)$
> 2. 直到$\mathit{X},\mathit{Y}$满足$Y \leq h(\mathit{X})$，那么令$\eta=\mathit{X}$
> 
> 则$\eta$的pdf为$p(z)$

## 1.3 变换抽样法

> $\mathbf{Theorem 1.3}$ 设随机变量$\xi$具有pdf $f(x)$，另有一函数$h(z)$严格单调，其反函数$h^{-1}$存在且可导，则$\eta = h(\xi)$的pdf为
> $$p(z)=f(h^{-1}(z))\left|\frac{d\,h^{-1}(z)}{dz}\right|$$

多元联合分布控制的随机变量同理，主打一个推导。

## 1.4 复合抽样法

该方法主要适用于所求分布的分布函数（或概率密度函数）可以用 个已知分布函数（或概率密度函数）的线性组合表示的情形。

我们在此将其表述为：
> 设随机变量$\eta$的分布函数和概率密度函数分别为$F(x)$，$f(x)$并且可以写成$$F(x) = \sum p_iF_i(x)$$或者$$f(x)=\sum p_if_i(x)$$
> 其中，$\sum p_i = 1$，那么在复合抽样法中，我们可以考虑按下面的步骤生成随机数：
> 1. 产生随机数$U\sim U(0,1)$，必然存在$J$，使得$U \in \left[\sum_{j=1}^{J-1}p_j, \sum_{j=1}^Jp_j\right)$
> 2. 根据$F_J$或$f_J$产生随机数

* 上面的方法可用全概率公式证明

## 1.5 近似抽样法

最简单地，可以根据*Levy-Lindenberg*中心极限定理，我们可以近似地通过任意分布的独立随机数生成标准正态分布的随机数，即通过：
$$\frac{\sum_{i=1}^n (X_i-\mu_i)}{\sqrt{\sum_{i=1}^n Var(X_i)}}$$来计算

### 对pdf近似进行抽样

想法为：将原pdf $f(x)$分解为：$$f(x)=\sum_{i=1}^n p_i f_i(x)$$其中，$f_i(x)$为已知的pdf，$p_i$为系数，且$\sum_{i=1}^n p_i = 1$。而后这样的pdf $f(x)$可以通过复合抽样法进行抽样。

在实践中，这一想法的具体实现就是Butler抽样法，其想法为：
1. 将pdf $f(x)$ 按面积分为$m$段（对无穷区间可能需要截断），即对于$m$段中的每一个$[x_{i-1}, x_i]$，$F(x_i) - F(x_{i-1}) = 1/m$，$i=1,\ldots,m$
2. 令$$f_i(x)=mf(x)\chi_{(x_{i-1}, x_i]}(x)$$，$p_i = 1/m$，$i=1,2,\ldots,m$
3. 对每一个$f_i(x)$，产生一个线性近似$\tilde{f}(x)$，并重新归一化，使其在$\mathbb{R}$上的积分为1。
4. 寻找一个简易的生成直线pdf的方法，此处将使用逆变换、变换、复合抽样法。

那么Butler抽样法的具体步骤为：
假定切割得到了$m$个小区间$\{(x_{j-1}, x_j]\}_{j=1}^n$
1. 产生 $R \sim U(0, 1)$ ，令$k = [mR+1]$;
2. 按如下规则产生随机数$\eta$:
   1. 产生$U_1, U_2\mathop{\sim}\limits^{iid} U(0,1)$
   2. 当$U_2 \leq d_k := \lvert f(x_k)-f(x_{k-1})\rvert(f(x_k)-f(x_{k-1}))^{-1}$时，取$$\eta = \left\{ \begin{aligned}
    x_{k-1} + (x_k-x_{k-1})\sqrt{U_1}, & \quad \text{if } f(x_k) > f(x_{k-1}) \\
    x_k + (x_{k-1}-x_k)\sqrt{1-U_1}, & \quad \text{if } f(x_k) < f(x_{k-1})
   \end{aligned}
   \right.$$当$U_2 > d_k$时，令$$\eta=x_{k-1} + (x_k-x_{k-1})U_1$$
   
这样的随机数近似服从$f(x)$的分布。

### 对cdf近似进行抽样

此处同理，甚至由于逆变换抽样法的存在，此处的形式避免了多余的计算，使得其形式更为简单。

其详细步骤为：
1. 将计算区间分割为$m$个小区间$\{(x_k,x_{k+1}]\}_{k=0}^n$，而后将原函数分解为：$$F(x)=\sum_{i=1}^n p_iF_i(x)$$ 其中：$$p_k = F(x_k) - F(x_{k-1})$$ $$ F_k(x) = \left\{ 
   \begin{aligned}
   0 &, \text{if } x \leq x_{k-1}\\
   \frac{F(x) - F(x_{k-1})}{p_k} &, \text{if } x_{k-1} < x \leq x_k\\
   1 &, \text{if } x > x_k
   \end{aligned}\right.$$
2. 生成均匀分布随机数$U_1, U_2 \mathop{\sim}\limits^{iid} U(0,1)$, 找到$k$使$U_1 \in [\sum_{i=1}^{k-1} p_i, \sum_{i=1}^k p_i)$
3. 令$$\eta = x_{k-1} + (x_k - x_{k-1})U_2$$

这样的随机数近似服从$F(x)$

### 对经验分布近似进行抽样

在这里，对于不同的经验分布形式，我们又有不同的方法。
首先讨论观测点$\{x_k\}_{k=0}^n$已知的情况。那么此时经验函数将会呈现出在每一个新的观测点上升一个固定值的特征，于是沿用前面的想法，有：
1. 产生随机数$U_1, U_2 \mathop{\sim}\limits^{iid} U(0,1)$
2. 寻找使得$U_1 \in [F(x_{k-1}), F(x_k))$的$k$，而后令$$\eta = x_{k-1} + (x_k - x_{k-1})U_2$$

而后，可以尝试讨论观测区间内的频数已知的情况：假定观测区间列为$\{[a_k, a_{k+1}]\}_{k=0}^{n-1}$
1. 产生随机数$U \sim U(0,1)$
2. 寻找$k$使得$F(x_{k-1}) < U < F(x_k)$， 而后令$$\eta = \frac{U - F(x_{k-1})}{F(x_k) - F(x_{k-1})}(x_k - x_{k-1}) + x_{k-1}$$

## 1.6 离散随机数的产生

在此仅仅阐述逆变换抽样法。这一方法如下：假定随机变量的全部可能取值为$\{x_i\}$，记$F(x) = \mathbb{P}(\eta \leq x)$，那么按照如下步骤产生随机数：
1. 产生$U\sim U(0,1)$
2. 寻找使得$U \in [F(x_{i-1}), F(x_i))$的$i$，而后令$\eta = x_i$。若$U \in [0, F(x_0))$，则令$\eta = x_0$

# 2. 随机向量随机数的抽样法

## 2.1 变换抽样法

> $\mathbf{Theorem 2.1}$ 设随机向量$\mathbf{X} = (X_1, X_2, \ldots, X_n)^T$的概率密度为$f(x_1, x_2, \ldots, x_n)$，而变换$\mathbf{Y} = (Y_1, Y_2, \ldots, Y_n)^T = \mathbf{h}(\mathbf{X})$，其中$\mathbf{h}(\mathbf{x}) = (h_1(\mathbf{x}), h_2(\mathbf{x}), \ldots, h_n(\mathbf{x}))^T$，且$\mathbf{h}(\mathbf{x})$的雅可比行列式$J(\mathbf{x})$在$\mathbb{R}^n$上处处非零，则$\mathbf{Y}$的概率密度为 $$g(y_1, y_2, \ldots, y_n) = f(\mathbf{h}^{-1}(\mathbf{y}))\lvert J(\mathbf{h}^{-1}(\mathbf{y}))\rvert$$

## 2.2 条件分布法

假设联合密度函数$f(x_1,x_2,\ldots,x_n)$可分解为多个分布的乘积：$$f(x_1,x_2,\ldots,x_n) = f_1(x_1)f_2(x_2|x_1)\cdots f_n(x_n|x_1,x_2,\ldots, x_{n-1})$$那么，我们可以按照如下步骤产生随机数：
1. 产生$x_1 \sim f_1(x_1)$
2. 给定$\xi_1=x_1$，产生$X_2 \sim f_2(x_2|\xi_1=x_1)$
3. 以此类推，直到给定$(\xi_1,\xi_2,\ldots,\xi_{n-1}) = (x_1,x_2,\ldots,x_{n-1})$， 产生$x_n \sim f_n(x_n|\xi_1=x_1,\xi_2=x_2,\ldots,\xi_{n-1}=x_{n-1})$

由此可见，这个方法需要可计算的各类边缘分布。