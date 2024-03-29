# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 09:19:24 2020

@author: JSEPULVEDA-PC

 @st.cache    
"""
# import matplotlib 
# import matplotlib.pyplot as plt
#@st.cache    
import streamlit as st
import datetime
import plotly
import plotly.graph_objects as go
import pandas as pd
from pandas import DataFrame
from plotly.graph_objs import *
import plotly.express as px
from typing import Dict
from pathlib import Path
import pygwalker as pyg
import streamlit.components.v1 as components

class Parametro:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def calcular_estadisticas(self):
        # Calcular valores máximo, mínimo y promedio para cada variable
        estadisticas = self.dataframe.describe().loc[['min', 'max', 'mean']]
        return estadisticas



def main():
    
        downloads_path = str(Path.home() / "Downloads")
         
        data_file = st.file_uploader("Suba el archivo",type=['xlsx'])
       
   
    
    
   
        st.title("APLICACION PARA CREAR GRAFICOS INTERACTIVOS")
        st.text("by @jsepulvedaf")
       
        df= pd.read_excel (data_file)
        df['fecha'] = pd.to_datetime(df['fecha'])
        df['n_date']=df['fecha']
        df.set_index('fecha',inplace=True)
        df.sort_values(by='fecha')
         
        df['Año'] = df.index.year                                
        df['Mes'] = df.index.month                               
        df['Dia'] = df.index.day
        df['hora'] = df.index.hour                       
        df['minuto']=df.index.minute
        
        maxima_d=max(df['n_date'])
        min_d=min(df['n_date'])
   
    
          
    
        st.dataframe(df)
        col1, col2  = st.columns(2)
   
        with col1:
           st.write('fecha minima es',min_d) 
           F1=st.date_input('entre la fecha inicial')
           st.write('la fecha inicial es', F1)
           start = F1
       
        with col2 :
           st.write('fecha maxima es',maxima_d)  
           F2=st.date_input('entre la fecha final')
           st.write('la fecha final es', F2)  
           end = F2
      
        Texto_titulo = st.text_input("ingrese el titulo grafico:", "")  
        df_analisis = df[start:end]
        df_analisis[:]
       
        # st.write(df_analisis)
        
        # col3, col4 = st.beta_columns(2)
        
        # hora_d=st.slider('seleccionar hora',0,1,23,1)
        
        # df_analisis=df_analisis[df_analisis['fecha'].dt.hour==hora_d]
        # with col3:
        #        Ho = st.number_input('Entre hora inicial 0-24')
        #        st.write('The current number is ', Ho)
        
        # with col4:
        #       H1 = st.number_input('Entre hora Final 0-24')
        #       st.write('The current number is ', H1)
       
             
        # df_filtro= (df_analisis ['hora']>=Ho) & (df_analisis['hora']<=H1 )  #filtro valores de 2 a 3 am
        # filtro=df_analisis[df_filtro]
        # st.dataframe(df_analisis) 
        nombre_columna = df_analisis.columns.tolist()
        title=Texto_titulo +".html"
             
        seleccion=st.multiselect("seleeciones los campos", nombre_columna)
        selected =df_analisis[seleccion]
        
        fig = px.line(selected, title ='Grafico: '+Texto_titulo+str(seleccion) )  
        # fig.show()
        # if st.button('Guardar gráfica en HTML'):
        # Código para salvar la gráfica en HTML
        # fig.write_html('grafica.html')
        # Llama a la función para generar la gráfica
           
       
            

        # Botón para guardar el archivo en el directorio de descargas del navegador
                  
        
       # Guarda el archivo en el directorio de descargas del navegador

         
       
        st.plotly_chart(fig, use_container_width=True)
        
        ruta = str(downloads_path+"/"+ title)
      
        if st.button('guardar Hmtl'):

          fig.write_html(ruta)
        
        parametro = Parametro(selected)
        estadisticas = parametro.calcular_estadisticas()
        st.text("Estadisticas Variables Selecionadas")
        st.dataframe(estadisticas)
  
    
       
    

    
if __name__ == '__main__':
    	main()    
    
  
    
    
	
    
       
    
