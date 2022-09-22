#!/bin/bash
# get all methods
curl -is -X "OPTIONS" "$1" | grep "allow" | awk '{print $2}' | cut -d "," -f 1-
