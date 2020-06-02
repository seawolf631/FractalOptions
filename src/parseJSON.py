import json

#Read JSON File
with open('../docs/exampleJSONData/AAPL_20yr_daily.json') as f:
    data = json.load(f)

for x in data["candles"]:
    print "High =",x['high'], " Low =",x['low']

