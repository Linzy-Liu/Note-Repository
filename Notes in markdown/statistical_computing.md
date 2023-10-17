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

## 2.3 舍选抽样法

> $\mathbf{Theorem 2.1}$ 设随机向量$\xi\in\mathbb{R}^n$在平行多面体$R:\,a_i\leq x_i\leq b_i\quad(i=1,2,\ldots,n)$上取值，联合密度函数$f(x)$存在上界$$f_0=\sup_{\xi\in R}f(x)<\infin$$那么按以下步骤产生随机数：
> 1. 产生随机数$U_0,U_1,\ldots,U_n\mathop{\sim}\limits^{iid}U(0,1)$
> 2. 若$U_0,U_1,\ldots,U_n$满足$U_0f_0\leq f((b_1-a_1)U_1+a_1,\ldots,(b_n-a_n)U_n+a_n)$，则令$\xi_i=(b_i-a_i)U_i+a_i,\quad(i=1,2,\ldots,n)$
> 则由此产生的随机向量$\xi$的联合密度函数为$f(x)$

## 2.4 离散随机向量随机数的抽样法

### 条件分布法

> $\mathbf{Theorem 2.2}$ 设随机向量$\xi=(\xi_1,\xi_2,\ldots,\xi_n)^T$的联合分布列为$$P(\xi_1=x_1,\xi_2=x_2,\ldots,\xi_n=x_n)=p(x_1,x_2,\ldots,x_n)$$那么，若$p(x_1,x_2,\ldots,x_n)$可分解为多个条件分布的乘积：$$p(x_1,x_2,\ldots,x_n)=p_1(x_1)p_2(x_2|x_1)\cdots p_n(x_n|x_1,x_2,\ldots,x_{n-1})$$那么，我们可以按照如下步骤产生随机数：
> 1. 产生$x_1\sim p_1(x_1)$
> 2. 给定$\xi_1=x_1$，产生$x_2\sim p_2(x_2|\xi_1=x_1)$
> 3. 以此类推，直到给定$(\xi_1,\xi_2,\ldots,\xi_{n-1})=(x_1,x_2,\ldots,x_{n-1})$，产生$x_n\sim p_n(x_n|\xi_1=x_1,\xi_2=x_2,\ldots,\xi_{n-1}=x_{n-1})$

一般而言，离散随机变量会给出各个条件分布。

# 3 参数估计的数值计算

在本一节，我们并不是对于一个完全未知的分布求它的某些统计量，而是对于一个已知的分布，验证某种求统计量的方法的有效性和正确性。比如，我们对于$X\sim N(0,1)$，我们采用$\bar{X}$来估计$\mu$，那么我们可以通过模拟的方法来验证这一估计的有效性。

## 3.1 点估计

在这一节，我们将会模拟：
1. 计算点估计的的期望是否接近真实值
2. 计算点估计的方差
3. 计算点估计的其他数字特征

### 3.1.1 期望与方差

我们在这一节中，面对着这样的一个问题：
> 对于随机变量$X$，存在一个统计量$\theta$，我们想要获取这一个统计量的期望与方差，但是我们无法直接计算，那么我们可以通过模拟的方法来计算这一统计量的期望与方差吗？

在这里，我们可以采取一个朴素而简单的方法：我们可以通过模拟随机变量$X$的$K$个样本，而后计算这一统计量的估计值$\hat{\theta}_1$，而后重复这一过程$N$次，得到$\hat{\theta}_1,\hat{\theta}_2,\ldots,\hat{\theta}_N$，最后便可以计算这一统计量的期望与方差的估计值。
$$
\begin{align*}
\mathbb{E}(\hat{\theta}) &\approx \frac{1}{N}\sum_{i=1}^N \hat{\theta}_i\\
Var(\hat{\theta}) &\approx \frac{1}{N-1}\sum_{i=1}^N (\hat{\theta}_i - \mathbb{E}(\hat{\theta}))^2
\end{align*}
$$

注意到，$\mathbb{E}(\hat{\theta})$事实上是$NK$个独立同分布的随机变量的均值，因而比如当$X\sim N(\mu,\sigma^2)$时，便可以计算得其理论方差为$\sigma^2/(NK)$

## 3.2 区间估计

在区间估计中，我们往往关心：置信度、区间长度等指标。

在此，我们的想法和上面一样，对于每次估计，抽取$K$个样本，从而根据给定的计算方法算得置信区间的下界$\hat{\theta}_L$与上界$\hat{\theta}_U$，这往往会在我们将要评估的方法中给出。
这样，我们就可以在$N$次重复实验中找到$N$个置信区间。那么最后数值计算的置信度(覆盖率)为：$$\widehat{Prob} = \frac{1}{N}\sum_{i=1}^N \chi_{[\hat{\theta}_L^{(i)}, \hat{\theta}_U^{(i)}]}(\theta)$$ 而置信区间(用于估计区间长度)为：$$\left[\frac{1}{N}\sum_{i=1}^N\hat{\theta}_L^{(i)}, \frac{1}{N}\sum_{i=1}^N\hat{\theta}_U^{(i)}\right]$$

# 4 假设检验数值计算

Type I error: 弃真
Type II error: 取伪
在这里，我们的目标是，在将第一类错误的水平$\alpha$控制在一定水平上时，尽量减少第二类错误$\beta$的概率。因此，在数值计算时，我们关心在控制$\alpha$的前提下，$1-\beta$有多靠近1。

那么根据$1-\beta = \mathbb{P}(X\in C|H_1)$(其中$C$为拒绝域)，我们可以通过模拟的方法来计算$1-\beta$。事实上，$\alpha$的计算同理。

## 4.1 参数检验

### 单总体

1. $H_0:\mu=\mu_0$ vs $H_1:\mu\neq\mu_0$
   1. $X\sim N(\mu,\sigma^2)$，$\sigma^2$已知
   2. $X\sim N(\mu,\sigma^2)$，$\sigma^2$未知
2. $H_0:\sigma^2=\sigma_0^2$ vs $H_1:\sigma^2\neq\sigma_0^2$
   1. $X\sim N(\mu,\sigma^2)$，$\mu$已知
   2. $X\sim N(\mu,\sigma^2)$，$\mu$未知

### 双总体

1. $H_0:\mu_1=\mu_2$ vs $H_1:\mu_1\neq\mu_2$
   1. $X_1\sim N(\mu_1,\sigma_1^2)$，$X_2\sim N(\mu_2,\sigma_2^2)$，$\sigma_1^2=\sigma_2^2$已知
   2. $X_1\sim N(\mu_1,\sigma_1^2)$，$X_2\sim N(\mu_2,\sigma_2^2)$，$\sigma_1^2=\sigma_2^2$未知
2. $H_0:\sigma_1^2=\sigma_2^2$ vs $H_1:\sigma_1^2\neq\sigma_2^2$
   1. $X_1\sim N(\mu_1,\sigma_1^2)$，$X_2\sim N(\mu_2,\sigma_2^2)$，$\mu_1,\mu_2$已知
   2. $X_1\sim N(\mu_1,\sigma_1^2)$，$X_2\sim N(\mu_2,\sigma_2^2)$，$\mu_1,\mu_2$未知

### 4.1.1 估计功效的数值计算

计算一类错误时：由$\alpha = \mathbb{P}(X\in C|H_0)$，可知：
1. 从$H_0$中产生$N$个样本
2. 计算统计量$T(x_1,x_2,\ldots,x_N)$的值，而后计算拒绝域$C$，得到$C_1$
3. 重复生成样本、计算统计量$K$次，那么就可以计算得到$\alpha$的估计值为：$$\hat{\alpha} = \frac{1}{K}\sum_{i=1}^K \chi_{C_1}(T^{(i)})$$

而对于功效，由于其表达式为：$1-\beta = \mathbb{P}(X\in C|H_1)$，只需考虑将样本从$H_1$中产生即可，其余步骤从上面的第2步开始。（此处的拒绝域$C$应当是在$H_0$下的拒绝域）

## 4.2 单样本的拟合优度检验

### 4.2.1 Pearson $\chi^2$检验

在这里，我们考虑的是，对于一个已知的分布$F(x)$，我们想要检验样本是否来自这一分布。那么我们的假设为：$H_0: F(x) = F_0(x)$ vs $H_1: F(x) \neq F_0(x)$
而后使用Pearson统计量：$$\chi^2 = \sum_{i=1}^k \frac{(n_i - np_i)^2}{np_i}$$ 这一统计量服从于$\chi^2(k-1)$的分布，其中$k$为分组数，$n_i$为第$i$组的样本数，$np_i$为第$i$组的理论概率。
对于分组的方案，我们有两种选择：
1. 等距分组：$[a, a+h), [a+h, a+2h), \ldots, [a+(k-1)h, a+kh)$
2. 等频分组：$[a, a_1), [a_1, a_2), \ldots, [a_{k-1}, a_k)$

### 4.2.2 Kolmogorov-Smirnov检验(K-S检验)

在此处，我们考虑的是，对于一个已知的分布$F(x)$，我们想要检验样本是否来自这一分布。那么我们的假设为：$H_0: F(x) = F_0(x)$ vs $H_1: F(x) \neq F_0(x)$。假设我们从获得了$N$个独立观测样本$X_1,X_2,\ldots,X_N$，那么就会有
经验分布函数$F_n(X)$。K-S统计量的思想是，我们将$F_n(X)$与$F_0(X)$的差值的绝对值的最大值作为统计量，即$$D_n = \sup_{i=1,2,\ldots,N}\lvert F_n(X_i) - F_0(X_i)\rvert$$
这一差值服从于Kolmogorov分布，即$$\mathbb{P}(D_n \leq x) = 1 - 2\sum_{k=1}^{+\infin}(-1)^{k-1} e^{-2nk^2x^2}, x\in(0,+\infty)$$

