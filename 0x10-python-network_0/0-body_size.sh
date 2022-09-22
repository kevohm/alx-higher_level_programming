#!/bin/bash
# curl -si to grab heaser in silent mode
curl -si $1 | grep Content-Length | tail -c 5
