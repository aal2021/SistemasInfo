import json
import sqlite3

import graphviz
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn import tree


def regresion(X, y):
    X_1dim = pd.DataFrame((X['cliclados'] / X['total']) * 0.75 + (X['permisos'] * 0.25))
    # Dividir el conjunto de datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X_1dim, y, test_size=0.6, random_state=80)
    # Crear un modelo de regresión lineal
    model = linear_model.LinearRegression()

    # Entrenar el modelo
    model.fit(X_train, y_train)

    # Predecir en el conjunto de prueba
    y_pred = model.predict(X_test)

    print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))

    plt.scatter(X_test, y_test, color="black")
    plt.plot(X_test, y_pred, color="blue", linewidth=3)
    # plt.xticks(())
    plt.yticks([0, 1])
    plt.xlabel('(Clicados/Total) * 0.75 + Permisos * 0.25')
    plt.ylabel('Clasificación Usuario')
    plt.show()

    return model

def predecir_regresion(model, nombre, telefono, provincia, permisos, total, phishing, cliclados):
    usuario = {
        'telefono': [telefono],
        'provincia': [provincia],
        'permisos': [permisos],
        'total': [total],
        'phishing': [phishing],
        'cliclados': [cliclados]
    }

    df_usuarios = pd.DataFrame(usuario)
    usuarios_1dim = pd.DataFrame((df_usuarios['cliclados'] / df_usuarios['total']) * 0.75 + (df_usuarios['permisos'] * 0.25))
    prediccion_nuevo = model.predict(usuarios_1dim)

    esCritico = True
    if prediccion_nuevo < model.coef_:
        esCritico = False

    return esCritico

def decisionTree(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=75)

    # Entrenar el modelo de árbol de decisión
    clf = tree.DecisionTreeClassifier(random_state=20)
    clf = clf.fit(X_train, y_train)

    # Imprimir el gráfico del árbol de decisión
    dot_data = tree.export_graphviz(clf, out_file=None,
                                    feature_names=X.columns,
                                    class_names=['No Crítico', 'Crítico'],  # Ejemplo de nombres de clases
                                    filled=True, rounded=True,
                                    special_characters=True)
    graph = graphviz.Source(dot_data)
    graph.render('tree.gv', view=True).replace('\\', '/')

    return clf

def predecir_decisionTree(clf, nombre, telefono, provincia, permisos, total, phishing, cliclados):
    usuario = {
        'telefono': [telefono],
        'provincia': [provincia],
        'permisos': [permisos],
        'total': [total],
        'phishing': [phishing],
        'cliclados': [cliclados]
    }

    df_usuario = pd.DataFrame(usuario)
    prediccion_nuevo = clf.predict(df_usuario)

    return prediccion_nuevo

def forest(X, y):
    # Entrenar el modelo de bosque aleatorio
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.6, random_state=24)
    clf = RandomForestClassifier(max_depth=2, random_state=0, n_estimators=10)
    clf.fit(X_train, y_train)

    for i in range(len(clf.estimators_)):
        estimator = clf.estimators_[i]
        dot_data = tree.export_graphviz(estimator,
                                        out_file=None,
                                        feature_names=X.columns.values,
                                        class_names=['No Crítico', 'Crítico'],  # Ejemplo de nombres de clases
                                        rounded=True,
                                        proportion=False,
                                        precision=2,
                                        filled=True)
        graph = graphviz.Source(dot_data)
        graph.render('tree' + str(i))

    return clf

def predecirForest(clf, nombre, telefono, provincia, permisos, total, phishing, cliclados):
    usuario = {
        'telefono': [telefono],
        'provincia': [provincia],
        'permisos': [permisos],
        'total': [total],
        'phishing': [phishing],
        'cliclados': [cliclados]
    }

    df_usuario = pd.DataFrame(usuario)
    prediccion_nuevo = clf.predict(df_usuario)

    return prediccion_nuevo
