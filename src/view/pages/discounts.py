import dash
from dash import html, dcc, callback, Output, Input

import dash_bootstrap_components as dbc

from src.controller.controller import get_discounts


dash.register_page(__name__)


def show_layout():
    return html.Div([
        html.H4('All discounts:'),
        dbc.Table([
            html.Thead([
                html.Tr([
                    html.Th(c) for c in ['Phrase', 'Amount']
                ])
            ]),
            html.Tbody([
            html.Tr([html.Td(c) for c in discount])
            for discount in get_discounts()
        ], id='discounts-content-list') 
        ], bordered=True)
    ])


layout = show_layout
