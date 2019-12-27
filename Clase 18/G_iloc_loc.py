# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 08:04:49 2019

@author: danie
"""

import pandas as pd 
path_save = 'C://Users//danie//Documents//py-taco-gallardo-daniel-alejandro//Clase 15//DATA//whole_artwork_data.pickle'
df = pd.read_pickle(path_save)

primero = df.loc[1035,'artist']

primero = df.loc[0]
primero = df.iloc[0]


df2 = df.set_index('id')

df3.