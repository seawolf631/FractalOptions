import http.client
import mimetypes

def pullLiveData(stockTicker):
    conn = http.client.HTTPSConnection("api.tdameritrade.com")
    payload = ''
    bearer = 'Zp2lT6u+u1qY5QgknhA3UQIFIVJPQr/wfNHbLZb8gbtZDGL9ivEHXlRImdASqU5FqNKPNwpQJdKT4wab0pBL6bi75xks6wH8j0asi12/c7L1WRKZK7qN486f5tnCrEdRYuBL2WKDxfKX43zIGuvvkACQLDyzKl/Jp5/72/mRyMpnR1vcsQVGLIgE/9Dn1bRyc4rXaWVqmXgYww7qUqxRH6GOlr5oqmDoLzxZoCS96dvQSTLGGNTjqMb4Xhg4xG5P9uSt5pBlUWK9yCWQGvgJIWO3Q0jr/hKONTCcHdC1bPyAQjXPhTPcAV12oxnY1tW37nWcDBuZ4K4XrKe/kf5kPHs5C1rxYfaySiw78vWdtxAs42nrXC4rq/wGtfUYhvlQHfcI9nkkijHK9nNwCEH+dHISd+wlAR5XQSSbC37FESwJkOMtm0knqlLr01NX2xIbh+FedOSZ1WTnzujGevVmc70Xa4XrkxPYmoeMlW+G2bqOe9AhjfZxrN38hGKLyY+pHcnXTq65a3PzfZlMF6xoDU59AYB6owaPSUj3OoK7VKTsBULRmvWf62llxkqqTxlVJFGNR6df9ddlGGhK1100MQuG4LYrgoVi/JHHvlYgT68Ytljhz8Ox9WF02t5SDJZh6NZKYJM26MyOXvenvhmJzOq+HmsxPlpojGbOJY282+vNVufqIl3dafW37+JA+LNKX3/vbGol2/dq11uXwIyTYix47J0UvCbB8FQd+Dn/ZU6z6TFmjXsKm/fU5xEIACTIHFVOidUxb0PW+32mYHLKrJPGqieVY29LLxyuEF6gZ5pYVLBrOMc2bCX1AzwDk1/ZjgTbb+LTip+HSgckJPFcFqKMc9jHkDG6OpukHP1Kjl6rZQl1eCdQ6vxQmlFL+JmbQvcjxW9zOBsFjRgkfvSgBuestvXzB0eYKlC8V7y71IMo4cpY/sF5ZNuKCnEFuKRchmrxRWmeMTe/OLSnicGDUI8Y2mms3Ji2s7YrQQdrib3r+yAqE3Yupa4jgkBzWJnkj1U/5EVwn3ccCDEyB7YbT0eTiYYnZabN3GBFrm3pcGDxinl5MI7dqJgFRKjgxtmXoViZ3Fc2DJ7KS1rOQ7Qv/lOL4jEP9fzoPcAegaWrCKAtDgqfXnu/fdKNVpPK70fLp4ldlSKe3oIpjRBg+RemQdpm6oE3ZFf+YLaMJ45D4XlmDxb0wizCTw==212FD3x19z9sWBHDJACbC00B75E'
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
