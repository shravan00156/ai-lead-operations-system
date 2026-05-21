from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

from database.connection import get_connection
from services.ai_service import score_lead
from services.telegram_service import send_telegram_message

router = APIRouter()


# =====================================================
# LEAD MODEL
# =====================================================

class Lead(BaseModel):

    name: str
    email: str
    company: str
    source: Optional[str] = "unknown"


# =====================================================
# CREATE LEAD
# =====================================================

@router.post("/leads")
async def create_lead(lead: Lead):

    connection = get_connection()

    try:

        cursor = connection.cursor()

        # ==========================================
        # AI LEAD SCORING
        # ==========================================

        ai_result = score_lead({
            "name": lead.name,
            "company": lead.company,
            "source": lead.source
        })

        score = ai_result["score"]
        priority = ai_result["priority"]

        # ==========================================
        # INSERT LEAD
        # ==========================================

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
                lead.name,
                lead.email,
                lead.company,
                lead.source,
                score,
                priority
            )
        )

        result = cursor.fetchone()

        if result is None:

            raise HTTPException(
                status_code=500,
                detail="Failed to create lead"
            )

        lead_id = result[0]

        connection.commit()

        # ==========================================
        # TELEGRAM ALERT
        # ==========================================

        message = f"""
🚀 New Lead Added

Name: {lead.name}
Email: {lead.email}
Company: {lead.company}

Priority: {priority}
Score: {score}
"""

        send_telegram_message(message)

        return {
            "success": True,
            "lead_id": lead_id,
            "score": score,
            "priority": priority
        }

    except Exception as e:

        connection.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    finally:

        cursor.close()
        connection.close()


# =====================================================
# GET ALL LEADS
# =====================================================

@router.get("/leads")
async def get_leads():

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

        leads = []

        for row in rows:

            leads.append({
                "id": row[0],
                "name": row[1],
                "email": row[2],
                "company": row[3],
                "source": row[4],
                "score": row[5],
                "priority": row[6]
            })

        return {
            "count": len(leads),
            "leads": leads
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    finally:

        cursor.close()
        connection.close()


# =====================================================
# GET SINGLE LEAD
# =====================================================

@router.get("/leads/{lead_id}")
async def get_single_lead(lead_id: int):

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

        if row is None:

            raise HTTPException(
                status_code=404,
                detail="Lead not found"
            )

        return {
            "id": row[0],
            "name": row[1],
            "email": row[2],
            "company": row[3],
            "source": row[4],
            "score": row[5],
            "priority": row[6]
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    finally:

        cursor.close()
        connection.close()


# =====================================================
# DELETE LEAD
# =====================================================

@router.delete("/leads/{lead_id}")
async def delete_lead(lead_id: int):

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

            raise HTTPException(
                status_code=404,
                detail="Lead not found"
            )

        connection.commit()

        return {
            "success": True,
            "deleted_lead_id": lead_id
        }

    except Exception as e:

        connection.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    finally:

        cursor.close()
        connection.close()