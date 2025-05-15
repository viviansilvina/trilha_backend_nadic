1. CRIAÇÃO DE TABELAS

CREATE TABLE usuarios (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(100),
  email VARCHAR(100),
  idade INT
);

CREATE TABLE pedidos (
  id SERIAL PRIMARY KEY,
  usuario_id INT REFERENCES usuarios(id),
  produto VARCHAR(100)
);

2. INSERINDO DADOS

INSERT INTO usuarios (nome, email, idade) VALUES
('Ana', 'ana@email.com', 25),
('João', 'joao@email.com', 30);

INSERT INTO pedidos (usuario_id, produto) VALUES
(1, 'Camiseta'),
(2, 'Livro');

3. ATUALIZANDO DADOS

UPDATE usuarios
SET idade = 26
WHERE nome = 'Ana';

4. DELETANDO DADOS

DELETE FROM pedidos
WHERE produto = 'Livro';

5. CONSULTAS SIMPLES

SELECT * FROM usuarios;

-- Pedidos com nome do usuário
SELECT usuarios.nome, pedidos.produto
FROM usuarios
JOIN pedidos ON usuarios.id = pedidos.usuario_id;

-- Usuário mesmo sem pedidos
SELECT usuarios.nome, pedidos.produto 
from usuarios 
left join pedidos on usuarios.id=pedidos.usuario_id;
