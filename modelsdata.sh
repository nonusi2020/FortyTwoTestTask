#!/usr/bin/env bash
date=$(date '+%Y_%m_%d')
./manage.py modelsinfo 2> "$date.dat"
