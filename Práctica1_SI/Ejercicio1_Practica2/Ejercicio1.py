import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def usuariosCriticos(n):

    # Conectar con la base de datos SQLite
    conn = sqlite3.connect('datos.db')

    # Leer los datos relevantes de la base de datos
    df = pd.read_sql_query('''SELECT u.id_usuario, u.contrasena_segura, (CAST(e.cliclados as float)/e.total)*100 as probabilidad_spam
                              FROM usuarios u
                              INNER JOIN emails e ON u.id_usuario = e.id_usuario
                              ''', conn)

    # Identificar usuarios con contraseñas débiles (aquí necesitarás definir cómo determinar las contraseñas débiles)
    usuarios_debiles = df[df['contrasena_segura']==0]

    # Seleccionar los 10 usuarios más críticos (con contraseñas débiles y alta probabilidad de spam)
    usuarios_criticos = usuarios_debiles.nlargest(n, 'probabilidad_spam')
    print(usuarios_criticos)

    # Graficar los resultados
    plt.figure(figsize=(10, 6))
    usuarios_criticos['probabilidad_spam'].plot(kind='bar', color='skyblue')
    plt.title('Los ' + str(n) + ' Usuarios Más Críticos')
    plt.xlabel('ID de Usuario')
    plt.ylabel('Probabilidad de Hacer Clic en Spam')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def paginaWebVulnerable(n):
    # Conectar con la base de datos SQLite
    conn = sqlite3.connect('datos.db')

    # Leer los datos relevantes de la base de datos
    df = pd.read_sql_query('''SELECT web, cookies, aviso, proteccion_datos FROM legal''', conn)

    # Calcular el número de políticas desactualizadas para cada página web
    df['politicas_desactualizadas'] = df[['cookies', 'aviso', 'proteccion_datos']].apply(lambda row: sum(row == 0),
                                                                                         axis=1)

    # Seleccionar las 5 páginas web con más políticas desactualizadas
    top_n_politicas_desactualizadas = df.nlargest(n, 'politicas_desactualizadas')

    # Graficar los resultados
    plt.figure(figsize=(12, 6))

    top_n_politicas_desactualizadas.set_index('web', inplace=True)
    top_n_politicas_desactualizadas.plot(kind='bar')

    # Añadir etiquetas y leyendas al gráfico
    plt.title('Las ' + str(n) + ' Páginas Webs Más Vulnerables')
    plt.xlabel('Página Web')
    plt.ylabel('Estado de las Políticas')
    plt.xticks(rotation=45)
    plt.legend()

    plt.tight_layout()
    plt.show()

usuariosCriticos(10)
paginaWebVulnerable(10)