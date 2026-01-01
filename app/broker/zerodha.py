from kiteconnect import KiteConnect
from app.core.config import settings

kite = KiteConnect(api_key=settings.KITE_API_KEY)

def get_login_url():
    return kite.login_url()

def generate_session(request_token: str):
    data = kite.generate_session(
        request_token,
        api_secret=settings.KITE_API_SECRET
    )
    kite.set_access_token(data["access_token"])
    return data

def set_access_token(token: str):
    kite.set_access_token(token)

def get_positions():
    return kite.positions()["net"]

def place_market_squareoff(tradingsymbol, exchange, quantity, transaction_type):
    return kite.place_order(
        variety=kite.VARIETY_REGULAR,
        exchange=exchange,
        tradingsymbol=tradingsymbol,
        transaction_type=transaction_type,
        quantity=quantity,
        product=kite.PRODUCT_NRML,
        order_type=kite.ORDER_TYPE_MARKET
    )
