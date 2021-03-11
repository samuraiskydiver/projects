from flask import Flask, render_template, request
import alpaca_trade_api as tradeapi
import config, json, requests

app = Flask(__name__)

api = tradeapi.REST(config.API_KEY, config.API_SECRET, base_url='https://paper-api.alpaca.markets')

@app.route('/')
def dashboard():
    orders = api.list_orders()
    
    return render_template('dashboard.html', alpaca_orders=orders)

@app.route('/webhook', methods=['POST'])
def webhook():
    webhook_message = json.loads(request.data)

    if webhook_message['passphrase'] != config.WEBHOOK_PASSPHRASE:
        return {
            'code': 'error',
            'message': 'nice try buddy'
        }
    
    price = webhook_message['strategy']['order_price']
    quantity = webhook_message['strategy']['order_contracts']
    symbol = webhook_message['ticker']
    side = webhook_message['strategy']['order_action']
    
    order = api.submit_order(symbol, quantity, side, 'limit', 'gtc', limit_price=price)

    # if a DISCORD URL is set in the config file, we will post to the discord webhook
    if config.DISCORD_WEBHOOK_URL:
        chat_message = {
            "username": "strategyalert",
            "avatar_url": "https://i.imgur.com/4M34hi2.png",
            "content": f"tradingview strategy alert triggered: {quantity} {symbol} @ {price}"
        }

        requests.post(config.DISCORD_URL, json=chat_message)

    return webhook_message