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

def atualizar_valor_venda(venda_id, novo_valor):
    with conectar_db() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE venda SET valor_total = %s WHERE id = %s;",
                (novo_valor, venda_id)
            )
            conn.commit()
    print(f"Venda {venda_id} atualizada para valor {novo_valor}")

def deletar_venda(venda_id):
    with conectar_db() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM venda WHERE id = %s;", (venda_id,))
            conn.commit()
    print(f"Venda {venda_id} deletada")

def listar_vendas_com_clientes():
    with conectar_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT c.nome, v.data_venda, v.valor_total
                FROM venda v
                JOIN cliente c ON v.oportunidade_id = (SELECT id FROM oportunidade WHERE cliente_id = c.id LIMIT 1);
            """)
            resultados = cur.fetchall()
            return resultados

def resumo_vendas_por_cliente():
    with conectar_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT c.nome, COUNT(v.id) AS total_vendas, SUM(v.valor_total) AS soma_valor
                FROM venda v
                JOIN oportunidade o ON v.oportunidade_id = o.id
                JOIN cliente c ON o.cliente_id = c.id
                GROUP BY c.nome
                HAVING SUM(v.valor_total) > 1000;
            """)
            resultados = cur.fetchall()
            return resultados

if __name__ == "__main__":

    atualizar_valor_venda(1, 5500.00)
    deletar_venda(5)
    
    vendas = listar_vendas_com_clientes()
    print("Vendas com clientes:")
    for venda in vendas:
        print(venda)

    resumo = resumo_vendas_por_cliente()
    print("\nResumo de vendas por cliente (acima de 1000):")
    for linha in resumo:
        print(linha)
