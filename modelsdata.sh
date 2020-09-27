#!/usr/bin/env bash
date=$(date '+%Y_%m_%d')
./manage.py modelsdata 2> "$date.dat"