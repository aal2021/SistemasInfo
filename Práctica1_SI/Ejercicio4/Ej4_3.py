import io
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def generar_grafico3():
    # Conectar con la base de datos SQLite
    conn = sqlite3.connect('datos.db')

    # Leer los datos relevantes de la base de datos
    df = pd.read_sql_query('''SELECT web, cookies, aviso, proteccion_datos FROM legal''', conn)

    # Calcular el número de políticas desactualizadas para cada página web
    df['politicas_desactualizadas'] = df[['cookies', 'aviso', 'proteccion_datos']].apply(lambda row: sum(row == 0), axis=1)

    # Seleccionar las 5 páginas web con más políticas desactualizadas
    top_5_politicas_desactualizadas = df.nlargest(5, 'politicas_desactualizadas')

    # Graficar los resultados
    plt.figure(figsize=(12, 6))

    top_5_politicas_desactualizadas.set_index('web', inplace=True)
    top_5_politicas_desactualizadas.plot(kind='bar')

    # Añadir etiquetas y leyendas al gráfico
    plt.title('Estado de las Políticas por Página Web')
    plt.xlabel('Página Web')
    plt.ylabel('Estado de las Políticas')
    plt.xticks(rotation=45)
    plt.legend()

    plt.tight_layout()

    # Capturar la salida del gráfico
    img_bytes = io.BytesIO()
    plt.savefig(img_bytes, format='png')
    img_bytes.seek(0)

    # Limpiar la figura para liberar memoria
    plt.clf()

    return img_bytes

