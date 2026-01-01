from fastapi import APIRouter

router = APIRouter(prefix="/pnl", tags=["pnl"])


@router.get("/summary")
def pnl_summary():
    """
    TEMP: Dummy P&L summary
    """
    return {
        "livePnl": 50.0,
        "dayMtm": 50.0,
        "marginUsedPercent": 18.4,
        "openPositionsCount": 2
    }