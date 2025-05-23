import psycopg2

DB_NAME = "postgres"
USER = "postgres"
PASSWORD = "1234"
HOST = "localhost"
PORT = "5432"

def conectar_db():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT
    )

def inserir_empresa(nome):
    with conectar_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO empresa (nome) VALUES (%s) RETURNING id;",
                (nome,)
            )
            empresa_id = cursor.fetchone()[0]
            conn.commit()
            return empresa_id

def inserir_cliente(nome, email, telefone, empresa_id):
    with conectar_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO cliente (nome, email, telefone, empresa_id) VALUES (%s, %s, %s, %s) RETURNING id;",
                (nome, email, telefone, empresa_id)
            )
            cliente_id = cursor.fetchone()[0]
            conn.commit()
            return cliente_id

def inserir_oportunidade(descricao, valor_estimado, status, cliente_id):
    with conectar_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO oportunidade (descricao, valor_estimado, status, cliente_id) VALUES (%s, %s, %s, %s) RETURNING id;",
                (descricao, valor_estimado, status, cliente_id)
            )
            oportunidade_id = cursor.fetchone()[0]
            conn.commit()
            return oportunidade_id

def inserir_venda(data_venda, valor_total, oportunidade_id):
    with conectar_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO venda (data_venda, valor_total, oportunidade_id) VALUES (%s, %s, %s) RETURNING id;",
                (data_venda, valor_total, oportunidade_id)
            )
            venda_id = cursor.fetchone()[0]
            conn.commit()
            return venda_id

def inserir_produto(nome, preco):
    with conectar_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO produto (nome, preco) VALUES (%s, %s) RETURNING id;",
                (nome, preco)
            )
            produto_id = cursor.fetchone()[0]
            conn.commit()
            return produto_id

def inserir_venda_produto(venda_id, produto_id, quantidade, preco_unitario):
    with conectar_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """INSERT INTO venda_produto (venda_id, produto_id, quantidade, preco_unitario)
                   VALUES (%s, %s, %s, %s)""",
                (venda_id, produto_id, quantidade, preco_unitario)
            )
            conn.commit()

def buscar_dados(tabela):
    with conectar_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {tabela};")
            return cursor.fetchall()

if __name__ == "__main__":
    empresa_id = inserir_empresa("Empresa X")

    cliente1_id = inserir_cliente("João Silva", "joao@email.com", "1111-2222", empresa_id)
    cliente2_id = inserir_cliente("Maria Souza", "maria@email.com", "3333-4444", empresa_id)

    oportunidade1_id = inserir_oportunidade("Oportunidade 1", 5000.00, "Aberta", cliente1_id)
    oportunidade2_id = inserir_oportunidade("Oportunidade 2", 15000.00, "Fechada", cliente2_id)

    venda1_id = inserir_venda("2025-05-20", 4800.00, oportunidade1_id)
    venda2_id = inserir_venda("2025-05-21", 15000.00, oportunidade2_id)

    produto1_id = inserir_produto("Produto A", 100.00)
    produto2_id = inserir_produto("Produto B", 200.00)

    inserir_venda_produto(venda1_id, produto1_id, 10, 100.00)
    inserir_venda_produto(venda2_id, produto2_id, 5, 200.00)

    print("Empresas:", buscar_dados("empresa"))
    print("Clientes:", buscar_dados("cliente"))
    print("Oportunidades:", buscar_dados("oportunidade"))
    print("Vendas:", buscar_dados("venda"))
    print("Produtos:", buscar_dados("produto"))
    print("Venda_Produto:", buscar_dados("venda_produto"))
