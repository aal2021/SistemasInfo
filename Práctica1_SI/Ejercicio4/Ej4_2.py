import io
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def generar_grafico2():
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
    usuarios_criticos = usuarios_debiles.nlargest(10, 'probabilidad_spam')

    # Graficar los resultados
    plt.figure(figsize=(10, 6))
    usuarios_criticos['probabilidad_spam'].plot(kind='bar', color='skyblue')
    plt.title('Los 10 Usuarios Más Críticos')
    plt.xlabel('ID de Usuario')
    plt.ylabel('Probabilidad de Hacer Clic en Spam')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Capturar la salida del gráfico
    img_bytes = io.BytesIO()
    plt.savefig(img_bytes, format='png')
    img_bytes.seek(0)

    # Limpiar la figura para liberar memoria
    plt.clf()

    return img_bytes
