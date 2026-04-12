import psycopg2

def get_conn():
    return psycopg2.connect(
        host="postgres",
        database="gravit",
        user="gravit",
        password="gravit"
    )
