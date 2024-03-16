import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Conectar con la base de datos SQLite
conn = sqlite3.connect('datos.db')

# Leer los datos relevantes de la base de datos
# Seleccionamos los el id_usuario, el si la contraseña es segura o no y la probabilidad de
# que un usuario clique en un email de phishing de todos los que recibe
df = pd.read_sql_query('''SELECT u.id_usuario, u.contrasena_segura, (CAST(e.cliclados as float)/e.total)*100 as probabilidad_spam
                          FROM usuarios u
                          INNER JOIN emails e ON u.id_usuario = e.id_usuario
                          ''', conn)

# Identificar usuarios con contraseñas débiles
usuarios_debiles = df[df['contrasena_segura']==0]

# Seleccionar los 10 usuarios más críticos (con contraseñas débiles y alta probabilidad de spam)
usuarios_criticos = usuarios_debiles.nlargest(10, 'probabilidad_spam')
print(usuarios_criticos)