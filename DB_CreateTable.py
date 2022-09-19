import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="xxxxxx",
    database="dbextrator"
)

mycursor = mydb.cursor()

mycursor.execute("""CREATE TABLE if NOT EXISTS tbl_extrator (
    id INT AUTO_INCREMENT PRIMARY KEY,
    loja VARCHAR(10),
    nome_cliente VARCHAR(100),
    cpf VARCHAR(20),
    nome_servico VARCHAR(50),
    tipo_servico VARCHAR(50),
    adesao VARCHAR(15),
    status_operacao VARCHAR(50),
    data_consig VARCHAR(15),
    usuario_operacao VARCHAR(50),
    valor_saque VARCHAR(20),
    valor_saque_autorizado VARCHAR(20),
    valor_saque_averbado VARCHAR(20),
    valor_solicitado_bruto VARCHAR(20),
    valor_portabilidade VARCHAR(20),
    saldo_devedor VARCHAR(20),
    valor_liberado VARCHAR(20),
    valor_premio VARCHAR(20),
    valor_pagos VARCHAR(20)
);""")

