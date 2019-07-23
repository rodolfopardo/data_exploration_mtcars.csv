#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 21:27:43 2019

@author: rodolfopardo
"""

import numpy as np
import pandas as pd


cars = pd.read_csv("~/Downloads/mtcars.csv")

#Conociendo nuestra base

cars[0:5]
cars.tail()
cars.dtypes

#Seleccionar todos los autos que tengas mas de 6 cilindradas 

cars[cars['Cylinders'] > 6]

#De los que tengan mayor cilidradas, todos los modelos Merc 

cars[(cars['Cylinders'] > 6) & (cars['Model'].str.contains("Merc"))]

#Seleccionar a todos los autos que tengan menos de cuatro carburadores 

cars[cars['Carburators'] < 4]

#De los que tengan menos de cuatro carburadores, todos los que sean Toyota

cars[(cars['Carburators'] < 4) & (cars['Model'].str.contains("Toyota"))]


#Estadistica descriptiva  MPG 
#Encontrando el valor maximo de mpg

cars['MPG'].max()

#Encontrando a que auto pertenece
cars[cars['MPG'] == 33.9]

#El minimo
cars['MPG'].min()

#Encontrando al minimo
cars[cars['MPG'] == 10.4]

#Otras estadisticas 

cars['MPG'].mean()
cars['MPG'].median()
q1 = cars['MPG'].quantile(0.25)
q3 = cars['MPG'].quantile(0.75)
cars['MPG'].describe()

#El IQR sirve para conocer que tan alejados se encuentran los valores 
iqr = q3-q1

#Histograma de frecuencias 
cars.hist()

#Identifiquemos que auto tiene más caballos de fuerza 

cars['Horsepower'].max()

cars[cars['Horsepower'] == 335]

#Y los que compiten con el Maserati que se encuentran entre 250 y 300 caballos de fuerza

cars[(cars['Horsepower'] > 250) & (cars['Horsepower'] < 300) ]

#FORD Pantera es su principal competidor 

#Identificando al auto con menor cantidad de caballos de fuerza 

cars['Horsepower'].min()

cars[cars['Horsepower'] == 52]

#Diferencia de caballos de fuerza entre Maserati y Honda 

diff = lambda x,y: x-y

min = cars['Horsepower'].min()
max = cars['Horsepower'].max()

diff(max,min)







