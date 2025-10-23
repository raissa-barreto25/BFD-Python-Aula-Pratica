# import sqlite3

# conection = sqlite3.Connection("aulas/escola_v2.db")

# cursor = conection.cursor()

# cursor.execute("""
#                SELECT *
#                FROM Aluno         
# """)

# #print(cursor.fetchall())

import sqlite3

con = sqlite3.Connection("aulas/escola_v2.db")

cursor = con.cursor()

query = cursor.execute("SELECT * FROM Aluno")

nome_alunos = cursor.execute("""
                             SELECT nome
                             FROM Aluno
                             WHERE nome = "Fred"
                             """)

for registro in query:
    print(registro)

con.close() #Fechar Banco de Dados
