import psycopg2


def get_connection():

    connection = psycopg2.connect(
        host="localhost",
        database="ai_lead_ops",
        user="postgres",
        password="postgres123"
    )

    return connection