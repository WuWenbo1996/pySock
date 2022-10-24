#!/bin/bash

mysql -ugaoya -pgaoya -e"source ./src/tableCreate.sql"

nohup python ./src/dataRecv.py
nohup python ./src/dataService.py
