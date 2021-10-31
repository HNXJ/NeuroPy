from dash.dependencies import Input, Output, State
from dash import html
from dash import dcc

import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
import numpy as np

import dash


def create_app(data=None, fqs=None, trials=3, frames=3, title="T", xlabel="C"
               , ylabel="C", fr=None, tr=None, bands=False):
        
    app = dash.Dash(__name__)
    
    app.layout = html.Div([
        # html.Button('update', id='update'),
        dcc.Dropdown(
            id='trial',
            options=[{'label': int(i+1), 'value': int(i)} for i in tr],
            value=tr[0]
        ),
        # dcc.Dropdown(
        #     id='frame',
        #     options=[{'label': int(i+1), 'value': int(i)} for i in range(len(fr)-1)],
        #     value='0'
        # ),
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
                # Input('update', 'n_clicks'), 
                Input('trial', 'value'), Input('frame', 'value')
            ],
            states=[
                State('trial', 'value'), State('frame', 'value')
            ]) 
    def update_1(value1, value2):
        
        # if n_clicks is None:
        #     return dash.no_update
        im = data[int(value2)-1, :, :, trial_ind[int(value1)]]
        y = np.array([data.shape[1] - i for i in range(data.shape[1])])
        
        if data.shape[1] == data.shape[2]:
            t = y
        else:
            t = fqs
        tit = title + ", Frame no. " + str(int(value2)) + " of trial no. " + str(int(value1)+1) + " for t in range [" + str(fr[int(value2)-1]) + "] - [" + str(fr[int(value2)]) + "]"
        
        bandlabels = ["Delta[0.1-3]", "Theta[3-8]", "Alpha[8-12]"
                      , "L-Beta[12-16]", "M-Beta[16-20]", "U-Beta[20-30]"
                      , "L-Gamma[30-50]", "M-Gamma[50-70]", "U-Gamma[70+]"]
        
        # annotations = []
        # for i in range(k):
        #     annotation = {
        #         'x': ((i+0.1)),
        #         'y': 0.5,
        #         'xref': 'x',
        #         'yref': 'y',
        #         'text': bandlabels[i],
        #         'align': 'center',
        #         'ay': 0,
        #         'opacity': 0,
        #         'bgcolor': 'green',
        #     }
        #     annotations.append(annotation)
        if bands:
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
               , ylabel="C", fr=None, tr=None, bands=False):
        
    app = dash.Dash(__name__)
    
    app.layout = html.Div([
        # html.Button('update', id='update'),
        # dcc.Dropdown(
        #     id='trial',
        #     options=[{'label': int(i+1), 'value': int(i)} for i in tr],
        #     value=tr[0]
        # ),
        # dcc.Dropdown(
        #     id='frame',
        #     options=[{'label': int(i+1), 'value': int(i)} for i in range(len(fr)-1)],
        #     value='0'
        # ),
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
                # Input('update', 'n_clicks'), 
                # Input('trial', 'value'), 
                Input('frame', 'value')
            ],
            states=[
                # State('trial', 'value'),
                State('frame', 'value')
            ]) 
    def update_1(value1):
        
        x = data[int(value1)-1, :, :]
        cat = y
        tit = title + ", Frame no. " + str(int(value1)) + " for t in range [" + str(fr[int(value1)-1]) + "] - [" + str(fr[int(value1)]) + "]"

        if dim==2:
            df = pd.DataFrame({
            'cat':cat, 'col_x':x[:, 0], 'col_y':x[:, 1]
            })
            df.head()
            
             
            fig = px.scatter(df, x='col_x', y='col_y',
                                color='cat',
                                title=tit)
            
            fig.update_layout(
                width=1420,
                height=600,
            )
            
            return fig
        
        elif dim==3:
            df = pd.DataFrame({
            'cat':cat, 'col_x':x[:, 0], 'col_y':x[:, 1], 'col_z':x[:, 2]
            })
            df.head()
            fig = px.scatter_3d(df, x='col_x', y='col_y', z='col_z',
                                color='cat',
                                title=tit)
            
            fig.update_layout(
                width=1420,
                height=600,
            )
            
            return fig
    
    return app


def heatmap(data=None, fqs=None, trials=1, frames=1, title="", xlabel="", ylabel=""
        ,fr=None, tr=None, bands=False):
    
    if fr==None:
        fr = [i for i in range(frames + 1)]
        
    app = create_app(data=data, fqs=fqs, trials=trials, frames=frames, title=title
                     , xlabel=xlabel, ylabel=ylabel, fr=fr, tr=tr, bands=bands)
    app.run_server(debug=False, use_reloader=False)
    

def scatter(data=None, y=None, dim=3, frames=1, title="", xlabel="", ylabel=""
        ,fr=None, tr=None, bands=False):
    
    if fr==None:
        fr = [i for i in range(frames + 1)]
        
    app = create_app_scatter(data=data, y=y, dim=dim, frames=frames, title=title
                     , xlabel=xlabel, ylabel=ylabel, fr=fr, tr=tr, bands=bands)
    app.run_server(debug=False, use_reloader=False)

