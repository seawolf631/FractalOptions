#!/bin/bash

curl -X POST --header "Content-Type: application/x-www-form-urlencoded" -d "grant_type=refresh_token&refresh_token=mfklITVnKww1YzbRRlo6OnNAnnnbREV1SqEosjwORN4g63M8QfkpPADC2LEo8Nd9tOoqMHnOpU/+/Q5csfZPaC2lUHeIzOd7B4ycKYGF8xvQc76QqpULBsUV6TwPrZslBfCQChcf1WCFtWa3QBJQj5ESYdZd1n/E4u8uwhQqA/faypePR/jPddlyrGvpUeFhKeVsoUGFlsKBui2PvVsffcGVzuZlNVg1pIXzIw/NuEaTVKDRtyP1Iw+OImVrdnJctOtmvXR1MILYFSUPIfppZgt6lFvUWOru2tl5Mh7uB6yf3vB91/qR4Dnlo/uKyK1f8d/UjtXNtoSZvyE3fjbps5VAVAx7UV3yNslIz/JtLsufd5FGPlxGnfAjw62aoFEWouwg2bjZuN8qX4P5zVxjHB67H5g+r+Y5Cyv4dptWnIgTWKu/0BRTp9qKWk/100MQuG4LYrgoVi/JHHvlPcNyUs7JJyQRIRmQg2PHZ6x7+yFW/RNpYMAbFZfOU3U9A3pNT+nlCsLK4j1wltrEfnlE9/GpOEikJwp0rWi6WLp4h/gfo+cBrfYVG7jGaRlIjCfJazE4phW5xFnFS+nPjMTdUqQr6pfemy9AM7w9sKAYXzieDCPN5Sg6sUo3Ex6V+mRyn3mePcS4cx+yeU/9L6mIjfJU9tLuas6ig4IyUeWQJYNvEBAkvBzL4+ohhCF53rFKfoYj55bAXi+hHUOlZ73zPCjWvTuARP+YYZTLdu+XxrjatAVg8Xm+a9ghmWnyMSXNWcmYHZre0YhROBSbvSr8wg3R/2QeXerBEO2mOJc1OjKY8NUaARJ5BSc5LLPM0Dp3/t01dBVswnI+Nv8IZKnIEvCavePlGi3krmj07L6HQjSwmRVLiAsikNJChTUzEG1+RjGfBRCRskc=212FD3x19z9sWBHDJACbC00B75E&access_type=offline&code=&client_id=H2PZBDOKOS3FLTGOPRBD0A9GX6UILCJL%40AMER.OAUTHAP&redirect_uri=https%3A%2F%2F127.0.0.1" "https://api.tdameritrade.com/v1/oauth2/token" >> docs/keys.json


REFRESH=$(grep -oP '"access_token" :\K[^,]*' docs/keys.json)
REFRESH=${REFRESH:2:-1}

input="stockList.txt"
while IFS= read -r line
do
      curl -X GET --header "Authorization:Bearer +tGUZZcXm58+6b2HY3kwEftibap2F6vk9MVYqgZ2s1gdQf48kqEteYewgJZelYAGNsSYiGs6ZgA2BfuGIhBbpc8rGzQ2gzn9J8VyRiVUhjI2ZmsB3WbGqXK+ikz7Lxb8IV/+q8nmflAN7mAlOOE5sH/a8eN/sIeczVWAWitEKN5Cm91nR4a70RSbb/ynj8ivvWWHGywC2SjA69VDgfCfk3qgSniDyDsCW3TpY2zMnRktkcFBB/Vc3cXHjzCgij/7i6+CJolsO9R+iF5uHT8rdc8NNm9qGHKlTAs2hUF9v6C7UxDVetWRa15k7l0sr/7FlMsIwZpNfaSLH7RwT14dOoHNcgHygyD0uxcIFMk6C9+2mN66AigW9fZdfd3gdNc/Jf3Kv4x1ykrnEUsyrj4EUVcJCJqY46CHmDqQ9F6Is7knG+4/Zlmghk7W9waRm61Od+baMANIoypcKkC4lPYPQ4pVLLCCHxA2I3eqzrm00cTUhq9HEIkLI+punWLxon5EysreWx8+Ny07adYG5JbRQxd6ZUPNuhQcNmqWLtoJQLW5nlKjJqj+Oo88dmjRD1wWkbkg8100MQuG4LYrgoVi/JHHvlyE5a/zCzDWx2Hm5KVQzFGr0in74Y3/u9IqhKj6aTfscQ9u4Eaj8JMxdg9XZzDhOm8zMbH93fUEaECcv2sj8TBsCezxs2esacIBMDJnaVU45CcbuQYtoF4FketWvyScD8VYH5mjA9GG9nd2RsIdBnZz6ZPN6uoYIENfzinhxL0lm3WPuPZq4STaza88GOC5g7UhWZo6+xBtxGjkZlevAikO8c+t/kZv/cOAIml9jYlAya6DvdYxGNMy2DA6vEhcNFehl5ZuW+PsP5TkzVrHuNYAJQTwVWEcFBMw6M7G/AVJ1TMGPqm+OUACzcFPJxgo68mnJghtAv+dbxbCC9AmUSFdBcQESfJD+WO8t2pmTNts5NIkxtq+ER3YX28qoHH293ujJNeM/onftavKIQHL0cArotoDaC+61fSZkcB9aV6Xw9In/Dv3H/spEkF0CFzeVBfEg/XJb10VZyeT9h1XZlWsUFKHZo10rI2dVx4IiPGujQDezB0TNunBN3Kj1SmUTliWVY7Zn24ZbHq7fEdHpaTfqWqqGGr77q87/QBMveBjuT0Tsv4j9hsfT6PL/YwqgFezNpL+212FD3x19z9sWBHDJACbC00B75E" "https://api.tdameritrade.com/v1/marketdata/${line}/pricehistory?apikey=H2PZBDOKOS3FLTGOPRBD0A9GX6UILCJL&periodType=year&period=20&frequencyType=daily&frequency=1&needExtendedHoursData=false" >> docs/exampleJSONData/${line}_data.json
done < "$input"
