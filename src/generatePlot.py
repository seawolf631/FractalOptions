import matplotlib.pyplot as plt
import psycopg2
from config import config

def getData(stock):
    params = config()
    conn = psycopg2.connect(**params)
    with conn:
        cur = conn.cursor()
        cur.execute("select (open-low)/open as percent_difference from historical_data where stock = \'%s\' order by percent_difference ASC;" % (stock))
        print("select (open-low)/open as percent_difference from historical_data where stock = \'%s\' order by percent_difference ASC;" % (stock))
        queryResult = cur.fetchall()
        cur.execute("select count(*) from historical_data where stock = \'%s\'" % (stock))
        rowLength = cur.fetchall()
    cur.close()
    conn.close()
    return queryResult, rowLength

with open('../stockList.txt') as f:
    for line in f:
        line = line.split()[0]
        x,y = getData(line)
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
        plt.title(line + " 20 yr. Daily Low % Return Survival Function (Log Scale)")
        plt.xscale('log')
        plt.yscale('log')
        plt.plot(x,newY)
        fileName = 'static/' + line + "_plot.png"
        plt.savefig(fileName)
        plt.close()
