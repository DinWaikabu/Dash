import pandas as pd
from dash.dependencies import Input, Output
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go


app = dash.Dash()

app.css.append_css({'external_url': 'https://codepen.io/amyoshino/pen/jzXypZ.css'})  


df = pd.read_csv('IPM.csv', delimiter=';')

indikator = df['Tahun'].unique()
indikator2 = df['Provinsi'].unique()
app.layout = html.Div([
        html.H1(children='Dashboard'),
    dcc.Tabs(id="tabs", children=[
        dcc.Tab(label='Tab Satu', children=[
            html.Div([
            dcc.Dropdown(
                    id='my-dropdown',
                    options=[{'label': i, 'value': i} for i in indikator], value="Tahun"
                    ),
            dcc.Graph(id='my-grafik')
            ])
        ]),
        dcc.Tab(label='Tab Dua', children=[
                 dcc.Dropdown(
                    id='dropdown2',
                    options=[{'label': i, 'value': i} for i in indikator2], value="Provinsi"
                    ),
            html.Div([
                    dcc.Graph(id='grafik2')
                    ])
        ]),
        dcc.Tab(label='Tab Tiga', children=[
                 html.H3('Belum Ada konten')
        ]),
])
],className='ten columns offset-by-one') 

@app.callback(Output('my-grafik','figure'), [Input('my-dropdown', 'value')])
def updateGrafik(pilih):
    dff= df[df['Tahun']==pilih]
    return {
            'data': [go.Bar(
                    x= dff['Provinsi'],
                    y=dff['IPM'])
                    ],
            'layout':{'title': 'Indeks Pembangunan Manusia',
                      'xaxis': dict(
                              title='Provinsi',
                              titlefont=dict(
                                      family='Courier New, monospace',
                                      size=20
                                      )),
                       'yaxis': dict(
                              title='IPM',
                              titlefont=dict(
                                      family='Helvetica, monospace',
                                      size=18))
                              }
            }
@app.callback(Output('grafik2', 'figure'),[Input('dropdown2', 'value')])
def upgarfik2(prov):
    dfg = df[df['Provinsi']==prov]
    return{
            'data':[go.Scatter(
                    x=dfg['Tahun'],
                    y=dfg['IPM'])
        ],
            'layout':{'title': 'Indeks Pembangunan Manusia',
                      'xaxis': dict(
                              title='Tahun',
                              titlefont=dict(
                                      family='Courier New, monospace',
                                      size=20
                                      )),
                       'yaxis': dict(
                              title='IPM',
                              titlefont=dict(
                                      family='Helvetica, monospace',
                                      size=18))
                      }
            }
        

if __name__ == '__main__':
    app.run_server(debug=True)  