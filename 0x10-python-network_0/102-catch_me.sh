#!/bin/bash

# Make a POST request with curl and include the data "user_id=98" in the request body
curl -sX PUT -d "user_id=98" 0.0.0.0:5000/catch_me -o /dev/null
