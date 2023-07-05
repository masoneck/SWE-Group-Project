import dash
from dash import html

import dash_bootstrap_components as dbc


dash.register_page(__name__)


layout = html.Div([
    html.H4('All items:'),

    dbc.Table([
        html.Thead([
            html.Tr([
                html.Th(c) for c in ('Name', 'Stock', 'Price', 'Inventory #', 'Department #')
            ])
        ]),
        html.Tbody([
            html.Tr([html.Td(c) for c in ('Red Apple', 7, 1.23, 1, 1)])
        ])
    ], bordered=True)
])
