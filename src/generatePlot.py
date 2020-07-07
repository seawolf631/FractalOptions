import matplotlib.pyplot as plt
import psycopg2
from config import config
from math import log,sqrt

def getData(stock,direction):
    params = config()
    conn = psycopg2.connect(**params)
    with conn:
        cur = conn.cursor()
        if(direction=='Negative'):
            cur.execute("select case when open=0 then 0 else (open-low)/open end as percent_difference from historical_data where stock=\'%s\' order by percent_difference ASC;" % (stock))
            print("select case when open=0 then 0 else (open-low)/open end as percent_difference from historical_data where stock=\'%s\' order by percent_difference ASC;" % (stock))
            queryResult = cur.fetchall()
        elif(direction=='Positive'):
            cur.execute("select case when open=0 then 0 else (high-open)/open end as percent_difference from historical_data where stock=\'%s\' order by percent_difference ASC;" % (stock))
            print("select case when open=0 then 0 else (high-open)/open end as percent_difference from historical_data where stock=\'%s\' order by percent_difference ASC;" % (stock))
            queryResult = cur.fetchall()
        cur.execute("select count(*) from historical_data where stock = \'%s\'" % (stock))
        rowLength = cur.fetchall()
    cur.close()
    conn.close()
    return queryResult, rowLength

with open('/home/ubuntu/FractalOptions/stockList.txt') as f:
    directions = ['Negative','Positive']
    for line in f:
        line = line.split()[0]
        for direction in directions:
            x,y = getData(line,direction)
            #Calculate Alpha
            lnSum = 0
            sample = 0
            for i in range(0,y[0][0] - 1):
                if(x[i][0] >= 0.01):
                    sample += 1
                    lnSum += log(x[i][0]/(0.01))
            if(lnSum>0):
                alpha = sample / lnSum
                error = alpha / sqrt(sample)
                info = "Alpha ~" + str(round(alpha,2)) + "  Error= +- " + str(round(error,2))


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
            plt.title(line + " 20 yr. Daily "+direction.upper()+" % Return Survival Function (Log Scale)")
            plt.xscale('log')
            plt.yscale('log')
            plt.text(0.0001, 0.001, info, {'color':'r','fontsize':12})
            plt.plot(x,newY)
            fileName = 'static/' + line + "_"+direction+"_plot.png"
            plt.savefig(fileName)
            plt.close()
