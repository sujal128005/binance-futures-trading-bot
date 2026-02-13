import logging
from binance.enums import *

logger = logging.getLogger(__name__)

def place_futures_order(client, symbol, side, order_type, quantity, price=None):
    try:
        params = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": order_type.upper(),
            "quantity": quantity
        }

        if order_type.upper() == "LIMIT":
            params["price"] = str(price)
            params["timeInForce"] = TIME_IN_FORCE_GTC

        logger.info(f"Request: {params}")
        response = client.futures_create_order(**params)
        logger.info(f"Response: {response}")
        return response

    except Exception as e:
        logger.error(f"Order Placement Failed: {e}")
        raise e
