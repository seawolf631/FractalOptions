import json
import psycopg2
import os
import re
from config import config
import sys
from math import log10

def resetDatabaseTables():
    params = config()
    conn = psycopg2.connect(**params)

    with conn:
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS stock_live_data;")
        cur.execute("DROP TABLE IF EXISTS options_live_data;")
    cur.close()
    conn.close()
    
def insertAlpha(stockTicker):
    params = config()
    conn = psycopg2.connect(**params)
    stockTicker = "\'" + stockTicker + "\'"
    
    with conn:
        cur = conn.cursor()
        alphaDict = {}
        stockQuery = cur.execute("select last from stock_live_data where stock=%s;" % (stockTicker))
        stockLast = float(cur.fetchone()[0])
        cur.execute("select * from options_live_data where delta <= 0.2 and stock=%s;" % (stockTicker))
        row = cur.fetchone()
        anchorStrike = row[2]
        anchorPrice = row[5]
        while row:
            daysToExp = row[9]
            row = cur.fetchone()
            if(row is not None):
                if(daysToExp != row[9]):
                    anchorStrike = row[2]
                    anchorPrice = row[5]
                else:
                    if(row[5] > 0.0 and anchorPrice > 0.0 and (row[5] - anchorPrice != 0)):
                        #print("last="+ str(row[5]) + "  anchorPrice=" + str(anchorPrice) + "  stockLast="+str(stockLast))
                        alpha = 1 - (log10(row[5]/anchorPrice)/log10((row[2]-stockLast)/(anchorStrike-stockLast)))
                        alphaDict[row[1]] = alpha
        for x in alphaDict:
            cur.execute("Update options_live_data SET alpha=%s where description=%s;" % (alphaDict[x],"\'"+x +"\'"))
    cur.close()
    conn.close()
    
def liveParseData(stockTicker):
#Connect to Postgres 
    params = config()
    conn = psycopg2.connect(**params)

    with conn:
        cur = conn.cursor()
        with open('../docs/exampleJSONData/'+stockTicker+'_live_data.json') as f:
            data = json.load(f)
            stockTicker = "\'" + stockTicker + "\'"
            cur.execute("CREATE TABLE IF NOT EXISTS stock_live_data(stock_price_id serial PRIMARY KEY, bid real NOT NULL,ask real NOT NULL, last real NOT NULL,volume real NOT NULL, fiftyTwo_week_high real NOT NULL,fiftyTwo_week_low real NOT NULL, stock varchar(8) NOT NULL);")
            
            cur.execute("Insert INTO stock_live_data (bid,ask,last,volume,fiftyTwo_week_high,fiftyTwo_week_low,stock) VALUES (%s,%s,%s,%s,%s,%s,%s);" % (data["underlying"]["bid"],data["underlying"]["ask"],data["underlying"]["last"],data["underlying"]["totalVolume"],data["underlying"]["fiftyTwoWeekHigh"],data["underlying"]["fiftyTwoWeekLow"],stockTicker))

            cur.execute("CREATE TABLE IF NOT EXISTS options_live_data(option_price_id serial PRIMARY KEY, description varchar(36) NOT NULL,strike real NOT NULL, bid real NOT NULL,ask real NOT NULL, last real NOT NULL,volume real NOT NULL, implied_volatility real NOT NULL, delta real NOT NULL, days_to_expiration real NOT NULL,stock varchar(8) NOT NULL, alpha real);")
            
            for x in data["callExpDateMap"]:
                for y in data["callExpDateMap"][x]:
                    cur.execute("Insert INTO options_live_data (description,strike,bid,ask,last,volume,implied_volatility,delta,days_to_expiration,stock) VALUES (\'%s\',%s,%s,%s,%s,%s,%s,%s,%s,%s);" % (data["callExpDateMap"][x][y][0]["description"].lower(),data["callExpDateMap"][x][y][0]["strikePrice"],data["callExpDateMap"][x][y][0]["bid"],data["callExpDateMap"][x][y][0]["ask"],data["callExpDateMap"][x][y][0]["last"],data["callExpDateMap"][x][y][0]["totalVolume"],data["callExpDateMap"][x][y][0]["volatility"],data["callExpDateMap"][x][y][0]["delta"],data["callExpDateMap"][x][y][0]["daysToExpiration"],stockTicker))

#Close Postgres Connection
    cur.close()
    conn.close()

input = sys.argv[1]

if(input == 'DELETE'):
    resetDatabaseTables()
else:
    liveParseData(input)
    insertAlpha(input)
