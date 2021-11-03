#Importeer streamlit
import streamlit as st

#Importeer de benodigde packages
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import statsmodels.api as sm
import seaborn as sns

#Titel toevoegen
st.title("✈️ NL luchthavens en COVID-19 ✈️")

#Tekst toevoegen
st.markdown("""
Welkom bij ons Dashboard over de Nederlandse Luchthavens in tijden van COVID-19!\n
\n
Wij zijn Coco de Brouwer en Inge Vijsma, derdejaars Aviation studenten en volgen momenteel de minor Data Science. 
Voor de eindpresentatie van het vak Visual Analytics hebben wij een Dashboard gemaakt over de bedrijvigheid van de Nederlandse Luchthavens tijdens de pandemie. 
Het Dashboard bestaat uit vijf verschillende soorten grafieken, deze zijn te selecteren in het keuzemenu. 
Zowel bij de histogram, boxplot en spreidingsdiagram kan de specifieke activiteit van de Nederlandse luchthavens gekozen worden. 
Bij de correlatie matrix kunnen de verschillende luchthavens geselecteerd worden. 
De kaart geeft een samenvattend beeld van de bedrijvigheid van de luchthavens tijdens de verschillende ontwikkelingen van COVID-19 weer. 
\n
Veel plezier met het bekijken van ons interactieve Dashboard en het uitproberen van de verschillende keuzemogelijkheden!
\n
----------
""")

#Kies inspectie
st.sidebar.title("Kies inspectie")
nav = st.sidebar.radio(label = "", 
                       options = ["Histogram", "Boxplot", "Spreidingsdiagram", "Correlatie Matrix", "Kaart"])

#--------------------
#Code voor histogram met keuze menu
if nav == "Histogram":
  
  #Tekst toevoegen
  st.markdown("""
  In de histogram wordt het aantal vluchten of passagiers per maand van 2019 tot en met 2021 weergeven. 
  Zo te zien is er een extreme daling in de bedrijvigheid van de luchthavens rond het begin van 2020. 
  Deze daling staat in verband met het begin van de pandemie in Nederland. 
  \n
  Met behulp van het keuzemenu kan de soort activiteit geselecteerd worden. 
  """)
  
  y = st.radio(label = "Kies gewenste activiteit:", 
               options = ["Totaal aantal vluchten", "Totaal aantal aangekomen vluchten", "Totaal aantal vertrokken vluchten", "Totaal aantal passagiers", 
                          "Totaal aantal aangekomen passagiers", "Totaal aantal vertrokken passagiers"])
  
  CBS = pd.read_csv('CBS_streamlit.csv')
  fig1 = px.bar(CBS, 
                x = "Periode", 
                y = y, 
                color = "Luchthaven", 
                hover_name = "Luchthaven",
                labels = {'Periode':'Datum'},
                opacity = 0.5,
                title = y + " Nederlandse luchthavens 2019-2021")

  #Dropdown buttons
  dropdown_buttons = [{'label':"Luchthavens NL", 'method':"update", 'args':[{"visible":[True, True, True, True, True]}]},
                      {'label':"Amsterdam Airport Schiphol", 'method':"update", 'args':[{"visible":[True, False, False, False, False]}]},
                      {'label':"Rotterdam The Hague Airport", 'method':"update", 'args':[{"visible":[False, True, False, False, False]}]},
                      {'label':"Eindhoven Airport", 'method':"update", 'args':[{"visible":[False, False, True, False, False]}]}, 
                      {'label':"Maastricht Aachen Airport", 'method':"update", 'args':[{"visible":[False, False, False, True, False]}]}, 
                      {'label':"Groningen Airport Eelde", 'method':"update", 'args':[{"visible":[False, False, False, False, True]}]}]

  #Update de figuur
  fig1.update_layout({'updatemenus':[{'active':0, 'buttons': dropdown_buttons}]})

  #Draai de x-as labels
  fig1.update_xaxes(tickangle = 45)

  #Laat de figuur zien
  st.plotly_chart(fig1)

#--------------------
#Code voor boxplot met keuze menu
elif nav == "Boxplot":
  
  #Tekst toevoegen
  st.markdown("""
  In de boxplot wordt het aantal vluchten of passagiers van 2019 tot en met 2021 weergeven. 
  Opvallend zijn de minimale waardes en de grote uiteenligging van de waardes in de boxplots van de verschillende luchthavens. 
  Ook dit is te verklaren aan de hand van de heersende pandemie in Nederland. 
  De ontwikkelingen van COVID-19 veroorzaken grote schommelingen in de drukte van de luchthavens. 
  \n
  Met behulp van het keuzemenu kan de soort activiteit geselecteerd worden. 
  """)
  
  y = st.radio(label = "Kies gewenste activiteit:", 
               options = ["Totaal aantal vluchten", "Totaal aantal aangekomen vluchten", "Totaal aantal vertrokken vluchten", "Totaal aantal passagiers", 
                          "Totaal aantal aangekomen passagiers", "Totaal aantal vertrokken passagiers"])
  
  CBS = pd.read_csv('CBS_streamlit.csv')
  
  fig3 = px.box(CBS, 
                x = 'Luchthaven', 
                y = y, 
                color = 'Luchthaven', 
                hover_name = 'Luchthaven',  
                title = y + " Nederlandse luchthavens 2019-2021")

  #Dropdown buttons
  dropdown_buttons = [{'label':"Luchthavens NL", 'method':"update", 'args':[{"visible":[True, True, True, True, True]}]},
                      {'label':"Amsterdam Airport Schiphol", 'method':"update", 'args':[{"visible":[True, False, False, False, False]}]},
                      {'label':"Rotterdam The Hague Airport", 'method':"update", 'args':[{"visible":[False, True, False, False, False]}]},
                      {'label':"Eindhoven Airport", 'method':"update", 'args':[{"visible":[False, False, True, False, False]}]}, 
                      {'label':"Maastricht Aachen Airport", 'method':"update", 'args':[{"visible":[False, False, False, True, False]}]}, 
                      {'label':"Groningen Airport Eelde", 'method':"update", 'args':[{"visible":[False, False, False, False, True]}]}]

  #Update de figuur
  fig3.update_layout({'updatemenus':[{'active':0, 'buttons': dropdown_buttons}]})

  #Laat de figuur zien
  st.plotly_chart(fig3)

#--------------------
#Code voor spreidingsdiagram met keuze menu
elif nav == "Spreidingsdiagram":
  
  #Tekst toevoegen
  st.markdown("""
  In het spreidingsdiagram wordt het aantal vluchten of passagiers uitgezet tegen het aantal overledenen van 2019 tot en met 2021 weergeven. 
  Het diagram bevat een algehele trendline die voor alle Nederlandse luchthaven samen geldt. 
  De trendline heeft een negatief verloop wat tevens ook naar verwachting is. 
  Hieruit valt te concluderen dat tijdens de pandemie minder mensen gebruik hebben gemaakt van de luchthavens dan gebruikelijk. 
  
  \n
  Met behulp van het keuzemenu kan de soort activiteit geselecteerd worden. 
  """)
  
  y = st.radio(label = "Kies gewenste activiteit:", 
               options = ["Totaal aantal vluchten", "Totaal aantal aangekomen vluchten", "Totaal aantal vertrokken vluchten", "Totaal aantal passagiers", 
                          "Totaal aantal aangekomen passagiers", "Totaal aantal vertrokken passagiers"])
  
  data1 = pd.read_csv('data_streamlit.csv')
  fig5 = px.scatter(data1, 
                    x = "Totaal aantal overledenen", 
                    y = y, 
                    hover_name = "Periode",
                    title = 'Nederlandse luchthavens en sterftecijfers 2020-2021', 
                    size = "Totaal aantal passagiers", 
                    color="Luchthaven", 
                    opacity = 0.5, 
                    size_max=60, 
                    trendline="ols", 
                    trendline_scope='overall')

  #Dropdown buttons
  dropdown_buttons = [{'label':"Luchthavens NL", 'method':"update", 'args':[{"visible":[True, True, True, True, True, True]}]},
                      {'label':"Amsterdam Airport Schiphol", 'method':"update", 'args':[{"visible":[True, False, False, False, False, True]}]},
                      {'label':"Rotterdam The Hague Airport", 'method':"update", 'args':[{"visible":[False, True, False, False, False, True]}]},
                      {'label':"Eindhoven Airport", 'method':"update", 'args':[{"visible":[False, False, True, False, False, True]}]}, 
                      {'label':"Maastricht Aachen Airport", 'method':"update", 'args':[{"visible":[False, False, False, True, False, True]}]}, 
                      {'label':"Groningen Airport Eelde", 'method':"update", 'args':[{"visible":[False, False, False, False, True, True]}]}]

  # #Update de figuur
  fig5.update_layout({'updatemenus':[{'active':0, 'buttons': dropdown_buttons}]})

  #Laat de figuur zien
  st.plotly_chart(fig5)

#--------------------
#Code voor correlatie matrix met keuze menu
elif nav == "Correlatie Matrix":
  
  y = st.radio(label = "Kies gewenste luchthaven:", 
               options = ["Amsterdam Airport Schiphol", "Rotterdam The Hague Airport", "Eindhoven Airport", "Maastricht Aachen Airport", "Groningen Airport Eelde"])
  
  data1 = pd.read_csv('data_streamlit.csv')
  data2 = data1[data1['Luchthaven'] == y]
  data_corr = data2[['Totaal aantal vluchten', 
                     'Totaal aantal passagiers', 
                     'Totaal aantal overledenen', 
                     'Verwacht aantal overledenen']]
  corrMatrix = data_corr.corr()
  fig6, ax = plt.subplots()
  sns.heatmap(corrMatrix, 
              annot = True, 
              cmap = 'Purples', 
              linewidths = 2, 
              linecolor = 'white', 
              square = True)
  plt.title(y + ' en sterftecijfers 2020-2021')
  st.pyplot(fig6)

#--------------------
#Code voor kaart
elif nav == "Kaart":
  data3 = pd.read_csv('data_merge_streamlit.csv')
  fig7 = px.scatter_geo(data_frame = data3,
                        lat = 'LAT', 
                        lon = 'LNG', 
                        hover_name = 'Luchthaven', 
                        hover_data = {'Luchthaven': False, 'Periode': True, 'Maatregelen': False, 'Totaal aantal vluchten': True, 'LAT': False, 'LNG': False, 
                                      'Totaal aantal passagiers': True, 'Totaal aantal overledenen': True}, 
                        projection = 'natural earth', 
                        scope = 'europe', 
                        color = 'Luchthaven', 
                        size = 'Totaal aantal vluchten', 
                        animation_frame = 'Maatregelen', 
                        opacity = 0.2, 
                        color_discrete_map = {'Amsterdam Airport Schiphol': 'Blue', 'Rotterdam The Hague Airport': 'Red', 'Eindhoven Airport': 'Green', 
                                              'Maastricht Aachen Airport': 'Yellow', 'Groningen Airport Eelde': 'Orange'},
                        title = 'Nederlandse luchthavens en COVID-19', 
                        fitbounds = 'locations', 
                        size_max = 100)
  st.plotly_chart(fig7)
