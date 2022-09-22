#!/bin/bash
# get all methods
curl -X OPTIONS "$1" -Is | grep allow | awk '{print $2}' | cut -d "," -f 1- --output-delimiter=', '
