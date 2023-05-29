#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 16:02:08 2023

##############################
#                            #
# MAQUINAS DE SOPORTE        #
# VECTORIAL                  #
#                            #
# GUIA DE EJERCICIOS         #
# Ejercicio 1                # 
#                            #
##############################

@author: Franco Neme
"""


#%% CARGA DE LIBRERIAS 
# = = = = = = = = = = =

import matplotlib.pyplot as plt
# import numpy as np
import os
import pandas as pd
import seaborn as sns

from sklearn import metrics, svm
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import warnings

warnings.filterwarnings('ignore')

#%% CREACION CARPETA DE SALIDAS
# = = = = = = = = = = = = = = = 

Carpeta_salidas_nombre = 'Ejercicio1'
Carpeta_salidas = os.path.join(os.getcwd(), '..', 'Salidas', Carpeta_salidas_nombre)

try:
    os.mkdir(Carpeta_salidas) # Creo directorio para las salidas del estimador
except:
    pass



#%% CARGA DE DATOS Y PREARMADO
# = = = = = = = = = = = = = = =

# Pre-tratamiento de datos
# ------------------------

datos_crudos = pd.read_csv('../Datasets/Clientes_Credito.csv', sep = ';', encoding='latin-1')

# Asignar a "Cliente" como el index del pd

datos_crudos.set_index(['Cliente'], inplace = True)

# 

# Division en matriz de caracteristicas y vector target
# -----------------------------------------------------

X = datos_crudos.iloc[:,:-1]
y = datos_crudos.iloc[:,-1]



#%% DIVISION EN VARIABLES DE ENTRENAMIENTO Y DE PRUEBA
# = = = = = = = = = = = = = = = = = = = = = = = = = = =

X_train1, X_test, y_train1, y_test = train_test_split(X, y, test_size = 0.2, stratify = y, 
                                                    random_state = 16)   
X_train, X_val, y_train, y_val = train_test_split(X_train1, y_train1, test_size = 0.2, stratify = y_train1, 
                                                  random_state = 16)


#%% FORMA1. MODELOS A TESTEAR
# = = = = = = = = = = = = = =

metricas = []

C = 1.0

models = {"lineal" : SVC(kernel="linear", C=C), 
          "lineal2" : svm.LinearSVC(C=C, max_iter=10000),
          "radial" : SVC(kernel="rbf", gamma=0.7, C=C),
          "polinomial": SVC(kernel="poly", degree=3, gamma="auto", C=C)}


# Testeo
# ------

for i in models:
    
    # Ajuste del clasificador
    
    models[i].fit(X_train1,y_train1)
    
    y_pred = models[i].predict(X_test)
    
    # Impresión de métricas
    
    print('\n\n---------------------------------\n---------------------------------\n')
    
    print("Modelo: " + i.upper() + '\n')
    
    print("acuracy:", metrics.accuracy_score(y_test,y_pred))
    
    print("precision:", metrics.precision_score(y_test,y_pred))
    
    print("recall" , metrics.recall_score(y_test,y_pred))
    
    print("\nMatriz de confusión:\n" , metrics.confusion_matrix(y_test, y_pred))
    
    ls = [i, metrics.accuracy_score(y_test,y_pred), metrics.precision_score(y_test,y_pred), metrics.recall_score(y_test,y_pred), metrics.confusion_matrix(y_test, y_pred)]
    
    # Plot matriz de confusión
    
    matriz = metrics.confusion_matrix(y_test, y_pred)
    
    sns.heatmap(matriz, annot=True)
    
    plt.title("Matriz de confusión. Modelo: " + i)
    plt.xlabel('Etiquetas predichas')
    plt.ylabel('Etiquetas reales')
    
    plt.savefig(Carpeta_salidas + '/' + 'matriz_confusion_Modelo_'+i+'.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # Prearmado csv de salida
    
    metricas.append(ls)
 


#%% FORMA 2. BUSQUEDA DE HIPERPARAMETROS POR VALIDACION CRUZADA 
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

gs = GridSearchCV(estimator = pipe_svc, param_grid = param_grid, scoring = None, cv = 4, n_jobs = -1)

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

print(f'\ntn, fp, fn, tp = {metrics.confusion_matrix(y_val, y_pred_sv).ravel()}')
print(f'\nVal_accuracy_svm = {100*svm.score(X_val, y_val)} %')  


#%% Ahora terminemos el trabajo, entrenando el que parece ser el
# mejor modelo pero sobre todo el cjto de entrenamiento 'train1'
# y luego veamos el rendimiento sobre el cjto de testeo 'test'

print('\n\n---------------------------------\n---------------------------------\n\nModelo opt: sobre cjto train1 y rendimiento sobre test\n')

svm.fit(X_train1, y_train1)
y_pred1 = svm.predict(X_test)

print(f'tn, fp, fn, tp = {metrics.confusion_matrix(y_test, y_pred1).ravel()}')

conf_svm = metrics.confusion_matrix(y_test, y_pred1)

print(f'Val_accuracy = {100*svm.score(X_test, y_test)} %')


#%% Salidas modelo optimo
# = = = = = = = = = = = = =

# Append este modelo "optimo" para salida csv
# -------------------------------------------


ls = [str("modelo_opt_" + gs.best_params_['svc__kernel']), metrics.accuracy_score(y_test,y_pred1), metrics.precision_score(y_test,y_pred1), metrics.recall_score(y_test,y_pred1), metrics.confusion_matrix(y_test, y_pred1)]

metricas.append(ls)

df_metricas = pd.DataFrame(metricas, columns = ["modelo", "accuracy", "precision", "recall", "matriz_confusion"])
df_metricas.to_csv(Carpeta_salidas + '/' + 'metricas.csv', index = False, header = True)

# Salida .png matriz de confusión
# -------------------------------

matriz = metrics.confusion_matrix(y_test, y_pred1)

sns.heatmap(matriz, annot=True)

plt.title("Matriz de confusión. Modelo_opt:" + gs.best_params_['svc__kernel'])
plt.xlabel('Etiquetas predichas')
plt.ylabel('Etiquetas reales')

plt.savefig(Carpeta_salidas + '/' + 'matriz_confusion_Modelo_Modelo_opt_'+gs.best_params_['svc__kernel']+'.png', dpi=300, bbox_inches='tight')
plt.show()
