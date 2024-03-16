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

# Leer datos del archivo JSON
with open('users_data_online.json') as f:
    data = json.load(f)
    usuarios = data['usuarios']

with open('legal_data_online.json') as f:
    data = json.load(f)
    legal = data['legal']

# Insertar datos en la base de datos
for usuario in usuarios:
    nombre_usuario, datos = usuario.popitem()
    telefono = datos['telefono']
    contrasena = datos['contrasena']
    provincia = datos['provincia']
    permisos = datos['permisos']
    fechas = datos['fechas']
    ips = datos['ips']
    total_emails = datos['emails']['total']
    phishing_emails = datos['emails']['phishing']
    cliclados_emails = datos['emails']['cliclados']

    contrasena_segura = 1
    with open('rockyou-20.txt') as f:
        for line in f.readlines():
            line = line.strip()
            line = line.encode('utf-8')
            hash_pass = hashlib.md5(line)
            hash_pass = hash_pass.hexdigest()
            if contrasena == hash_pass:
                contrasena_segura = 0
                break
# Insertar usuario
    c.execute('''INSERT INTO usuarios (nombre_usuario, telefono, contrasena, contrasena_segura, provincia, permisos)
                 VALUES (?, ?, ?, ?, ?, ?)''', (nombre_usuario, telefono, contrasena, contrasena_segura, provincia, permisos))
    id_usuario = c.lastrowid

    # Insertar emails
    c.execute('''INSERT INTO emails (id_usuario, total, phishing, cliclados)
                 VALUES (?, ?, ?, ?)''', (id_usuario, total_emails, phishing_emails, cliclados_emails))

    # Insertar fechas
    for fecha in fechas:
        c.execute('''INSERT INTO fechas (id_usuario, fecha)
                     VALUES (?, ?)''', (id_usuario, fecha))

    # Insertar IPs
    for ip in ips:
        if ip != "N" and ip != "o" and ip != "n" and ip != "e":
            c.execute('''INSERT INTO ips (id_usuario, ip)
                         VALUES (?, ?)''', (id_usuario, ip))
