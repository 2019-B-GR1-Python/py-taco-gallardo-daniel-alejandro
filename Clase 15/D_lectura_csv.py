# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 08:20:33 2019

@author: danie
"""

import pandas as pd
import os

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