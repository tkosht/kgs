#!/bin/sh

q="taylor+swift"
api_key=$(cat .api_key)
n_limit=3

url="https://kgsearch.googleapis.com/v1/entities:search"
url="$url?query=$q&key=$api_key&limit=$n_limit&indent=True"
curl -s -S $url
