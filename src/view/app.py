import dash
from dash import Dash, html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
from pages import inventory

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )

app.layout = dbc.Container([
	html.H1("Store Admin Portal",
                        className='text-center text-primary mb-4'),
    html.Div([
        dcc.Tabs(id="tabs", value='tab-1', className='nav-tabs', children=[
            dcc.Tab(label='Items', value='tab-1'),
            dcc.Tab(label='Users', value='tab-2'),
            dcc.Tab(label='Current Orders', value='tab-3'),
            dcc.Tab(label='Previous Orders', value='tab-4')
        ]),
        html.Div(id='tabs-content')
         ],
        className='card bg-primary mb-3',
        style={'width': '80%', 'align': 'center'})
])

# ---------- Callbacks ----------

@callback(Output('tabs-content', 'children'),
              Input('tabs', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H6("Item:"),
              dcc.Textarea(
                    id='textarea-user',
                    placeholder='Enter Item Name',
                    rows='1',
                    maxLength='32',
                    style={'width': '80%'}),
              html.H6("Value:"),
              dcc.Textarea(
                    id='textarea-pass',
                    placeholder='Value',
                    rows='1',
                    maxLength='32',
                    style={'width': '80%'}),
              html.Div(),
              html.Button('Submit', id='textarea-state-button', n_clicks=0),
              html.Div(id='textarea-state-example-output', style={'whiteSpace': 'pre-line'})
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Tab content 2')
        ])
    elif tab == 'tab-3':
        return html.Div([
            html.H3('Tab content 3')
        ])
    elif tab == 'tab-4':
        return html.Div([
            html.H3('Tab content 4')
        ])
    

# Run this app with `python3 app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
if __name__ == '__main__':
    app.run(debug=True)
