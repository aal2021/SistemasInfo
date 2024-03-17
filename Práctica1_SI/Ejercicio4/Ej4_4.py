import io
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def generar_grafico4():
    # Conectar con la base de datos SQLite
    conn = sqlite3.connect('datos.db')

    # Leer los datos relevantes de la base de datos
    df = pd.read_sql_query('''SELECT web, creacion, cookies, aviso, proteccion_datos FROM legal''', conn)

    # Calcular si la web cumple todas las políticas de privacidad
    df['cumple_politicas'] = (df['cookies'] == 1) & (df['aviso'] == 1) & (df['proteccion_datos'] == 1)

    # Agrupar por año de creación y contar el número de webs que cumplen todas las políticas y las que no
    grouped = df.groupby(['creacion', 'cumple_politicas']).size().unstack(fill_value=0)
    #el unstack es para que en el grafico en la misma columna veamos el numero de webs que cumplen las politicas
    #y las que no. Sino tendriamos dos columnas, una para el true y otra para el false
    print(grouped)

    # Graficar los resultados
    grouped.plot(kind='bar', stacked=True, figsize=(10, 6))
    plt.title('Webs según Año de Creación y Cumplimiento de Políticas de Privacidad')
    plt.xlabel('Año de Creación')
    plt.ylabel('Número de Webs')
    plt.legend(['No Cumple', 'Cumple'], title='Cumplimiento de Políticas')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Capturar la salida del gráfico
    img_bytes = io.BytesIO()
    plt.savefig(img_bytes, format='png')
    img_bytes.seek(0)

    # Limpiar la figura para liberar memoria
    plt.clf()

    return img_bytes
