import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc


external_stylesheets = [dbc.themes.BOOTSTRAP]
app = Dash(external_stylesheets=external_stylesheets, use_pages=True, pages_folder='src/view/pages')

app.layout = html.Div([
	html.H1('Administrative Backend:'),

    html.Div([
        html.Div(
            dcc.Link(
                f"{page['name']} - {page['path']}", href=page["relative_path"]
            )
        )
        for page in dash.page_registry.values()
    ]),
    #TODO: add default page or home page to remove 404 error
	dash.page_container
])

# Run this app with `python3 app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
def start():
    app.run(debug=True)
