import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output,State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
dfdata = pd.read_csv('Brand_mobil_20102017.csv')
dfpred = pd.read_csv('pred_gabungan.csv')
dfdata.dropna(inplace=True)
app.layout = html.Div(children=[
        html.H1('Prediction Car Sales by Brand'),
        html.P(html.H3('Created by: Gilang')),
        dcc.Tabs(value = 'tabs',id='tabs-1',children=[
           

        dcc.Tab(label='Plot Awal', value='tab-2',children=[
            html.Div(
                html.Div(                
                dcc.Dropdown(id='dropdown_awal', options=[
                                                    {'label':'Toyota','value':'Toyota'},
                                                    {'label':'Daihatsu', 'value':'Daihatsu'},
                                                    {'label':'Honda', 'value':'Honda'},
                                                    {'label':'Mitsubishi', 'value':'Mitsubishi'},
                                                    {'label':'Suzuki', 'value':'Suzuki'},
                                                    {'label':'Others', 'value':'Others'},

                ], value = 'Toyota')
            ,className='col-3'), className='row'
            ),
            html.Div(children = dcc.Graph(
                id='awal',
                figure={'data':[
                    go.Scatter(
                        x=dfdata['Periode'],
                        y=dfdata['Toyota'],
                        mode='lines',
                    )
                ],
                'layout':go.Layout(
                    xaxis={'title':'Years'},
                    yaxis={'title':'Unit'},
                    hovermode='closest'
                )}
            )
            )
            ]),
        dcc.Tab(label = 'Plot Prediksi', value = 'tab-prediksi',children=[
            html.Div(
                html.Div(                
                dcc.Dropdown(id='dropdown_prediksi', options=[
                                                    {'label':'Toyota','value':'Toyota'},
                                                    {'label':'Daihatsu', 'value':'Daihatsu'},
                                                    {'label':'Honda', 'value':'Honda'},
                                                    {'label':'Mitsubishi', 'value':'Mitsubishi'},
                                                    {'label':'Suzuki', 'value':'Suzuki'},
                                                    {'label':'Others', 'value':'Others'},

                ], value = 'Toyota')
            ,className='col-3'), className='row'
            ),
            html.Div(children = dcc.Graph(
                id='prediksi',
                figure={'data':[
                    go.Scatter(
                        x=dfpred['Periode'],
                        y=dfpred['Toyota'],
                        mode='lines',
                    )
                ],
                'layout':go.Layout(
                    xaxis={'title':'Years'},
                    yaxis={'title':'Unit'},
                    hovermode='closest'
                )}
            )
            )
            ]
           ),
                

            
            
        ]),

])

@app.callback(
    Output(component_id='awal', component_property='figure'),
    [Input(component_id='dropdown_awal', component_property='value')]
)

def create_line(x1):
    figure={'data':[
                go.Scatter(
                    x=dfdata['Periode'],
                    y=dfdata[x1],
                    mode='lines',
                )
            ],
            'layout':go.Layout(
                xaxis={'title':'Years'},
                yaxis={'title':'Unit'},
                hovermode='closest'
            )}
    return figure

@app.callback(
    Output(component_id='prediksi', component_property='figure'),
    [Input(component_id='dropdown_prediksi', component_property='value')]
)

def create_line(x1):
    figure={'data':[
                go.Scatter(
                    x=dfpred['Periode'],
                    y=dfpred[x1],
                    mode='lines',
                )
            ],
            'layout':go.Layout(
                xaxis={'title':'Years'},
                yaxis={'title':'Unit'},
                hovermode='closest'
            )}
    return figure

# @app.callback(
#     Output(component_id = 'Graph-bar', component_property = 'figure'),
#     [Input(component_id = 'contoh-dropdown', component_property = 'value'),
#     Input(component_id = 'contoh-dropdown1', component_property = 'value')]
# )

# def create_graph_bar (x1,x2):
#     figure = {
#                     'data': [
#                         {'x':df['Married'],'y':df[x1],'type':'bar','name' : x1},
#                         {'x':df['Married'],'y':df[x2],'type':'bar','name':x2}
#                     ],
#                     'layout':{'title':'Bar Chart'}
#                 }
#     return figure

# @app.callback(
#     Output(component_id = 'graph-pie', component_property = 'figure'),
#     [Input(component_id = 'contoh-dropdown3', component_property = 'value')]
# )

# def create_pie (X3):
#     figure= {'data' : [
#                     go.Pie(
#                         labels = ['Catalogs {}'.format (i) for i in list(df['Catalogs'].unique())],
#                                   values = [df.groupby('Catalogs').mean()[X3][i]for i in list(df['Catalogs'].unique())],
#                                   sort = False)
#                     ],
#                     'layout': {'title':'Mean Pie Chart'}
#                 }
#     return figure


if __name__ == '__main__':
    app.run_server(debug=True)