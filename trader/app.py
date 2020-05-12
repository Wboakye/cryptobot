from flask import Flask
from trader import Trader

development_mode = True

app = Flask(__name__)

#TODO create prod conditional
if development_mode:
    trader = Trader(50, 500)
    trader.start()

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()


"""
Strategy: the high price will be assigned to Price.high_price. If gains are under 3% abd price falls under % loss_tolerance or 
price is over 5% and falls under 75% of gains, sell, save sell price clear Price.high_price. Buy when price 

"""



