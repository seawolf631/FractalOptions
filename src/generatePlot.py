import matplotlib.pyplot as plt
import psycopg2

def getData():
    conn = psycopg2.connect(host="localhost", port = 5432, database =  , user="postgres", password=)
    with conn:
        cur = conn.cursor()
        cur.execute("select (open-low)/open as percent_difference from historical_data order by percent_difference ASC;")
        queryResult = cur.fetchall()
        cur.execute("select count(*) from historical_data")
        rowLength = cur.fetchall()
    cur.close()
    conn.close()
    return queryResult, rowLength

x,y = getData()
y=y*y[0][0]
newY = []
n=0
i=0
for k in y:
    for j in k:
        newValue = (j-i)/(j)
        newY += (newValue,)
        i += 1
    n += 1

plt.xlabel("|X|")
plt.ylabel("P(>X)")
plt.title("AAPL 20 yr. Daily Low % Return Survival Function (Log Scale)")
plt.xscale('log')
plt.yscale('log')
plt.plot(x,newY)
plt.savefig('static/plot.png')
