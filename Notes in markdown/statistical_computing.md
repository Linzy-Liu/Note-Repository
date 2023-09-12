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