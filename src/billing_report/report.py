
import psycopg2
from datetime import datetime, timedelta

DB_HOST = 'localhost'
DB_NAME = 'notificacoes'
DB_USER = 'user'
DB_PASS = 'password'

conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)
cursor = conn.cursor()

# Relatório de Cobrança
def gerar_relatorio_cobranca():
    ontem = datetime.now() - timedelta(days=1)
    cursor.execute("SELECT customer_name, COUNT(*) FROM notificacoes WHERE event_datetime >= %s GROUP BY customer_name", (ontem,))
    cobranca = cursor.fetchall()
    
    print("Relatório de Cobrança (Diário)")
    for cliente, notificacoes in cobranca:
        valor = notificacoes * 0.04  # Exemplo: R$ 0,04 por notificação
        print(f"Cliente: {cliente}, Notificações: {notificacoes}, Valor: R$ {valor:.2f}, Data: {ontem.strftime('%Y-%m-%d')}")
    print("\n")

# Relatório Detalhado de Notificações por Cliente
def gerar_relatorio_detalhado(cliente):
    cursor.execute("SELECT message_id, payload, event_datetime FROM notificacoes WHERE customer_name = %s", (cliente,))
    relatorio = cursor.fetchall()
    
    print(f"Relatório Detalhado de Notificações - Cliente: {cliente}")
    for message_id, payload, event_datetime in relatorio:
        print(f"Mensagem ID: {message_id}, Payload: {payload}, Data Hora: {event_datetime}")
    print("\n")

# Exemplo de execução dos relatórios
gerar_relatorio_cobranca()
gerar_relatorio_detalhado("Acme")

# Fechamento da conexão
conn.close()
