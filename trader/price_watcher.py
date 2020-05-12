import websocket
import time
import json
try:
    import thread
except ImportError:
    import _thread as thread


class PriceWatcher:
    def __init__(self, trader):
        self.trader = trader
        self._current_price = None

    def start(self):
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp("wss://ws.coincap.io/prices?assets=bitcoin",
                                    on_message=self.on_message,
                                    on_error=self.on_error,
                                    on_close=self.on_close)
        ws.on_open = self.on_open
        ws.run_forever()

    def on_message(self, message):
        message = json.loads(message)
        message = float(message['bitcoin'])
        self._current_price = message
        self.update_trader()

    def on_error(self, error):
        print(error)

    def on_close(self):
        print("### closed ###")

    def on_open(self, ws):
        def run(*args):
            for i in range(3):
                time.sleep(1)
                ws.send("Hello %d" % i)
            time.sleep(1)
            ws.close()
            print("thread terminating...")

        thread.start_new_thread(run, ())

    def update_trader(self):
        self.trader.assess_prices(self._current_price)

    def get_current_price(self):
        return self._current_price


