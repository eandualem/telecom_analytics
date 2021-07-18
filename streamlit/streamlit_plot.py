def hist(sr):
    x = [" " + str(i) for i in sr.index]
    fig = px.histogram(x=x, y=sr.values, height=700)
    st.plotly_chart(fig)


def histogram(hist_data, group_labels, bin_size=1, curve_type='normal', show_hist=True, invert=False):
    if(invert):
        hist_data.reverse()
        group_labels.reverse()
    fig = ff.create_distplot(hist_data, group_labels, bin_size=bin_size,
                             curve_type=curve_type, show_hist=show_hist)
    fig.update_layout()
    st.plotly_chart(fig)

def scatter(df, x, y, c=None, s=None, mx=None, my=None, af=None, fit=None):
    fig = px.scatter(df, x=x, y=y, color=c, size=s, marginal_y=my,
                     marginal_x=mx, trendline=fit, animation_frame=af)
    st.plotly_chart(fig)


def scatter3D(df, x, y, z, c=None, s=None, mx=None, my=None, af=None, fit=None):
    fig = px.scatter_3d(df, x=x, y=y, z=z, color=c, size=s,
                        animation_frame=af, size_max=18)
    st.plotly_chart(fig)

