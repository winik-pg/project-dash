import plotly.express as px
import os
#import geopandas as gpd
import pandas as pd
import plotly.graph_objects as go
import seaborn as sbn
import dash
import dash_core_components as dcc
import dash_html_components as html
import folium
import dash_table
import dash_bootstrap_components as dbc
from datetime import date


#######################################################################

# Abrir BD
#os.chdir(r"C:\Users\PRIME\AnacondaProjects\Project_curso\\")
mun = gpd.read_file('00mun.shp') #Para mapas
base = pd.read_csv('Tabla 1. Variación mensual (AÑO ANTERIOR) (mapas).csv')#, encoding= "Utf-8") #Para mapa

#cdmx_delit = pd.read_excel('cdmx deaths.xlsx')  #Para gráfica
df2= pd.read_csv("Tabla 2. Delitos Zacatecas (2020)_2.csv")#, encoding= "Latin-1")



#crear una Gráfica 
##################################################################################

pv = pd.pivot_table(df2, index=['Municipio'], columns=['Tipo de delito'], values=['ene-20'],aggfunc=sum, fill_value = 0)

g1 = go.Bar(x=pv.index, y=pv[('ene-20', 'Robo')], name = 'ROBO')
gr1 = go.Bar(x=pv.index, y=pv[('ene-20', 'Violencia familiar')], name = 'VIOLENCIA FAMILIAR')
gra1 = go.Bar(x=pv.index, y=pv[('ene-20', 'Lesiones')], name = 'LESIONES')
graf1 = go.Bar(x=pv.index, y=pv[('ene-20', 'Otros delitos del Fuero Común')], name = 'OTROS DELITOS DEL FUERO COMÚN')
grafi1 = go.Bar(x=pv.index, y=pv[('ene-20', 'Daño a la propiedad')], name = 'DAÑO A LA PROPIEDAD')
grafic1 = go.Bar(x=pv.index, y=pv[('ene-20', 'Fraude')], name = 'FRAUDE')
grafica1 = go.Bar(x=pv.index, y=pv[('ene-20', 'Amenazas')], name = 'AMENAZAS')

# Display figure





#######################################################################

#Dash
app = dash.Dash()
colors = {
    'background': '#111111',
    'text': '#C0C0C0'
}


# Titulo de la página  ############################################################

app = dash.Dash()
colors = {
    'background': '#111111',
    'text': '#C0C0C0'
}


# Titulo de la página  ############################################################


app.title = 'Analytics Dashboard'
app.layout = html.Div(children=[
  
    html.Div(children = [ 
    dbc.NavbarSimple(
        children=[
        dbc.NavItem(dbc.NavLink("Web Portal",
                                style={'textAlign': 'center','color': colors['text']},
                                       href="https://plotly.com/python/figure-labels/")),
        ],
        brand="Analytics Dashboard",
        brand_href="https://matplotlib.org/gallery/api/font_family_rc_sgskip.html",
        color="#E3E4E5",
        dark=True,)],
        style={'textAlign': 'center','color': colors['text'],
               'font-family': 'Montserrat', 'font-weight': 'bold','width': '100%',},
        ),
#app.layout = html.Div(children=[
    html.Div(children = [ dcc.Markdown(
        ''' 
    # Segunda GRAN prueba de Dashboard
    ## prueba sobre delitos
    ###### jueves 28 de enero de 2020
''',
       #brand="winra prueba de Dashboard",
       #brand_href="#",
       #color="#FFE5B4",
       #dark=True,
        )],style={'font-family': 'Montserrat',# 'sans-serif',
                  'textAlign': 'center','color': colors['text'],'width': '100%'}
        ),
     
    
##GRAFICAS O MAPAS   #####################################################################
##primera franja
#    
#    html.Div( children = [dcc.Graph(id='grafica1',
#              figure= {'data':[g1,gr1,gra1,graf1,grafi1,grafic1,grafica1],
#                       'layout': go.Layout(paper_bgcolor='black', #color de fondo
#                                           plot_bgcolor='black',
#                                           title='Mayor incidencia delictiva',
#                                           barmode='group')})],
#             style = {'margin': '1% 0px 0px 0px', 'width':'60%',
#                     'font-family': 'Montserrat',#Cambia tipo de letra
#                    }), #Fondo de grafico
##segunda franja
#    html.Div(children = [dcc.Graph(style={'backgroundColor': colors['background']},
#                                   figure=tabla2)],
#             style={'margin': '1% 0px 0px 0px', 'width':'35%',
#                   'font-family': 'Montserrat',
#                   'backgroundColor': colors['background']}),
#    
#    html.Div(children =[dcc.Graph(figure=grafica2)],
#             style={'margin': '2% 0px 0px 1px', 'width':'22%',
#                   'font-family': 'Montserrat',
#                   'backgroundColor': colors['background']}),
#    html.Div(children = [dcc.Graph(figure=grafica3)],
#            style={'margin': '2% 0px 0px 1px', 'width':'22%',
#                  'font-family': 'Montserrat',
#                  'backgroundColor': colors['background']}),
#    html.Div(children =[dcc.Graph(figure=grafica4)],
#             style={'margin': '2% 0px 0px 1px', 'width':'22%',
#                   'font-family': 'Montserrat',
#                   'backgroundColor': colors['background']}),
#    html.Div(children = [dcc.Graph(figure=grafica5)],
#            style={'margin': '2% 0px 0px 0px', 'width':'22%',
#                  'font-family': 'Montserrat',
#                  'backgroundColor': colors['background']}),
#    
##tercera franja
#    html.Div(children =[dcc.Graph(figure=grafica6)],
#             style={'margin': '3% 0px 0px 0px', 'width':'100%',
#                   'font-family': 'Montserrat',
#                   'backgroundColor': colors['background']}),
#
##cuarta franja
#    html.Div(children = [dcc.Graph(figure=mapa1)],
#            style={'margin': '4% 0px 0px 0px', 'width':'35%',
#                  'font-family': 'Montserrat',
#                  'backgroundColor': colors['background']}),
#
##    html.Div(children = [dcc.Graph(figure=grafica7)],
##            style={'margin': '2% 0px 0px 0px', 'width':'30%'}),
#    html.Div(children =[dcc.Graph(figure=grafica8)],
#             style={'margin': '2% 0px 0px 0px', 'width':'60%',
#                   'font-family': 'Montserrat',
#                   'backgroundColor': colors['background']}),
#
##quinta franja
#    html.Div(children = [dcc.Graph(figure=grafica9)],
#            style={'margin': '2% 0px 0px 0px', 'width':'100%',
#                  'font-family': 'Montserrat',
#                  'backgroundColor': colors['background']}),
#
##sexta franja    
#    html.Div(children = [dcc.Graph(figure=mapa2)],
#            style={'margin': '2% 0px 0px 0px', 'width':'50%',
#                  'font-family': 'Montserrat',
#                  'backgroundColor': colors['background']}),
#
#    html.Div(children = [dcc.Graph(figure=tabla1)],
#             style={'margin': '2% 0px 0px 0px', 'width':'50%',
#                   'font-family': 'Montserrat',
#                   'backgroundColor': colors['background']})
##
    
],style={'display': 'flex','flex-direction': 'row','flex-wrap': 'wrap','overflow': 'hidden',
        'font-family': 'Montserrat','backgroundColor': colors['background']}, #Color de fondo dash
                     # dark=True,
                     )

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)
    app.server.static_folder = 'static'  


# In[ ]:





# In[ ]:




