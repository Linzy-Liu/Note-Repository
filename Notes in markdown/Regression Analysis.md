本笔记仅用于简要记录，并不会阐述idea

# Premiliar

## DataSets

1. Cross-Sectional data
2. Time-series data
3. Pooled cross-sectional data
4. Panel data

Copied from ChatGPT:
> * Cross-sectional data is like taking a photograph of a group of people at a party at a specific moment. You get a single snapshot of everyone present at that instant.
> * Pooled cross-sectional data is like taking photographs of groups of people at multiple parties on different days. When you look at all the photos together, you see different people across the different days.
> * Panel data (to add another dimension) would be like taking photos of the same group of people at different times. You see how each person changes or evolves over time.

# MLR(Multiple Linear Regression)

It has a standard shape as \[y = \beta_0+\beta_1x_1+\beta_2x_2+\ldots + \beta_kx_k + u\] where $y$ is dependent variable, $x_i$ are independent variables, and $u$ denotes error terms, disturbance, unobservables, etc.
And it can be written in the form of $$\textit{Y}=\textit{X}\beta + u$$

**Attention**: The *Linear* in its name implies that this model is an affine mapping of the parameters.

With OLS (Ordinary Least Square) algorithm, we have the estimation of the parameters: $\hat{\beta} = (X^TX)^{-1}X^TY$

## Evaluation of the model

* Total Sum of the Squares $SST = \sum (y_i - \bar{y})^2$
* Explained Sum of Squares $SSE = \sum (\hat{y}_i - \bar{y})^2$
* Residual Sum of Squares $SSR = \sum (y_i - \hat{y}_i)^2$

And we define $R^2 = SSE/SST$. The $R^2$ could be compared if and only if:
1. the depedent variable is the same for different models
2.  the independent variables in one model have to be all included in another model

## The assumptions of MLR

**MLR.1** Linear in parameters
**MLR.2** Random sampling
**MLR.3** No perfect collinearity
* The collinearity could be measured by Variance Inflation Factor(VIF), which could be calculated by $VIF_j=\frac{1}{1-R_j^2}$


**MLR.4** Zero conditional mean (The value of the explanatory variables must contain no information about the mean of the unobserved factors)
* **Theorem**(Unbiasedness of OLS) If MLR.1-MLR.4 holds, then $\mathbb{E}(\hat{\beta}_j)=\beta_j$

**MLR.5** Homoskedasticity. That is to say, $Var(u_i|x_i) = \sigma^2$, where $\sigma$ is a constant.

Assumptions MLR.1 through MLR.5 are collectively called **Gauss-Markov assumptions**

***Theorem*** Under assumptions MLR.1 through MLR.5, conditional on the sample values of the independent variables, $$Var(\hat{\beta}_j) = \frac{\sigma^2}{SST_j(1-R_j^2)}$$where $SST_j$ is the total sample variation $SST_j=\sum_{i=1}^n(x_{ij}-\bar{x}_j)^2$ 

And we could estimate $\sigma^2$ by $\hat{\sigma}^2=\left(\sum_{i=1}^n\hat{u}_i^2\right)/df$，where $df$ denotes degrees of freedom. $df$ can be calculated by *(number of observations) - (number of estimated parameters) - 1*

***Theorem*** Under the **Gauss-Markov assumptions**, $\mathbb{E}(\hat{\sigma}^2)=\sigma^2$

***Theorem***(Gauss-Markov Theorem) Under the Gauss-Markov assumption, the OLS estimators are the best linear unbiased estimators of the regression coefficients. Namely, $$Var(\hat{\beta}_j)\leq Var(\tilde{\beta}_j)$$ for all $\tilde{\beta}_j=\sum_{i=1}^n w_{ij}y_i$ for which $\mathbb{E}(\tilde{\beta}_j) = \beta_j$

**MLR.6** Normality of errors. That is to say, $u_i \sim N(0,\sigma^2)$
> Under normality, OLS is the best (even nonlinear) unbiased estimator. This is ensured by the maximum likelihood property of OLS.

In practice, we ensure the assumption by the Central Limit Theorem.
**Corrollary** Under MLR.1-MLR.6, we have: $$\hat{\beta}_j \sim N(\beta_j, Var(\hat{\beta}_j))$$which is equivalent to $$ \frac{\hat{\beta}_j - \beta_j}{\sigma(\hat{\beta}_j)} \sim N(0,1)$$

## Hypothesis testing

Here we have two main types of hypothesis testing: **t-test** and **F-test**. ~~There is nothing different from the statistics we have learned before but the specific variables we are testing.~~

### F-test

For the **F-test**, we have null hypothesis $H_0: R^2=0$ against $H_1: R^2 \not ={0}$. And we have the test statistic $$F=\frac{SSE/k}{SSR/(n-k-1)}$$ which follows the F-distribution with $k$ and $n-k-1$ degrees of freedom. To remember this, we can receive the concept in the following way: given that $k$ is the number of independent variables, the model could explain $k$ obersevations at most, and the rest $n-k-1$ observations are explained by the residuals.

And here we have the rejection region: $$F>F_{k,n-k-1}(\alpha)$$ We can also use the p-value to test the hypothesis. The p-value is the probability of observing a test statistic at least as extreme as the one computed from the sample data, assuming that the null hypothesis is true. And we reject the null hypothesis if the p-value is less than the significance level $\alpha$.

### t-test

For the **t-test**, we have null hypothesis $H_0: \beta_j=0$ against $H_1: \beta_j \not ={0}$. And we have the test statistic $$t=\frac{\hat{\beta}_j}{\sigma(\hat{\beta}_j)}$$ which follows the t-distribution with $n-k-1$ degrees of freedom. Here we compute $\sigma(\hat{\beta}_j)$ by $\sqrt{Var(\hat{\beta}_j)}$. And here we have the rejection region: $$|t|>t_{n-k-1}(\alpha/2)$$ where we want two-side test($H_1: \beta_j \not ={0}$) and $$ t>t_{n-k-1}(\alpha)$$ where we want one-side test($H_1: \beta_j > 0$ here).

Some constants if the size of dataset is big enough:

| significance | $\lvert t\rvert > t_{val}$ |
| :----------: | :------------: |
|     0.1      |      1.645     |
|     0.05     |      1.96      |
|     0.01     |      2.576     |

## Complex hypothesis testing

### Testing linear combinations of parameters

For hypothesis like $H_0: \beta_j = a_j$ against $H_1: \beta_j \not = a_j$, we can use the t-test. And we have the test statistic $$t=\frac{\hat{\beta}_j-a_j}{\sigma(\hat{\beta}_j)}$$

For hypothesis testing like $H_0: \beta_1 = \beta_2$ against $H_1: \beta_1 \not = \beta_2$, we can use the t-test. And we have the test statistic $$t=\frac{\hat{\beta}_1-\hat{\beta}_2}{\sqrt{Var(\hat{\beta}_1-\hat{\beta}_2)}}$$

Here we neglect the degrees of freedom by increasing the size of dataset.

### Testing restrictions on multiple parameters

For hypothesis like $H_0: \beta_j = 0, j\in I_{restrict}$ against hypothesis $H_1: H_0 \text{ is false}$ where $k$ is a positive integer, we can use the F-test, where $I_{restrict} \subset \mathbb{N}$. Suppose the cardinal number of $I_{restrict}$ is $q$, then we have the test statistic $$F=\frac{(SSR_r-SSR_{ur})/q}{SSR_{ur}/(n - k - 1)} \sim F_{q, n-k-1}$$where $SSR_r$ is the sum of squared residuals from the restricted model and $SSR_{ur}$ is the sum of squared residuals from the unrestricted model.The restricted model is defined by the model with restriction that $\beta_j = 0$ for $j \in I_{restrict}$. 
