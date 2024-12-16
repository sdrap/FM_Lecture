# Project I


## Equilibrium Price

In the lecture we assumed that the market is arbitrage free in the sense that Arbitrages makes the market ill defined.
The main reason is that if an arbitrage suddenly exists, arbitrageurs would immediately size this opportunity driving the prices by law of offer and demand within the arbitrage free bounds.

In the following we show that prices that are negociated between different agents on the market yields a price for the underlying assets that is arbitrage free.

Since we are woriking in a one period model we will make some simplifying assumptions (no dividends).

A company wants to go IPO by issuing $M$ shares with an outcome $S_1 \sim \mathcal{N}(\mu, \sigma^2)$.(1)
In the market we have $N$ potential buyers denoted by $i=1, \ldots, N$, that can aquire $\eta^i$ of this share for a price $S_0$ to be negociated among each of them.
We assume that every buyer does not hold assets or cash at the begining, hence start with $0$.(2)
We also assume that there is no interest rate, i.e. $r = 0$.
{.annotate}

1.  This is already an irrealistic assumption since the share value at time $1$ might be negative but we could carry similar argumentation with a log normal distribution or just a binomial model.

2.  You can see how the system change if those investors comes with some money, or if they have some radom endowment.

For a price of $S_0$, and strategy $\eta^i$, the wealth of buyer $i$ is given by

\[
\begin{equation*}
W^i = \eta^i \Delta X_1 = \eta^i S_1 - \eta^i S_0 
\end{equation*}
\]

In order to make investors trading with each others we need to give them some objectives.
In economic terms, it means that they evaluate the future outcomes $W$ in terms of utility, that is 

\[
U^i(W) = E\left[ u^i(W) \right]
\]

where $u^i:\mathbb{R} \to \mathbb{R}$ is a convex function.(1)
In our cases, we assume that $u^i(x) = -e^{-\gamma^i x}/\gamma^i$ where $\gamma^i >0$ is the risk aversion of investor $i$.
{.annotate}

1.  The utility function means first that for every two investment $W$ and $\tilde{W}$, then $U(\lambda W + (1-\lambda)\tilde{W})\geq \lambda U(W) + (1-\lambda)U(\tilde{W}) \geq \min\{U(W), U(\tilde{W})$, meaning that the investor favors diversified outcome rather than concentrated ones. Furthermore since the function is increasing, better outcomes for sure yields better utility.

A Radner Equilibrium is defined as follows

!!! definition "Definition: Radner Equilibrium"

    An equilibrium is characterised by the vector of investments $(\bar{\eta}^1, \ldots, \bar{\eta}^N)$ of the $N$ investors and an agreed price $\bar{S}_0$, such that

    1. **Individual optimality:** Given the equilibrium price $\bar{S}_0$, no investor can get better than his own strategic purchase, that is

        \[
          U^i(\bar{\eta}^i (S_1 - \bar{S}_0)) \geq U^i(\eta^i (S_1 - \bar{S}_0))
        \]

        for any other possible allocation $\eta^i$ and for any investor $i$.

    2. **Market Clearing:** There is so much to share as it is offered.
        In other terms the total amount of shares held by the investors should equal (or at least be less than) the total amount of shares proposed.

        \[
            \sum \eta^i =M
        \]


given this definition, your goal is to show that there exists and equilibrium and investigate it.

1. For a given investor $i$ and a price $S_0$, compute the optimal amount of shares it aquires by computing 

    \[
      \eta^i(S_0) = \mathrm{argmax}_{\eta^i} U^i(W^i)
    \]

2. For the optimal response solution of each agent $\eta^i(S_0)$ for a given price, solve for $S_0$ using the market clearing condition, that is $\bar{S}_0$ solving

    \[
      \sum \eta^i(S_0) = M
    \]

3. Compute the amount of money raised by the IPO as a function of $\mu$ (the sure premises on returns) and $\sigma$ the volatility to which this company is subject to.

!!! warning
    If you want to make it simple at the begining, consider that each $\gamma^i$ are the same $\gamma$.
    Furthermore, check online what is the expectation of $E[e^{\gamma^i Z}]$ when $Z$ is a normal distribution.


!!! proof

    1. We are given a price $S_0$, and try to find the best strategy for agent $i$ (since it is indepedent of $i$ we drop the index $i$ for the moment).

        We want to find $\eta(S_0)$ such that

        \[
          U(\eta(S_0)(S_1 - S_0)) \geq U(\eta (S_1 - S_0))
        \]

        for any other buy decision $\eta$.
        
        Since $\eta \mapsto U(\eta (S_1 -S_0))$ is concave, we just need to compute the first order condition which yield (a mathematician would pay attention about the derivation under the expectation sign...)

        \[
            \begin{align*}
              \frac{d U(\eta (S_1 - S_0))}{d\eta} & = -\frac{1}{\gamma}\frac{d}{d\eta}E\left[ e^{-\gamma(S_1 - S_0)} \right]\\
              & = -\frac{1}{\gamma}E\left[ \frac{d}{d\eta}e^{-\gamma \eta (S_1 - S_0)} \right]\\
              & = E\left[ (S_1 - S_0) e^{-\gamma \eta(S_1-S_0)} \right]\\
              & = e^{\gamma \eta S_0}E\left[ (S_1 - S_0) e^{-\gamma \eta S_1} \right]
            \end{align*}
        \]

        Setting equal to $0$ with $e^{\gamma \eta S_0} >0$, it follows that the first order condition reads as 
        
        \[
          E[S_1 e^{-\gamma \eta S_1}]=S_0E[e^{-\gamma \eta S_1}]
        \]
       
