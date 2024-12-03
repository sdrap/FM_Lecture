# Derivative Securities

A *contingent claim* is a contract between a seller and a buyer where the seller agrees to deliver a certain payoff at a future time.
A contingent claim is called a *derivative* if this contract is written as a payoff depending on some underlying, such as stocks, bonds, indices, portfolios, or funds.
Options are specific derivatives characterized by parameters like strike price and expiration date.
While definitions may vary, the mathematical interpretation remains consistent.

!!! example "Examples of Derivatives"

    In the presentation of the different derivatives we consider a financial market with a generic asset $S$.

   
    <div class="grid cards" markdown>

    -   __Forward/Future Contract__

        ---
        
        A forward contract is an agreement between two parties to buy or sell an asset $S$ at a future time for a price $K$ fixed today.
        The payoff for the contract owner is determined by the difference between the asset price and the agreed price:  
          
        \[
            C^{fw} = S - K
        \]

    -   __Forward Payoff__

        ---
    
        ![Forward Payoff](./../../images/forward_payoff_dark.svg#only-dark){ align = right}
        ![Forward Payoff](./../../images/forward_payoff_white.svg#only-light){ align=right}
    </div>

    <div class="grid cards" markdown>

    -   __European Put/Call Option__

        ---

        A European Call or Put option grants the right, but not the obligation, to buy or sell an asset $S$ at a future time for a *strike price* $K$ fixed today.        
        The payoff is
        
        \[
            \begin{align*}
              C^{call} & = (S - K)^+
                        =
            \begin{cases}
              S - K & \text{if } S \geq K, \\
              0 & \text{otherwise}.
            \end{cases}\\
            C^{put} & = (K - S)^+
                     =
            \begin{cases}
              K - S & \text{if } K \geq S, \\
              0 & \text{otherwise}.
            \end{cases}
            \end{align*}
        \]

        European call and put options are related by the formula 

        \[
          C^{call} - C^{put} = S - K
        \]

    -   __European Call/Put Payoff__

        ---
    
        ![Call/Put Payoff](./../../images/call_put_payoff_dark.svg#only-dark){ align = right}
        ![Call/Put Payoff](./../../images/call_put_payoff_white.svg#only-light){ align=right}
    </div>

    <div class="grid cards" markdown>

    -   __Straddle Option__

        ---
        
        The goal of a straddle option is to profit from significant price movements of the underlying asset, regardless of the direction.
        It grants the right to get the price deviation (positive or negative) of the underlying asset with respect to a strike $K$.

        The payoff is:

        \[
          C^{straddle} = |S - K| =
          \begin{cases}
            S-K & \text{ if } S\geq K\\
            K-S & \text{ if } S <K
          \end{cases}
        \]
        
        Note that a straddle option is equivalent to holding a call and a put option with the same strike.

        \[
          C^{straddle}(K) = C^{call}(K) + C^{put}(K)
        \]

    -   __Straddle Option Payoff__

        ---
    
        ![Straddle Payoff](./../../images/straddle_payoff_dark.svg#only-dark){ align = right}
        ![Straddle Payoff](./../../images/straddle_payoff_white.svg#only-light){ align=right}
    </div>

    <div class="grid cards" markdown>

    -   __Butterfly Option__

        ---
        
        A butterfly option has somehow the counter effect to a straddle option in the sense that it is designed to profit from price movement around a given target $K$ within an interval $\underline{K} < K <\overline{K}$.

        The payoff is:

        \[
          C^{butterfly} = 
          \begin{cases}
            0 & \text{if }S<\underline{K} \text{ or }S>\overline{K}\\
            S-\underline{K} & \text{if } \underline{K}\leq S\leq K\\
            \overline{K} - S & \text{if } K<S \leq \overline{K}
          \end{cases}
        \]
        
        Note that such a straddle option can also be written as a combination of put and call options strikes

        \[
          C^{butterfly}(\underline{K}, K, \overline{K}) = C^{call}(\underline{K}) + C^{call}(\overline{K}) - 2 C^{call}(K)
        \]

        Usually, the strike $K$ is at the mid point between $\underline{K}$ and $\overline{K}$.

    -   __Butterfly Option Payoff__

        ---
    
        ![Butterfly Payoff](./../../images/butterfly_payoff_dark.svg#only-dark){ align = right}
        ![Butterfly Payoff](./../../images/butterfly_payoff_white.svg#only-light){ align=right}
    </div>

   
Note that each of these options can be expressed as $f(S)$, where $S$ is the underlying asset, and $f: \mathbb{R} \to \mathbb{R}$ is some continuous function.

!!! definition "Definition: Contingent Claim"
    - A *contingent claim* $C$ is a positive random variable.(1)
        {.annotate}

        1.  In a strictly more general sense it does not need to be strictly positive but usually bounded from below. See for instance forward contracts.

    - A *derivative* $C$ is a contingent claim that depends only on the information provided by the underlying on which it is written.
        In other terms, $C = f(\boldsymbol{S}_1)$ for some continuous function $f:\mathbb{R}^d \to [0, \infty)$.(1)
        {.annotate}

        1.  In a more general fashion, it means that $C$ is $\sigma(\boldsymbol{S}_1)$-measurable, which with some proof work can be shown to be equivalent to $C = f(\boldsymbol{S}_1)$ for some measurable function $f$.



## Pricing a Contingent Claim

Given a contingent claim $C$, the goal is to determine a *fair price* $\pi(C)$ at which it can be sold.
To do this, we analyze the situation from the seller's perspective:

1. **Time 0:** 
    The seller receives $\pi(C)$ and deposits it into their bank account. This amount is used to invest in a strategy $\boldsymbol{\eta}$ in $\mathbb{R}^d$.
    The holdings in the bank account become $\pi(C) - \boldsymbol{\eta} \cdot \boldsymbol{S}_0$ and the golding in assets becomes $\boldsymbol{\eta}\cdot \boldsymbol{S}_0$.
    The initial portfolio value is $\bar{V}_0(\boldsymbol{\eta}) = \pi(C)$.

2. **Time 1:**
    The seller delivers the payoff $C$ to the buyer while benefiting from their investment strategy $\boldsymbol{\eta}$.
    The discounted portfolio value minus the discounted payoff is:

    $$
      V_1(\boldsymbol{\eta}) - \frac{C}{1 + r} = \pi(C) + \boldsymbol{\eta} \cdot \Delta\boldsymbol{X}_1 - \frac{C}{1 + r}
    $$

In an ideal situation, the seller of the option would like to get out with gains without downside risk, that is, *fully hedge* the position.
Hence, the seller aims to ensure:

$$
\pi(C) + \boldsymbol{\eta} \cdot \Delta\boldsymbol{X}_1 \geq \frac{C}{1 + r} 
$$


Such a price $\pi(C)$ together with the smart strategy $\boldsymbol{\eta}$ means that the seller super hedge his position.
Considering all the possible prices and smart strategies that super hedge the position allows to define the lowest price at which the seller is willing to sell the option without taking risk, the **super-hedging price**


$$
\bar{\pi}(C) = \inf \left\{ x \in \mathbb{R} : x + \boldsymbol{\eta} \cdot \Delta\boldsymbol{X}_1 \geq \frac{C}{1 + r}, \; \text{for some } \boldsymbol{\eta} \in \mathbb{R}^d \right\}.
$$

Conversely, the buyer's perspective leads to the **sub-hedging price**, $\underline{\pi}(C)$:

$$
\underline{\pi}(C) = \sup \left\{ y \in \mathbb{R} : y + \boldsymbol{\nu} \cdot \Delta\boldsymbol{X}_1 \leq \frac{C}{1 + r}, \; \text{for some } \boldsymbol{\nu} \in \mathbb{R}^d \right\}.
$$


It seems economically reasonable that prices $y$ from the buyer sub-hedging their position should be lower than the prices $x$ of the seller super-hedging their positions.
This is however true if the market is arbitrage free as seen in the subsequent proposition.

To simplify our exposition, let us provide the notation for pricing measures

\[
\mathcal{P}^\ast := \left\{ P^\ast \sim P \colon E^{P^\ast}\left[ \Delta \boldsymbol{X}_1 \right] = 0 \text{ and } dP^\ast/dP \text{ is bounded}\right\}
\]

In particular, the FTAP can be formulated as "The market is arbitrage free if and only if $\mathcal{P}^\ast$ is not empty".

??? remark "Remark: Geometric Interpretation I"

    Define $I$ and $J$ as the set of super- and sub-hedging prices, respectively:

    \[
    \begin{align*}
        I & := \left\{ x \in \mathbb{R}\colon x+\boldsymbol{\eta}\cdot \Delta \boldsymbol{X}_1 \geq \frac{C}{1+r}\text{ for some smart strategy }\boldsymbol{\eta} \in \mathbb{R}^d \right\}\\
        J & := \left\{ y \in \mathbb{R}\colon y+\boldsymbol{\nu}\cdot \Delta \boldsymbol{X}_1 \leq \frac{C}{1+r}\text{ for some smart strategy }\boldsymbol{\nu} \in \mathbb{R}^d \right\}\\
    \end{align*}
    \]

    For which holds $\bar{\pi}(C) = \inf I$ and $\underline{\pi}(C) = \sup J$.

    These two sets, $I$ and $J$, are eventually intervals
    

    !!! danger "**Lemma**"
    
        * $I$ is either an interval of the form $[\bar{\pi}(C), \infty)$ or $(\bar{\pi}(C), \infty)$
        * $J$ is either an interval of the form $(-\infty, \underline{\pi}(C)]$ or $(-\infty, \underline{\pi}(C))$
    
    !!! quote "**Proof**"
    
        We show only the first assertion, the second follows the same argumentation.
        Clearly $\bar{\pi}(C)$ is the lower bound of the set $I$, whether or not it is a minimum or an infimum.
        We just have to show that for any $x$ in $I$, if $m>0$, then $x+m$ is also in $I$.
        This follows however from the definition, as for a smart strategy $\boldsymbol{\eta}$ such that
    
        \[x + \boldsymbol{\eta}\cdot \Delta \boldsymbol{X}_1 \geq \frac{C}{1+r}\]
        
        It follows immediately that 
    
    
        \[x +m + \boldsymbol{\eta}\cdot \Delta \boldsymbol{X}_1 \geq m +\frac{C}{1+r} \geq \frac{C}{1+r}\]
    
        showing that $x+m$ is in $I$.


We are now in position to show the first proposition regarding the super- and sub-hedging price


!!! proposition

    If the market is arbitrage free, then for any super-hedging price $x$, sub-hedging price $y$ and any pricing measure $P^\ast$ it holds

    \[
        y \leq E^{P^\ast}\left[ \frac{C}{1+r} \right] \leq x
    \]

    In particular, we get
   
    \[
        \underline{\pi}(C) \leq \inf_{P^\ast \in \mathcal{P}^\ast} E^{P^\ast}\left[ \frac{C}{1+r} \right]\leq \sup_{P^\ast \in \mathcal{P}^\ast} E^{P^\ast}\left[ \frac{C}{1+r} \right]\leq \bar{\pi}(C)
    \]

??? proof

    Let $x$ be a super-hedging price and $y$ be a subhedgin price.
    By definition, there exists smart strategies $\boldsymbol{\eta}$ and $\boldsymbol{\nu}$ in $\mathbb{R}^d$ such that

    \[
        y + \boldsymbol{\nu}\cdot \Delta \boldsymbol{X}_1 \leq \frac{C}{1+r} \leq x + \boldsymbol{\eta}\cdot \Delta \boldsymbol{X}_1
    \]

    Now, since the market is arbitrage free, according to the FTAP, for any pricing measure $P^\ast$ in $\mathcal{P}^\ast$ which is not empty, by taking expectation of this inequality, it holds
    
    \[
        y + \underbrace{E^{P^\ast}\left[\boldsymbol{\nu}\cdot \Delta \boldsymbol{X}_1\right]}_{=0} \leq E^{P^\ast}\left[\frac{C}{1+r} \right]\leq x + \underbrace{E^{P^\ast}\left[\boldsymbol{\eta}\cdot \Delta \boldsymbol{X}_1\right]}_{=0}
    \]

    showing the first assertion.

    Since this inequality holds for any super hedging price $x$, any sub hedging price $y$ and any pricing measure $P^\ast$, by the definition of $\bar{\pi}(C)$ and $\underline{\pi}(C)$ the second assertion follows.


We however still need to define the notion of of a fair price for a contingent claim and how it relates to the super-/sub-hedging price.


!!! definition "Definition: Fair Price of Contingent Claims"

    Given a contingent claim $C$, a price $\pi(C)$ is called a *fair price* if the original financial market extended with the new financial instrument $S^{d+1}$ given by

    \[
      S^{d+1}_0 = \pi(C) \quad \text{and}\quad S^{d+1}_1 = C
    \]

    is arbitrage free.

    We denote by $\Pi(C)$ the set of all possible fair prices for the contingent claim $C$.

In other terms, if the financial market considers the new financial instrument $C$ traded at price $\pi(C)$ it remains arbitrage free.
As pendant to the super- and sub-hedging price, with the help of the FTAP we can connect arbitrage free prices to pricing measures as follows.

!!! proposition 

    Let $C$ be a contingent claim on an arbitrage-free financial market.
    Then the set of fair prices for the contingent claim $C$ is non-empty and given by:
    
    \[
      \Pi(C) := \left\{ E^{P^\ast}\left[ \frac{C}{1+r} \right] : P^\ast \sim P \text{ pricing measure with bounded density}  \right\}.
    \]

??? proof
    
    A price $\pi(C)$ for $C$ is fair if the extended financial market is arbitrage-free.
    By the **FTAP**, it follows that there exists a pricing measure $\hat{P}$ equivalent to $P$ with bounded density such that:

    \[
        E^{\hat{P}}\left[\frac{\boldsymbol{S}_1}{1+r}\right] = \boldsymbol{S}_0, \quad \text{and} \quad E^{\hat{P}}\left[\frac{C}{1+r}\right] = \pi(C).
    \]
    
    In particular, $\hat{P}$ is a pricing measure equivalent to $P$ for the smaller market $\boldsymbol{S}$, that is, an element of $\mathcal{P}^\ast$, showing that:
    
    \[
        \Pi(C) \subseteq \{ E^{P^\ast}[C/(1+r)] : P^\ast \in \mathcal{P}^\ast \}.
    \]
    
    Reciprocally, let $\pi(C)$ be an element of $\{ E^{P^\ast}[C/(1+r)] : P^\ast \in \mathcal{P}^\ast \}$.
    It follows that $\pi(C) = E^{P^\ast}[C/(1+r)]$ for some $P^\ast \sim P$ with bounded density.
    Hence, $P^\ast$ is a pricing measure equivalent to $P$ for the extended market, showing by the **FTAP** that the extended market is arbitrage-free.
    Hence, $\pi(C) \in \Pi(C)$, proving the reverse inclusion.(1)
    {.annotate }

    1.  The proof is not fully complete unless we can show that we can show that $\Pi(C)$ is non-empty.
        As done previously, we pick a probability measure $\tilde{P}$ equivalent to $P$ such that $E^{\tilde{P}}[C] < \infty$. Under $\tilde{P}$, the market is arbitrage-free.
        The **FTAP** guarantees the existence of a pricing measure $P^\ast$ equivalent to $P$ with bounded density. 
        In particular, $E^{P^\ast}[C] < \infty$, and therefore:
        
        \[
            \pi(C) = E^{P^\ast}[C/(1+r)] \in \Pi(C).
        \]

We are now in place to show the relation ship between super- sub-hedging prices, pricing measures and fair prices.
In a nuttshell that the following illustration holds


![Super- Sub-Hedging](./../../images/superhedging_dark.svg#only-dark)
![Super- Sub-Hedging](./../../images/superhedging_white.svg#only-light)



!!! theorem "Theorem: Super/Sub Hedging and Fair Prices"

    Let $C$ be a contingent claim.
    For

    \[
        \begin{align*}
            J & = \left\{ y\in \mathbb{R}\colon y + \boldsymbol{\eta}\cdot \Delta \boldsymbol{X}_1 \leq \frac{C}{1+r} \text{ for some }\boldsymbol{\eta}\in \mathbb{R}^d \right\} && \text{Risk free subhedging prices}\\
            \underline{\pi}(C) & = \sup J && \text{Sub-hedging price}\\
            I & = \left\{ x\in \mathbb{R}\colon x + \boldsymbol{\nu}\cdot \Delta \boldsymbol{X}_1 \leq \frac{C}{1+r} \text{ for some }\boldsymbol{\nu}\in \mathbb{R}^d \right\} && \text{Risk free superhedging prices}\\
            \underline{\pi}(C) & = \inf I && \text{Super-hedging price}\\
            \Pi(C) & = \left\{ \pi(C)\colon \text{fair prices} \right\} && \text{Fair prices}\\
            \mathcal{P}^\ast & = \left\{ P^\ast \sim P \colon P^\ast \text{ is a pricing measure} \right\} && \text{Pricing measures}
        \end{align*}
    \]

    If the market is arbitrage free, then it holds that $J$, $I$, and $\Pi(C)$ are intervals such that $J\leq \Pi(C) \leq I$.
    Furthermore 

    \[
        \begin{align*}
            J & = (-\infty, \underline{\pi}(C)] &
            \Pi(C) & = \left\{ E^{P^\ast}\left[ \frac{C}{1+r} \right] \colon P^\ast \in \mathcal{P}^\ast \right\} &
            I & = [\overline{\pi}(C), \infty ) 
        \end{align*}
    \]

    and

    \[
        \begin{align*}
            \underline{\pi}(C) & = \inf \Pi(C) & \overline{\pi}(C) & = \sup \Pi(C)
        \end{align*}
    \]


??? proof

    We already saw that $J$ and $I$ are intervals (see geometric interpretation remark above).
    We also say that $\Pi(C) = \{E^{P^\ast}[C/(1+r)]\colon P^\ast \in \mathcal{P}^\ast\}$ and that $J \leq \Pi(C) \leq I$.
    The fact that $\Pi(C)$ is also an interval follows directly from $\mathcal{P}^\ast$ is a convex set, same argumentation as for $\mathcal{C}$ in the proof of the **FTAP**.

    We are left to show that $\underline{\pi}(C) \in J$ and $\overline{\pi}(C) \in I$ and that $\underline{\pi}(C) = \inf \Pi(C)$ as well as $\overline{\pi}(C)  = \sup \Pi(C)$.

    
    Let us proove that $\overline{\pi}(C) = \sup \Pi(C)$.
    We already know that $\overline{\pi}(C) \geq \sup \Pi(C)$
    Suppose $\sup \Pi(C) < \infty$, otherwise the equality is trivial.
    Let $m > \sup \Pi(C)$.
    By definition, the market extended with $(m, C)$ admits an arbitrage opportunity.
    That is, there exist $\boldsymbol{\eta} \in \mathbb{R}^d$ and $\mu \in \mathbb{R}$ such that:
    
    \[
        \begin{cases}
            P\left[\boldsymbol{\eta} \cdot \Delta \boldsymbol{X}_1 + \mu \left(\frac{C}{1+r} - m\right) \geq 0\right] = 1, \\
            P\left[\boldsymbol{\eta} \cdot \Delta \boldsymbol{X}_1 + \mu \left(\frac{C}{1+r} - m\right) > 0\right] > 0.
        \end{cases}
    \]
    
    Since the original market is arbitrage-free, it follows that $\mu \neq 0$.
    Taking the expectation of the positive random variable $\boldsymbol{\eta} \cdot \Delta \boldsymbol{X}_1 + \mu \left(\frac{C}{1+r} - m\right)$ with respect to $P^\ast \in \mathcal{P}^\ast$ yields:
    
    \[
        \mu E^{P^\ast}\left[\frac{C}{1+r} - m\right] \geq 0.
    \]
    
    By definition of $m$, this implies $\mu < 0$.
    Defining $\boldsymbol{\nu} = -\boldsymbol{\eta}/\mu \in \mathbb{R}^d$ yields:
    
    \[
        m + \boldsymbol{\nu} \cdot \Delta \boldsymbol{X}_1 \geq \frac{C}{1+r},
    \]
    
    showing that $m$ is in $I$, and therefore $m \geq \bar{\pi}(C)$. Consequently:
    
    \[
        \sup \Pi(C) \geq \bar{\pi}(C).
    \]

    The same argumentation shows that $\overline{\pi}(C) = \inf \Pi(C)$.

    We are left to show that $\overline{\pi}(C)$ is in $I$.
    Without loss of generality, due to the law of one price, we may assume that there is no redundancy; that is, $\boldsymbol{\eta} \cdot \Delta \boldsymbol{X}_1 = 0$ implies $\boldsymbol{\eta} = 0$.  

    Pick a sequence $(m_n)$ of elements in $I$ such that $m_n \downarrow \overline{\pi}(C)$ and denote by $\boldsymbol{\eta}^n$ the corresponding sequence of strategies such that:

    \[
        m_n + \boldsymbol{\eta}^n \cdot \Delta \boldsymbol{{X}_1 \geq \frac{C}{1 + r}.
    \]

    If $(\boldsymbol{\eta}^n)$ is bounded, up to a subsequence, we may assume that $\boldsymbol{\eta}^n \to \boldsymbol{\eta} \in \mathbb{R}^d$, for which it holds:

    \[
        \frac{C}{1 + r} \leq m_n + \boldsymbol{\eta}^n \cdot \Delta \boldsymbol{X}_1 \to \bar{\pi}(C) + \boldsymbol{\eta} \cdot \Delta \boldsymbol{X}_1,
    \]

    showing that $\bar{\pi}(C)$ is in I.

    If $\lim \|\boldsymbol{\eta}^n\| = \infty$, up to a subsequence, it follows that $\boldsymbol{\eta}^n / \|\boldsymbol{\eta}^n\| \to \boldsymbol{\mu}$ with $\|\boldsymbol{\mu}\| = 1$.

    However, it follows that:
    \[
        0 \leq \lim \frac{C}{\|\boldsymbol{\eta}^n\|(1 + r)} = \lim \frac{\boldsymbol{\eta}^n}{\|\boldsymbol{\eta}^n\|} \cdot \Delta \boldsymbol{X}_1 + \frac{m_n}{\|\boldsymbol{\eta}^n\|} = \boldsymbol{\mu} \cdot \Delta \bs{X}_1
    \]

    Since the market is arbitrage-free, it must follow that $\boldsymbol{\mu} \cdot \Delta \boldsymbol{X}_1 = 0$, which by the non-redundancy assumption implies $\boldsymbol{\mu} = 0$, leading to a contradiction since $\|\boldsymbol{\mu}\| = 1$.


!!! definition
    
    A contingent claim $C$ is called *replicable* — *attainable*, *hedgeable*, or *redundant* — if there exists a portfolio with start value $\bar{V}_0$ and strategy $\boldsymbol{\eta} \in \mathbb{R}^d$ such that:
    
    \[
        C = \bar{V}_1 = \bar{V}_0 + \boldsymbol{\eta} \cdot \left(\boldsymbol{S}_1 - \boldsymbol{S}_0(1+r)\right).
    \]

In other term, a contingent claim is replicable if its outcome can be fully attained by a self financing portfolio.

!!! proposition

    Let $C$ be a contingent claim in an arbitrage-free market. Then:

    - $C$ is replicable if and only if $\overline{\pi}(C) = \underline{\pi}(C)$ which is the unique price of the contingent claim

    - If $C$ is not replicable, then $\overline{\pi}(C) > \underline{\pi}(C)$, and:
    
    \[
        \Pi(C) = \left(\overline{\pi}(C), \underline{\pi}(C)\right).
    \]

??? proof

    Clearly, if $C$ is replicable, it follows that $\underline{\pi}(C) = \overline{\pi}(C)$ by the definition of $\underline{\pi}$ and $\overline{\pi}$.
    The reciprocal follows from the second assertion.
    To prove the second assertion:

    1. **$\Pi(C)$ is an interval**
    2. **Non-replicability implies that $\bar{\pi}(C) \not\in \Pi(C)$**:
        Indeed, by the previous theorem, there exists a strategy $\boldsymbol{\eta}$ such that:
   
        \[
            \bar{\pi}(C) + \boldsymbol{\eta} \cdot \Delta \boldsymbol{X}_1 \geq \frac{C}{1+r}.
        \]
    
        Since $C$ is not replicable, this inequality cannot hold with equality $P$-almost surely.
        This demonstrates $\bar{\pi}(C) \not\in \Pi(C)$.

    Since $\overline{\pi}(C) = \sup \Pi(C)$, it follows that $\Pi(C)$ forms an open interval:
    
    \[
        \Pi(C) = \left(\underline{\pi}(C), \overline{\pi}(C)\right)
    \]

A condition that garantees that every contingent claim is replicable and henceforth with a unique price is when $\mathcal{P}^\ast$ contains a unique pricing measure.
In such a market every contingent claim is uniquely priced and hedgable.
In other terms every contingent claim in a complete financial market is redundant since they can all be achieved by a portfolio.
A market with a unique pricing measure is called a **complete** market

On the other hand, the proposition shows that unless the claim is attainable, then fair prices of a contingent claim are not unique.
The choice of a fair price (and therefore a deal) for such a contingent claim is henceforth due to an agreement between the buyer and the seller to choose a price within the interval $\Pi(C)$.
Therefore, they both have to accept some downside risk since neither will have a price in their confort risk free zone.


