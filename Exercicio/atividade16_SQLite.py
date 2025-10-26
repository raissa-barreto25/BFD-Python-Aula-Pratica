# Questão 01 e 02

import sqlite3

coneccao = sqlite3.Connection("Exercicio/escola_v2.db")
cursor = coneccao.cursor()
# cursor.execute("""
#                SELECT *
#                FROM Aluno
#                """)
# print(cursor.fetchall())

# Questão 03

# cursor.execute("""
#                SELECT 
#                     nome, 
#                     nota1, 
#                     nota2, 
#                     (nota1 + nota2) / 2 AS Media
#                FROM Aluno
#                ORDER BY Media DESC
#                LIMIT 10
#                """)
# print(cursor.fetchall())

# Questão 04

# query = cursor.execute("SELECT * FROM Aluno")

# cursor.execute("""
#                SELECT *
#                FROM Aluno
#                LEFT JOIN Turma
#                ON id_turma = Turma.id
#                """)
# print(cursor.fetchall())

# Questão 05

query = cursor.execute("SELECT * FROM Aluno")

cursor.execute("""
               SELECT *
               FROM Aluno
               LEFT JOIN Turma
               ON nome = Turma.nome
               WHERE nome = "Turma B"
               """)
print(cursor.fetchall())