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
    fig = px.scatter_3d(df, x=x, y=y, z=z, color=c, size=s, animation_frame=af)
    fig.show()
