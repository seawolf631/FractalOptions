#!/bin/bash

python3 ~/FractalOptions/src/parseLiveDataJSON.py DELETE

curl --location --request POST 'https://api.tdameritrade.com/v1/oauth2/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'grant_type=refresh_token' \
--data-urlencode 'refresh_token=EnaUTbODY+rAlfyhsTNQ+cbYWiLcjiKaBsSzcC0PB+wl12QPp+YuemsIqXAQzUxNTYp4k/tJPI8mCOoKO5bq6IwofcMdDexRT4KeyS/dp2UwRT/KWQlOf6nZE9fs2eM2wpJkpe0CtPPIEUqzBCdFeNDKcG/xN53sT5ua7FZM+tIBqoKbLMnpvQBI/zgzkuYLms05ALDcdGyovAyTZdBaQbhEXnoqoV00lFDRGEbXNBL4WCLXiYyhd/6GXRUZx0XgAFQxq7s3OhwlmjdajC6+FFkVeyaMfxX/eRg7rlOYTArBQKFrM/DDFaMXsqpuGgYXvVquRxzAI0xdBY2nZCUPGkoWH9Srp/QkdYO1JbzV+Pnu9LGMfNx1EqTf2XHA1CQzNCMqZnvI8gd5BXQKIANKPP04GsEIvZndx28rT0vAKlr1AvvUpAmSQkKiHDu100MQuG4LYrgoVi/JHHvlLp8ncp5/Gw3Tj/A5U/8xyOkrKw8rkr1SqCZt1+eGHL9Y2j4e7NNhidKrdil7rX+kNXd034UBROKBfHb9ruKqtXPII1EQH29nRL+L121BKRUvNQTlQwObdUoyfndnZ9ZKajCvCslS0b57+sTUGVuExpPaSO1l5xBVYyBwV5Y+vxRAX5x2FKCnl6xhAZtLbf7HwvvFZfTPDJdkG8343FG4hlZonGYfzfmCj6PQ5sSzByFnyqyIBBDz5hroBWPHQb4XJeuuydFmfe930jG9sd4lDjy7kzney+7swu+6+Zmih7IMSw2SJSSMMMNsBVeRzJvVqp6asi74m+LJ+L7SxHNqHcoe0vaBsadXdrP+UYazas1IzyAkqOhOIO3FrGcCCxvEAgrdT3qP713mcjxBqSDkjAz8juSTasr/XMT4UHLhCpd1/m24TQIrFZKeLSw=212FD3x19z9sWBHDJACbC00B75E' \
--data-urlencode 'client_id=H2PZBDOKOS3FLTGOPRBD0A9GX6UILCJL@AMER.OAUTHAP' \
--data-urlencode 'redirect_uri=https://127.0.0.1' >> ~/FractalOptions/docs/keys.json

REFRESH=$(grep -oP '"access_token" :\K[^,]*' ~/FractalOptions/docs/keys.json)
REFRESH=${REFRESH:2:-1}

end=$((SECONDS+1500))
input="/home/ubuntu/FractalOptions/stockList.txt"
while IFS= read -r line
do
    if [ $end -lt $SECONDS ]; then
	rm ~/FractalOptions/docs/keys.json
	
	curl --location --request POST 'https://api.tdameritrade.com/v1/oauth2/token' \
	     --header 'Content-Type: application/x-www-form-urlencoded' \
	     --data-urlencode 'grant_type=refresh_token' \
	     --data-urlencode 'refresh_token=EnaUTbODY+rAlfyhsTNQ+cbYWiLcjiKaBsSzcC0PB+wl12QPp+YuemsIqXAQzUxNTYp4k/tJPI8mCOoKO5bq6IwofcMdDexRT4KeyS/dp2UwRT/KWQlOf6nZE9fs2eM2wpJkpe0CtPPIEUqzBCdFeNDKcG/xN53sT5ua7FZM+tIBqoKbLMnpvQBI/zgzkuYLms05ALDcdGyovAyTZdBaQbhEXnoqoV00lFDRGEbXNBL4WCLXiYyhd/6GXRUZx0XgAFQxq7s3OhwlmjdajC6+FFkVeyaMfxX/eRg7rlOYTArBQKFrM/DDFaMXsqpuGgYXvVquRxzAI0xdBY2nZCUPGkoWH9Srp/QkdYO1JbzV+Pnu9LGMfNx1EqTf2XHA1CQzNCMqZnvI8gd5BXQKIANKPP04GsEIvZndx28rT0vAKlr1AvvUpAmSQkKiHDu100MQuG4LYrgoVi/JHHvlLp8ncp5/Gw3Tj/A5U/8xyOkrKw8rkr1SqCZt1+eGHL9Y2j4e7NNhidKrdil7rX+kNXd034UBROKBfHb9ruKqtXPII1EQH29nRL+L121BKRUvNQTlQwObdUoyfndnZ9ZKajCvCslS0b57+sTUGVuExpPaSO1l5xBVYyBwV5Y+vxRAX5x2FKCnl6xhAZtLbf7HwvvFZfTPDJdkG8343FG4hlZonGYfzfmCj6PQ5sSzByFnyqyIBBDz5hroBWPHQb4XJeuuydFmfe930jG9sd4lDjy7kzney+7swu+6+Zmih7IMSw2SJSSMMMNsBVeRzJvVqp6asi74m+LJ+L7SxHNqHcoe0vaBsadXdrP+UYazas1IzyAkqOhOIO3FrGcCCxvEAgrdT3qP713mcjxBqSDkjAz8juSTasr/XMT4UHLhCpd1/m24TQIrFZKeLSw=212FD3x19z9sWBHDJACbC00B75E' \
	     --data-urlencode 'client_id=H2PZBDOKOS3FLTGOPRBD0A9GX6UILCJL@AMER.OAUTHAP' \
	     --data-urlencode 'redirect_uri=https://127.0.0.1' >> ~/FractalOptions/docs/keys.json

	REFRESH=$(grep -oP '"access_token" :\K[^,]*' ~/FractalOptions/docs/keys.json)
	REFRESH=${REFRESH:2:-1}
	
	end=$((SECONDS+1500))
    fi
    curl --location --request GET 'https://api.tdameritrade.com/v1/marketdata/chains?apikey=H2PZBDOKOS3FLTGOPRBD0A9GX6UILCJL&symbol='${line}'&contractType=ALL&strikeCount=30&includeQuotes=TRUE&strategy=SINGLE&range=ALL&expMonth=ALL' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer '${REFRESH} >> ~/FractalOptions/docs/exampleJSONData/${line}_live_data.json
    echo ${line}
    python3 ~/FractalOptions/src/parseLiveDataJSON.py ${line}
    rm ~/FractalOptions/docs/exampleJSONData/${line}_live_data.json
    sleep 0.1
done < "$input"

rm ~/FractalOptions/docs/keys.json

    
