# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 07:51:07 2019

@author: danie
"""

import pandas as pd
path_save = 'C://Users//danie//Documents//py-taco-gallardo-daniel-alejandro//Clase 15//DATA//whole_artwork_data.pickle'
df = pd.read_pickle(path_save)

#Obtener nombres de los artistas.
serie_artistas_repetidos = df["artist"]
artistas = pd.unique(serie_artistas_repetidos)
artistas.size

#Contar elementos que coincidan con un criterio
blake = df["artist"] == "Blake, William"
blake.value_counts()

df["artist"].value_counts()


df_blake = df[blake]
