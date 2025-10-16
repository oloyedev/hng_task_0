import httpx
from app.config import settings


def fetch_cat_fact():
    try:
        with httpx.Client(timeout=settings.REQUEST_TIMEOUT) as client:
            response = client.get(settings.CAT_API_URL)
            response.raise_for_status()
            data = response.json()
            return {"success": True, "fact": data.get("fact")}
    except httpx.RequestError:
        return {"success": False, "error": "Sorry, Cat API is not live right now."}
    except Exception:
        return {"success": False, "error": "An unexpected error occurred while fetching cat fact."}
