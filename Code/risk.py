#%%

from lib.standard_lib import *
from IPython.display import display, HTML


import plotly
plotly.offline.init_notebook_mode()
display(HTML(
    '<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-MML-AM_SVG"></script>'
))
import numpy as np
from scipy.stats import norm
#%%


# Generate data for the normal distribution
x = np.linspace(-4, 4, 500)
cdf = norm.cdf(x)

# Calculate 90% quantile
quantile_90 = norm.ppf(0.90)

# Create the figure
fig = go.Figure()

# Add the CDF line
fig.add_trace(go.Scatter(x=x, y=cdf, mode='lines', name='CDF', line=dict(color=plt_colors[0])))

# Add the vertical line at the origin

fig.add_shape(
    type="line",
    x0=-4,
    y0=0.9,
    x1=4,
    y1=0.9,
    line=dict(color=plt_colors[2], width=2, dash="dash"),
    )

fig.add_annotation(
    x= -3,
    y=0.95,
    text=r'$\text{Confidence Level }1-\alpha\\$',
    showarrow=False,
    font=dict(size=24, color=plt_colors[2])
)



fig.add_shape(type="line", x0=quantile_90, y0=0, x1=quantile_90, y1=0.9,
              line=dict(color=plt_colors[1], width=2, dash="dash"))

# Annotate the quantile with '$V@R_{\\alpha}$'
fig.add_annotation(
    x=quantile_90, 
    y=0, 
    text=r'$V@R_{\alpha}(L)$',
    showarrow=True,
    arrowhead=2,
    ax=80,
    ay=-50,
    font=dict(size=24, color=plt_colors[1]),  # Bigger text size and color
    arrowcolor=plt_colors[1],  # Arrow color
    arrowsize=2 
    )

fig.add_annotation(
    x=-1, 
    y=norm.cdf(-1), 
    text=r'$m \mapsto F_L(m) = P[L\leq m]$',
    showarrow=True,
    arrowhead=2,
    ax=-120,
    ay=-50,
    font=dict(size=24, color=plt_colors[0]),  # Bigger text size and color
    arrowcolor=plt_colors[0],  # Arrow color
    arrowsize=2 
    )


fig.add_trace(go.Scatter(x=x, y=cdf, mode='lines', name='CDF', line=dict(color=plt_colors[0])))


# Remove the grid and update layout
fig.update_layout(showlegend=False,
                  xaxis=dict(visible = False),
                  yaxis=dict(visible = False, range = [-0.1, 1.1]),
                  margin=dict(l=20, r=20, t=20, b=20))

# Show the plot

fig_white = fig
fig_black = fig
fig_white.add_hline(y=0, line_color='black', line_width=2)
fig_white.add_hline(y=1, line_color='black', line_width=2)
fig_white.add_vline(x=0, line_color='black', line_width=1)
fig_white.update_layout(template = "plotly_white+draft")
fig_white.write_image("./../docs/images/var_white.svg")
fig_black.add_hline(y=0, line_color='grey', line_width=2)
fig_black.add_hline(y=1, line_color='grey', line_width=2)
fig_black.add_vline(x=0, line_color='grey', line_width=1)
fig_black.update_layout(template = "plotly_dark+draft")
fig_black.write_image("./../docs/images/var_dark.svg")
