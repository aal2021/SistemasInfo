import sqlite3
import pandas as pd

def usuariosCriticos(n):
    # Conectar con la base de datos SQLite
    conn = sqlite3.connect('datos.db')

    # Leer los datos relevantes de la base de datos
    df = pd.read_sql_query('''SELECT u.nombre_usuario, u.contrasena_segura, (CAST(e.cliclados as float)/e.total)*100 as probabilidad_spam
                              FROM usuarios u
                              JOIN emails e ON u.id_usuario = e.id_usuario
                              ''', conn)

    # Identificar usuarios con contraseñas débiles (aquí necesitarás definir cómo determinar las contraseñas débiles)
    usuarios_debiles = df[df['contrasena_segura']==0]

    # Seleccionar los 10 usuarios más críticos (con contraseñas débiles y alta probabilidad de spam)
    usuarios_criticos = usuarios_debiles.nlargest(n, 'probabilidad_spam')
    print(usuarios_criticos)

    # Retornar el informe como una cadena
    return usuarios_criticos.to_string(index=False)


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
    print(top_n_politicas_desactualizadas)

    # Informe como cadena
    return top_n_politicas_desactualizadas.to_string(index=False)
