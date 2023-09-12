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
**MLR.4** Zero conditional mean (The value of the explanatory variables must contain no information about the mean of the unobserved factors)

**Theorem**(Unbiasedness of OLS) If MLR.1-MLR.4 holds, then $\mathbb{E}(\hat{\beta}_j)=\beta_j$

**MLR.5** Homoscedasticity. That is to said, $Var(u_i|x_i) = \sigma^2$, where $\sigma$ is a constant.
