instala a biblioteca de flask e conectot
banco de dados:

-- Criação do banco de dados
CREATE DATABASE bd_diabete;

-- Seleciona o banco de dados para uso
USE bd_consulta;

-- Criação da tabela consultas
CREATE TABLE consultas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    numero VARCHAR(20) NOT NULL,
    genero VARCHAR(10) NOT NULL,
    data_nascimento DATE NOT NULL,
    data_consulta DATE NOT NULL,
    especialidade VARCHAR(255) NOT NULL,
    observacoes TEXT
);
