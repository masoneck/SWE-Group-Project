import dash
from dash import html, dcc, callback, Output, Input

import dash_bootstrap_components as dbc

from src.controller.controller import get_orders


dash.register_page(__name__)


def show_layout():
    return html.Div([
        html.H4('All orders:'),
        dbc.Table([
            html.Thead([
                html.Tr([
                    html.Th(c) for c in ['ID', 'Date', 'Customer ID', 'Total', 'Is Complete', 'Sales orders']
                ])
            ]),
            html.Tbody([
            html.Tr([html.Td(c) for c in order])
            for order in get_orders()
        ], id='orders-content-list') 
        ], bordered=True)
    ])


layout = show_layout
