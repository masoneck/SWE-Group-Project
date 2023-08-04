import dash
from dash import Dash, html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
#from pages import inventory

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
          Input('tabs', 'value')
          )
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H6("Item:"),
              dcc.Textarea(
                    id='textarea-item',
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
              html.Button('Submit', id='submit-button1', n_clicks=0),
              html.Div(
                  html.Div(id='items-output', style={'whiteSpace': 'pre-line'}),
                  className='bg-white', 
                  style={'width' : '80%'})
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H6("User:"),
            dcc.Textarea(
                    id='textarea-user',
                    placeholder='User Name',
                    rows='1',
                    style={'width': '80%'}),
            html.H6("Value:"),
            dcc.Textarea(
                    id='textarea-pass',
                    placeholder='Value',
                    rows='1',
                    style={'width': '80%'}),
            html.Div(),
            html.Button('Submit', id='submit-button2', n_clicks=0),
            html.Div(
                html.Div(id='users-output', style={'whiteSpace': 'pre-line'}),
                className='bg-white', 
                style={'width' : '80%'})
        ])
    elif tab == 'tab-3':
        return html.Div([
            html.H6("List of Current Orders:"),
            html.P("Sort by:"),
            dcc.Dropdown(['Date', 'Customer','Order Cost'], 'Date', id='selector1'),
            html.Div(
                html.Div(id='curr-orders-output', style={'whiteSpace': 'pre-line'}),
                className='bg-secondary', 
                style={'width' : '80%'})
        ])
    elif tab == 'tab-4':
        return html.Div([
            html.H6("List of Previous Orders:"),
            html.P("Sort by:"),
            dcc.Dropdown(['Date', 'Customer','Order Cost'], 'Date', id='selector2'),
            html.Div(
                html.Div(id='prev-orders-output', style={'whiteSpace': 'pre-line'}),
                className='bg-secondary', 
                style={'width' : '80%'})
        ])
    
@callback(
    Output('items-output', 'children'),
    Input('submit-button1', 'n_clicks'),
    State('textarea-item', 'value')
    )
def update_output(n_clicks, value):
    lines = ["one line", "two line", "three line"] #Load db strings here
    childlist = []
    i = 0
    for each in lines:
        childlist.append(html.Tr(lines[i]))
        i += 1
    if n_clicks > 0:
            return html.Table(className='table table-striped table-active', children=childlist)
        
@callback(
    Output('users-output', 'children'),
    Input('submit-button2', 'n_clicks'),
    State('textarea-user', 'value')
    )
def update_output2(n_clicks, value):
    lines = ["one line", "two line", "three line"] #Load db strings here
    childlist = []
    i = 0
    for each in lines:
        childlist.append(html.Tr(lines[i]))
        i += 1
    if n_clicks > 0:
            return html.Table(className='table table-striped', children=childlist)

@callback(
    Output('curr-orders-output', 'children'),
    Input('selector1', 'value')
)
def update_output3(value):
    lines = ["one line", "two line", "three line"] #Load db strings here
    childlist = []
    i = 0
    for each in lines:
        childlist.append(html.Tr(lines[i]))
        i += 1
    return html.Table(className='table table-striped', children=childlist)

@callback(
    Output('prev-orders-output', 'children'),
    Input('selector2', 'value')
)
def update_output4(value):
    lines = ["one line", "two line", "three line"] #Load db strings here
    childlist = []
    i = 0
    for each in lines:
        childlist.append(html.Tr(lines[i]))
        i += 1
    return html.Table(className='table table-striped', children=childlist)
# Run this app with `python3 app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
if __name__ == '__main__':
    app.run(debug=True)
