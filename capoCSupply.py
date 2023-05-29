from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def get_circulating_supply():
    total_supply = get_total_supply()
    burned_supply = get_burned_supply()
    circulating_supply = total_supply - burned_supply
    circulating_supply_in_bnb = circulating_supply / 1e18  # Convert to BNB
    return jsonify(circulating_supply=circulating_supply_in_bnb)

def get_total_supply():
    response = requests.get('https://api.bscscan.com/api?module=stats&action=tokensupply&contractaddress=0x922722e9ef614ec9a3e94b78496e92abfbb5a624&apikey=YEMEFWMH1EGKM3IG79DI7UB2FRBQ9KFAFD')
    data = response.json()
    total_supply = int(data['result'])
    return total_supply

def get_burned_supply():
    response = requests.get('https://api.bscscan.com/api?module=account&action=tokenbalance&contractaddress=0x922722e9ef614ec9a3e94b78496e92abfbb5a624&address=0x000000000000000000000000000000000000dead&tag=latest&apikey=YEMEFWMH1EGKM3IG79DI7UB2FRBQ9KFAFD')
    data = response.json()
    burned_supply = int(data['result'])
    return burned_supply

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
