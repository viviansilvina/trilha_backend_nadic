import psycopg2

DB_NAME = "postgres"
USER = "postgres"
PASSWORD = "1234"
HOST = "localhost"
PORT = "5432"

def conecta_db():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT
    )

def criar_tabelas(sql):
    with conecta_db() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)

def main_create():
    comandos = [
        """
        CREATE TABLE IF NOT EXISTS empresa (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS cliente (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            email VARCHAR(100),
            telefone VARCHAR(20),
            empresa_id INTEGER NOT NULL,
            FOREIGN KEY (empresa_id) REFERENCES empresa(id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS contato (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            email VARCHAR(100),
            cargo VARCHAR(100),
            cliente_id INTEGER NOT NULL,
            FOREIGN KEY (cliente_id) REFERENCES cliente(id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS oportunidade (
            id SERIAL PRIMARY KEY,
            descricao TEXT,
            valor_estimado NUMERIC(10,2),
            status VARCHAR(50),
            cliente_id INTEGER NOT NULL,
            FOREIGN KEY (cliente_id) REFERENCES cliente(id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS venda (
            id SERIAL PRIMARY KEY,
            data_venda DATE,
            valor_total NUMERIC(10,2),
            oportunidade_id INTEGER NOT NULL,
            FOREIGN KEY (oportunidade_id) REFERENCES oportunidade(id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS produto (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            preco NUMERIC(10,2)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS venda_produto (
            venda_id INTEGER NOT NULL,
            produto_id INTEGER NOT NULL,
            quantidade INTEGER,
            preco_unitario NUMERIC(10,2),
            PRIMARY KEY (venda_id, produto_id),
            FOREIGN KEY (venda_id) REFERENCES venda(id),
            FOREIGN KEY (produto_id) REFERENCES produto(id)
        );
        """
    ]

    for comando in comandos:
        criar_tabelas(comando)

    print("Tabelas criadas com sucesso.")

if __name__ == "__main__":
    main_create()
