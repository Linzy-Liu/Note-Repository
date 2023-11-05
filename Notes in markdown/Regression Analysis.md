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

And we could estimate $\sigma^2$ by $\hat{\sigma}^2=\left(\sum_{i=1}^n\hat{u}_i^2\right)/df$，where $df$ denotes degrees of freedom. $df$ can be calculated by *(number of observations) - (number of estimated parameters)*

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

For hypothesis like $H_0: \beta_j = 0, j\in I_{restrict}$ against hypothesis $H_1: H_0 \text{ is false}$ we can use the F-test, where $I_{restrict} \subset \mathbb{N}$. Suppose the cardinal number of $I_{restrict}$ is $q$, and $k$ is the number of parameters, then we have the test statistic $$F=\frac{(SSR_r-SSR_{ur})/q}{SSR_{ur}/(n - k)} \sim F_{q, n-k}$$where $SSR_r$ is the sum of squared residuals from the restricted model and $SSR_{ur}$ is the sum of squared residuals from the unrestricted model.The restricted model is defined by the model with restriction that $\beta_j = 0$ for $j \in I_{restrict}$. 

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

We can use the **Breusch-Pagan test** to test for heteroskedasticity. The null hypothesis is $H_0: \sigma^2 = \sigma^2(x_1, x_2, \ldots, x_k)$ against $H_1: \sigma^2 \not = \sigma^2(x_1, x_2, \ldots, x_k)$. And we have the test statistic $$LM = nR^2 \sim \chi^2_{k-1}$$where $R^2$ is the $R^2$ from the regression of $u^2$ on $x_1, x_2, \ldots, x_k$. 

And we could also test the joint significance of the parameters of the regression of $u^2$ on $x_1, x_2, \ldots, x_k$. Suppose the original regression has been conducted, then we will obtain $\hat{u}_i$s. We will have $$\hat{u}^2 = \delta_0 + \delta_1x_1 + \ldots + \delta_kx_k + v$$ where $v$ is a random variable with mean $0$. And we can use F statistic to test the joint significance of $\delta_j$s. That is $$F = \frac{R^2/(k-1)}{(1-R^2)/(n-k)} \sim F_{k-1, n-k}$$ where $k$ is the number of parameters and $n$ is the number of observations.

Or **White test** could be used. That is, we regress $\hat{u}_i^2$ on $\hat{y}$ and $\hat{y}^2$ : $$ \hat{u}_i^2 = \delta_0 + \delta_1\hat{y}_i + \delta_2\hat{y}_i^2 + v_i$$and test the joint significance of the parameters $\delta_1$ and $\delta_2$. It is worth noting that the Breusch-Pagen statistic $LM = nR^2 \sim \chi^2_2$ is the same as the statistic in White test.

### Robust standard errors

We can try to use **Feasible GLS**(FGLS in short) to estimate the variance of error term $u$. We assume: $$Var(u|x)=\sigma^2 \exp(\delta_0+\delta_1x_1+\ldots+\delta_kx_k)=\sigma^2h(x)$$ With this assumption, we have $$u^2 = \sigma^2 \exp(\delta_0+\delta_1x_1+\ldots+\delta_kx_k) v$$ where $v$ is a random variable with mean $1$. And we can make a regession on $\log(u^2)$ on $x_1, x_2, \ldots, x_k$ to get the estimate of $\delta_j$.

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

We tend to use the **Hausman test** to test for endogeneity. The null hypothesis is $H_0: Cov(x, u) = 0$ against $H_1: Cov(x, u) \not = 0$. In fact, we are testing whether the efficient of 2SLS and OLS has significant difference on endogeneous variable. We write it in formula as below:
Suppose the formula in two steps are :
$$\begin{aligned}
\text{Step 1: } & x_i = \pi_0 + \pi_1z_i + \pi_2x_{i2} + \ldots + \pi_kx_{ik} + v_i \\
\text{Step 2: } & y_i = \beta_0 + \beta_1\hat{x}_i + \beta_2x_{i2} + \ldots + \beta_kx_{ik} + u_i
\end{aligned}$$
Then we just need to regress the formula below:
$$y_i = \beta_0 + \beta_1x_i + \beta_2x_{i2} + \ldots + \beta_kx_{ik} + \delta \hat{v}_i + e_i$$
The Hausman test here is equivalent to test whether $\delta = 0$.

#### Testing for IV relevance

In such case, we just need to exam the coefficient of IVs on the reduced form of 2SLS regression. If the coefficient is significant, then the IVs are relevant to the endogeneous variable. The "reduced form" here means the equation below:
$$x_i = \pi_0 + \pi_1z_{i1} + \pi_1z_{i2} + \ldots + \pi_1z_{im} + \pi_2x_{1} + \ldots + \pi_kx_{i-1} + v_i$$ where $z_{ij}$ is the $j$th IV.

#### Testing for IV exogeneity

The idea is that, if all instruments are exogenous, the 2SLS residuals should be uncorrelated with the instruments, up to sampling error. Then we have the following overifdentification test, which is usually called **Sargan test**.

**Testing Overidentifying restrictions**
1.  Estimate the structural equation by 2SLS and obtain the 2SLS residuals, $\hat{u}$.
2.  Regress $\hat{u}$ on all exogenous variables(Including IVs and exogenous variables in the equation). Obtain the R-squared, say, $R^2$.
3. Under the null hypothesis that all IVs are uncorrelated with $u$, $nR^2 \sim \chi^2(q)$, where $q$ is the number of IVs minus the total number of endogenous explanatory variables, and $n$ stands for the number of samples. If $nR^2$ exceeds (say) the 5% critical value in the $\chi^2(q)$ distribution, we reject $H_0$ and conclude that at least some of the IVs are not exogenous.

# Time Series

We can know that the time series data has the following features:
1. Temporal ordering.
2. Dependence on past values.(Serial correlation)
3. Randomness.

And we have the following models for time series data:
1. **Static models**: $y_t = \beta_0 + \beta_1x_{1t} + \beta_2x_{2t} + \ldots + \beta_kx_{kt} + u_t$
2. **Finite distributed lag model**: $y_t = \beta_0 + \beta_1x_t + \delta_1x_{t-1} + \delta_2x_{t-2} + \ldots + \delta_kx_{t-k} + u_t$

## TS Assumptions

**TS.1** Linear in parameters
**TS.2** No perfect collinearity
**TS.3** Zero conditional mean
   * (Comtemporaneous) Exogeneity: $\mathbb{E}(x_t|u_t)=0$, the mean of the error term is unrelated to the explanatory variables of the same period.
   * Strict exogeneity: $\mathbb{E}(u_t|x_1, x_2, \ldots, x_t) = 0$, the mean of the error term is unrelated to the explanatory variables of all periods.

**TS.4** Homoskedasticity. That is to say, $Var(u_t|x_1, x_2, \ldots, x_t) = \sigma^2$, where $\sigma$ is a constant.
**TS.5** No serial correlation. That is to say, $Corr(u_t, u_s|x_1, x_2, \ldots, x_t)=0$
**TS.6** Normality of errors

***Theorem***: If from TS.1 to TS.3 holds, then $\mathbb{E}(\hat{\beta}_j)=\beta_j$

***Theorem***: Under TS.1-TS.6, the OLS estimators is BLUE of the regression coefficients.

***Theorem***: Under TS.1-TS.6, the the OLS estimators have the usual normal distribution (conditional on $\mathbf{X}$). The usual F-tests and t-tests are valid.

## dummy variables in TS

Dummy variables are used to isolate certain periods that may be systematically different. For example, we can use dummy variables to isolate the effect of a policy change. And it works in the same way as the dummy variables in cross-sectional data. The dummy variables can also be used to capture seasonal effects.

And we usually import trending variables when:
* If the dependent variable displays an obvious trending behaviour
* If both the dependent and some independent variables have trends
* If only some of the independent variables have trends; their effect on the dependent variable may only be visible after a trend has been substracted.

## Serial correlation

In practice, we could merely see an instance that fits the TS.5 perfectly. When serial correlation occurs, the OLS estimators are still unbiased and consistent, but they are no longer efficient. And the standard errors are biased downward. And the t-statistics and F-statistics are biased.

### Testing for serial correlation

Suppose we have regression model:
$$
\begin{align*}
y_t &= \beta_0 + \beta_1x_{1t} + \beta_2x_{2t} + \ldots + \beta_kx_{kt} + u_t \\
u_t &= \rho u_{t-1} + \epsilon_t
\end{align*}
$$ And the hypothesis is $H_0: \rho=0$

#### method 1: Residual Correlogram

We can compute the residual correlation by $$r_k = \frac{\sum_{t=k+1}^T \hat{u}_t\hat{u}_{t-k}}{\sum_{t=1}^T \hat{u}_t^2}$$ And significant boundary is $\plusmn 2\sqrt{T}$

#### method 2: Durbin-Watson test

The Durbin-Watson test is a test for serial correlation in the residuals from a regression analysis. The Durbin-Watson statistic will always have a value between 0 and 4. A value of 2 means that there is no autocorrelation detected in the sample. Values approaching 0 indicate positive serial correlation and values toward 4 indicate negative serial correlation.

Our hypothesis here will be $H_0: \rho=0$ against $H_1: \rho > 0$ or $H_1: \rho < 0$. And we have the test statistic $$dw = \frac{\sum_{t=2}^T(\hat{u}_t-\hat{u}_{t-1})^2}{\sum_{t=2}^T \hat{u}_t^2}$$
We have two bounds $d_L$ and $d_U$ for the test statistic. 
* If $dw < d_L$, we reject $H_0$ and conclude that there is positive serial correlation.
* If $dw > d_U$, we reject $H_0$ and conclude that there is negative serial correlation. 
* If $d_L < dw < d_U$, we fail to reject $H_0$. And the test is inconclusive.

#### method 3: Breusch-Godfrey test

The Breusch-Godfrey test is a test for serial correlation in the residuals from a regression analysis. In this test, we assume that the correlation between residuals could be written as $$ \hat{u}_t = \beta_0 + \beta_1x_{1t} + \ldots + \beta_kx_{kt} + \rho_1\hat{u}_{t-1} + \rho_2\hat{u}_{t-2} + \ldots + \rho_q\hat{u}_{t-q} + e_t$$ where $e_t$ is the error term. And we have the hypothesis $H_0: \rho_1 = \rho_2 = \ldots = \rho_q = 0$ against $H_1: \rho_j \not = 0$ for at least one $j$. And we have the test statistic $$LM = T\sum_{j=1}^q r_j^2 \sim \chi^2_q$$ where $r_j$ is the residual correlation at lag $j$.

### Dealing with serial correlation

#### method 1: Cochrane-Orcutt procedure

Concerning the equation in the last section, we can use the Cochrane-Orcutt procedure to deal with the serial correlation. The idea is to use the OLS estimators of the equation below to replace the OLS estimators of the original equation.
$$
\begin{align*}
y_t &= \beta_0 + \beta_1x_{1t} + \beta_2x_{2t} + \ldots + \beta_kx_{kt} + u_t \\
u_t &= \rho u_{t-1} + \epsilon_t
\end{align*}
$$
And we have the following steps:
1. Estimate the original equation by OLS and obtain the residuals $\hat{u}_t$.
2. Regress $\hat{u}_t$ on $\hat{u}_{t-1}$ and obtain the coefficient $\hat{\rho}$.
3. Replace the original equation with the equation below: $$y_t - \rho y_{t-1} = \beta_0(1-\hat{\rho}) + \beta_1(x_{1t} - \hat{\rho}x_{1(t-1)}) + \ldots + (u_t - \hat{\rho}u_{t-1}) $$ we can see that the new equation is free of serial correlation while the coefficients of original equation stay the same.

Howerver, we can see that the precedure can not be appied to the first sample because we do not have the value of $y_0$. Then there are two ways to deal with this problem:
1. We can omit the first sample.
2. We could let the fist sample calculated by follows:
   $$
   \begin{align*}
   y_1^* &= \sqrt{1-\hat{\rho}^2}y_1 & x_{11}^* &= \sqrt{1-\hat{\rho}^2} \\
   x_{12}^* &= \sqrt{1-\hat{\rho}^2}x_1 & \hat{u}_1^* &= \sqrt{1-\hat{\rho}^2}\hat{u}_1 \\ 
   \end{align*}
   $$

# DiD Model(Difference in Difference Model)

## The basic idea

The basic idea of DiD model is to compare the difference between the treatment group and the control group before and after the treatment. And we have the following regression model:
$$y_{it} = \beta_0 + \beta_1D_i + \beta_2T_t + \beta_3(D_i \times T_t) + u_{it}$$ where $D_i$ is the dummy variable for the treatment group, $T_t$ is the dummy variable for the period after the treatment. And we can see that $\beta_3$ is the coefficient of interest.
And the DiD estimator is $$\hat{\beta}_3 = (\bar{y}_{1,T} - \bar{y}_{1,C}) - (\bar{y}_{0,T} - \bar{y}_{0,C})$$ where $\bar{y}_{1,T}$ is the average of the treatment group after the treatment, $\bar{y}_{1,C}$ is the average of the control group after the treatment, $\bar{y}_{0,T}$ is the average of the treatment group before the treatment, and $\bar{y}_{0,C}$ is the average of the control group before the treatment.

The significance of the DiD estimator implies that the treatment has significant effect on the treatment group.

# Limited Dependent Variables

Limited Dependent Variables, LDV for short, are the dependent variables whose range is substaintively restricted. And we have the following types of LDV:
1. Binary variables
2. Nonnegative variables
3. Censored variables
4. Count variables
5. Nonnegative variables with excess zeros

## Linear Probability Model(LPM)

Linear Probability Model(LPM)
:  The linear probability model is a regression model in which the dependent variable is binary. The LPM is a special case of the probit model and the logit model.

The LPM is the simplest model for binary dependent variables. And we have the following regression model:
$$\mathbb{P}(y_i=1|\mathbf{x}) = \beta_0 + \beta_1x_{i1} + \beta_2x_{i2} + \ldots + \beta_kx_{ik}$$ where $y_i$ is the binary dependent variable. And we can see that the LPM is a special case of the linear regression model. And we can use the OLS to estimate the parameters.

## Binary Choice Model

Binary Choice Model
:  The binary choice model is a regression model in which the dependent variable is binary. The binary choice model is a generalization of the linear probability model.

The idea of the model is to use the latent variable to represent the binary dependent variable. The idea here is identical to the calssification quetion in Machine learning. And we have the following regression model:
$$\mathbb{P}(y_i=1|\mathbf{x}) = G(\beta_0 + \beta_1x_{i1} + \beta_2x_{i2} + \ldots + \beta_kx_{ik})$$ where $y_i^*$ is the latent variable and $y_i$ is the binary dependent variable. And we can see that the LPM is a special case of the linear regression model. The $G$ here is somewhat similar to the activation function in Machine Learning. And we can use the MLE to estimate the parameters. 
The $G$ could be the following functions:
1. Probit function: $G(z) = \Phi(z)$(Standard Normal CDF)
2. Logit function: $G(z) = \frac{1}{1+\exp(-z)}$

### Goodness of fit

We can use the pseudo R-squared to measure the goodness of fit. And we have the following formula:
$$\hat{R}^2 = 1 - \log{L_{ur}} / \log{L_0}$$ where $L_{ur}$ is the likelihood of the unrestricted model and $L_0$ is the likelihood of the model with only intercept.

Or we could use correration based measures. And we have the following formula:\[Corr(y_i, \tilde{y}_i)\] 

### Hypothesis testing

The usual t-tests can be used for single parameter hypothesis testing. And there are 3 alternatives for multiple parameter hypothesis testing:
1. Wald test
2. Likelihood ratio test
3. Lagrange multiplier test

The **Likelihood ratio test** is the most powerful test among the three tests. Its idea is to compare the likelihood of the restricted model and the likelihood of the unrestricted model. And we have the following formula:
$$LR = -2(\log{L_r} - \log{L_{ur}}) \sim \chi^2_q$$ where $q$ is the number of restrictions.
