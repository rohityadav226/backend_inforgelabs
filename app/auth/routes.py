from fastapi import APIRouter
from app.broker.zerodha import get_login_url

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
def login():
    """
    Step 1 of Zerodha auth:
    Return the Zerodha login URL to frontend
    """
    return {
        "login_url": get_login_url()
    }

