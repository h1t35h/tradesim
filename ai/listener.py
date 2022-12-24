import logging
from kiteconnect import KiteTicker

logging.basicConfig(level=logging.DEBUG)

TRADE_LIST = []

kws = KiteTicker("","")


def on_ticks(ws, ticks):
    logging.debug((f"Ticks: {ticks}"))

def on_connect(ws, response):
    ws.subscribe(TRADE_LIST)
    ws.set_mode(ws.MODE_FULL, TRADE_LIST)

def on_close(ws, code, reason):
    ws.stop()

