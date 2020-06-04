from flask import Flask, render_template, request
app = Flask(__name__)
import psycopg2
import matplotlib.pyplot as plt
import io


def getData():
    conn = psycopg2.connect(host="localhost", port = 5432, database = , user="postgres", password=)
    with conn:
        cur = conn.cursor()
        cur.execute("select (open-low)/open as percent_difference from historical_data order by percent_difference DESC limit 10;")
        queryResult = cur.fetchall()
        cur.execute("select count(*) from historical_data")
        rowLength = cur.fetchall()
    cur.close()    
    conn.close()
    return queryResult, rowLength
        
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def get_stock_ticker():
    stockTicker = request.form['stockTicker']
    return stockTicker

if __name__ == "__main__":
    app.run(host='0.0.0.0',port = 80, debug=True)
