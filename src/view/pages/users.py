import dash
from dash import html, dcc, callback, Output, Input

import dash_bootstrap_components as dbc

from src.controller.controller import get_users


dash.register_page(__name__)


def show_layout():
    return html.Div([
        html.H4('All users:'),
        dbc.Table([
            html.Thead([
                html.Tr([
                    html.Th(c) for c in ['ID', 'Email', 'First name', 'Last name', 'Orders']
                ])
            ]),
            html.Tbody([
            html.Tr([html.Td(c) for c in user])
            for user in get_users()
        ], id='users-content-list') 
        ], bordered=True)
    ])


layout = show_layout
