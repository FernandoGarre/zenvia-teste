
from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

DB_HOST = 'localhost'
DB_NAME = 'notificacoes'
DB_USER = 'user'
DB_PASS = 'password'

@app.route('/')
def painel():
    conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)
    cursor = conn.cursor()
    cursor.execute("SELECT customer_name, COUNT(*) FROM notificacoes GROUP BY customer_name")
    data = cursor.fetchall()
    conn.close()
    return render_template('painel.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
