#!/bin/bash
# get all methods
curl -is -X "OPTIONS" "$1" | grep "Allow" | cut -d " " -f 2-
