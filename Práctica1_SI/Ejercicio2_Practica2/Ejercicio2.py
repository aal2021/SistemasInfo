import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def usuariosCriticosMas50(n):

    # Conectar con la base de datos SQLite
    conn = sqlite3.connect('datos.db')

    # Leer los datos relevantes de la base de datos
    df = pd.read_sql_query('''SELECT u.nombre_usuario, u.contrasena_segura, (CAST(e.cliclados as float)/e.total)*100 as probabilidad_spam
                              FROM usuarios u
                              INNER JOIN emails e ON u.id_usuario = e.id_usuario
                              ''', conn)

    # Identificar usuarios con contraseñas débiles (aquí necesitarás definir cómo determinar las contraseñas débiles)
    usuarios_debiles = df[df['contrasena_segura']==0]

    # Seleccionar los 10 usuarios más críticos (con contraseñas débiles y alta probabilidad de spam)
    usuarios_criticos = usuarios_debiles.nlargest(n, 'probabilidad_spam')

    usuarios_criticos_mas50 = usuarios_criticos[usuarios_criticos['probabilidad_spam'] > 50]
    print(usuarios_criticos_mas50)

    # Graficar los resultados
    plt.figure(figsize=(10, 6))
    usuarios_criticos_mas50.set_index('nombre_usuario')['probabilidad_spam'].plot(kind='bar', color='skyblue')
    plt.title('Los ' + str(n) + ' Usuarios Más Críticos con Probabilidad > 50')
    plt.xlabel('Nombre de Usuario')
    plt.ylabel('Probabilidad de Hacer Clic en Spam')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def usuariosCriticosMenos50(n):

    # Conectar con la base de datos SQLite
    conn = sqlite3.connect('datos.db')

    # Leer los datos relevantes de la base de datos
    df = pd.read_sql_query('''SELECT u.nombre_usuario, u.contrasena_segura, (CAST(e.cliclados as float)/e.total)*100 as probabilidad_spam
                              FROM usuarios u
                              INNER JOIN emails e ON u.id_usuario = e.id_usuario
                              ''', conn)

    # Identificar usuarios con contraseñas débiles (aquí necesitarás definir cómo determinar las contraseñas débiles)
    usuarios_debiles = df[df['contrasena_segura']==0]

    # Seleccionar los 10 usuarios más críticos (con contraseñas débiles y alta probabilidad de spam)
    usuarios_criticos = usuarios_debiles.nlargest(n, 'probabilidad_spam')

    usuarios_criticos_menos50 = usuarios_criticos[usuarios_criticos['probabilidad_spam'] < 50]
    print(usuarios_criticos_menos50)

    # Graficar los resultados
    plt.figure(figsize=(10, 6))
    usuarios_criticos_menos50.set_index('nombre_usuario')['probabilidad_spam'].plot(kind='bar', color='skyblue')
    plt.title('Los ' + str(n) + ' Usuarios Más Críticos con Probabilidad < 50')
    plt.xlabel('Nombre de Usuario')
    plt.ylabel('Probabilidad de Hacer Clic en Spam')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

usuariosCriticosMas50(10)
usuariosCriticosMenos50(10)