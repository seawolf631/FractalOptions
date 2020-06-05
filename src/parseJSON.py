import json
import psycopg2

#Connect to Postgres
conn = psycopg2.connect(host="localhost", port = 5432, database = , user="postgres", password=)

with conn:
    cur = conn.cursor()

#Read Historical Data JSON File
    with open('../docs/exampleJSONData/AAPL_20yr_daily.json') as f:
        data = json.load(f)
    cur.execute("DROP TABLE IF EXISTS historical_data;")
    cur.execute("CREATE TABLE historical_data(historical_price_id serial PRIMARY KEY, open real NOT NULL,low real NOT NULL, high real NOT NULL,close real NOT NULL, stock varchar(8) NOT NULL);")

    stock="\'AAPL\'"
    for x in data["candles"]:
        cur.execute("Insert INTO historical_data (open,low,high,close,stock) VALUES (%s,%s,%s,%s,%s);" % (x['open'],x['low'],x['high'],x['close'],stock))
        print ("Insert INTO historical_data (open,low,high,close,stock) VALUES (%s,%s,%s,%s);" % (x['open'],x['low'],x['high'],x['close']))

#Read Options JSON File
    with open('../docs/exampleJSONData/AAPL_Option_Data.json') as f:
        data = json.load(f)
    cur.execute("DROP TABLE IF EXISTS stock_live_data;")
    cur.execute("CREATE TABLE stock_live_data(stock_price_id serial PRIMARY KEY, bid real NOT NULL,ask real NOT NULL, last real NOT NULL,volume real NOT NULL, fiftyTwo_week_high real NOT NULL, fiftyTwo_week_low real NOT NULL, stock varchar(8) NOT NULL);")

    cur.execute("Insert INTO stock_live_data (bid,ask,last,volume,fiftyTwo_week_high,fiftyTwo_week_low,stock) VALUES (%s,%s,%s,%s,%s,%s,%s);" % (data["underlying"]["bid"],data["underlying"]["ask"],data["underlying"]["last"],data["underlying"]["totalVolume"],data["underlying"]["fiftyTwoWeekHigh"],data["underlying"]["fiftyTwoWeekLow"],stock))

    
    cur.execute("DROP TABLE IF EXISTS options_live_data;")
    cur.execute("CREATE TABLE options_live_data(option_price_id serial PRIMARY KEY, description varchar(36) NOT NULL, bid real NOT NULL,ask real NOT NULL, last real NOT NULL,volume real NOT NULL);")
    for x in data["putExpDateMap"]:
        for y in data["putExpDateMap"][x]:
            cur.execute("Insert INTO options_live_data (description,bid,ask,last,volume) VALUES (\'%s\',%s,%s,%s,%s);" % (data["putExpDateMap"][x][y][0]["description"].lower(),data["putExpDateMap"][x][y][0]["bid"],data["putExpDateMap"][x][y][0]["ask"],data["putExpDateMap"][x][y][0]["last"],data["putExpDateMap"][x][y][0]["totalVolume"]))
    
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
