import http.client
import mimetypes


def pullLiveData(stockTicker):
    conn = http.client.HTTPSConnection("api.tdameritrade.com")
    payload = ''
    bearer = 'rjlUMWL+wJzEJ0UdRalUyinnDDvS8Mf4V8XefEP6ICJ9V3Q4HR6vs+hM6nIQ+CLkLAGKgvtjuZ/29PGOv8FtAsFfUUZI60L/QMrgkpUiLqZYAAXSt0JpXjiNNbvP8sqKxIx+2uZ31Owa33NXXdfe+EdKDC65PRWMr/VEYuzsLjG+cXs6zfvd7Q6IP4IrN9zpKbU5/4uqjKXqCWMmE2b/JzSwfyVeN2vv8Gg8ZGHgy/K5M2rVbkkKieRb50PRazF8wsO+ONIH68ItIlqKdtug4CfuM2A7S6BNLOKAeyDPUQYodIHoZtDzbzrJdqRxVVSSMhqpnNNEV0Q6ezENHJTxJZrYY2an1HR5b542zALRJ+qUzzIHLhwNs7+54d0t78arsYzRd8uKNKB3BFdF4Vp+uxZGk/oEsyUFzRnSaurHZZF8p2/ypl2f4qdyTtYENon12R4Iae31n4cmMg/VZCC12srjeUWXk5ACs8JMxt7ael9VgDzRvnXEf6OYo7aByuIVZJDteYWcMEvVnEzgYEx+yJuH9m6KTTbWFWk3q9Ffz1Abi5abQfGPeS4wYSoXMFWJkZCqyvjsT+nL6Avex100MQuG4LYrgoVi/JHHvlDIoxess7RRlinHzPdyaaOIIkpTRibMhUjpb6oXGniu00lVXg0f/AF9AxAdr4wypdETrmUkNAynk+0C4HvdoFj/cVZRBo737iK8odXoEMzCNPH8sDGYspvC/nRxNiFwpPXa2zFNwc4IilSgUtf8XBSc945XjZHn07O93vCdMPV9EOn2yGwh6xcnSpIDdJkD30Po7F1JQ65CUos46eYDwU888K+31XTphSjMbmm1v35DGTcC8APmT/OPcXV6+OP4JrqyclJ/PCbuYCoZjTuCGyjiTe7a8X+UbhFREhzmtcJbfg3ss+2T/vAZ0EiQXzFMk/kdprTOEKW0GZyNLLQYKJu/dFJoRTa1ICbPH+x8h7pgRexzE5S8WQUgIS9qh4l60/uCUi2yBXTy/qD1XvDzRtNPHb5CT/VQjUY99NpZ/Tgcalb7nHAA/mt61eKH0U23HkaknDm1VMkYKXoBXZVU00KVLx3jiIRmnG0Ww+zKVMiSoGPc+X9RMJWaxn31H31yVdwvvAtsM7m1duf+W1xxPD6HmZs7kZmtqCU43g4UJTpvNl6y53yS1Sl3u44NZ4ppIMb64IXdvZNKjrBdkQ==212FD3x19z9sWBHDJACbC00B75E'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + bearer
    }
    stock = stockTicker
    conn.request("GET", "/v1/marketdata/chains?apikey=H2PZBDOKOS3FLTGOPRBD0A9GX6UILCJL&symbol="+stock+"&contractType=ALL&strikeCount=30&includeQuotes=TRUE&strategy=SINGLE&range=ALL&expMonth=ALL", payload, headers)
    res = conn.getresponse()
    data = res.read()
    file = open("../docs/exampleJSONData/live_option_data.json","w")
    file.write(data.decode("utf-8"))
    file.close()







