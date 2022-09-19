from conexao import criar_conexao, fechar_conexao


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

    con.commit()
    fechar_conexao(con)
