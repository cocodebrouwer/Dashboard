import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import statsmodels.api as sm

st.title("✈️ Dashboard Eindpresentatie ✈️")

st.markdown("""
Welkom!\n
\n
Bij ons Dashboard over onze eindpresenatie als alles lukt in ieder geval....
\n
""")
st.sidebar.title("Luchthaven")
language = st.sidebar.radio(label="", options=["Schiphol", "Maastricht"])





#Code voor interactieve barplot met plotly.express
CBS = pd.read_csv('CBS_streamlit.csv')
fig1 = px.bar(CBS, 
              x = "Periode", 
              y = "Totaal aantal vluchten", 
              color = "Luchthaven", 
              hover_name = "Luchthaven",
              labels = {'Periode':'Datum'},
              opacity = 0.5,
              title = 'Totaal aantal vluchten Nederlandse luchthavens 2019-2021')

#Dropdown buttons
dropdown_buttons = [{'label':"Luchthavens NL", 'method':"update", 'args':[{"visible":[True, True, True, True, True]}]},
                    {'label':"Amsterdam Airport Schiphol", 'method':"update", 'args':[{"visible":[True, False, False, False, False]}]},
                    {'label':"Rotterdam The Hague Airport", 'method':"update", 'args':[{"visible":[False, True, False, False, False]}]},
                    {'label':"Eindhoven Airport", 'method':"update", 'args':[{"visible":[False, False, True, False, False]}]}, 
                    {'label':"Maastricht Aachen Airport", 'method':"update", 'args':[{"visible":[False, False, False, True, False]}]}, 
                    {'label':"Groningen Airport Eelde", 'method':"update", 'args':[{"visible":[False, False, False, False, True]}]}]

#Update de figuur
fig1.update_layout({'updatemenus':[{'active':0, 'buttons':dropdown_buttons}]})

#Draai de x-as labels
fig1.update_xaxes(tickangle = 45)

#Laat de figuur zien
fig1.show()





#Code voor interactieve barplot met plotly.express
fig2 = px.bar(CBS, 
              x = "Periode", 
              y = "Totaal aantal passagiers", 
              color = "Luchthaven", 
              hover_name = "Luchthaven",
              labels = {'Periode':'Datum'},
              opacity = 0.5,
              title = 'Totaal aantal passagiers Nederlandse luchthavens 2019-2021')

#Dropdown buttons
dropdown_buttons = [{'label':"Luchthavens NL", 'method':"update", 'args':[{"visible":[True, True, True, True, True]}]},
                    {'label':"Amsterdam Airport Schiphol", 'method':"update", 'args':[{"visible":[True, False, False, False, False]}]},
                    {'label':"Rotterdam The Hague Airport", 'method':"update", 'args':[{"visible":[False, True, False, False, False]}]},
                    {'label':"Eindhoven Airport", 'method':"update", 'args':[{"visible":[False, False, True, False, False]}]}, 
                    {'label':"Maastricht Aachen Airport", 'method':"update", 'args':[{"visible":[False, False, False, True, False]}]}, 
                    {'label':"Groningen Airport Eelde", 'method':"update", 'args':[{"visible":[False, False, False, False, True]}]}]

#Update de figuur
fig2.update_layout({'updatemenus':[{'active':0, 'buttons':dropdown_buttons}]})

#Draai de x-as labels
fig2.update_xaxes(tickangle = 45)

#Laat de figuur zien
fig2.show()





#Code voor interactieve boxplot met plotly.express
fig3 = px.box(CBS, 
              x = 'Luchthaven', 
              y = "Totaal aantal vluchten", 
              color = 'Luchthaven', 
              hover_name = 'Luchthaven',  
              title = 'Aantal vluchten Nederlandse luchthavens 2019-2021')

#Dropdown buttons
dropdown_buttons = [{'label':"Luchthavens NL", 'method':"update", 'args':[{"visible":[True, True, True, True, True]}]},
                    {'label':"Amsterdam Airport Schiphol", 'method':"update", 'args':[{"visible":[True, False, False, False, False]}]},
                    {'label':"Rotterdam The Hague Airport", 'method':"update", 'args':[{"visible":[False, True, False, False, False]}]},
                    {'label':"Eindhoven Airport", 'method':"update", 'args':[{"visible":[False, False, True, False, False]}]}, 
                    {'label':"Maastricht Aachen Airport", 'method':"update", 'args':[{"visible":[False, False, False, True, False]}]}, 
                    {'label':"Groningen Airport Eelde", 'method':"update", 'args':[{"visible":[False, False, False, False, True]}]}]

#Update de figuur
fig3.update_layout({'updatemenus':[{'active':0, 'buttons':dropdown_buttons}]})

#Laat de figuur zien
fig3.show()





#Code voor interactieve boxplot met plotly.express
fig4 = px.box(CBS, 
              x = 'Luchthaven', 
              y = "Totaal aantal passagiers", 
              color = 'Luchthaven', 
              hover_name = 'Luchthaven',  
              title = 'Aantal passagiers Nederlandse luchthavens 2019-2021')

#Dropdown buttons
dropdown_buttons = [{'label':"Luchthavens NL", 'method':"update", 'args':[{"visible":[True, True, True, True, True]}]},
                    {'label':"Amsterdam Airport Schiphol", 'method':"update", 'args':[{"visible":[True, False, False, False, False]}]},
                    {'label':"Rotterdam The Hague Airport", 'method':"update", 'args':[{"visible":[False, True, False, False, False]}]},
                    {'label':"Eindhoven Airport", 'method':"update", 'args':[{"visible":[False, False, True, False, False]}]}, 
                    {'label':"Maastricht Aachen Airport", 'method':"update", 'args':[{"visible":[False, False, False, True, False]}]}, 
                    {'label':"Groningen Airport Eelde", 'method':"update", 'args':[{"visible":[False, False, False, False, True]}]}]

#Update de figuur
fig4.update_layout({'updatemenus':[{'active':0, 'buttons':dropdown_buttons}]})

#Laat de figuur zien
fig4.show()





#Code voor interactieve scatterplot met plotly.express
data1 = pd.read_csv('data_streamlit.csv')
fig5 = px.scatter(data1, 
                  x = "Totaal aantal overledenen", 
                  y = "Totaal aantal vluchten", 
                  size = "Totaal aantal passagiers", 
                  hover_name = "Periode",
                  color = "Luchthaven",  
                  opacity = 0.5, 
                  size_max = 60,
                  trendline = 'ols', 
                  #trendline_scope = 'overall', 
                  title = 'Nederlandse luchthavens en sterftecijfers 2020-2021')

#Dropdown buttons
dropdown_buttons = [{'label':"Luchthavens NL", 'method':"update", 'args':[{"visible":[True, True, True, True, True]}]},
                    {'label':"Amsterdam Airport Schiphol", 'method':"update", 'args':[{"visible":[True, False, False, False, False]}]},
                    {'label':"Rotterdam The Hague Airport", 'method':"update", 'args':[{"visible":[False, True, False, False, False]}]},
                    {'label':"Eindhoven Airport", 'method':"update", 'args':[{"visible":[False, False, True, False, False]}]}, 
                    {'label':"Maastricht Aachen Airport", 'method':"update", 'args':[{"visible":[False, False, False, True, False]}]}, 
                    {'label':"Groningen Airport Eelde", 'method':"update", 'args':[{"visible":[False, False, False, False, True]}]}]

#Update de figuur
fig5.update_layout({'updatemenus':[{'active':0, 'buttons':dropdown_buttons}]})

#Laat de figuur zien
fig5.show()





#Code voor correlatie matrix 
data2 = data1[data1['Luchthaven'] == 'Amsterdam Airport Schiphol']
data_corr = data2[['Totaal aantal vluchten', 
                   'Totaal aantal passagiers', 
                   'Totaal aantal overledenen', 
                   'Verwacht aantal overledenen']]
corrMatrix = data_corr.corr()
sn.heatmap(corrMatrix, 
           annot = True, 
           cmap = 'Purples', 
           linewidths = 2, 
           linecolor = 'white', 
           square = True)
plt.title('Schiphol en sterftecijfers 2020-2021')
plt.show()





data3 = pd.read_csv('data_merge_streamlit.csv')
px.scatter_geo(data_frame = data3, 
               lat = 'LAT', 
               lon = 'LNG', 
               hover_name = 'Luchthaven', 
               hover_data = {'Luchthaven': False, 'Periode': True, 'Maatregelen': False, 'Totaal aantal vluchten': True, 
                             'LAT': False, 'LNG': False, 'Totaal aantal passagiers': True, 'Totaal aantal overledenen': True}, 
               projection = 'natural earth', 
               scope = 'europe', 
               color = 'Luchthaven', 
               size = 'Totaal aantal vluchten', 
               animation_frame = 'Maatregelen', 
               opacity = 0.2, 
               color_discrete_map = {'Amsterdam Airport Schiphol': 'Blue', 'Rotterdam The Hague Airport': 'Red', 
                                     'Eindhoven Airport': 'Green', 'Maastricht Aachen Airport': 'Yellow', 
                                     'Groningen Airport Eelde': 'Orange'},
               title = 'Nederlandse luchthavens en COVID-19', 
               fitbounds = 'locations', 
               size_max = 100)

