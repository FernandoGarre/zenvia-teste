
from kafka import KafkaConsumer
import json
import psycopg2

KAFKA_TOPIC = 'notificacoes'
KAFKA_SERVER = 'localhost:9092'
DB_HOST = 'localhost'
DB_NAME = 'notificacoes'
DB_USER = 'user'
DB_PASS = 'password'

conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)
cursor = conn.cursor()

consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_SERVER,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    notificacao = message.value
    cursor.execute(
        "INSERT INTO notificacoes (customer_id, message_id, customer_name, payload, event_datetime) VALUES (%s, %s, %s, %s, %s)",
        (notificacao['customer_id'], notificacao['message_id'], notificacao['customer_name'], notificacao['payload'], notificacao['event_datetime'])
    )
    conn.commit()
