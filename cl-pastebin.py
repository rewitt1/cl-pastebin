#!/usr/bin/env python

import pastebin
import ConfigParser
import argparse
import os
import sys

parser = argparse.ArgumentParser()

parser.add_argument('--devkey', help="pastebin devkey")
parser.add_argument('--user', help="pastebin username")
parser.add_argument('--password', help="pastebin password")

args = parser.parse_args()

config = ConfigParser.ConfigParser()
config.read(os.path.join(os.environ["HOME"], ".cl-pastebin", ".config"))

devkey = args.devkey or config.get("pastebin", "devkey")
user = args.user or config.get("pastebin", "user") or None
password = args.password or config.get("pastebin", "password")

api = pastebin.PastebinAPI()
apikey = api.generate_user_key(devkey, user, password)

result = api.paste(devkey, sys.stdin.read(), apikey)
print result
