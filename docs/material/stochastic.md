# Stochastic Processes

Stochastic processes mean that you want to carry over *time* the idea that outcomes will be revealed as time goes by.
Considering for instance your view of the evolution of a financial asset.
At the very begining your decisions towards it relies only on what you can forsee in the future about its evolution however as times goes buy you learn more and more infromation about the nature of this financial asset.



!!! example

    We consider a probability space $(\Omega, \mathcal{F}, P)$ and a sequence $(Y_t)$ of independent identically distributed (iid) random variables such that
  
    \[
      P[Y_t = 1] = P[Y_1 = 1] = \frac{1}{2} = P[Y_1 = -1] = P[Y_t = -1]
    \]

    In other terms, $Y_n$ represent the result of tossing a fair coin at time $t$ with $1$ if tail and $-1$ if head.

    We define the (symetric) random walk as

    \[
      S_0 = 100 \quad \text{and} \quad S_t = S_{t-1} + Y_t = 100 + \sum_{s=1}^t Y_s
    \]

    this produces the following possible paths

    
    ![Random Walk](./../images/rw_dark.svg#only-dark){align = right}
    ![Random Walk](./../images/rw_white.svg#only-light){ align = right}


    Now for a price of $100$ RMB you have the choice between the different games.

    1. **All In:** Receive the value of the random walk after 100 coin tosses, that is $S_{100}$.
    2. **Stop Gain:** If the random walk reaches $120$, you stop the game and cash $120$, otherwize you get $S_{100}$
    3. **Stop Loss:** If the random walk falls to $90$, you stop the game and cash $90$, otherwize you get $S_{100}$.
    4. **Stop Gain/Loss:** If the random walk reaches $120$ or $90$ you stop the gain an cash $120$ or $90$ respectively, otherwize you get $S_{100}$.
    5. **Not a gambler:** I don't play and keep my $100$ RMB


    Now which game would you venture in and why?
    Which game would bring you in expectation the best outcome?


## Information, Conditional Expectation

Information is considered as a $\sigma$-algebra of events.
Now information means that we have an increasing sequence of events that we are aware of, called a filtration.

!!! definition "Definition: Filtration"

    A **filtration** $\mathbb{F} = (\mathcal{F}_t)_{t=0, \ldots, T}$ is a collection of $\sigma$-algebra of events such that

    \[ \mathcal{F}_0 \subseteq \mathcal{F}_1 \subseteq \cdots \subseteq \mathcal{F}_T\]

In other terms, the collection of events known at time $s$ is included in the set of events known at time $t\geq s$.

!!! warning 
    
    It is not necessary but throughout we make the assumption that 

    \[\mathcal{F}_0 = \{\emptyset, \Omega\} \quad \text{and}\quad \mathcal{F}_T = \mathcal{F}\]

    In other terms, we assume that at time zero we know nothing and at time $T$ we know everything.

    !!! lemma

        If a random variable $\xi$ is $\mathcal{F}_0=\{\emptyset, \Omega\}$-measurable, then it must be constant.

    ??? proof

        It is a basic exercise to check.
        Suppose that a random variable $\xi$ is $\mathcal{F}_0=\{\emptyset, \Omega\}$-measurable then it constant.
        Indeed, if it where not, let $\omega_1$ and $\omega_2$ be two states on which $\xi(\omega_1) < \xi(\omega_2)$, let $x$ be such that $\xi(\omega_1)<x<\xi(\omega_2)$.
        It follows that $\omega_1 \in A=\{\xi\leq x\}$ while $\omega_2 \not \in A$.
        This is however not possible since the event $A$ is either $\Omega$ or $\emptyset$.


        

    In this case, it follows that any random variable $\xi$ which is $\mathcal{F}_0$ measurable must be constant.


!!! definition 

    A family $X = (X_t)$ of random variable indexed by time is called a **stochastic process**.
    
    A stochastic process $X$ is called 

    * **Adapted:** if $X_t$ is $\mathcal{F}_t$-measurable for every $t$;
    * **Predictable:** if $X_t$ is $\mathcal{F}_{t-1}$-measurable for every $t$

??? remark

    For predictability, one needs to specify a convention for $X_0$.
    either we say that predictable processes starts at time $1$ or we say that $\mathcal{F}_{-1} = \mathcal{F}_0 = \{\emptyset, \Omega\}$.

## Martingales

Martingales are the most important object to study the properties of stochastic processes.

!!! definition

    A stochastic process $X = (X_t)_{t=0, \ldots, T}$ is called a **martingale** if

    1. $X$ is adapted
    2. $X$ is integrable
    3. $X$ satisfies the martingale property

        \[
            E[X_{t+1}|\mathcal{F}_t] = X_t
        \]

    It is a **super-martingale** if 

    1. $X$ is adapted
    2. $X$ is integrable
    3. $X$ satisfies the super martingale property

        \[
            E[X_{t+1}|\mathcal{F}_t] \leq X_t
        \]

    It is a **sub-martingale** if 

    1. $X$ is adapted
    2. $X$ is integrable
    3. $X$ satisfies the super martingale property

        \[
            E[X_{t+1}|\mathcal{F}_t] \geq X_t
        \]

Clearly, $X$ is a sub-martingale if and only if $-X$ is a super-martingale and $X$ is a martingale if and only if it is a super and sub martingale at the same time.

!!! warning

    Note that the notion of martingale (sup or super) depends on the measure considered.
    A martingale under a probability measure $P$ might no longer be a martingale under another probability measure.

!!! proposition "Doob-Meyer Decomposition"

    Let $X$ be an integrable and adapted process.
    It can be uniquely decomposed into:
    
    \[
    X=M+A,
    \]
    
    where $A$ is a predictable process with $A_0=0$ and $M$ is a martingale.  

    The process $X$ is a super-martingale if and only if $A$ is decreasing and a sub-martingale if and only if $A$ is increasing.

!!! proof

    **Existence:** 
    Suppose that we have a decomposition $X = M+A$ with $M$ martingale and $A$ predictable, then it must hold that

    \[
        \begin{align*}
            0 & = E[M_{t+1} - M_t|\mathcal{F}_t]\\
                & = E[X_{t+1} - X_t - A_{t+1} + A_t | \mathcal{F}_t]\\
                & = E[X_{t+1} - X_t  | \mathcal{F}_t] - A_{t+1} + A_t &&A \text{ is predictable}
        \end{align*}
    \]

    showing that $A_{t+1} =  E[X_{t+1} - X_t |\mathcal{F}_t] - A_t$.

    We therefore define recursively

    \[
        \begin{equation*}
            \begin{cases}
                A_0 & = 0\\
                A_{t+1} & = E[X_{t+1} - X_{t}|\mathcal{F}_t] - A_t
            \end{cases}
        \end{equation*}
    \]

    which by induction can be shown to be predictable and starting at $0$.
    Then $M = X+A$ by the previous computations is a martingale defining the decomposition.

    **Uniqueness:**
    Suppose that $X = M+A = \tilde{M} + \tilde{A}$ be two decompositions.
    It follows that $M - \tilde{M}$ is a martingale and predictable.
    It follows that for every $t$ it must hold

    \[
        \begin{align*}
            0 &= E\left[ (M_{t+1} - M_t) - (\tilde{M}_{t+1} - \tilde{M}_t) |\mathcal{F}_t \right] && \text{Martingale property}\\
            & = (M_{t+1} - M_t) - (\tilde{M}_{t+1} - \tilde{M}_t) && M-\tilde{M}\text{ is predictable}
        \end{align*}
    \]

    We therefore get that

    \[
        M_{t+1} - \tilde{M}_{t+1} = M_{t} - \tilde{M}_{t} = \cdots = M_0 - \tilde{M}_0 = \tilde{A}_0 - A_0 = 0-0 = 0 
    \]

    showing that $M=\tilde{M}$ and therefore $A=\tilde{A}$.

!!! proposition

    Let $M$ be an adapted and integrable process.
    The two following assertions are equivalent:

    1. $M$ is a martingale
    2. for any bounded predictable process $\eta = (\eta_t)$, the process $V= (V_t)$
        
        \[
            V_t = V_0 + \sum_{s=1}^t \eta_s (M_s - M_{s-1})
        \]

        is a martingale.

!!! proof

    Suppose that $M$ is a martingale and let $\eta$ be a bounded predictable process.
    By definition $V$ is adapted.
    Furthermore, denoting by $c$ the constant bounding $\eta$, it holds that
    
    \[
        |V_t| \leq |V_0| + c \sum_{s=1}^t (|M_s| + |M_{s-1}|)
    \]

    which is a a sum of integrable random variables hence integrable.
    As for the martingale property

    \[
        \begin{align*}
            E[V_{t+1} - V_t|\mathcal{F}_t] & = E[\eta_{t+1} (M_{t+1} - M_t) | \mathcal{F}_t]\\
            & = \eta_{t+1} E[M_{t+1}- M_t |\mathcal{F}_t] && \eta\text{ is predictable}\\
            & = 0 && M\text{ is a martingale}\\
        \end{align*}
    \]

    Reciprocally, for $V_0 = M_0$ and $\eta_t = 1$ for every $t$ by hypotheses, $V$ is a martingale.
    However $V_t = M_t$ for every $t$.


