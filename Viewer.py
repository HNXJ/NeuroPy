import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import dash


def create_app(trials=3, frames=3, title="T", xlabel="C", ylabel="C"):
        
    app = dash.Dash(__name__)
    
    app.layout = html.Div([
        html.Button('update', id='update'),
        dcc.Dropdown(
            id='trial',
            options=[{'label': int(i+1), 'value': int(i)} for i in range(trials)],
            value='0'
        ),
        dcc.Dropdown(
            id='frame',
            options=[{'label': int(i+1), 'value': int(i)} for i in range(frames)],
            value='0'
        ),
        dcc.Graph(id='updated-graph')
    ])
    
    @app.callback(
            Output('updated-graph', 'figure'), inputs=[
                Input('update', 'n_clicks'), Input('trial', 'value'), Input('frame', 'value')
            ],
            states=[
                State('trial', 'value'), State('frame', 'value')
            ])
    
    def update_1(n_clicks, value1, value2):
        
        if n_clicks is None:
            return dash.no_update
            
        im = np.random.rand(10, 10) * int(value1) + int(value2)
        y = np.arange(10)
        t = y
        
        return {
            'data':[go.Heatmap(z=im, y=y, x=t)], 'layout': go.Layout(
                    title=title,
                    xaxis=dict(title=xlabel),
                    yaxis=dict(title=ylabel)
                )
        }
    
    return app


def run():
    
    app = create_app(trials=5, frames=4)
    app.run_server(debug=False, use_reloader=False)
    
