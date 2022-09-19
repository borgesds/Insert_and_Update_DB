from conexao import criar_conexao, fechar_conexao


def update_db(status_operacao, valor_pago, adesao):

    con = criar_conexao("localhost", "root", "lostawer", "dbextrator")
    cursor = con.cursor()

    sql = """UPDATE tbl_extrator_teste SET status_operacao = %s,
             valor_pagos = %s
             WHERE adesao = %s"""

    valores = (status_operacao, valor_pago, adesao)

    cursor.execute(sql, valores)
    con.commit()

    print()

    fechar_conexao(con)
