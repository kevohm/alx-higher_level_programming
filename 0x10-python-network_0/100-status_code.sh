#!/bin/bash
# To send a GET request to the URL, and displays the body of the response A header variable X-School-User-Id must be sent with the value 98
curl -sI -o /dev/null -w "%{http_code}" "$1"
