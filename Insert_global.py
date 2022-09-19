# pip install mysql-connector-python
# buscar do arquivo conexao o criar_conexao e fechar_conexao
from conexao import criar_conexao, fechar_conexao
import pandas as pd


def insert_banco(loja, nome_cliente, cpf, adesao,
                 status_operacao, valor_pagos):

    con = criar_conexao("localhost", "root", "lostawer", "dbextrator")
    cursor = con.cursor()

    sql = """INSERT INTO tbl_extrator_teste (
             loja, nome_cliente, cpf, adesao,
             status_operacao, valor_pagos) VALUES (
             %s, %s, %s, %s, %s, %s)"""

    valores = (loja, nome_cliente, cpf, adesao,
               status_operacao, valor_pagos)

    cursor.execute(sql, valores)

    cursor.close()
    con.commit()
    fechar_conexao(con)


# INITIALIZE
# Ler arquivo
df = pd.read_csv('base/BD_Extrator_input.csv', sep=";", low_memory=False)
df = df.fillna(0)


# dados para inserção
for i, l in df.iterrows():
    insert_banco(l[0], l[1], l[2], l[3], l[4], l[5])

    print(f'Subindo para o banco de dados index = {i}')

print('FINALIZADO O ENVIO DO EXTRATOR!!')
