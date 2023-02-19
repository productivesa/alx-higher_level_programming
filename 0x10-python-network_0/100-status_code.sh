#!/bin/bash
# script that sends a request to url passed an argument
curl -s -o /dev/null -w "%{http_code}" "$1"
