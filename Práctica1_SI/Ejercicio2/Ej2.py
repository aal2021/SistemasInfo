import sqlite3
import json
import hashlib

# Crear conexión a la base de datos
conn = sqlite3.connect('datos.db')
c = conn.cursor()

# Crear tablas
c.execute('''CREATE TABLE usuarios (
                id_usuario INTEGER PRIMARY KEY,
                nombre_usuario TEXT,
                telefono INTEGER,
                contrasena TEXT,
                contrasena_segura INTEGER,
                provincia TEXT,
                permisos INTEGER
            )''')

c.execute('''CREATE TABLE emails (
                id_email INTEGER PRIMARY KEY,
                id_usuario INTEGER,
                total INTEGER,
                phishing INTEGER,
                cliclados INTEGER,
                FOREIGN KEY (id_usuario) REFERENCES usuarios (id_usuario)
            )''')

c.execute('''CREATE TABLE fechas (
                id_fecha INTEGER PRIMARY KEY,
                id_usuario INTEGER,
                fecha TEXT,
                FOREIGN KEY (id_usuario) REFERENCES usuarios (id_usuario)
            )''')

c.execute('''CREATE TABLE ips (
                id_ip INTEGER PRIMARY KEY,
                id_usuario INTEGER,
                ip TEXT,
                FOREIGN KEY (id_usuario) REFERENCES usuarios (id_usuario)
            )''')

c.execute('''CREATE TABLE legal (
                id_legal INTEGER PRIMARY KEY,
                web TEXT,
                cookies INTEGER,
                aviso INTEGER,
                proteccion_datos INTEGER,
                creacion INTEGER
            )''')
