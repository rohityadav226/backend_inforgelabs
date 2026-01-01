from fastapi import APIRouter
from app.broker.zerodha import place_market_squareoff

router = APIRouter(prefix="/squareoff")

@router.post("")
def squareoff(payload: dict):
    for inst in payload["instruments"]:
        place_market_squareoff(
            tradingsymbol=inst["symbol"],
            exchange=inst["exchange"],
            quantity=abs(inst["qty"]),
            transaction_type="SELL" if inst["qty"] > 0 else "BUY"
        )
    return {"status": "ok"}
