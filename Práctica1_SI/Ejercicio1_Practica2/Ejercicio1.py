import base64
import sqlite3
from io import BytesIO

import pandas as pd
import matplotlib.pyplot as plt
from flask import render_template


def usuariosCriticosGraf(n):

    # Conectar con la base de datos SQLite
    conn = sqlite3.connect('datos.db')

    # Leer los datos relevantes de la base de datos
    df = pd.read_sql_query('''SELECT u.nombre_usuario, u.contrasena_segura, (CAST(e.cliclados as float)/e.total)*100 as probabilidad_spam
                              FROM usuarios u
                              INNER JOIN emails e ON u.id_usuario = e.id_usuario
                              ''', conn)

    # Identificar usuarios con contraseñas débiles
    df['contrasena_segura'] = df['contrasena_segura']
    usuarios_debiles = df[df['contrasena_segura'] == False]

    # Seleccionar los n usuarios más críticos (con contraseñas débiles y alta probabilidad de spam)
    usuarios_criticos = usuarios_debiles.nlargest(n, 'probabilidad_spam')
    print(usuarios_criticos)

    # Graficar los resultados
    plt.figure(figsize=(10, 6))
    usuarios_criticos.set_index('nombre_usuario')['probabilidad_spam'].plot(kind='bar', color='skyblue')
    plt.title('Los ' + str(n) + ' Usuarios Más Críticos')
    plt.xlabel('Nombre de Usuario')
    plt.ylabel('Probabilidad de Hacer Clic en Spam')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Convertir el gráfico a una imagen base64 para mostrarlo en la página web
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return plot_url


def paginaWebVulnerableGraf(n):
    # Conectar con la base de datos SQLite
    conn = sqlite3.connect('datos.db')

    # Leer los datos relevantes de la base de datos
    df = pd.read_sql_query('''SELECT web, cookies, aviso, proteccion_datos, creacion FROM legal''', conn)

    # Calcular el número de políticas desactualizadas para cada página web
    df['politicas_desactualizadas'] = df[['cookies', 'aviso', 'proteccion_datos']].apply(lambda row: sum(row == 0),
                                                                                         axis=1)

    # Seleccionar las 5 páginas web con más políticas desactualizadas
    top_n_politicas_desactualizadas = df.nlargest(n, ['politicas_desactualizadas', 'creacion'])
    print(top_n_politicas_desactualizadas)

    # Graficar los resultados
    plt.figure(figsize=(12, 6))

    top_n_politicas_desactualizadas.set_index('web', inplace=True)
    ax = top_n_politicas_desactualizadas['politicas_desactualizadas'].plot(kind='bar')

    # Añadir etiquetas y leyendas al gráfico
    plt.title('Las ' + str(n) + ' Páginas Webs Más Vulnerables')
    plt.xlabel('Página Web')
    plt.ylabel('Número de Políticas Desactualizadas')
    plt.xticks(rotation=45)

    ax.set_yticks(range(0, 4))
    ax.set_yticklabels(range(0, 4))

    plt.tight_layout()

    # Convertir el gráfico a una imagen base64 para mostrarlo en la página web
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return plot_url
