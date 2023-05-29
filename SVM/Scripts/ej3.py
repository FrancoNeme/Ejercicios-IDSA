#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 20:54:54 2023

##############################
#                            #
# MAQUINAS DE SOPORTE        #
# VECTORIAL                  #
#                            #
# GUIA DE EJERCICIOS         #
# Ejercicio 3                # 
#                            #
##############################

@author: Franco Neme
"""

#%% CARGA DE LIBRERIAS 
# = = = = = = = = = = =

# import matplotlib.pyplot as plt
import numpy as np
# import os
import pandas as pd
import plotly.io as pio
import plotly.express as px
# import seaborn as sns

from sklearn import metrics
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import warnings

warnings.filterwarnings('ignore')

#%% CREACION CARPETA DE SALIDAS
# = = = = = = = = = = = = = = = 

# Carpeta_salidas_nombre = 'Ejercicio3'
# Carpeta_salidas = os.path.join(os.getcwd(), '..', 'Salidas', Carpeta_salidas_nombre)

# try:
#     os.mkdir(Carpeta_salidas) # Creo directorio para las salidas del estimador
# except:
#     pass



#%% CARGA DE DATOS Y PREARMADO
# = = = = = = = = = = = = = = =

# Pre-tratamiento de datos
# ------------------------

datos_crudos = pd.read_excel('../Datasets/Grupos Comerciales.csv.xlsx')

# Asignar a "Cliente" como el index del df

datos_crudos.set_index(['Cliente'], inplace = True)

# Codificacion ternaria para el target

datos_crudos['Comercial'] = datos_crudos.Comercial.map({'A': 0, 'B': 1, 'C': 2})

# Division en matriz de caracteristicas y vector target
# -----------------------------------------------------

datos = datos_crudos.copy() 

y = np.array(datos['Comercial']) 
X = np.array(datos.drop(['Comercial'],1))



#%% COMO SON TRES CARACTERISTICAS VOY A APROVECHAR Y VER LA DISTRIBUCION DE PUNTOS
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

pio.renderers.default = 'browser'

fig = px.scatter_3d(datos, x='Importe', y='Margen', z='Km',
              color='Comercial')
fig.show()

'''
And if you'd like display your figure in the browser as a fully interactive version, just run:
import plotly.io as pio
pio.renderers.default='browser'

Now your figure will be displayed in your default browser.

To switch back to producing your figure in Spyder, just run:

import plotly.io as pio
pio.renderers.default='svg'
'''

# Observo que los datos no son perfectamente separables linealmente
# Pero sí veo que no se superponen, con truco del kernel tranquilamente
# podría establecer un buen hiperlano. Hay una buena separación de cada
# clase en el espacio 3D. Se puede aplicar SVM.



#%% DIVISION EN VARIABLES DE ENTRENAMIENTO Y DE PRUEBA
# = = = = = = = = = = = = = = = = = = = = = = = = = = =

X_train1, X_test, y_train1, y_test = train_test_split(X, y, test_size = 0.2, stratify = y, 
                                                    random_state = 16)   

X_train, X_val, y_train, y_val = train_test_split(X_train1, y_train1, test_size = 0.2, stratify = y_train1, 
                                                  random_state = 16)



#%% BUSQUEDA DE HIPERPARAMETROS POR VALIDACION CRUZADA 
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 


# Grid de hiperparámetros
# -------------------------

param_range = [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]
degree_range = [i+1 for i in range(5)]

param_grid = [{'svc__C': param_range,'svc__kernel': ['linear']}, 
              {'svc__C': param_range,'svc__gamma': param_range,'svc__kernel': ['rbf', 'poly'],'svc__degree':degree_range }]


# Búsqueda por validación cruzada
# --------------------------------

svc = SVC(random_state = 16)

pipe_svc = make_pipeline(StandardScaler(), svc)

gs = GridSearchCV(estimator = pipe_svc, param_grid = param_grid, scoring = None, cv = 10, n_jobs = -1)

gs.fit(X_train, y_train)


# print best parameter after tuning
# ---------------------------------
print('\n\n---------------------------------\n---------------------------------\n\nModelo opt:\n')
print(f'Mejor score: {100*gs.best_score_} %')
print(f'Mejores parámetros: {gs.best_params_}')  


# Veamos la matriz de confusión 
# ------------------------------

svm = gs.best_estimator_        # elegimos el que mejor salió
svm.fit(X_train, y_train)       # entrenamos...
y_pred_sv = svm.predict(X_val)  # ... y predecimos sobre el cjto de validación

# matriz de confusión y accuracy

print("\nMatriz de confusión:\n" , metrics.confusion_matrix(y_val, y_pred_sv))
print(f'\nVal_accuracy_svm = {100*svm.score(X_val, y_val)} %')  



#%% Ahora terminemos el trabajo, entrenando el que parece ser el
# mejor modelo pero sobre todo el cjto de entrenamiento 'train1'
# y luego veamos el rendimiento sobre el cjto de testeo 'test'

print('\n\n---------------------------------\n---------------------------------\n\nModelo opt: sobre cjto train1 y rendimiento sobre test\n')

svm.fit(X_train1, y_train1)

y_pred1 = svm.predict(X_test)

print("\nMatriz de confusión:\n" , metrics.confusion_matrix(y_test, y_pred1))

conf_svm = metrics.confusion_matrix(y_test, y_pred1)

print(f'\nVal_accuracy = {100*svm.score(X_test, y_test)} %')


#%%
