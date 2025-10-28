# # importando o driver do sqlite
# import sqlite3
# from pathlib import Path

# # Diretório do arquivo atual
# #BASE_DIR = Path(__file__).resolve().parent
# #print(BASE_DIR)

# # Caminho completo do banco
# #DB_PATH = BASE_DIR / "db" / "escola_v2.db"
# #print(DB_PATH)

# # inicia a conexao com o banco de dados.
# db_connection = sqlite3.connect('db/escola_v2.db')

# # cria o cursor
# cursor = db_connection.cursor()

# # executa qualquer comando SQL suportado pelo sqlite
# cursor.execute("""
# SELECT * 
# FROM Aluno
# """)

# # Salva o resultado da query na variável
# query_result = cursor.fetchall()

# # Imprime o resultado da query
# print(query_result)

# # Encerra a conexao com o banco de dados
# db_connection.close()

# import sqlite3

# db_connection = sqlite3.connect("db/escola_v2.db")
# cursor = db_connection.cursor()
# cursor.execute("""
#         SELECT * 
#         FROM Aluno
#         """)
# rows = cursor.fetchmany(5)

# while rows:
#     for row in rows:
#         print(row)
#     rows = cursor.fetchmany(5)
# db_connection.close()

# import sqlite3

# with sqlite3.connect("db/escola_v2.db") as db_connection:
#     cursor = db_connection.cursor()
#     cursor.execute("""
#         SELECT * 
#         FROM Aluno
#         """)
#     for row in cursor:
#         print(row)

# db_connection.close()

import sqlite3
from pathlib import Path

db_connection = sqlite3.connect("db/loja.db")

cursor = db_connection()