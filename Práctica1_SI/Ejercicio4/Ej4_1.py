import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Conectar con la base de datos SQLite
conn = sqlite3.connect('datos.db')

# Leer los datos de la tabla
df = pd.read_sql_query('''SELECT u.id_usuario, u.permisos, f.fecha
                                   FROM usuarios u INNER JOIN fechas f ON f.id_usuario=u.id_usuario
                                   ''', conn)

df_perm = df.groupby("permisos")
df_perm_0 = df_perm.get_group(0).copy()
df_perm_1 = df_perm.get_group(1).copy()

# Convertir la columna de fechas al formato datetime
df_perm_0['fecha'] = pd.to_datetime(df_perm_0['fecha'], format='%d/%m/%Y')
df_perm_1['fecha'] = pd.to_datetime(df_perm_1['fecha'], format='%d/%m/%Y')

# Ordenar los datos por usuario y fecha
df_perm_0_order = df_perm_0.sort_values(by=['id_usuario', 'fecha'])
df_perm_1_order = df_perm_1.sort_values(by=['id_usuario', 'fecha'])

# Calcular la diferencia de tiempo entre cambios de contraseña por usuario
df_perm_0_order['diferencia_tiempo'] = df_perm_0_order.groupby('id_usuario')['fecha'].diff()
df_perm_1_order['diferencia_tiempo'] = df_perm_1_order.groupby('id_usuario')['fecha'].diff()

df_perm_0_order['diferencia_tiempo'] = pd.to_numeric(df_perm_0_order['diferencia_tiempo'].dt.days, downcast='integer')
df_perm_1_order['diferencia_tiempo'] = pd.to_numeric(df_perm_1_order['diferencia_tiempo'].dt.days, downcast='integer')

# Calcular la media de tiempo entre cambios de contraseña por usuario
media_tiempo_por_usuario_normal = df_perm_0_order.groupby('id_usuario')['diferencia_tiempo'].mean()
media_tiempo_por_usuario_priv = df_perm_1_order.groupby('id_usuario')['diferencia_tiempo'].mean()

# print("Media de tiempo entre cambios de contraseña por usuario:")
# print(media_tiempo_por_usuario_normal)
# print(media_tiempo_por_usuario_priv)

