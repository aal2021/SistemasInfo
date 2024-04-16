import subprocess
from flask import Flask, render_template, request, make_response, send_file
import io
from reportlab.pdfgen import canvas

from Ejercicio4.Ej4_1 import generar_grafico1
from Ejercicio4.Ej4_2 import generar_grafico2
from Ejercicio4.Ej4_3 import generar_grafico3
from Ejercicio4.Ej4_4 import generar_grafico4
from Ejercicio4_Practica2.GeneradorPDFs import usuariosCriticos
from fpdf import FPDF



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

@app.route('/GeneradorPDF', methods=['GET', 'POST'])
def generar_pdf():
    if request.method == 'POST':
        # Obtener el número de usuarios a incluir en el informe desde el formulario
        num_elementos = int(request.form['num_elementos'])

        # Generar informe de usuarios críticos
        informe_usuarios = usuariosCriticos(num_elementos)

        with open('usuarios_criticos.txt', 'w') as file:
            file.write(informe_usuarios)

        # Convertir el archivo de texto en PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        with open('usuarios_criticos.txt', 'r') as file:
            for line in file:
                pdf.cell(200, 10, txt=line, ln=True)

        pdf.output("usuarios_criticos.pdf")

        #Si es POST devuelve el PDF
        return send_file("usuarios_criticos.pdf", as_attachment=True)

    #Si es GET devuelve la plantilla
    return render_template('generador_pdf.html')

if __name__ == '__main__':
   app.run(debug = True)
