-- w3schools.com 
-- SELECT para pegar as colunas de uma lista 
-- Comando para listar as tabelas do BD .tables
-- Mostra o esquema de criação da tabela .schema 
-- Retorna todas as colunas da tabela Aluno 
-- SELECT *
-- FROM Aluno;

-- SELECT id_turma, COUNT() as n_alunos
-- FROM Aluno
-- GROUP BY id_turma
-- HAVING n_alunos > 20;

-- SELECT id_turma, COUNT() as n_alunos
-- FROM Aluno
-- WHERE (nota1+nota2) /2 >7
-- GROUP BY id_turma
-- HAVING n_alunos > 5;
-- max pega a maior nota 
-- SELECT nome, MAX((nota1+nota2)/2) AS media
-- FROM Aluno;

-- min pega a menor nota
-- SELECT nome, MIN((nota1+nota2)/2) AS media
-- FROM Aluno;
-- SUM soma total
-- AVG Media dos alunos 

-- SELECT nome
-- FROM Aluno
-- WHERE nome = 'Felipe Melo'

-- SELECT nome
-- FROM Aluno
-- WHERE nome IN ('Felipe Melo', 'João Pereira')

SELECT nome
FROM Aluno
WHERE nome LIKE '%lipe%'

-- Underline _ quantidade de caracter 