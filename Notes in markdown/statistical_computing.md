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