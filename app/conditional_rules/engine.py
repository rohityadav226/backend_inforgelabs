import time
from app.broker.zerodha import get_positions, place_market_squareoff

active_rules = []

def run_engine():
    while True:
        positions = get_positions()
        pnl_map = {p["tradingsymbol"]: p["pnl"] for p in positions}

        for rule in active_rules:
            combined_pnl = sum(pnl_map.get(sym, 0) for sym in rule["symbols"])

            if combined_pnl <= rule["trigger"]:
                for sym in rule["symbols"]:
                    # square off
                    pass

                rule["active"] = False

        time.sleep(1)
