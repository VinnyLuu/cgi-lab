#!/usr/bin/env python3

import os
import json
import sys
from templates import secret_page, _wrapper, after_login_incorrect
from secret import username, password

query_string = sys.stdin.read(int(os.environ["CONTENT_LENGTH"]))
POST={}
args=query_string.split('&')

for arg in args: 
    t=arg.split('=')
    if len(t)>1: k, v=arg.split('='); POST[k]=v

if "username" in POST and "password" in POST:
    if POST["username"] == username and POST["password"] == password:
        print("Content-Type: text/html")
        print("Set-Cookie: login=successful")
        print()
        print(_wrapper(secret_page(username, password)))
    else:
        print(_wrapper(after_login_incorrect()))
