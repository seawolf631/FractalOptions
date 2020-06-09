from flask import Flask, render_template, request
app = Flask(__name__)
import psycopg2
import matplotlib.pyplot as plt
import io
from config import config

def getData():
    params = config()
    conn = psycopg2.connect(**params)
    with conn:
        cur = conn.cursor()
        cur.execute("select * from stock_live_data;")
        row = cur.fetchone()
        stockBid = row[1]
        stockAsk = row[2]
        stockLast = row[3]
        stockVolume = row[4]
        stock_fifty_two_week_high = row[5]
        stock_fifty_two_week_low = row[6]

        cur.execute("select * from options_live_data;")
        optionList = []
        row = cur.fetchone()
        optionList.append(row)
        while row:
            row = cur.fetchone()
            optionList.append(row)
    cur.close()    
    conn.close()
    return stockBid, stockAsk, stockLast, stockVolume, stock_fifty_two_week_high, stock_fifty_two_week_low, optionList
        
@app.route("/")
def index():
    stockBid, stockAsk, stockLast, stockVolume, stock_fifty_two_week_high, stock_fifty_two_week_low,optionList = getData()
    templateData = {
        'stockBid':stockBid,
        'stockAsk':stockAsk,
        'stockLast':stockLast,
        'stockVolume':stockVolume,
        'stock_fifty_two_week_high':stock_fifty_two_week_high,
        'stock_fifty_two_week_low':stock_fifty_two_week_low,
        'optionList':optionList
        }
    return render_template('index.html',**templateData)

@app.route("/", methods=['POST'])
def get_stock_ticker():
    stockTicker = request.form['stockTicker']
    return stockTicker

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=False)
