# Stochastic Processes

Stochastic processes mean that you want to carry over *time* the idea that outcomes will be revealed as time goes by.
Considering for instance your view of the evolution of a financial asset.
At the very begining your decisions towards it relies only on what you can forsee in the future about its evolution however as times goes buy you learn more and more infromation about the nature of this financial asset.

Let us consider the following example


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

The answer to the second question is that all the games in expectation are equal.

