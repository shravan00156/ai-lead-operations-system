from pydantic import BaseModel
from typing import Optional


# =====================================================
# LEAD MODEL
# =====================================================

class Lead(BaseModel):

    name: str
    email: str
    company: str
    source: Optional[str] = "unknown"


# =====================================================
# LEAD RESPONSE MODEL
# =====================================================

class LeadResponse(BaseModel):

    id: int
    name: str
    email: str
    company: str
    source: str
    score: int
    priority: str


# =====================================================
# AI SCORE RESPONSE MODEL
# =====================================================

class AIScoreResponse(BaseModel):

    score: int
    priority: str