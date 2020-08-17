import sys
import os
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style
args = sys.argv
headers = {'user-agent': 'Mozilla/5.0'}
if not os.path.exists(args[1]):
    os.mkdir(args[1])
pages = []
path = []
history = []
url = []
tags = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li']
while True:
    page_request = input()
    if page_request == 'exit':
        break
    elif page_request == "back":
        try:
            history.pop()
            a = history.pop()
            path.append(args[1])
            path.append("/")
            ctr = a.count(".")
            if ctr == 2:
                star = a.find(".")
                dot = a.find(".", star+1)
            elif ctr==1:
                dot= a.find(".")
            shorter = a.replace(a[dot:], "")
            path.append(shorter)
            path.append(".txt")
            pth = "".join(path)
            try:
                with open(pth, "r") as p:
                    r = p.read()
                    print(r)
            except Exception:
                pass
            history.append(a)
            path.clear()
        except IndexError:
            pass
    elif "." not in page_request and page_request not in pages:
        print("Error: Incorrect URL")
        continue
    elif "." not in page_request and page_request in pages:
        history.append(page_request)
        path.append(args[1])
        path.append("/")
        ctr = page_request.count(".")
        if ctr == 2:
            star = page_request.find(".")
            dot = page_request.find(".", star + 1)
        elif ctr == 1:
            dot = page_request.find(".")
        shorter = page_request.replace(page_request[dot:], "")
        path.append(shorter)
        path.append(".txt")
        pth = "".join(path)
        try:
            with open(pth, "r") as p:
                r = p.read()
                print(r)
        except Exception:
            pass
        history.append(page_request)
        path.clear()
    else:
        pages.append(page_request)
        history.append(page_request)
        path.append(args[1])
        path.append("/")
        ctr = page_request.count(".")
        if ctr == 2:
            star = page_request.find(".")
            dot = page_request.find(".", star + 1)
        elif ctr == 1:
            dot = page_request.find(".")
        shorter = page_request.replace(page_request[dot:], "")
        path.append(shorter)
        path.append(".txt")
        pth = "".join(path)
        if "https://" not in page_request:
            url.append("https://")
        url.append(page_request)
        url_ = "".join(url)
        with open(pth, "w") as webpage:
            r = requests.get(url_, headers=headers)
            soup = BeautifulSoup(r.content, "html.parser")
            cont = soup.find_all(tags)
            lnks = soup.find_all("a")
            for i in range(len(lnks)):
                lnks[i] = lnks[i].text
            for element in cont:
                if element.text in lnks:
                    print(Fore.BLUE + element.text)
                else:
                    print(Style.RESET_ALL + element.text)
            for line in cont:
                webpage.write(line.text)
        path.clear()
        url.clear()
