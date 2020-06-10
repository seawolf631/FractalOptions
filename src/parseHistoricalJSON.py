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
    
#Close Postgres Connection
cur.close()
conn.close()
