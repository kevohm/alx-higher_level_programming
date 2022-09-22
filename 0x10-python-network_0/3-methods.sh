#!/bin/bash
# get all methods
curl -is -X "OPTIONS" "$1" | grep "allow" | cut -d " " -f 2-
