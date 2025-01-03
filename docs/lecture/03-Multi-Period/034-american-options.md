# American Options

So far, even if the outcome of European contingent claims may depend on the sequence of events previous to the maturity, the contract is settled for a given time horizon.
In *American type* of contingent claim, the buyer can claim the payoff at any time before the settlement.

!!! definition
    
    An *American contingent claim* is a non-negative adapted stochastic process:
    
    \[
    C=(C_t)_{0\leq t\leq T}.
    \]
    
    The value $C_t(\omega)$ represents the outcome that a buyer can claim if he/she exercises at time $t$ in state $\omega$.

!!! example

    The most classical example of American contingent claims are the American call and put options:
    
    \[
    C_t^{call}=\left( S_t^i-K \right)^+ \quad \text{and} \quad C_t^{put}=\left( K-S_t^i \right)^+,
    \]
    
    for $t=0,\ldots, T$.

!!! remark

    Note that a European contingent claim $C$ can be viewed as a special case of an American one.  
    Indeed, it would correspond to the stochastic process:
    
    \[
    C_t=
    \begin{cases}
    0 & \text{if } t=0,\ldots, T-1, \\\\
    C & \text{if } t=T.
    \end{cases}
    \]


## Hedging Strategy for the Seller

We first consider the problem of a hedging strategy for the seller of an American contingent claim $C$.
Hereby, we denote by $H$ the discounted contingent process, that is:

\[
H_t=\frac{C_t}{B_t}, \quad t=0,\ldots, T.
\]

!!! warning
    We suppose throughout that the financial market is arbitrage-free and, even more, complete.
    This means there exists only one pricing measure $P^\ast$ equivalent to $P$.

We want to compute the minimal amount of capital $U_t$ that the seller at time $t$ should have in order to pay the buyer of the contingent claim in case this person exercises their claim.
We make this computation backward:

- **Time $T$**:
    Suppose that at time $T$, the buyer did not exercise its claim previously.
    Then the discounted amount of capital needed to satisfy the buyer is exactly:

    \[
    U_T=H_T
    \]

- **Time $T-1$**:
    Suppose that we are at time $T-1$. We face two situations.

    Either the buyer decides to exercise now, and we need at least:
  
    \[
    U_{T-1} \geq H_{T-1}
    \]
  
    Or it decides to wait another time period, and we have to hedge against the capital we need in the next period $U_T$.
    Since the market is complete with a value $E^{P^\ast}[U_T|\mathcal{F}_{T-1}]$ at time $T-1$ I can find a strategy $\boldsymbol{\eta}_T$ which will replicate $U_T$, that is

    \[
        E^{P^\ast}[U_T |\mathcal{F}_{T-1}] + \boldsymbol{\eta}_T\cdot \Delta \boldsymbol{X}_T = U_T
    \]

    It follows that the capital required today to hedge this case must be:

    \[
        U_{T-1} \geq E^{P^\ast}\left[ U_T |\mathcal{F}_{T-1} \right]
    \]

    Altogether, this means:
  
    \[
    U_{T-1} = \max\left\{ H_{T-1}, E^{\ast}\left[ U_T | \mathcal{F}_{T-1} \right] \right\} = H_{T-1} \vee E^{P^\ast}\left[ U_T | \mathcal{F}_{T-1} \right].
    \]

- **Time $t \leq T-1$**:
    The same argumentation means we have to reserve at least:
  
    \[
        U_t \geq H_t,
    \]
  
    as well as the minimum amount of capital $U_{t+1}$ needed from tomorrow in expectation under the pricing measure, that is:
  
    \[
    U_t \geq E^{P^\ast}\left[ U_{t+1} | \mathcal{F}_t \right].
    \]
  
    Altogether, it follows that:
  
    \[
    U_t = \max\left\{ H_t, E^{P^\ast}\left[ U_{t+1} | \mathcal{F}_t \right] \right\} = H_t \vee E^{P^\ast}\left[ U_{t+1} | \mathcal{F}_t \right].
    \]

This recursive scheme is called the *Snell Envelope*.

!!! definition "Definition: The Snell Enveloppe"

    Let $H$ be an adapted process, $P^\ast$-integrable.
    The Snell Envelope of $H$ is defined inverse recursively as follows:
    
    \[
    \begin{equation*}
        \begin{cases}
            U_T =H_T\\
            \\
            U_t=H_t \vee E^{P^\ast}\left[ U_{t+1} | \mathcal{F}_t \right] &\text{for } t=T-1,\ldots, 0.
        \end{cases}
    \end{equation*}
    \]

The Snell envelope satisfies the following inequality:

\[
\begin{align*}
   E^{P^\ast}\left[ U_{t+1} | \mathcal{F}_t \right] & \leq  H_t \vee E^{P^\ast}\left[ U_{t+1} | \mathcal{F}_t \right] \\
      & = U_t
\end{align*}
\]

Processes satisfying this inequality are called super-martingales:

!!! definition "Definition: Super/Sub Martingales"

    A process $X$ is called a $P^\ast$-super-martingale if:
    
    1. $X$ is adapted;
    2. $X$ is $Q$-integrable;
    3. $E^{P^\ast}[X_{t+1}|\mathcal{F}_t] \leq X_t$ for every $t=0,\ldots,T-1$.
    
    A process $X$ is called a $Q$-sub-martingale if $-X$ is a $Q$-super-martingale.


The Snell envelope is an example of $P^\ast$-super-martingale with particular property

!!! proposition

    Let $H$ be an adapted and $P^\ast$-integrable process.
    The Snell envelope $U$ of $H$ is a $P^\ast$-super-martingale and the smallest $P^\ast$-super-martingale among those dominating $H$.
    That is, if $V$ is a $P^\ast$ super-martingale such that $V_t \geq H_t$ for all $t$, then $V\geq U$.
    
!!! proof

    From the definition of $U$, it follows immediately that $U$ is a $P^\ast$-super-martingale.
    Let $V$ be another $P^\ast$-super-martingale such that $V_t \geq H_t$ for every $t$.
    By backward induction we show that $V_t \geq U_t$.

    * For $t = T$, by definition we have $V_T \geq H_T = U_T$

    * For $t = T-1$, we have
        * $V_{T-1} \geq H_{T-1}$ since $V$ dominates $H$
        * $V_{T-1}\geq E^{P^\ast}[V_T|\mathcal{F}_{T-1}] = E^{P^\ast}[U_T|\mathcal{F}_{T-1}]$ since $V$ is a super martingale and $V_T \geq U_T$.
        
        All together it follows that $V_{T-1}\geq H_{T-1}\vee E^{P^\ast}[U_T|\mathcal{F}_{T-1}] = U_{T-1}$.

    The argumentation follows the same logic for every other step.


!!! example

    Consider the CRR model where the American contingent claim is path-independent, that is:
    
    \[
    H_t = h_t(S_t),
    \]
    
    for some functions $h_t:\mathbb{R}\to \mathbb{R}$.
    This is particularly the case for American put and call options since $S^0$ does not depend on the states $\omega \in \Omega$.
    The American option scheme for the computation of the Snell envelope $U_t=u_t(S_t)$ reads as follows:
    
    \[
      u_T(x)=h_T(x), \quad \text{and} \quad u_t(x)= h_t(x) \vee \left( u_{t+1}(x(1+u) )p + u_{t+1}(x(1+d))(1-p) \right),
    \]
    
    for $t=0,\ldots, T-1$, where $p=(r-d)/(u-d)$.
    
