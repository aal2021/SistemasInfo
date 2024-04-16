import sqlite3
import pandas as pd

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

    # Retornar el informe como una cadena
    return usuarios_criticos.to_string()




