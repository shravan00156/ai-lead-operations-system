from database.connection import get_connection


def init_database():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS leads (
            id SERIAL PRIMARY KEY,
            name TEXT,
            email TEXT,
            company TEXT,
            source TEXT,
            score INTEGER,
            priority TEXT
        )
        """
    )

    connection.commit()

    cursor.close()
    connection.close()

    print("Leads table ready")