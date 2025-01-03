#%%

from lib.standard_lib import *
from IPython.display import display, HTML


import plotly
plotly.offline.init_notebook_mode()
display(HTML(
    '<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-MML-AM_SVG"></script>'
))
#%%

# define the symetric random walk

def random_walk(start, T):
    x = np.zeros(T+1)
    x[0] = start
    for t in range(1, T+1):
        x[t] = x[t-1] + np.random.choice([-1, 1])
    return x

X = np.arange(100+1)
Y = random_walk(100, 100)

# Create the figure
fig = go.Figure()

for k in range(5):
    fig.add_scatter(
        x=X,
        y=random_walk(100, 100),
        mode='lines',
        name=f"Random walk {k+1}",
        showlegend=False
    )


fig.update_layout(template = "plotly_white+draft")

fig.show()

#%%
fig_white = fig
fig_black = fig
fig_white.update_layout(template = "plotly_white+draft")
fig_white.write_image("./../docs/images/rw_white.svg")
fig_black.update_layout(template = "plotly_dark+draft")
fig_black.write_image("./../docs/images/rw_dark.svg")
