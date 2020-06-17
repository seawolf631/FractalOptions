#!/bin/bash

input="../stockList.txt"
while read p;
do
    FILENAME=$p"_data.json"
    echo $FILENAME
    aws s3 cp s3://fractal-data/$FILENAME ../docs/exampleJSONData/$FILENAME
    python3 parseJSON.py ../docs/exampleJSONData/$FILENAME
    rm ../docs/exampleJSONData/$FILENAME
done < $input
