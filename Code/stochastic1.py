#%%

from lib.standard_lib import *
from lib.functions import *
from IPython.display import display, HTML


import plotly
plotly.offline.init_notebook_mode()
display(HTML(
    '<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-MML-AM_SVG"></script>'
))
#%%

# define the symetric random walk
T = 100
start = 100
paths = 5
seed = 150,

X = np.arange(100+1)
Y = random_walk(T, start = start, paths = paths, seed = seed)

# Create the figure
fig = go.Figure()

for k in range(paths):
    fig.add_scatter(
        x=X,
        y=Y[:, k],
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


#%%

# gemoetric random walk

# define the symetric random walk
T = 100
start = 100
paths = 3
seed = 108,
u = 0.05
d = 1/1.05 - 1

X = np.arange(T+1)
Y = geom_walk(T, start = start, u = u, d= d, paths = paths, seed = seed)

# Create the figure
fig = go.Figure()

for k in range(paths):
    fig.add_scatter(
        x=X,
        y=Y[:, k],
        mode='lines',
        name=f"Random walk {k+1}",
        showlegend=False,
        line_shape = 'linear'
    )


fig.update_layout(template = "plotly_white+draft")

fig.show()



#%%


#%%

# Asian Option

# define the geom random walk
T = 100
start = 100
paths = 3
seed = 101,
u = 0.05
d = 1/1.05 - 1

X = np.arange(T+1)
Y = geom_walk(T, start = start, u = u, d= d, paths = paths, seed = seed)

# Create the figure
fig = go.Figure()

for k in range(paths):
    fig.add_scatter(
        x=X,
        y=Y[:, k],
        mode='lines',
        name=f"Random walk {k+1}",
        showlegend=False,
        line_shape = 'linear',
        line = dict(color = plt_colors[k]),
        opacity = 1
    )
    avg = Y[:, k].cumsum() / np.arange(1, T+2)
    fig.add_scatter(
        x=X,
        y=avg,
        mode='lines',
        name=f"Average walk {k+1}",
        showlegend=False,
        line_shape = 'linear',
        line=dict(dash='dash', color = plt_colors[k]),
        opacity=1
    )


fig.update_layout(
    showlegend=False,
    xaxis=dict(
        showline = False,
        zeroline = False,
        showgrid = True,
        showticklabels = True,
        tickmode = 'array',
        tickvals = [0, 100],
        ticktext = [r'$0$',r'$T$'],
        range = [-0.2, 100.2]
        ),
    yaxis=dict(
        showline = False,
        zeroline = False,
        showgrid = True,
        tickmode = 'array',
        tickvals = [100, 110],
        ticktext = [r'$S_0$',r'$K$'],
    )
)
fig_white = fig
fig_black = fig

fig_white.add_hline(y = 110, line_color = "black", line_width = 2)
fig_white.update_layout(template = "plotly_white+draft")
fig_white.write_image("./../docs/images/asian_white.svg")
fig_white.add_hline(y = 110, line_color = "grey", line_width = 2)
fig_black.update_layout(template = "plotly_dark+draft")
fig_black.write_image("./../docs/images/asian_dark.svg")

#%%

#%%

# Barrer Option

# define the geom random walk
T = 100
start = 100
paths = 3
seed = 101,
u = 0.05
d = 1/1.05 - 1

X = np.arange(T+1)
Y = geom_walk(T, start = start, u = u, d= d, paths = paths, seed = seed)

# Create the figure
fig = go.Figure()

for k in range(paths):
    fig.add_scatter(
        x=X,
        y=Y[:, k],
        mode='lines',
        name=f"Random walk {k+1}",
        showlegend=False,
        line_shape = 'linear',
        line = dict(color = plt_colors[k]),
        opacity = 1
    )

    fig.add_scatter(
        x=X,
        y=np.maximum.accumulate(Y[:, k]),
        mode='lines',
        name=f"Random walk {k+1}",
        showlegend=False,
        line_shape = 'linear',
        line = dict(color = plt_colors[k], dash = 'dash'),
        opacity = 0.3
    )


fig.add_hline(y = 160, line_color = plt_colors[-3], line_width = 2)

fig.update_layout(
    showlegend=False,
    xaxis=dict(
        showline = False,
        zeroline = False,
        showgrid = True,
        showticklabels = True,
        tickmode = 'array',
        tickvals = [0, 100],
        ticktext = [r'$0$',r'$T$'],
        range = [-0.2, 100.2]
        ),
    yaxis=dict(
        showline = False,
        zeroline = False,
        showgrid = True,
        tickmode = 'array',
        tickvals = [100, 110, 160],
        ticktext = [r'$S_0$',r'$K$', r'$B$'],
    )
)

fig_white = fig
fig_black = fig

fig_white.add_hline(y = 110, line_color = "black", line_width = 2)
fig_white.update_layout(template = "plotly_white+draft")
fig_white.write_image("./../docs/images/barrer_white.svg")
fig_white.add_hline(y = 110, line_color = "grey", line_width = 2)
fig_black.update_layout(template = "plotly_dark+draft")
fig_black.write_image("./../docs/images/barrer_dark.svg")

fig_white.show()



