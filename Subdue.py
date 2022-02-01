#!/usr/bin/python3
# Title: Subdue - Compact Subdomain Fuzzing Tool for CTFs
# Author: Lem0nSec_
# Version: 1.0 

# MIT License
#
# Copyright (c) 2022 lem0nSec
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import argparse
import string
import random
import requests
import concurrent.futures
import warnings
from termcolor import colored

banner = '''

     @@@@@  @   @  @@@@@   @@@     @   @  @@@@@
     @      @   @  @    @  @   @   @   @  @ 
     @      @   @  @    @  @    @  @   @  @ 
     @@@@@  @   @  @  @@   @    @  @   @  @@@
         @  @   @  @    @  @    @  @   @  @ 
         @  @   @  @    @  @   @   @   @  @ 
     @@@@@  @@@@@  @@@@@   @@@     @@@@@  @@@@@
    '''

print (banner)
print (colored(" " * 35 + "by Lem0nSec_\n", "yellow"))

def test_values():
    data = []
    characters = string.ascii_letters + "-_"
    for i in range(15):
        selection = random.choice(characters)
        data.append(selection)
    value = "".join(data)
    headers_test = {"host":f"{value}.{url}"}
    if ssl == False:
        r = requests.get(f"http://{IP}", headers=headers_test, allow_redirects=False)
    else:
        warnings.filterwarnings("ignore")
        r = requests.get(f"https://{IP}", headers=headers_test, verify=False, allow_redirects=False)
    return r

def request(url, sub):
    sub = sub.strip()
    if ssl == False:
        headers = {"host": f"{sub}.{url}"}
        r = requests.get(f"http://{IP}", headers=headers, allow_redirects=False)
        if (len(test.content) != len(r.content)) and (len(test.content.splitlines()) != len(r.content.splitlines())):
            print (colored("[+] ", "green") + f"Valid subdomain found: {sub}.{url}\n" + colored("[+] ", "green") + f"Content bytes: {len(r.content)}\n" + colored("[+] ", "green") + f"Content lines: {len(r.content.splitlines())}\n")
    else:
        warnings.filterwarnings("ignore")
        headers = {"Host":f"{sub}.{url}"}
        r = requests.get(f"https://{IP}", headers=headers, verify=False, allow_redirects=False)
        if (len(test.content) != len(r.content)) and (len(test.content.splitlines()) != len(r.content.splitlines())):
            print (colored("[+] ", "green") + f"Valid subdomain found: {sub}.{url}\n" + colored("[+] ", "green") + f"Content bytes: {len(r.content)}\n" + colored("[+] ", "green") + f"Content lines: {len(r.content.splitlines())}\n")
    
def main():
    global IP, url, ssl, test
    parser = argparse.ArgumentParser(description="Welcome to Subdue! A compact subdomain fuzzing tool for CTFs")
    parser.add_argument("-i", help="Target IP", required=True)
    parser.add_argument("-d", help="Target domain", required=True)
    parser.add_argument("-w", help="Wordlist", required=True)
    parser.add_argument("-k", help="SSL option", action="store_true", required=False)
    parser.add_argument("-t", help="Number of concurrent threads (default 5)", type=int, default=5)
    args = parser.parse_args()
    IP = args.i
    url = args.d
    wordlist = args.w
    ssl = args.k
    threads = args.t
    print (f"\n[*] Brute-forcing subdomains in '{url}'\n")
    test = test_values()
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        attempt = {executor.submit(request, url, sub): sub for sub in open(wordlist).readlines()}
        return attempt

if __name__ == "__main__":
    main()
