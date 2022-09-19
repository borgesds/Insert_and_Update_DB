import mysql.connector


def criar_conexao(host, usuario, password, banco):
    return mysql.connector.connect(
        host=host,
        user=usuario,
        password=password,
        database=banco
    )


def fechar_conexao(con):
    return con.close()

