#!/bin/bash
# bash script that takes url,sends a request
# to url and display size od body response
curl - sI "$1" | grep "Content-Length:" | cut - d " " - f 2
