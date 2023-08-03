import dash
from dash import html

import dash_bootstrap_components as dbc

from src.controller.controller import get_orders


dash.register_page(__name__)

layout = html.Div([
    html.H4('All orders:'),

    dbc.Table([
        html.Thead([
            html.Tr([
                html.Th(c) for c in ['ID', 'Date', 'Customer ID', 'Total', 'Is Complete', 'Sales Items']
            ])
        ]),
        html.Tbody([
            html.Tr([html.Td(c) for c in order])
            for order in get_orders()
        ]) 
    ], bordered=True)
])
