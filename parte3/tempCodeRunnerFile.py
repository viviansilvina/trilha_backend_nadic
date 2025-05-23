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

def inserir_dados():
    comandos = [
        "INSERT INTO empresa (nome) VALUES ('Empresa X') ON CONFLICT DO NOTHING;",
        "INSERT INTO cliente (nome, email, telefone, empresa_id) VALUES ('João Silva', 'joao@email.com', '1111-2222', 1);",
        "INSERT INTO cliente (nome, email, telefone, empresa_id) VALUES ('Maria Souza', 'maria@email.com', '3333-4444', 1);",
    ]
    with conecta_db() as conn:
        with conn.cursor() as cur:
            for comando in comandos:
                cur.execute(comando)
        conn.commit()
    print("Dados inseridos")


def atualizar_dados():
    comando = "UPDATE venda SET status = 'Enviado' WHERE id = 2;"
    with conecta_db() as conn:
        with conn.cursor() as cur:
            cur.execute(comando)
        conn.commit()
    print("Dados atualizados")

def deletar_dados():
    comando = "DELETE FROM venda WHERE id = 1;"
    with conecta_db() as conn:
        with conn.cursor() as cur:
            cur.execute(comando)
        conn.commit()
    print("Dados deletados")

def consultas():
    with conecta_db() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM cliente;")
            cliente = cur.fetchall()
            print("Cliente:", cliente)

            cur.execute("""
                SELECT c.nome, p.data_pedido, p.valor_total, p.status
                FROM cliente c
                JOIN venda p ON c.id = p.cliente_id;
            """)
            venda = cur.fetchall()
            print("venda com cliente:", venda)

            cur.execute("""
                SELECT cliente_id, COUNT(*) AS total_venda, SUM(valor_total) AS soma_valor
                FROM venda
                GROUP BY cliente_id
                HAVING SUM(valor_total) > 100;
            """)
            agrupamento = cur.fetchall()
            print("Agrupamento de venda:", agrupamento)

def main_insert():
    
    consultas()

if __name__ == "__main__":
    main_insert()
