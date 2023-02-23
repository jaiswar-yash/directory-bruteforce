import requests
import sys
import argparse

parser = argparse.ArgumentParser(description="Directory Brute-forcing")
parser.add_argument("--url", type = str, help = "The Target URL", required = True)
parser.add_argument("--wordlist",type = str, help = "The path of the wordlist", required = True)

args = parser.parse_args()

url = args.url
wordlist = args.wordlist

def write(word):
    f1 = open("write1.txt","a")
    f1.write(word + "\n")

read = open(wordlist, "r+",buffering=10000,encoding='utf-8')

while True:
    word = read.readline().strip()
    if not word:
        break
    surl = url+word

    try:
        response = requests.get(surl)
        if(response.status_code == 200):
            print("[+] found : -", surl)
        else:
            print("[-] Not Found : - ", surl)
    except requests.exceptions.RequestException as e:
        print("Error: write URL in http://website.com/ format \n\n", e)
        break

