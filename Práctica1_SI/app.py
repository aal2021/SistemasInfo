import subprocess
from flask import Flask, render_template, request, make_response, send_file
from Ejercicio4.Ej4_1 import generar_grafico1
from Ejercicio4.Ej4_2 import generar_grafico2
from Ejercicio4.Ej4_3 import generar_grafico3
from Ejercicio4.Ej4_4 import generar_grafico4
from Ejercicio4_Practica2.DatosDeOtraAPI import noticasOtraAPI
from Ejercicio4_Practica2.GeneradorPDFs import usuariosCriticos
from Ejercicio4_Practica2.GeneradorPDFs import paginaWebVulnerable
from fpdf import FPDF

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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


@app.route('/GeneradorPDF_Ej4', methods=['GET', 'POST'])
def generar_pdf():
    if request.method == 'POST':
        # Obtener el número de usuarios a incluir en el informe desde el formulario
        num_elementos = int(request.form['num_elementos'])

        # Generar informe de usuarios críticos
        informe_usuarios = usuariosCriticos(num_elementos)
        informe_paginas = paginaWebVulnerable(num_elementos)

        with open('usuarios_criticos.txt', 'w') as file:
            file.write(informe_usuarios)

        with open('paginas-vulnerables.txt', 'w') as file:
            file.write(informe_paginas)

        # Convertir el archivo de texto en PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", style="IB", size=20)

        #Título
        pdf.set_xy(0, 20)
        pdf.cell(210, 10, txt="Informe sobre usuarios críticos", ln=True, align='C')

        # Agregar los datos como una tabla
        pdf.set_xy(10, 40)
        pdf.set_font("Arial", size=12)


        with open('usuarios_criticos.txt', 'r') as file:
            for line in file:
                pdf.cell(180, 10, txt=line, ln=True, border=1, align='C')

        pdf.ln(11)
        with open('paginas-vulnerables.txt', 'r') as file:
            for line in file:
                pdf.cell(180, 10, txt=line, ln=True, border=1, align='C')

        pdf.output("informe_critico.pdf")

        #Si es POST devuelve el PDF
        return send_file("informe_critico.pdf", as_attachment=True)

    #Si es GET devuelve la plantilla
    return render_template('generador_pdf.html')

@app.route('/Noticias_Ej4')
def otra_api():
    articles = noticasOtraAPI()
    return render_template('noticias.html', articles=articles)


if __name__ == '__main__':
    app.run(debug=True)
