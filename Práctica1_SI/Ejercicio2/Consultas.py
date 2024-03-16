import pandas as pd
import sqlite3

# Conectarse a la base de datos
conn = sqlite3.connect('datos.db')

# Calcular el número de muestras
df_muestras = pd.read_sql_query('''SELECT COUNT(DISTINCT id_usuario) AS num_muestras FROM usuarios''', conn)
n_muestras = df_muestras.values[0][0]
print("Número de Muestras: %d" % n_muestras)
print("---------------------------------------------------------------")


#SUM((COUNT(fecha) - AVG(COUNT(fecha))) * (COUNT(fecha) - AVG(COUNT(fecha)))) / (COUNT(fecha) - 1) AS desviacion_fechas
# Calcular media y desviación estándar de fechas
df_fechas = pd.read_sql_query('''SELECT COUNT(fecha) AS num_fechas_user  
                                   FROM fechas
                                   GROUP BY id_usuario''', conn)

desviacion_fechas = df_fechas.std().values[0]
media_fechas = df_fechas.mean().values[0]
print("Media Fechas: %.4f" % media_fechas)
print("Desviación Estándar Fechas: %.4f" % desviacion_fechas)
print("---------------------------------------------------------------")


# Calcular media y desviación estándar de IPs
df_ips = pd.read_sql_query('''SELECT COUNT(ip) AS num_ips_user
                                FROM ips
                                GROUP BY id_usuario''', conn)

desviacion_ips = df_ips.std().values[0]
media_ips = df_ips.mean().values[0]
print("Media IPs: %.4f" % media_ips)
print("Desviación Estándar IPs: %.4f" % desviacion_ips)
print("---------------------------------------------------------------")