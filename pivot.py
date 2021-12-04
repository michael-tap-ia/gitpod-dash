import dash
from dash import dash_table
from dash.dependencies import Input, Output
from dash import dcc # dash core components
from dash import html
import dash_pivottable

import pandas as pd

df = pd.read_csv('https://bit.ly/elements-periodic-table')

app = dash.Dash(__name__)

app.layout =  html.Div([
    dash_pivottable.PivotTable(
    id='table',
    data=df.to_dict('records'),
    cols=[], #input - drop-down
    colOrder="key_a_to_z",
    rows=[], #input - drop-down
    rowOrder="key_a_to_z",
    rendererName="Table",
    aggregatorName="Count",
    vals=[]
),
    html.Div(
        id='output'
    )
])

@app.callback(Output('output', 'children'),
              [Input('table', 'cols'),
               Input('table', 'rows'),
               Input('table', 'rowOrder'),
               Input('table', 'colOrder'),
               Input('table', 'aggregatorName'),
               Input('table', 'rendererName')])

def display_props(cols, rows, row_order, col_order, aggregator, renderer):
    return [
        html.P(str(cols), id='columns'),
        html.P(str(rows), id='rows'),
        html.P(str(row_order), id='row_order'),
        html.P(str(col_order), id='col_order'),
        html.P(str(aggregator), id='aggregator'),
        html.P(str(renderer), id='renderer'),
    ]

if __name__ == '__main__':
    app.run_server(debug=True)
