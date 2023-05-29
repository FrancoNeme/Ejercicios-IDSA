#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 20:01:30 2023

##############################
#                            #
# MAQUINAS DE SOPORTE        #
# VECTORIAL                  #
#                            #
# GUIA DE EJERCICIOS         #
# Ejercicio 2                # 
#                            #
##############################

@author: Franco Neme
"""


#%% CARGA DE LIBRERIAS 
# = = = = = = = = = = =

# import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
# import seaborn as sns

# from sklearn import metrics, svm
# from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, train_test_split
# from sklearn.pipeline import make_pipeline
# from sklearn.preprocessing import StandardScaler
import warnings

warnings.filterwarnings('ignore')

#%% CREACION CARPETA DE SALIDAS
# = = = = = = = = = = = = = = = 

Carpeta_salidas_nombre = 'Ejercicio2'
Carpeta_salidas = os.path.join(os.getcwd(), '..', 'Salidas', Carpeta_salidas_nombre)

try:
    os.mkdir(Carpeta_salidas) # Creo directorio para las salidas del estimador
except:
    pass



#%% CARGA DE DATOS Y PREARMADO
# = = = = = = = = = = = = = = =

# Pre-tratamiento de datos
# ------------------------

datos_crudos = pd.read_csv('../Datasets/Registro Fraude.csv', sep = ';', encoding='latin-1')

# Asignar a "Cliente" como el index del pd

datos_crudos.set_index(['Id'], inplace = True)

# Cambiar los valores "no" y "si" a booleanos (int)

datos_crudos['Reembolso'] = datos_crudos.Reembolso.map({'no': 0, 'si': 1})

datos_crudos['Fraude'] = datos_crudos.Fraude.map({'no': 0, 'si': 1})

# Codificacion One Hot

datos_crudos = pd.get_dummies(datos_crudos, dtype=int)

# Division en matriz de caracteristicas y vector target
# -----------------------------------------------------

datos = datos_crudos.copy() 

y = np.array(datos['Fraude']) 
X = np.array(datos.drop(['Fraude'],1))



#%% DIVISION EN VARIABLES DE ENTRENAMIENTO Y DE PRUEBA
# = = = = = = = = = = = = = = = = = = = = = = = = = = =

X_train1, X_test, y_train1, y_test = train_test_split(X, y, test_size = 0.2, stratify = y, 
                                                    random_state = 16)   

X_train, X_val, y_train, y_val = train_test_split(X_train1, y_train1, test_size = 0.2, stratify = y_train1, 
                                                  random_state = 16)
