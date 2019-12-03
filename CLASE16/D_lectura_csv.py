# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 08:20:33 2019

@author: danie
"""

import pandas as pd
import numpy as np
import os
import sqlite3

# 1) JSON CSV HTML XML
# 2) bINARY fILES -> (!#mf 3748792348)
# 3) Relational Databases

path = 'C://Users//danie//Documents//py-taco-gallardo-daniel-alejandro//Clase 15//DATA//artwork_data.csv'
df = pd.read_csv(
        path,
        nrows = 10)

columnas = ['id','artist','title','medium','year','acquisitionYear','height','width','units']
df2 = pd.read_csv(
        path,
        nrows = 10,usecols=columnas)

df3 = pd.read_csv(
        path,
        nrows = 10,
        usecols=columnas,
        index_col = 'id')

path_save = 'C://Users//danie//Documents//py-taco-gallardo-daniel-alejandro//Clase 15//DATA//artwork_data.pickle'
path_save2 = 'C://Users//danie//Documents//py-taco-gallardo-daniel-alejandro//Clase 15//DATA//whole_artwork_data.pickle'

df3.to_pickle(path_save)

df4 = pd.read_csv(path)
df4.to_pickle(path_save2)

df5 = pd.read_pickle(path_save2)

dfs = pd.read_pickle(path_save2)
df = dfs.iloc[49980:50019,:].copy()

#ARCHIVOS A LOS QUE PUEDE EXPORTAR UN DATAFRAME
#JSON
#EXCEL
#SQL


### EXCEL  ##

path_guardado = 'C://Users//danie//Documents//py-taco-gallardo-daniel-alejandro//Clase 15//DATA//mi_df_completo.xlsx'
df.to_excel(path_guardado)
df.to_excel(path_guardado, index = False)

columnas = ['artist','title','year']
df.to_excel(path_guardado, columns = columnas)

### Multiples Hojas de Trabajo ###

path_multiple = 'C://Users//danie//Documents//py-taco-gallardo-daniel-alejandro//Clase 15//DATA//mi_df_multiples.xlsx'
writer = pd.ExcelWriter(path_multiple, engine = 'xlsxwriter')
df.to_excel(writer, sheet_name = 'Primera')
df.to_excel(writer, sheet_name = 'Segunda', index = False)
df.to_excel(writer, sheet_name = 'Tercera', columns = columnas)

writer.save()

numero_artistas = df['artist'].value_counts()
path_colores = 'C://Users//danie//Documents//py-taco-gallardo-daniel-alejandro//Clase 15//DATA//mi_df_colores.xlsx'
writer = pd.ExcelWriter(path_colores, engine = 'xlsxwriter')

numero_artistas.to_excel(writer, sheet_name = 'Artistas')

hojas_artistas = writer.sheets['Artistas']

rango_celdas = 'B2:B{}'.format(len(numero_artistas.index) + 1)

formato_artistas = {
        "type":"2_color_scale",
        "min_value":"10",
        "min_type":"percentile",
        "max_value":"99",
        "max_type":"percentile"}
hojas_artistas.conditional_format(rango_celdas,formato_artistas)        
writer.save()

import xlsxwriter
workbook = xlsxwriter.Workbook('C://Users//danie//Documents//py-taco-gallardo-daniel-alejandro//Clase 15//DATA//chart_line.xlsx')
worksheet = workbook.add_worksheet()

# Add the worksheet data to be plotted.
data = numero_artistas.values
worksheet.write_column('A1', data)

# Create a new chart object.
chart = workbook.add_chart({'type': 'line'})

# Add a series to the chart.
chart.add_series({'values': '=Sheet1!$A$1:$A$6'})

# Insert the chart into the worksheet.
worksheet.insert_chart('C1', chart)

workbook.close()

