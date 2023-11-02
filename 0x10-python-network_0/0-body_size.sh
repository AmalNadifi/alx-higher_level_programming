#!/bin/bash
# The following script takes in a URL, sends a request to that URL, and displays the size of the body of the response

# The requirements:
#	The size must be displayed in bytes
#	Use of curl is required
curl -s "$1" | grep -i Content-Length | cut -d " " -f2
