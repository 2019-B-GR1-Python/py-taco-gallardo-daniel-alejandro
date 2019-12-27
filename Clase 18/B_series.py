# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 07:57:35 2019

@author: danie
"""

#Series
import numpy as np
import pandas as pd

lista_numeros = [1,2,3,4]
tupla_numeros = (1,2,3,4)
np_numeros = np.array((1,2,3,4))

serie_a = pd.Series(lista_numeros)
serie_b = pd.Series(tupla_numeros)
serie_c = pd.Series(np_numeros)

series_d = pd.Series([True,
                      False,
                      12,
                      12.12,
                      "Daniel",
                      None,
                      (),
                      [],
                      {"nombre","Daniel"}
                      ])

series_d[3]

lista_ciudades = ["Ambato","Cuenca","Loja","Quito"]
serie_ciudad = pd.Series(lista_ciudades,index=["A","C","L","Q"])
serie_ciudad["Q"]
serie_ciudad[3]

valores_ciudad = {"Ibarra":9500,
                  "Guayaquil":10000,
                  "Cuenca":7000,
                  "Quito":8000,
                  "Loja":3000}

serie_valor_ciudad = pd.Series(valores_ciudad)

serie_valor_ciudad[0]
serie_valor_ciudad["Ibarra"]

ciudades_menores_5000 = serie_valor_ciudad < 5000
ciudades_S5 = serie_valor_ciudad[ciudades_menores_5000]

s_mas = serie_valor_ciudad * 1.1

serie_valor_ciudad["Quito"] = serie_valor_ciudad["Quito"] - 50

print("Loja" in serie_valor_ciudad)

print("Lima" in serie_valor_ciudad)
print("Loja" in serie_valor_ciudad)

n_square = np.square(serie_valor_ciudad)

n_sen = np.sin(serie_valor_ciudad)

ciudades_uno = pd.Series({"Montanita":300,
                          "Guayaquil":10000,
                          "Quito":2000})

ciudades_dos = pd.Series({"Loja":300,"Guayaquil":10000})

ciudades_dos["Montanita"] = 0
ciudades_dos["Quito"] = 0
ciudades_uno["Loja"] = 0

print(ciudades_dos + ciudades_uno)

#Repetir indices
ciudad_add = ciudades_uno.add(ciudades_dos)
#No repetir indices
ciu_concatenadas_v = pd.concat([ciudades_uno,ciudades_dos], verify_integrity = True)

ciu_append = ciudades_uno.append(ciudades_dos,verify_integrity = True)

#Estadistica
print(np.max(ciudades_uno))
print(ciudades_uno.max())
print(pd.Series.max(ciudades_uno))

print(np.min(ciudades_uno))
print(ciudades_uno.min())
print(pd.Series.min(ciudades_uno))

ciudades_uno.mean()
ciudades_uno.median()
np.average(ciudades_uno)

#Filtrado
ciudades_uno.head(2)
ciudades_uno.tail(2)

ciudades_uno.sort_values(ascending = False).head(2)
ciudades_uno.sort_values().tail(2)

def calculo(valor):
    if(valor <= 1000):
        return valor*1.05
    if(valor > 1000 and valor <= 5000):
        return valor*1.10
    if(valor > 5000):
        return valor*1.15

ciudad_calculada = ciudades_uno.map(calculo)
ciudad_calculada
#Cuando No cumple la condicion 
#Aplica la formula
print(ciudades_uno.where(ciudades_uno < 1000, ciudades_uno*1.05))







