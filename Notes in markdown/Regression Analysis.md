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

The assumption from MLR.1 to MLR.6 are called the **Classical Linear Model(CLM)** assumptions.

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

## Dummy Variables

Dummy Variables
:  A dummy variable is a variable that takes on the value 0 or 1 to indicate the absence or presence of some categorical effect that may be expected to shift the outcome.

And the interpretation of the dummy variables is the difference between the group with dummy variable 1 and the group with dummy variable 0. The standard form of regression model with dummy variable is $$y_i = \beta_0 + \beta_1x_{i1} + \beta_2x_{i2} + \ldots + \beta_kx_{ik} + \delta_1d_{i1} + \delta_2d_{i2} + \ldots + \delta_md_{im} + u_i$$ where $d_{ij}$ is the dummy variable for the $j$th group of the $i$th observation.
Given that a category with 2 possible values has only one degree of freedom, we should beware of collinearity. And another cause of collinearity is that category itself may exclude some combinations of other independent variables.

For the hypothesis testing of dummy variables, we can use the t-test. The t-test here makes no difference from the t-test we have learned before.

### Chow test

Chow test is used to test whether the coefficients of two groups are the same. The null hypothesis is $H_0:$ all betas for the associated independent variables are the same across two different groups.
Then we have the statistc $$ F = \frac{(SSE_{pooled} - SSE_{subsamples})/k}{SSE_{subsamples}/(n-2k)} \sim F_{k, n-2k}$$where $k$ is the number of parameters and $n$ is the number of observations. $SSE_{pooled}$ is the sum of squared residuals from the regression model on all data and $SSE_{subsamples}$ is the sum of SSE of the regression model on each subsample. For example, if we have two groups, then we have $SSE_{subsamples} = SSE_1 + SSE_2$, and $SSE_{pooled}$ is the SSE of the regression model on the combination of two groups.

### Dummy interaction variables

The idea in interaction variable is that the slope may related to the dummy variable. For example, we have the model $$y_i = \beta_0 + \beta_1x_i + \beta_2d_i + \beta_3(x_id_i) + u_i$$ where $d_i$ is the dummy variable. And obviously the slope of independent variable $x_i$ is $\beta_1 + \beta_3d_i$. And the $x_id_i$ here is called the interaction variable.

The tests on such model is the same as the tests on the model with normal dummy variables.

# MLR without certain assumptions

## Heteroskedasticity

Heteroskedasticity
:  Heteroskedasticity is a systematic change in the variance of the error term over the range of values of an independent variable or variables. It is a violation of the assumption of homoskedasticity.

### Testing for heteroskedasticity

We can use the **Breusch-Pagan test** to test for heteroskedasticity. The null hypothesis is $H_0: \sigma^2 = \sigma^2(x_1, x_2, \ldots, x_k)$ against $H_1: \sigma^2 \not = \sigma^2(x_1, x_2, \ldots, x_k)$. And we have the test statistic $$LM = nR^2 \sim \chi^2_{k-1}$$where $R^2$ is the $R^2$ from the regression of $u^2$ on $x_1, x_2, \ldots, x_k$. And we have F statistic $$F = \frac{R^2/(k-1)}{(1-R^2)/(n-k)} \sim F_{k-1, n-k}$$ where $k$ is the number of parameters and $n$ is the number of observations.

### Robust standard errors

We can try to use **feasible GLS** to estimate the variance of error term $u$. We assume: $$Var(u|x)=\sigma^2 \exp(\delta_0+\delta_1x_1+\ldots+\delta_kx_k)=\sigma^2h(x)$$ With this assumption, we have $$u^2 = \sigma^2 \exp(\delta_0+\delta_1x_1+\ldots+\delta_kx_k) v$$ where $v$ is a random variable with mean $1$. And we can make a regession on $\log(u^2)$ on $x_1, x_2, \ldots, x_k$ to get the estimate of $\delta_j$.

## Endogeneity

Endogeneity
:  Endogeneity is a situation in which an explanatory variable is correlated with the error term. It is a violation of the assumption of exogeneity.

### Endogeneity problem

The endogeneity problem always occurs when:
1. The dependent variable is determined by a variable that is not included in the model.
2. Variables have stimultaneous relationship.
3. The dependent variable is determined by a variable that is measured with error.
4. The sampling method is biased.

### Instrumental Variables(IV)

Instrumental Variables(IV)
:  An instrumental variable is a variable that is correlated with the endogenous explanatory variable but is uncorrelated with the error term. Namely, we have the conditions below for an IV $z$:
   1. $Cov(z, x) \not = 0$
   2. $Cov(z, u) = 0$
   3. The IV does not appear in the regression equation.
We can see that the features of IV above satisfy the features of the independent variables in the regression model. So we can use IV to solve the endogeneity problem by switch the endogenous variable with the IV.

### Two-stage least squares(2SLS)

2SLS is a critical method to solve the endogeneity problem. The idea is to use the IV to replace the endogenous variable in the regression model. And we have the following steps:
1. Regress the endogenous variable on the IV and other independent variables to get the fitted value $\hat{x}$.
2. Replace the endogenous variable with the fitted value $\hat{x}$ in the regression model.
3. Use OLS to estimate the parameters of the regression model with replaced endogenous variable.

### Tests for endogeneity

In the anlysis above, we have the questions below:
1. Whether the replaced variable is endogeneous.
2. Whether the IVs are exogeneous.
3. Whether the IVs are relevant to the endogenous variable.

Then we have the following tests:

#### Testing for endogeneity

We tend to use the **Hausman test** to test for endogeneity. The null hypothesis is $H_0: Cov(x, u) = 0$ against $H_1: Cov(x, u) \not = 0$. Considering in 2SLS, we can obtain the inner residual 