#!/bin/bash

mysql -ugaoya -pgaoya -e"source ./src/tableCreate.sql"

python ./src/dataRecv.py
python ./src/dataService.py
