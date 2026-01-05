import mysql.connector

def inserir_usuario(usuario, senha):
    conexao = None
    cursor = None
    try:
        conexao = mysql.connector.connect(
            host='',
            user='',
            password='',
            database=''
        )
        cursor = conexao.cursor()
        sql = "INSERT INTO usuarios (usuario, pwrd) VALUES (%s, %s)"
        cursor.execute(sql, (usuario, senha))
        conexao.commit()
        print('Dados inseridos com sucesso no MySQL')

    except mysql.connector.Error as erro:
        print("Erro ao inserir no MySQL:", erro)

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()


def buscar_usuario(usuario):
    conexao = None
    cursor = None
    try:
        conexao = mysql.connector.connect(
            host='',
            user='',
            password='',
            database=''
        )
        cursor = conexao.cursor(dictionary=True)
        sql = "SELECT * FROM usuarios WHERE usuario = %s"
        cursor.execute(sql, (usuario,))
        resultado = cursor.fetchone()  # retorna None se não existir
        return resultado

    except mysql.connector.Error as e:
        print("Erro MySQL:", e)
        return None

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()
