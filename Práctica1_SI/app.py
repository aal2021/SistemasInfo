from flask import Flask, send_file, Response
import subprocess

from Ejercicio4.Ej4_1 import generar_grafico1
from Ejercicio4.Ej4_2 import generar_grafico2
from Ejercicio4.Ej4_3 import generar_grafico3
from Ejercicio4.Ej4_4 import generar_grafico4

app = Flask(__name__)

@app.route('/EJ2')
def root2():
    output = subprocess.check_output(['python', 'Ejercicio2/Consultas.py'])
    output2 = output.decode("latin1")
    output3 = output2.replace('\n', '<br>')
    return output3

@app.route('/EJ3')
def root3():
    output = subprocess.check_output(['python', 'Ejercicio3/EJ3.py'])
    output2 = output.decode("latin1")
    output3 = output2.replace('\n', '<br>')
    return output3

@app.route('/EJ4/1')
def root4_1():
    img_bytes = generar_grafico1()
    return send_file(img_bytes, mimetype='image/png')

@app.route('/EJ4/2')
def root4_2():
    img_bytes = generar_grafico2()
    return send_file(img_bytes, mimetype='image/png')

@app.route('/EJ4/3')
def root4_3():
    img_bytes = generar_grafico3()
    return send_file(img_bytes, mimetype='image/png')

@app.route('/EJ4/4')
def root4_4():
    img_bytes = generar_grafico4()
    return send_file(img_bytes, mimetype='image/png')

if __name__ == '__main__':
   app.run(debug = True)
