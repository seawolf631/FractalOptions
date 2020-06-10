import json
import psycopg2
import os
import re
from config import config
import sys

#Connect to Postgres
params = config()
conn = psycopg2.connect(**params)

with conn:
    cur = conn.cursor()
    
#Read Historical Data JSON File
    #cur.execute("DROP TABLE IF EXISTS historical_data;")
    cur.execute("CREATE TABLE IF NOT EXISTS historical_data(historical_price_id serial PRIMARY KEY, open real NOT NULL,low real NOT NULL, high real NOT NULL,close real NOT NULL, stock varchar(8) NOT NULL);")
    filePath = sys.argv[1]
    print(filePath)
    with open(filePath) as f:
        data = json.load(f)
        file=os.path.basename(filePath)
        stock = "\'" + file.split("_")[0] + "\'"
        for x in data["candles"]:
                        cur.execute("Insert INTO historical_data (open,low,high,close,stock) VALUES (%s,%s,%s,%s,%s);" % (x['open'],x['low'],x['high'],x['close'],stock))
                        
    #rootdir = '../docs/exampleJSONData'
    #for subdir, dirs, files in os.walk(rootdir):
     #   for file in files:
      #      if(file.split("_")[1] == "data.json"):
       #         with open(os.path.join(subdir,file)) as f:
        #            data = json.load(f)
         #           stock="\'" + file.split("_")[0] + "\'"
          #          for x in data["candles"]:
           #             cur.execute("Insert INTO historical_data (open,low,high,close,stock) VALUES (%s,%s,%s,%s,%s);" % (x['open'],x['low'],x['high'],x['close'],stock))
            #            print ("Insert INTO historical_data (open,low,high,close,stock) VALUES (%s,%s,%s,%s,%s);" % (x['open'],x['low'],x['high'],x['close'],stock))

#Read Options JSON File
appleStock = "\'AAPL\'"
with open('../docs/exampleJSONData/AAPL_Option_Data.json') as f:
    data = json.load(f)
    cur.execute("DROP TABLE IF EXISTS stock_live_data;")
    cur.execute("CREATE TABLE stock_live_data(stock_price_id serial PRIMARY KEY, bid real NOT NULL,ask real NOT NULL, last real NOT NULL,volume real NOT NULL, fiftyTwo_week_high real NOT NULL, fiftyTwo_week_low real NOT NULL, stock varchar(8) NOT NULL);")

    cur.execute("Insert INTO stock_live_data (bid,ask,last,volume,fiftyTwo_week_high,fiftyTwo_week_low,stock) VALUES (%s,%s,%s,%s,%s,%s,%s);" % (data["underlying"]["bid"],data["underlying"]["ask"],data["underlying"]["last"],data["underlying"]["totalVolume"],data["underlying"]["fiftyTwoWeekHigh"],data["underlying"]["fiftyTwoWeekLow"],appleStock))

    
    cur.execute("DROP TABLE IF EXISTS options_live_data;")
    cur.execute("CREATE TABLE options_live_data(option_price_id serial PRIMARY KEY, description varchar(36) NOT NULL, bid real NOT NULL,ask real NOT NULL, last real NOT NULL,volume real NOT NULL, implied_volatility real NOT NULL);")
    for x in data["putExpDateMap"]:
        for y in data["putExpDateMap"][x]:
            cur.execute("Insert INTO options_live_data (description,bid,ask,last,volume,implied_volatility) VALUES (\'%s\',%s,%s,%s,%s,%s);" % (data["putExpDateMap"][x][y][0]["description"].lower(),data["putExpDateMap"][x][y][0]["bid"],data["putExpDateMap"][x][y][0]["ask"],data["putExpDateMap"][x][y][0]["last"],data["putExpDateMap"][x][y][0]["totalVolume"],data["putExpDateMap"][x][y][0]["volatility"]))
    
#Close Postgres Connection
cur.close()
conn.close()
