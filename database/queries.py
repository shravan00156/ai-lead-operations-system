from database.connection import get_connection


# =====================================================
# CREATE LEAD
# =====================================================

def insert_lead(
    name,
    email,
    company,
    source,
    score,
    priority
):

    connection = get_connection()

    try:

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO leads
            (
                name,
                email,
                company,
                source,
                score,
                priority
            )
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING id
            """,
            (
                name,
                email,
                company,
                source,
                score,
                priority
            )
        )

        result = cursor.fetchone()

        if result is None:
            return None

        connection.commit()

        return result[0]

    finally:

        cursor.close()
        connection.close()


# =====================================================
# GET ALL LEADS
# =====================================================

def fetch_all_leads():

    connection = get_connection()

    try:

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                id,
                name,
                email,
                company,
                source,
                score,
                priority
            FROM leads
            ORDER BY id DESC
            """
        )

        rows = cursor.fetchall()

        return rows

    finally:

        cursor.close()
        connection.close()


# =====================================================
# GET SINGLE LEAD
# =====================================================

def fetch_single_lead(lead_id):

    connection = get_connection()

    try:

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                id,
                name,
                email,
                company,
                source,
                score,
                priority
            FROM leads
            WHERE id = %s
            """,
            (lead_id,)
        )

        row = cursor.fetchone()

        return row

    finally:

        cursor.close()
        connection.close()


# =====================================================
# DELETE LEAD
# =====================================================

def delete_lead_by_id(lead_id):

    connection = get_connection()

    try:

        cursor = connection.cursor()

        cursor.execute(
            """
            DELETE FROM leads
            WHERE id = %s
            RETURNING id
            """,
            (lead_id,)
        )

        deleted = cursor.fetchone()

        if deleted is None:
            return None

        connection.commit()

        return deleted[0]

    finally:

        cursor.close()
        connection.close()