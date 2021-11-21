from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html


import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
import dash


def create_app(data=None, fqs=None, trials=3, frames=3, title="T", xlabel="C"
               , ylabel="C", fr=None, tr=None, bands=False, cat_labels=None):
        
    app = dash.Dash(__name__)
    
    app.layout = html.Div([
        # html.Button('update', id='update'),
        dcc.Dropdown(
            id='trial',
            options=[{'label': int(i+1), 'value': int(i)} for i in tr],
            value=tr[0]
        ),
        dcc.Graph(id='updated-graph')
        ,
        dcc.Slider(
                id='frame',
                min=1,
                max=len(fr)-1,
                step=1,
                value=1,
                marks={i : "{} ms".format(fr[i]) for i in range(len(fr))
                },
            ),
            html.Div(id='slider-output')
        
    ])
    
    trial_ind = dict()
    cnt = 0
    for i in tr:
        
        trial_ind[i] = cnt
        cnt += 1
    
    @app.callback(
            Output('updated-graph', 'figure')
            , inputs=[
                Input('trial', 'value'), Input('frame', 'value')
            ],
            states=[
                State('trial', 'value'), State('frame', 'value')
            ]) 
    
    def update_1(value1, value2):
        
        ych = [data.shape[1] - i - 1 for i in range(data.shape[1])]
        im = data[int(value2)-1, ych, :, trial_ind[int(value1)]]
        y = [str(data.shape[1] - i) for i in range(data.shape[1])]
        yinv = []
        # print(im.shape)
        for i in range(len(y)-1, -1, -1):
            yinv.append(y[i])
        if data.shape[1] == data.shape[2]:
            t = yinv
        else:
            t = fqs
            
        tit = title + ", Frame no. " + str(int(value2)) + " of trial/section no. " + str(int(value1)+1) + " for t in range [" + str(fr[int(value2)-1]) + "] - [" + str(fr[int(value2)]) + "]"
        
        bandlabels = ["Delta[0.1-3]", "Theta[3-8]", "Alpha[8-12]"
                      , "L-Beta[12-16]", "M-Beta[16-20]", "U-Beta[20-30]"
                      , "L-Gamma[30-50]", "M-Gamma[50-70]", "U-Gamma[70-100]"
                      , "UI-Gamma[100-150]", "UII-Gamma[150-200]", "UIII-Gamma[200-250]"]
        
        if bands==True:
            return {
                'data':[go.Heatmap(z=im, y=y, x=bandlabels)]
                , 'layout': go.Layout(autosize=False,
                        width=1420,
                        height=600,
                        title=tit,
                        xaxis=dict(title=xlabel),
                        yaxis=dict(title=ylabel)
                        )
                }
        elif not cat_labels==None:
             yl = list(reversed(cat_labels))
             return {
                 'data':[go.Heatmap(z=im, y=yl, x=cat_labels)]
                 , 'layout': go.Layout(autosize=False,
                         width=1420,
                         height=600,
                         title=tit,
                         xaxis=dict(title=xlabel),
                         yaxis=dict(title=ylabel)
                         )
                 }
         
        return {
            'data':[go.Heatmap(z=im, y=y, x=t)]
            , 'layout': go.Layout(autosize=False,
                    width=1420,
                    height=600,
                    title=tit,
                    xaxis=dict(title=xlabel),
                    yaxis=dict(title=ylabel)
                    )
            }
    
    return app


def create_app_scatter(data=None, y=None, dim=3, frames=3, title="T", xlabel="C"
               , ylabel="C", fr=None, trials=None, bands=False):
        
    app = dash.Dash(__name__)
    
    app.layout = html.Div([

        dcc.Graph(id='updated-graph')
        ,
        dcc.Slider(
                id='frame',
                min=1,
                max=len(fr)-1,
                step=1,
                value=1,
                marks={i : "{} ms".format(fr[i]) for i in range(len(fr))
                },
            ),
            html.Div(id='slider-output')
        
    ])
    
    @app.callback(
            Output('updated-graph', 'figure')
            , inputs=[
                Input('frame', 'value')
            ],
            states=[
                State('frame', 'value')
            ]) 
    
    def update_1(value1):
        
        x = data[int(value1)-1, :, :]
        cat = y
        tit = title + ", Frame no. " + str(int(value1)) + " for t in range [" + str(fr[int(value1)-1]) + "] - [" + str(fr[int(value1)]) + "]"

        if dim==2:
            df = pd.DataFrame({
            'cat':cat, 'col_x':x[:, 0], 'col_y':x[:, 1], 'trial':trials
            })
            df.head()
            
             
            fig = px.scatter(df, x='col_x', y='col_y',
                                color='cat',
                                title=tit)
            
            fig.update_layout(
                width=1440,
                height=680,
            )
            
            return fig
        
        elif dim==3:
            df = pd.DataFrame({
            'cat':cat, 'col_x':x[:, 0], 'col_y':x[:, 1],
            'col_z':x[:, 2], 'trial':trials
            })
            df.head()
            fig = px.scatter_3d(df, x='col_x', y='col_y', z='col_z',
                                color='cat', text='trial',
                                title=tit)
            
            fig.update_layout(
                width=1440,
                height=680,
            )
            
            return fig
    
    return app


def heatmap(data=None, fqs=None, trials=1, frames=1, title="title", xlabel="x", ylabel="y"
        ,fr=None, tr=None, bands=False, cat_labels=None):
    
    fr = get_frames(fr=fr, frames=frames)
    app = create_app(data=data, fqs=fqs, trials=trials, frames=frames, title=title
                     , xlabel=xlabel, ylabel=ylabel, fr=fr, tr=tr, bands=bands,
                     cat_labels=cat_labels)
    # app.run_server(debug=False, use_reloader=False)
    return app


def scatter(data=None, y=None, dim=3, frames=1, title="title", xlabel="x", ylabel="y"
        ,fr=None, trials=None, bands=False):
    
    fr = get_frames(fr=fr, frames=frames)
    app = create_app_scatter(data=data, y=y, dim=dim, frames=frames, title=title
                     , xlabel=xlabel, ylabel=ylabel, fr=fr, trials=trials, bands=bands)
    # app.run_server(debug=False, use_reloader=False)
    return app


def get_frames(fr=None, frames=1):
    
    if fr==None:
        fr = [i for i in range(frames + 1)]
    
    return fr

