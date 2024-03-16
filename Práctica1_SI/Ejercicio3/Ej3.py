import pandas as pd
import sqlite3

# Conectarse a la base de datos
conn = sqlite3.connect('datos.db')



df = pd.read_sql_query('''SELECT *
                                   FROM usuarios u INNER JOIN emails e ON e.id_usuario=u.id_usuario
                                   ''', conn)

df_perm = df.groupby("permisos")
df_perm_0 = df_perm.get_group(0)
df_perm_1 = df_perm.get_group(1)

# Calcular la información solicitada para la variable dentro del email de phishing para permisos igual a 0
print("Para permisos igual a 0:")
print("Número de observaciones:", len(df_perm_0))
print("Número de valores ausentes (missing):", df_perm_0['phishing'].isnull().sum())
print("Mediana:", df_perm_0['phishing'].median())
print("Media:", df_perm_0['phishing'].mean())
print("Varianza:", df_perm_0['phishing'].var())
print("Valor máximo:", df_perm_0['phishing'].max())
print("Valor mínimo:", df_perm_0['phishing'].min())

# Calcular la información solicitada para la variable dentro del email de phishing para permisos igual a 1
print("\nPara permisos igual a 1:")
print("Número de observaciones:", len(df_perm_1))
print("Número de valores ausentes (missing):", df_perm_1['phishing'].isnull().sum())
print("Mediana:", df_perm_1['phishing'].median())
print("Media:", df_perm_1['phishing'].mean())
print("Varianza:", df_perm_1['phishing'].var())
print("Valor máximo:", df_perm_1['phishing'].max())
print("Valor mínimo:", df_perm_1['phishing'].min())

print("\n-------------------------------------------------------------------------------------")

df_pass = df.groupby("contrasena_segura")
df_pass_0 = df_pass.get_group(0)
df_pass_1 = df_pass.get_group(1)

# Calcular la información solicitada para la variable dentro del email de phishing para permisos igual a 0
print("\nPara contraseñas no seguras:")
print("Número de observaciones:", len(df_pass_0))
print("Número de valores ausentes (missing):", df_pass_0['phishing'].isnull().sum())
print("Mediana:", df_pass_0['phishing'].median())
print("Media:", df_pass_0['phishing'].mean())
print("Varianza:", df_pass_0['phishing'].var())
print("Valor máximo:", df_pass_0['phishing'].max())
print("Valor mínimo:", df_pass_0['phishing'].min())

# Calcular la información solicitada para la variable dentro del email de phishing para permisos igual a 1
print("\nPara contraseñas seguras:")
print("Número de observaciones:", len(df_pass_1))
print("Número de valores ausentes (missing):", df_pass_1['phishing'].isnull().sum())
print("Mediana:", df_pass_1['phishing'].median())
print("Media:", df_pass_1['phishing'].mean())
print("Varianza:", df_pass_1['phishing'].var())
print("Valor máximo:", df_pass_1['phishing'].max())
print("Valor mínimo:", df_pass_1['phishing'].min())
