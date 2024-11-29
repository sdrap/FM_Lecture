# Notations

The following notations will be used throughout the course:

- **Natural Numbers:** $\mathbb{N} = \{1, 2, \ldots\}$, $\mathbb{N}_0 = \{0, 1, 2, \ldots\}$.
- **Integers:** $\mathbb{Z} = \{\ldots, -2, -1, 0, 1, 2, \ldots\}$
- **Rational Numbers:** $\mathbb{Q} = \{ p/q\colon p \in \mathbb{Z}, q \in \mathbb{N}\}$
- **Real Numbers:** $\mathbb{R}$
- Vectors in $\mathbb{R}^d$ are denoted in bold font, $\boldsymbol{x} = (x^1, \dots, x^d)$, and are assumed to be column vectors.  
- Vectors with positive components $\mathbb{R}^d_+ = \{\boldsymbol{x} \in \mathbb{R}^d : x^k \geq 0, k=1,\ldots,d\}$ and vectors with strictly positive components $\mathbb{R}^d_{++} = \{\boldsymbol{x} \in \mathbb{R}^d : x^k > 0, k=1,\ldots,d\}$.  
- **Scalar Product:** $\boldsymbol{x} \cdot \boldsymbol{y} := \sum x_k y_k$ denotes the scalar product of $\boldsymbol{x}$ and $\boldsymbol{y}$ in $\mathbb{R}^d$.  
- $\beta \boldsymbol{x} := (\beta x_1, \ldots, \beta x_d)$ represents the multiplication of $\boldsymbol{x}$ in $\mathbb{R}^d$ by a scalar $\beta \in \mathbb{R}$.  
- $\boldsymbol{x} + \boldsymbol{y} := (x_1 + y_1, \ldots, x_d + y_d)$ represents vector addition in $\mathbb{R}^d$.  
- For scalars $x, y \in \mathbb{R}$, the following notations are used:  

    $$
      x \vee y = \max\{x, y\}, \quad x \wedge y = \min\{x, y\}, \quad x^+ = \max\{x, 0\}, \quad x^- = \max\{-x, 0\}.
    $$

    Notably, $x = x^+ - x^-$ and $|x| = x^+ + x^-$.  

