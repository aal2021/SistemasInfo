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

# Calcular media y desviación estándar de emails de phishing
df_phishing_emails = pd.read_sql_query('''SELECT cliclados AS clicados_phishing_user
                                           FROM emails''', conn)

desviacion_emails = df_phishing_emails.std().values[0]
media_emails = df_phishing_emails.mean().values[0]
print("Media Emails Phishing Clicados: %.4f" % media_emails)
print("Desviación Estándar Emails Phishing Clicados: %.4f" % desviacion_emails)
print("---------------------------------------------------------------")

# Calcular valor mínimo y máximo de emails recibidos
df_min_max_emails = pd.read_sql_query('''SELECT MIN(total) AS min_total_emails, MAX(total) AS max_total_emails FROM emails''', conn)
min_emails = df_min_max_emails.values[0][0]
max_emails = df_min_max_emails.values[0][1]
print("Mínimo Número de Emails Recibidos: %d" % min_emails)
print("Máximo Número de Emails Recibidos: %d" % max_emails)
print("---------------------------------------------------------------")

# Calcular valor mínimo y máximo de emails de phishing de un administrador
df_admin_emails = pd.read_sql_query('''SELECT MIN(cliclados) AS min_admin_phishing, MAX(cliclados) AS max_admin_phishing
                                       FROM emails e
                                       JOIN usuarios u ON e.id_usuario = u.id_usuario
                                       WHERE u.permisos = 1''', conn)
min_admin_emails = df_admin_emails.values[0][0]
max_admin_emails = df_admin_emails.values[0][1]
print("Mínimo Número de Emails de Phishing en los que Interactuó un Admin: %d" % min_admin_emails)
print("Máximo Número de Emails de Phishing en los que Interactuó un Admin: %d" % max_admin_emails)
print("---------------------------------------------------------------")

# # Cerrar conexión a la base de datos
conn.close()
