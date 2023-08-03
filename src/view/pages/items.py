import dash
from dash import html, dcc, callback, Output, Input

import dash_bootstrap_components as dbc

from src.controller.controller import get_items


dash.register_page(__name__)

layout = html.Div([
    dcc.Input(id='item-search-input', placeholder='Enter item...', type='text'),
    html.H4('All items:'),
    dbc.Table([
        html.Thead([
            html.Tr([
                html.Th(c) for c in ['ID', 'Name', 'Stock', 'Price', 'Department ID']
            ])
        ]),
        html.Tbody(id='items-content-list') 
    ], bordered=True)
])

@callback(
    Output('items-content-list', 'children'),
    Input('item-search-input', 'value')
)
def update_items_content(value):
    return [
        html.Tr([html.Td(c) for c in item])
        for item in get_items()
    ]