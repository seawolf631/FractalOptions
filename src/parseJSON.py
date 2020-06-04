import json
import psycopg2

#Connect to Postgres
conn = psycopg2.connect(host="localhost", port = 5432, database = , user="postgres", password=)

with conn:
    cur = conn.cursor()

#Read JSON File
    with open('../docs/exampleJSONData/AAPL_20yr_daily.json') as f:
        data = json.load(f)
    cur.execute("DROP TABLE IF EXISTS historical_data;")
    cur.execute("CREATE TABLE historical_data(price_id serial PRIMARY KEY, open real NOT NULL,low real NOT NULL, high real NOT NULL,close real NOT NULL, stock varchar(8) NOT NULL);")

    stock="\'AAPL\'"
    for x in data["candles"]:
        cur.execute("Insert INTO historical_data (open,low,high,close,stock) VALUES (%s,%s,%s,%s,%s);" % (x['open'],x['low'],x['high'],x['close'],stock))
        print ("Insert INTO historical_data (open,low,high,close,stock) VALUES (%s,%s,%s,%s);" % (x['open'],x['low'],x['high'],x['close']))

#Queries
    cur.execute("select (open-low)/open as percent_difference from historical_data order by percent_difference DESC limit 10;")
    query_results = cur.fetchall()
    print(query_results)
    cur.execute("select count(*) from historical_data;")
    query_results = cur.fetchall()
    print(query_results)

#Close Postgres Connection
cur.close()
conn.close()
