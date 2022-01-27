#!/usr/bin/python3
# Title: Subdue - Compact Subdomain Fuzzing Tool for CTFs
# Author: Lem0nSec_
# Version: 1.0 

# This tool will fuzz subdomains within a specified domain and using a specified wordlist. 
# A positive result is given when the values of 'content bytes' and 'content lines' for a
# fuzzed potential subdomain diverge from those of another subdomain obtained using a 
# random string.
# Bear in mind that Subdue has been written with CTF-like challenges in mind. For this reason, 
# it may not be a suitable tool for real-world engagements.

# All rights are reserved

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
