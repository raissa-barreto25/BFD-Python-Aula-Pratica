"""Banco de Dados
    Dado: Valor Bruto (nome, idade, endereço, foto...),
    informação: Dado organizado em um contexto,
    Conhecimento: Compreensão e aplicação das informações .
    
    Banco de dados: Colação organizada de informações,
    Tabelas: Estrutura que organiza os dados,
    Registros: Entradas de dados,
    Campos: Representa os atributos do registro
    
    Entidade: São objetos do mundo real que queremos armazenar.Viram tabelas no banco.
        forte: existe por si só
        fraca: depende de outra para existir
    Atributo: São caracteristicas das entidades. 
        simples: (nome, idade)
        composto: (endereço = rua + numero + cidade)
        Derivado: (Idade, que pode ser derivafa da data de nascimento)
    Obs. todo banco de dados tem que ter um ID.
    
    Representam etapas de abstração no projeto de um banco de dados
    
    Conceitual
        Representa a visão de alto nivel, sem se preocupar com tecnologia.
        Geralmente feito em DER(Diagrama entidade-relacionamento)
        
    Lógica
        traduz o modelo conceitual para algo mais próximo do banco de dados
        
    Fisico
        é a implementação no SGBD(Sistema Gerenciador de banco de dados) (MySQL, ProtgreSQL, Orecle etc)
        inclui comandos SQL
        
    Cardinalidades: Definem quantos elementos de uma entidade podem ser relacionar com outra
        1:1 (um para um) - cada pessoa tem um CPF
        1:N (um para muitos) - um professor ministra várias turmas,
        N:N (muitos para muitos) - um aluno pode cursar várias disciplinas e cada disciplinas pode ter vários alunos.
        
    """