import httpx
from app.config import settings


def fetch_cat_fact():
    try:
        with httpx.Client(timeout=settings.REQUEST_TIMEOUT) as client:
            response = client.get(settings.CAT_API_URL)
            response.raise_for_status()

            data = response.json()
            fact = data.get("fact")

            if not fact:
                return {
                    "success": False,
                    "error": "Cat fact unavailable. API returned unexpected data."
                }

            return {"success": True, "fact": fact}

    except httpx.TimeoutException:
        return {"success": False, "error": "Request timed out. Please try again later."}

    except httpx.HTTPStatusError as e:
        return {
            "success": False,
            "error": f"Cat API returned an error: {e.response.status_code}"
        }

    except httpx.RequestError:
        return {"success": False, "error": "Sorry, Cat API is not live right now."}

    except Exception as e:
        return {"success": False, "error": f"Unexpected error: {str(e)}"}
