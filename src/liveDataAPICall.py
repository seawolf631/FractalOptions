import http.client
import mimetypes


def pullLiveData(stockTicker):
    conn = http.client.HTTPSConnection("api.tdameritrade.com")
    payload = ''
    bearer = 'RRq5h5RITACPngJBRAgPTOECoF0buT1Bmt/0QUhdJDUWUI0qJ1Ys8asNZjuJE3doIbUhPOEia+5yhkqRR59t8wKX8XY3Gv/QeJygtC0ESMMtIW0Ai9IVJO7E5+HdmoYlBobGBTQryuhZX+WSPzs5RI8iSiuQCO9D51bwzHVzGsrqOo9C5we+KwotFCCSnbu2GoC+jKmUa7eskZMoWj4vZ7hyYFzBK6S/JYo3W4yx9YhJV7SHDI5fuPX8nkH98uPBVRX4cFO9xPDOEQHaZMzOTmZLn2xwuAX0uR0Gp37DFiqbgRU4aNMgBesooeTO/xgeAGes9z4PxGyDbgl8VsN0RHtUFzB0Nyk5jIVOZXmvmqhxxzRQamGm/APJ3iPqoBAjD0PBvYqoGz4t6zTpUH6SDnRKRESh+idAFeBNxdLgAi/nEY5tnezsnZCl/wLRvnZf9HcGpOYCcWAKWgbg7ovlDz2d0wg7baPLetthK2OmiCJTGgFGw+tlBcPtE7bApdCkIuPaT0z0Ut7yqJmXaB/QkyaVAUNpZMLgf1l5t78YfIcVRbqqD1QBNX+NgkeNYAeRdSMfzc5/h1UY09aFS100MQuG4LYrgoVi/JHHvldf+0qFx6bTV7gSJzoyyalrAQcRZZTtT37/KPYQD2KmB8/8Adv/zwYGGWu7jpnRW0LEPfIpVyfWojPhnyKyWKHkN3OM6oElvTZmqmHSysXl3+gbTWo814Kfryjk7z0UN3fPxTNO0eOtVNssBJBkjAJIj0unst+rBipNCZ2ltLtxLYkCgTro3OLWjDGi4tzV8m9k28kBUumPyUoTarnikc4dzijvpH9bHDPRn28YgldRil2pFrAvf6a/++wtWTO3z1CNrW1O3liVKOaeSM4eNY10a6IYuOHUO5UclUmmsa0u3T9dsW58fq7xqmh9AX/iZrKH31PO10txfjNhk0mrvDAhTJp5etjKhimVK75lFZ70xmFfJ4mTAKhaNwQLbac0wN16+wPkakNSrZ/QB+rwCvAwjhH/VWaPP9Nzf7MLZkbchIY0kIImf3sbX8MXkj/0PHb7CaogAqnPeOa4R7NC66OtgLBCbOcHa1lPeSpcyMKvPuA/CxZ4lZXSb3D+VeqB6uN7z1ffhUpR4gJgEGln1a1Sg/ZupIfjuX/FH/WrvbODwWzc2Dno4XrZQRviaxVIyKmPniomThr36JHHuw==212FD3x19z9sWBHDJACbC00B75E'
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







