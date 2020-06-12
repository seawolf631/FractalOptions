import json
import psycopg2
import os
import re
from config import config
import sys
import liveDataAPICall

def liveParseData(stockTicker):
#Connect to Postgres 
    params = config()
    conn = psycopg2.connect(**params)

    with conn:
        cur = conn.cursor()
        print(stockTicker)
        liveDataAPICall.pullLiveData(stockTicker)
        stockTicker = "\'" + stockTicker + "\'"
        with open('../docs/exampleJSONData/live_option_data.json') as f:
            data = json.load(f)
            cur.execute("DROP TABLE IF EXISTS stock_live_data;")
            cur.execute("CREATE TABLE stock_live_data(stock_price_id serial PRIMARY KEY, bid real NOT NULL,ask real NOT NULL, last real NOT NULL,volume real NOT NULL, fiftyTwo_week_high real NOT NULL,fiftyTwo_week_low real NOT NULL, stock varchar(8) NOT NULL);")
    
            cur.execute("Insert INTO stock_live_data (bid,ask,last,volume,fiftyTwo_week_high,fiftyTwo_week_low,stock) VALUES (%s,%s,%s,%s,%s,%s,%s);" % (data["underlying"]["bid"],data["underlying"]["ask"],data["underlying"]["last"],data["underlying"]["totalVolume"],data["underlying"]["fiftyTwoWeekHigh"],data["underlying"]["fiftyTwoWeekLow"],stockTicker))




            cur.execute("DROP TABLE IF EXISTS options_live_data;")
            cur.execute("CREATE TABLE options_live_data(option_price_id serial PRIMARY KEY, description varchar(36) NOT NULL,bid real NOT NULL,ask real NOT NULL, last real NOT NULL,volume real NOT NULL, implied_volatility real NOT NULL);")
            for x in data["callExpDateMap"]:
                for y in data["callExpDateMap"][x]:
                    cur.execute("Insert INTO options_live_data (description,bid,ask,last,volume,implied_volatility) VALUES (\'%s\',%s,%s,%s,%s,%s);" % (data["callExpDateMap"][x][y][0]["description"].lower(),data["callExpDateMap"][x][y][0]["bid"],data["callExpDateMap"][x][y][0]["ask"],data["callExpDateMap"][x][y][0]["last"],data["callExpDateMap"][x][y][0]["totalVolume"],data["callExpDateMap"][x][y][0]["volatility"]))

#Close Postgres Connection
    cur.close()
    conn.close()
