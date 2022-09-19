import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="xxxxxx",
    database="dbextrator"
)

mycursor = mydb.cursor()

mycursor.execute("""CREATE TABLE if NOT EXISTS tbl_extrator_teste (
    id INT AUTO_INCREMENT PRIMARY KEY,
    loja VARCHAR(10),
    nome_cliente VARCHAR(100),
    cpf VARCHAR(20),
    adesao VARCHAR(15),
    status_operacao VARCHAR(50),
    valor_pagos VARCHAR(20)
);""")

print('TABELA Database Criada!!!')