#!/bin/bash
# script that takes in a url and display http method
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
