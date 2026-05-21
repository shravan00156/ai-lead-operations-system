def score_lead(lead_data):

    source = (lead_data.get("source") or "").lower()

    score = 50
    priority = "medium"

    if "linkedin" in source:
        score = 90
        priority = "high"

    elif "website" in source:
        score = 75
        priority = "medium"

    return {
        "score": score,
        "priority": priority
    }