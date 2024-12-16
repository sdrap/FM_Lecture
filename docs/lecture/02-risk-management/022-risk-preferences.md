# Risk Preferences and Measures

Up to now, we have presented potential examples of risk measures and discussed their shortcomings regarding particular properties we consider sound for risk assessment.
Furthermore, the selection of these measures might appear arbitrary.
In the following, we aim to formalize what *risk* and *uncertainty* mean.

On the one hand, *uncertainty* refers to the fact that multiple outcomes might occur.
In other terms, this can be understood as the consideration of a set $\Omega$ within a probability space.
The concept of uncertainty is thus an *objective* matter, inherently related to the nature of the world.

On the other hand, *risk* represents a *subjective* or personal perception of uncertainty.
It depends on one's viewpoint and can be seen as a prudent response to uncertainty.
To model this in a consistent mathematical framework, we rely on the so-called *decision theory*, which captures preferences among different possible choices.
We denote the set of possible choices $x$ by $\mathcal{X}$
In our context, uncertain outcomes are modeled as random variables, meaning we consider a vector space $\mathcal{X}$ of random variables (primarily bounded for mathematical convenience).


!!! definition "Definition: Preference Order and Numerical Representation"

    A *preference order* $\preccurlyeq$ on $\mathcal{X}$ is a binary relation $x \preccurlyeq y$ that states choice $y$ is preferred to choice $x$.
    We assume this relation fulfills the following *normative* properties:

    - **Transitivity**: $x \preccurlyeq y$ and $y \preccurlyeq z$ implies $x \preccurlyeq z$;
    - **Completeness**: for any two possible choices $x$ and $y$, then either $x \preccurlyeq y$ or $y \preccurlyeq x$.

    A function $U\colon \mathcal{X} \to \mathbb{R}$ is called a *numerical representation* (sometimes called utility) of a preference order $\preccurlyeq$ if 

    \[
        x \preccurlyeq y \quad \text{if and only if} \quad U(x)\leq U(y)
    \]

Preference orders are generic to represent the subjective view on those outcomes.
The first property tells you that if you find $y$ preferable to $x$ and $z$ preferable to $y$, then you should also find $z$ preferable to $y$.
This property seems quite natural.
The second property tells you that if you are given any two elements, you are always able to express a preference between them.
This second property is eventually strong as it requires you to always be  able to decide among any two out of a possibly infinitly large set $\mathcal{X}$ which one is the more risky.
These two rational (decision theorist would call them *normative*) assumptions are often falsified in empirical decision theory but these are meant to model a fully rational behavior in terms of decision towards these prospective outcomes.
A for a numerical representation it is a mapping of this preference ranking into $\mathbb{R}$.


??? note

    Note first, that if we have a numerical representation $U$ for a preference order $\preccurlyeq$, it is not unique.
    Any strictly increasing function $\phi \colon \mathbb{R} \to \mathbb{R}$ will define another numerical representation $\tilde{U} = \phi \circ U$.
    Indeed, $x \preccurlyeq y$ is equivalent to $U(x)\leq U(y)$ which is equivalent to $\phi(U(x)) = \tilde{U}(x) \geq \tilde{U}(y) = \phi(U(y))$.

    Second, starting directly with a function $U \colon \mathcal{X} \to \mathbb{R}$ it defines a preference order $\succcurlyeq$ by 

    \[
        x \preccurlyeq y : \Leftrightarrow U(x)\leq U(y)
    \]

    As an exercice, show that $\succcurlyeq$ so defined through a function $R$ is a preference order, that is, satisfies transitivity and completness.

    Third, even if a numerical function defines a preference order, the reciprocal is not necessarily true.
    Indeed, it requires some additional assumptions so that for a given preference order you can find a numerical representation $R$ of which.
    This is however most of the time the case under resonable assumptions.

    !!! proposition

        If the set $\mathcal{X}$ is countable(1) then any preference order $\preccurlyeq$ on $\mathcal{X}$ admits a numerical representation.
        {.annotate}

        1.  Meaning that you can enumerate it by a subset of $\mathbb{N}$.


    !!! proof

        Without loss of generality, we assume that $\mathcal{X} = \{x_1, \ldots, x_n, \ldots\}$.

        On $\mathbb{N}$ we consider the probability measure $P[\{n\}] = p_n = 1/{2^n}$ since $\sum p_n = 1$.
        Now, for each $x_n$, define $A_n = \{k\colon x_k \preccurlyeq x_n\}$ which is the set of indices $k$ of those elements in $\mathcal{X}$ which are less prefered than $x_n$.
        By definition, it holds that $x_n \preccurlyeq x_m$ if and only if $A_n \subseteq A_m$.
        The function

        \[
          \begin{equation*}
            \begin{split}
              U \colon \mathcal{X} & \longrightarrow \mathbb{R}\\
                        x_n & \longmapsto U(x_n) = P\left[ A_n \right] = \sum_{\{k\colon L_k \preccurlyeq L_n\}} p_k
            \end{split}
          \end{equation*}
        \]
    

        defines a numerical representation of $\preccurlyeq$.
        Indeed, $x_n \preccurlyeq x_m$ if and only if $A_n \subseteq A_m$.
        Since the probability measure $P$ assign a strict probability to any element of $\mathbb{N}$, it also holds that $A_n \subseteq A_m$ if and only if $U(x_n) = P[A_n] \leq P[A_m] = U(x_m)$ which ends the proof. 
        
    This proposition makes use of probability measures to define the numerical representation.
    Such an argumentation extends to more general sets as long as you can connect somehow the sublevel sets $\{\tilde{x}\colon \tilde{x}\preccurlyeq x\}$, usually using some topological arguments with smoothness.
    
    If such smoothness does not hold, then it is possible to construct examples of preference orders that might not have a numerical representation.

    !!! example "The lexicographical order does not admit a numerical representation"

        Consider $\mathcal{X} = [0, 1]\times [0, 1]$ and define the lexicographical order as

        \[
            x = (x_1, x_2) \preccurlyeq (y_1, y_2)=y \quad \text{if and only if}\quad 
            \begin{cases}
              \text{either } &x_1 < x_2 \\
              \text{or } &x_1 = x_2 \quad \text{and}\quad y_1\leq y_2
            \end{cases}
        \]

        It is relatively easy to show that this is indeed a preference order (akin to the book ordering in a library).
        However since the set if not countable and the preference order is somehow not very smooth, it is possible to show that there can not be a numerical representation of $\preccurlyeq$.
        You can give a try as an exercise by assuming that there exists such a numerical representation and show that you get a contradiction.

Decision theory usually takes the viewpoint of preference and utility (the higher the better).
To speak about risk we however think in terms of risk and consider as choices the possible loss profiles $\mathcal{L}$, that is, random variables representing losses.
Furthermore for just notatios, we consider complete binary relations $\succcurlyeq$ in the sense of $L_1 \succcurlyeq L_2$ meaning that "$L_1$ is more risky than $L_2$".
In other terms you rank loss profiles with $\succcurlyeq$ according to the preception of risk you have of both.
However, the simple properties of a preference order $\succcurlyeq$ on $\mathcal{L}$ do tno really tell us about risk perception per-se.


!!! definition "Definition: Risk Order and Risk Measures"

    A preference order $\succcurlyeq$ on $\mathcal{L}$ is called a *risk order* if the following two additional assumptions are fulfilled:

    - **Diversification**: if $L_1$ is more risky than $L_2$ then any diversified position between the two is less risky than the worse one:

        \[
            \text{if } L_1 \succcurlyeq L_2 \quad \text{then}\quad L_1 \succcurlyeq \lambda L_1 + (1-\lambda) L_2, \quad \text{for every } 0 \leq \lambda \leq 1
        \]

    - **Monotonicity (worse for sure is more risky)**: if the loss of $L_1$ are worse than the loss of $L_2$ in any states of the world, then $L_1$ is more risky than $L_2$:

        \[
            \text{if } L_1(\omega) \geq L_2 (\omega) \text{ for every } \omega \quad \text{then }\quad L_1 \succcurlyeq L_2
        \]

    A numerical representation $R\colon \mathcal{L} \to \mathbb{R}$ of a risk order is called a *risk measure*.


These two additional properties are expressing quite reasonable key features of what one might expect as a risk perception.

They do have consequences in terms of resulting properties for risk measure. 

!!! proposition
    Let $R$ be a numerical representation of a preference order $\succcurlyeq$ on $\mathcal{L}$.
    Then the following assertions are equivalent:
    
    - $\succcurlyeq$ is a risk order;
    - $R$ is:
        - *Quasi-convex*: $\max\{R(L_1), R(L_2)\} \geq R(\lambda L_1 + (1-\lambda) L_2)$ for every $0 \leq \lambda \leq 1$;
        - *Monotone*: $L_1(\omega) \geq L_2(\omega)$ for every $\omega$ implies $R(L_1) \geq R(L_2)$.

??? proof
    Let $L_1$ and $L_2$ be two loss profiles.
    Assume that $\succcurlyeq$ is a risk order.
    As for the quasi-convexity, due to the completeness of the relation, we may assume without loss of generality that $L_1 \succcurlyeq L_2$ which is equivalent to $R(L_1) = \max\{R(L_1), R(L_2)\}$.
    Now for every $0 \leq \lambda \leq 1$ it follows from the diversification property that $L_1 \succcurlyeq \lambda L_1 + (1-\lambda) L_2$ which implies $\max\{R(L_1), R(L_2)\} = R(L_1) \geq R(\lambda L_1 + (1-\lambda) L_2)$ showing quasi-convexity of $R$.

    As for the monotonicity, assume that $L_1(\omega) \geq L_2(\omega)$ for every $\omega$.
    It follows from the monotonicity assumtion that $L_1 \succcurlyeq L_2$ which implies that $R(L_1) \geq R(L_2)$ showing the monotonicity of $R$.
    
    The fact that a numerical representation is quasi-convex and monotone implies that $\succcurlyeq$ is a risk order follows the reverse argumentation and is straightforward to verify.


This proposition states in particular that neither the mean variance risk measure nor the value at risk do represent in any way an order that is a risk order.
Some additional properties can be required from a risk measure, however they might not be representative of the risk order itself.

!!! definition

    A risk measure $R$ is called

    * **Cash-Invariance:** if $R(L-m) = R(L) - m$ for every $m$ in $\mathbb{R}$;
    * **Positive-Homogeneous:** if $R(\lambda L) = \lambda R(L)$ for every $\lambda >0$;
    * **Law-Invariant:** if $R(L) = R(\tilde{L})$ whenever the CDF of $L$ and $\tilde{L}$ coincide.


Aside from the law-invariance, the other two properties do no longer hold if I transform the risk measure with a strictly increasing transformation.
Nevertheless they are common and useful for practical reasons.


!!! remark "Cash-Invariance"

    The cash-invariance is something that is usually required from a regulatory or financial viewpoint.
    The reasoning goes as follows: a financial institution has a position $X$ in risky assets.
    The question is how much liquidity (cash) $m$ shall be present in the bank account so that the overall position (cash plus risky assets) yields an acceptable risk.
    The threshold required is that an overall position is deemed acceptable if the total risk assessment is below $0$.
    The total loss profile being $L-m$ where $L= - X$, it means that $0\geq R(L-m) = R(L) - m$ due to cash invariance or $m\geq R(L)$.
    In other terms, the minimal amount of liquidity so that the risky position in assets of the institution is deemd acceptable is $m = R(L)$.
    Therefore the interpretation of the risk measure as a capital requirement.
    The cash-invariance has also some interesting consequences for a risk measure since cash-invariance plus quasi-convexity implies convexity.

    !!! lemma
        Let $R$ be a cash-invariant risk measure, then $R$ is convex.

    
    ??? proof
        
        Let $R$ be a cash-invariant risk measure, $0\leq \lambda \leq 1$ and $L_1$, $L_2$ be two loss profiles.
        We want to show that $R(\lambda L_1 + (1-\lambda)L_2)\leq \lambda R(L_1) + (1-\lambda)R(L_2)$.
        Defining $m_1 = R(L_1)$ and $m_2 = R(L_2)$, it is equivalent to show $R(\lambda L_1 + (1-\lambda)L_2) - \lambda m_1 - (1-\lambda)m_2 \leq 0$.
        By cash invariance and quasiconvexity we get

        \[
          \begin{align*}
            R(\lambda L_1 + (1-\lambda)L_2) - \lambda m_1 - (1-\lambda)m_2 & = R\left( \lambda L_1 + (1-\lambda) L_2 - \lambda m_1 - (1-\lambda)L_2 \right) && \text{(Cash Invariance)}\\
              & = R\left( \lambda (L_1 - m_1) + (1-\lambda)(L_2 - m_2) \right)\\
              & \leq \max \left\{ R(L_1 - m_1), R(L_2 - m_2) \right\} && \text{(Quasiconvexity)}\\
              & = \max \left\{ R(L_1) - m_1, R(L_2) - m_2 \right\} && \text{(Cash Invariance)}\\
              & = \max \{0, 0\} = 0 && (m_i = R(L_i))\\
              & = 0
          \end{align*}
        \]

!!! remark "Positive Homogeneity"

    Positive homogeneity also has a financial interpretation.
    If $L$ represents the loss exposure of an investment with risk $R(L)$, then scaling this investment by a factor $\lambda >0$ will also scale the corresponding risk by $\lambda$.
    That such a property is desirable is not totally clear, one would rather expect a super linear scaling of the risk.
    However positive homogeneity do have many properties that are desirable from a mathematical/implementation viewpoint. 
    As seen later in the next chapter, it is the underlying reason that one can get a decomposition in terms of marginal risk of the total risk.
    Furthermore it has the property of sub-additivity

    !!! lemma

        Let $R$ be a cash-invariant risk measure.
        If $R$ is positive homogeneous, it holds that

        \[
            R(L_1 + L_2) \leq R(L_1) + R(L_2)
        \]
    
    ??? proof
        
        Let $R$ be a cash-invariant risk measure which is positive homogeneous.
        Due to the cash invariance, $R$ is convex.
        It follows from convexity and positive homogeneity that

        \[
          \begin{align*}
            R( L_1 + L_2) & = R\left( 2 \left(\frac{1}{2}L_1 +\frac{1}{2}L_2\right)\right)\\
              & = 2 R\left(\frac{1}{2}L_1 +\frac{1}{2}L_2\right)&& \text{(Positive Homogeneity)}\\
              & \leq 2 \left( \frac{1}{2}R(L_1) + \frac{1}{2}R(L_2)\right) && \text{(Convexity)}\\
              & = R(L_1) +R(L_2)
          \end{align*}
        \]


