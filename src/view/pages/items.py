import dash
from dash import html

import dash_bootstrap_components as dbc

from src.controller.controller import get_items


dash.register_page(__name__)

layout = html.Div([
    html.H4('All items:'),

    dbc.Table([
        html.Thead([
            html.Tr([
                html.Th(c) for c in ['ID', 'Name', 'Stock', 'Price', 'Department ID']
            ])
        ]),
        html.Tbody([
            html.Tr([html.Td(c) for c in item])
            for item in get_items()
        ]) 
    ], bordered=True)
])
