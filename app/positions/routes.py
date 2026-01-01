from fastapi import APIRouter
from app.broker.zerodha import get_positions

router = APIRouter(prefix="/positions")

@router.get("")
def positions():
    raw = get_positions()

    positions = []
    total_pnl = 0

    for p in raw:
        pnl = p["pnl"]
        total_pnl += pnl

        positions.append({
            "instrument": p["tradingsymbol"],
            "qty": p["quantity"],
            "avg_price": p["average_price"],
            "ltp": p["last_price"],
            "pnl": pnl
        })

    return positions
# {
#         "positions": positions,
#         "total_pnl": total_pnl
#     }

# from fastapi import APIRouter

# router = APIRouter(prefix="/positions", tags=["positions"])

# @router.get("")
# def get_positions():
#     """
#     TEMP: Dummy positions for frontend stabilization
#     Replace with Zerodha positions later
#     """

#     positions = [
#         {
#             "id": "NIFTY24JAN18000CE",
#             "symbol": "NIFTY24JAN18000CE",
#             "qty": 50,
#             "avgPrice": 120.0,
#             "ltp": 105.0,
#             "pnl": -750.0,
#             "pnlPercent": -12.5,
#             "instrumentType": "CE"
#         },
#         {
#             "id": "NIFTY24JAN17500PE",
#             "symbol": "NIFTY24JAN17500PE",
#             "qty": -50,
#             "avgPrice": 98.0,
#             "ltp": 82.0,
#             "pnl": 800.0,
#             "pnlPercent": 16.3,
#             "instrumentType": "PE"
#         }
    # ]

    # return positions
