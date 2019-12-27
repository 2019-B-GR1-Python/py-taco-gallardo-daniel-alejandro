# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 07:43:53 2019

@author: danie
"""

import numpy as np
import pandas as pd

arr_pand = np.random.randint(0,10,6).reshape(2,3)

df1 = pd.DataFrame(arr_pand)
s1 = df1[0]
s2 = df1[1]
s3 = df1[2]

serie_a = pd.Series([5,6])
df1[3] = serie_a

#Operaciones entre series como columnas de dataframe
df1[4] = s1*s2

datos_fisicos1 = pd.DataFrame(arr_pand,columns=['Estatura (cm)','Peso g','Edad (años)'])

datos_fisicos2 = pd.DataFrame(
        arr_pand,columns=[
                'Estatura (cm)',
                'Peso g',
                'Edad (años)'],index=['Daniel','Alejandro'])

#Setear filas y columnas despues de crea el Dataframe
df1.index = ['Daniel','Alejandro']
df1.columns =['A','B','C','D','E']

