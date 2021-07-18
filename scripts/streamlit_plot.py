def scatter(df, x, y, c=None, s=None, mx=None, my=None, af=None, fit=None, interactive=False):
    fig = px.scatter(df, x=x, y=y, color=c, size=s, marginal_y=my,
                     marginal_x=mx, trendline=fit, animation_frame=af)
    if(interactive):
        st.plotly_chart(fig)
    else:
        st.image(pio.to_image(fig, format='png', width=1200))


def scatter3D(df, x, y, z, c=None, s=None, mx=None, my=None, af=None, fit=None, rotation=[1, 1, 1], interactive=False):
    fig = px.scatter_3d(df, x=x, y=y, z=z, color=c, size=s,
                        animation_frame=af, size_max=18)

    fig.update_layout(scene=dict(camera=dict(eye=dict(x=rotation[0], y=rotation[1], z=rotation[2]))),
                      )
    if(interactive):
        st.plotly_chart(fig)
    else:
        st.image(pio.to_image(fig, format='png', width=1200))


def hist(sr, interactive=False):
    x = ["Id: " + str(i) for i in sr.index]
    fig = px.histogram(x=x, y=sr.values)
    if(interactive):
        st.plotly_chart(fig)
    else:
        st.image(pio.to_image(fig, format='png', width=1200))


def mult_hist(sr, rows, cols, title_text, subplot_titles, interactive=False):
    fig = make_subplots(rows=rows, cols=cols, subplot_titles=subplot_titles)
    for i in range(rows):
        for j in range(cols):
            x = ["-> " + str(i) for i in sr[i+j].index]
            fig.add_trace(go.Bar(x=x, y=sr[i+j].values), row=i+1, col=j+1)
    fig.update_layout(showlegend=False, title_text=title_text)
    if(interactive):
        st.plotly_chart(fig)
    else:
        st.image(pio.to_image(fig, format='png', width=1200))
