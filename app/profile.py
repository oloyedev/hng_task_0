from fastapi import APIRouter, HTTPException
from datetime import datetime, timezone
from typing import Union
from .schema import ProfileResponse, UserProfile, SuccessResponse, ErrorResponse
from .services import fetch_cat_fact
from .config import settings

router = APIRouter()

@router.get("/me", response_model=Union[SuccessResponse, ErrorResponse])
def get_user_profile():
    try:
        user_data = UserProfile(
            email=settings.USER_EMAIL,
            name=settings.USER_NAME,
            stack=settings.USER_STACK
        )

        fact_result = fetch_cat_fact()

        if fact_result["success"]:
            return {
                "status": "success",
                "user": user_data,
                "timestamp": datetime.now(timezone.utc),
                "fact": fact_result["fact"]
            }

        raise HTTPException(
            status_code=503,
            detail=fact_result["error"]
        )

    except HTTPException as http_err:
        # FastAPI's own error
        return {
            "status": "failed",
            "user": user_data,
            "timestamp": datetime.now(timezone.utc),
            "error": str(http_err.detail)
        }

    except Exception as e:
        return {
            "status": "failed",
            "user": user_data if 'user_data' in locals() else None,
            "timestamp": datetime.now(timezone.utc),
            "error": f"Internal server error: {str(e)}"
        }
