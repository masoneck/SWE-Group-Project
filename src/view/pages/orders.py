import dash
from dash import html, dcc, callback, Output, Input

import dash_bootstrap_components as dbc

from src.controller.controller import get_orders


dash.register_page(__name__)


def show_layout():
    return html.Div([
        html.H2('All orders:'),
        html.H5('Sort by:'),
        dcc.RadioItems(['Date', 'Customer', 'Total'], 'Total', inline=True, id='sort-by-button'),
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


@callback(
    Output('orders-content-list', 'children'),
    Input('sort-by-button', 'value')
)
def show_layout_by_order(value):
    if value == 'Total':
        row_idx = 3
    elif value == 'Customer':
        row_idx = 2
    elif value == 'Date':
        row_idx = 1
    else:
        row_idx = 0
    return [
        html.Tr([html.Td(c) for c in order])
        for order in sorted(get_orders(), key=lambda o: o[row_idx])
    ]

layout = show_layout
