import io

from flask import Flask, send_file, Response
import subprocess
from flask import render_template
from flask import request
import json
import jsonify
import plotly.graph_objects as go
from matplotlib import pyplot as plt

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



if __name__ == '__main__':
   app.run(debug = True)
