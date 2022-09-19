from conexao import criar_conexao, fechar_conexao


def select_dados(ade):
    con = criar_conexao("localhost", "root", "xxxxxx", "dbextrator")
    cursor = con.cursor()

    cursor.execute(f"""SELECT tb.adesao
                       FROM tbl_extrator_teste tb
                       where adesao = {ade}""")

    myresult = cursor.fetchall()

    for x in myresult:
        if myresult:
            return x[0]
        else:
            return 0

    fechar_conexao(con)
