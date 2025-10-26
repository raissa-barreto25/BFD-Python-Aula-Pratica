-- Questão 01

-- SELECT *
-- FROM Aluno

-- Questão 02

-- SELECT nome, nota1
-- FROM Aluno

-- Questão 03

-- SELECT nome, nota2
-- FROM Aluno
-- WHERE nota2 > 8

-- Questão 04

-- SELECT nome, data_nascimento
-- FROM Aluno
-- WHERE data_nascimento > '2000-01-01';

-- Questão 05

-- SELECT nome, mensalidade
-- FROM Curso
-- WHERE mensalidade >= 600;

-- Questão 06

-- SELECT nome, ano
-- FROM Turma
-- ORDER BY ano ASC;

-- Questão 07

-- SELECT ano, COUNT (*) AS quantidade_turmas
-- FROM Turma
-- GROUP BY ano;

-- Questão 08

-- SELECT id_turma, AVG (nota1) AS Media
-- FROM Aluno
-- GROUP BY id_turma;

-- Questão 09

-- SELECT ano, COUNT (*) as quantidade_turmas
-- FROM Turma
-- GROUP BY ano
-- HAVING COUNT (*) > 2;

-- Questão 10

-- SELECT nome, mensalidade
-- FROM Curso
-- ORDER BY mensalidade DESC;
