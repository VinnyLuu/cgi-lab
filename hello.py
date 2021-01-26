#!/usr/bin/env python3

import os
import json
from templates import login_page, _wrapper, secret_page
from secret import username, password

print("Content-Type: text/html")
print()

# Question 1
# print()
# print(json.dumps(dict(os.environ), indent=2))

# Question 2
# if len(os.environ["QUERY_STRING"]) > 0: 
#     print(os.environ["QUERY_STRING"].split("=")[1])

# Question 3
# if "HTTP_USER_AGENT" in os.environ.keys():
#     print(os.environ["HTTP_USER_AGENT"])

# Question 4
if os.environ["HTTP_COOKIE"].split("=")[1] == "successful":
    print(_wrapper(secret_page(username, password)))
else:
    print(_wrapper(login_page()))
