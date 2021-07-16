import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots

def myLayout(title, x_title, y_title, mode, width, height, margin):
    return go.Layout(
        title=title,
        yaxis=dict(title=x_title),
        xaxis=dict(title=y_title),
        legend=dict(x=0, y=1.0, bgcolor='rgba(255, 255, 255, 0)',
                    bordercolor='rgba(255, 255, 255, 0)'),
        barmode=mode,
        bargap=0.15,
        bargroupgap=0.1,
        width=width,
        height=height,
        margin=margin
    )


def BarTrace(x, y, names):
    trace = []
    for i in range(y.shape[0]):
        trace1 = go.Bar(
            x=x,
            y=y[i],
            name=names[i]
        )
        trace.append(trace1)
    return trace


def barChart(x, y, names, title="", x_title="x", y_title="y", mode='group', full=False):
    width = None
    height = None
    margin = None
    if not (full):
        width = 540
        height = 460
        margin = dict(b=12, l=12, pad=0, r=6, t=54)
    trace = BarTrace(x=x, y=y, names=names)
    fig = go.Figure(data=trace, layout=myLayout(
        title, x_title, y_title, mode, width, height, margin))
    fig.show()


def scatter(df, x, y, c=None, s=None, mx=None, my=None, af=None, fit=None):
    fig = px.scatter(df, x=x, y=y, color=c, size=s, marginal_y=my,
                     marginal_x=mx, trendline=fit, animation_frame=af)
    fig.show()


def scatter3D(df, x, y, z, c=None, s=None, mx=None, my=None, af=None, fit=None):
    fig = px.scatter_3d(df, x=x, y=y, z=z, color=c, size=s,
                        animation_frame=af, size_max=18)
    fig.show()


def histogram(hist_data, group_labels, bin_size=1, curve_type='normal', show_hist=True, invert=False):
    if(invert):
        hist_data.reverse()
        group_labels.reverse()
    fig = ff.create_distplot(hist_data, group_labels, bin_size=bin_size,
                             curve_type=curve_type, show_hist=show_hist)
    fig.update_layout()
    fig.show()


def hist(sr):
  x = ["Id: " + str(i) for i in sr.index]
  fig = px.histogram(x=x, y=sr.values)
  fig.show()


def mult_hist(sr, rows, cols, title_text, subplot_titles):
  fig = make_subplots(rows=rows, cols=cols, subplot_titles=subplot_titles)
  for i in range(rows):
    for j in range(cols):
      x = ["-> " + str(i) for i in sr[i+j].index]
      fig.add_trace(go.Bar(x=x, y=sr[i+j].values ), row=i+1, col=j+1)
  fig.update_layout(showlegend=False, title_text=title_text)
  fig.show()
