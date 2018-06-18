import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd 
from dash.dependencies import Input, Output



dt = pd.read_csv('data/PLR2017-Exec-Min_T2_HT2_ETPT-BG_BA.csv',sep=';',encoding='latin-1')
print(dt.columns)

tmp = pd.DataFrame(dt.groupby('Type de Budget')['Type de Budget'].count())







app = dash.Dash()

app.scripts.config.serve_locally = True




vertical = True


if not vertical :

    app.layout = html.Div(children=[
        html.H1(children='Datafin'),

        html.Div(children='''
        A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': tmp.index.values, 
                'y': tmp['Type de Budget'].values, 
                'type': 'bar', 
                'name': 'Type de Budget'}   
            ],
            'layout': {
                'subtitle': 'Exécution par Ministère en autorisation d\'engagement (AE), crédit de paiement (CP) et emploi en temps plein travaillé (ETPT\npar titre 2 / hors titre 2 pour le budget général et les deux budgets annexes.'
            }
        }
    )
])

else:
    app.layout = html.Div([
        dcc.Tabs(
            tabs=[
                {'label': 'Analytical summary', 'value': 1},
                {'label': 'Usage Over Time', 'value': 2},
                {'label': 'Predictions', 'value': 3},
                {'label': 'Description', 'value': 4},
            ],
            value=1,
            id='tabs'
            
            ),
        html.Div(id='tab-output')
    ], style={
        'width': '80%',
        'fontFamily': 'Sans-Serif',
        'margin-left': 'auto',
        'margin-right': 'auto'
    })


@app.callback(Output('tab-output','children'),[Input('tabs','value')])
def display_content(value=2):

    data=[
                {'x': tmp.index.values, 
                'y': tmp['Type de Budget'].values, 
                'type': 'bar',
                'name': 'Type de Budget'}  ,



                {'x': tmp.index.values, 
                'y': tmp['Type de Budget'].values, 
                'type': 'box',
                'name': 'Type de Budget'}


                ]

    return html.Div([
        dcc.Graph(
            id='graph',
            figure={
                'data': data,
                'layout': {
                    'margin': {
                        'l': 30,
                        'r': 0,
                        'b': 30,
                        't': 0
                    },
                    'legend': {'x': 0, 'y': 1}
                }
            }
        )
    ])




             


if __name__ == '__main__':
    app.run_server(debug=True)
