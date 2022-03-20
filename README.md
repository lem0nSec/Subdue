# Subdue - A Compact Subdomain Fuzzing Tool for CTFs
[![GitHub license](https://img.shields.io/github/license/lem0nSec/Subdue)](https://github.com/lem0nSec/Subdue/blob/main/LICENSE.txt)   ![](https://img.shields.io/badge/python-3.x-yellow)
------------------------------------------------------------------------
Subdue is a Python3 script which aims to provide a <u>quick and easy-to-use solution for subdomain fuzzing</u>. It was born from a need to simplify and speed up the enumeration of virtual hosts in a CTF-like context, as well as to provide an alternative solution to more advanced tools performing general fuzzing operations.




## How it works
------------------------------------------------------------------------
Subdue will fuzz subdomains within a specified domain and using a given wordlist. A positive result is given when the values of 'content bytes' and 'content lines' for a potentially valid subdomain diverge from those of an invalid subdomain obtained using a 15-character random string.
**Bear in mind that Subdue has been written with CTF-like challenges in mind. For this reason, it may not be a suitable tool for real-world engagements. Use it responsibly!!**




## Usage:
------------------------------------------------------------------------
```
./subdue.py -h


     @@@@@  @   @  @@@@@   @@@     @   @  @@@@@
     @      @   @  @    @  @   @   @   @  @ 
     @      @   @  @    @  @    @  @   @  @ 
     @@@@@  @   @  @  @@   @    @  @   @  @@@
         @  @   @  @    @  @    @  @   @  @ 
         @  @   @  @    @  @   @   @   @  @ 
     @@@@@  @@@@@  @@@@@   @@@     @@@@@  @@@@@
    
                                   by Lem0nSec_

usage: subdue_dev.py [-h] -i I -d D -w W [-k] [-t T]

Welcome to Subdue! A compact subdomain fuzzing tool for CTFs

optional arguments:
  -h, --help  show this help message and exit
  -i I        Target IP
  -d D        Target domain
  -w W        Wordlist
  -k          SSL option
  -t T        Number of concurrent threads (default 5)
```
**Example:** `./subdue.py -i 10.10.10.10 -d test.site -w subdomains_example_list.txt -t 10`




## Requirements:
------------------------------------------------------------------------
- Requests: `pip3 install requests`
- Termcolor: `pip3 install termcolor`




## Threading support:
------------------------------------------------------------------
Subdue has recently implemented support for concurrent threads:

![Threads_differences1](https://user-images.githubusercontent.com/98479572/152024171-b15725aa-6b05-4007-b37e-5d267af62345.png)


*Enjoy!!*
