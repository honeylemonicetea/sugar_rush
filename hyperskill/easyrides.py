import json
import re

data = input()
jstring = json.loads(data)
#empty containers and ctrs
validation = dict()
ids = set()
street_names = set()
stop_type = []
buses = dict()
stop_groups = {"S":[], "O": [], "F":[]}
transfers = dict()
#stage5
buslines = set()
# stage 6
ondemands = []
others = []

err = 0
ferr = 0

#non-empty containers
mistakes = {"bus_id": 0, "stop_id": 0, "stop_name": 0, "next_stop": 0, "stop_type": 0, "a_time": 0}
suffixes = ["Road", "Avenue", 'Boulevard', "Street"]
stop_types = ["S", "", "F"]
format_errors = {"stop_name": 0, "stop_type": 0, "a_time": 0}

#A transfer stop is a stop shared by at least two bus lines.

def transfer_stops(jstring):
    global transfers
    #initialize
    for dict in jstring:
        stopn = dict.get("stop_name")
        transfers[stopn] = 0
    for dict in jstring:
        stopn = dict.get("stop_name")
        transfers[stopn] += 1
    return transfers

def stops_grouped(jstring, trans_dict):
    stps = set()
    global stop_groups
    for type in stop_types:
        if type != "":
            for dict in jstring:
                for key in dict.items():
                    typ = dict.get("stop_type")
                    if type == typ:
                        stop = dict.get("stop_name")
                        stps.add(stop)
        else:
            for key, val in trans_dict.items():
                if val > 1:
                    stps.add(key)

        if type == "S":
            word = "Start"
        elif type == "":
            word = "Transfer"
        elif type == "F":
            word = "Finish"
        print(f"{word} stops: {len(stps)} {sorted(list(stps))}")
        stps.clear()

def bus_ids(dic):
    id_val = dic.get("bus_id")
    ids.add(id_val)

def format_checker(jstring):  # stop_name, stop_type, a_time
    name_template = "[A-Z].*"
    time_templ = "[0-2][0-9]:[0-5][0-9]"
    global ferr
    for dic in jstring:
        for key in dic.keys():
            val = dic.get(key)
            if key == "stop_name":
                test_split = val.split(" ")
                if len(test_split) > 1:
                    result1 = bool(re.match(name_template, val))
                    result2 = test_split[-1] in suffixes
                    res = result1 and result2
                    if res == False:
                        format_errors[key] += 1
                        ferr += 1
                else:
                    format_errors[key] += 1
                    ferr += 1

            elif key == "stop_type":
                if val in stop_types or val == "":
                    res = True
                else:
                    format_errors[key] += 1
                    ferr += 1
            elif key == "a_time":
                if len(val) == 5:
                    res = bool(re.match(time_templ, val))
                    if res == False:
                        format_errors[key] += 1
                        ferr += 1
                else:
                    format_errors[key] += 1
                    ferr += 1

def type_err(jstring):
    global err
    for dic in jstring:
        for key in dic.keys():
            val = dic.get(key)
            typo = type(val)
            if val != "":
                if typo != int:
                    if key == "bus_id" or key == "stop_id" or key == "next_stop":
                        mistakes[key] += 1
                        err += 1
                elif typo != str:
                    if key == 'stop_name' or key == "a_time":
                        mistakes[key] += 1
                        err += 1
                    elif key == "stop_type":
                        if typo != str or len(val) > 1:
                            mistakes[key] += 1
                            err += 1
            elif val == "" and key != "stop_type":
                mistakes[key] += 1
                err += 1

def stops_id(jstring):
    # find all ids
    for dic in jstring:
        bus_ids(dic)
    for id in ids:
        for dic in jstring:
            if id == dic.get("bus_id"):
                street = dic.get("stop_name")
                street_names.add(street)
        validation[id] = len(street_names)
        street_names.clear()

def stop_checker(jstring):
    for item in jstring:
        bus_ids(item)
    for id in ids:
        for item in jstring:
            if id == item.get("bus_id"):
                stop = item.get("stop_type")
                stop_type.append(stop)
        if stop_type[0] == "S" and stop_type[-1] == 'F':
            buses[id] = stop_type
            stop_type.clear()
        else:
            print(f"There is no start or end stop for the line: {id}.")
            return False

def time_check(jstring):
    global buslines
    #create a set of bus ids, iterate
    current_time = "00:00"
    issues = 0
    for dict in jstring:
        id = dict.get("bus_id")
        buslines.add(id)
    #check lines one by one
    for line in buslines:
        for dict in jstring:
            ln = dict.get("bus_id")
            if ln == line:
                time = dict.get("a_time")
                station = dict.get("stop_name")
                if current_time < time:
                    current_time = time
                else:
                    print(f"bus_id line {line}: wrong time on station {station}")
                    issues += 1
        current_time = "00:00"
    if issues == 0:
        return False
    buslines.clear()


def on_demand(jstring):
    global ondemands
    global others
    wrong = []
    for dict in jstring:
        typo = dict.get("stop_type")
        name = dict.get("stop_name")
        if typo == "O":
            ondemands.append(name)
        else:
            others.append(name)
    for item in ondemands:
        if item in others:
            wrong.append(item)
    if len(wrong) == 0:
        return False
    else:
        return wrong


#format_checker(jstring)
#stops_id(jstring)
"""
r = stop_checker(jstring)
if r != False:
    trans_dict = transfer_stops(jstring)
    stops_grouped(jstring, trans_dict)
"""
"""print(f"Type and required field validation: {err} errors")
for key, value in mistakes.items():
    print(f"{key}: {value}")"""

"""print(f"Format validation: {ferr} errors")
for key, value in format_errors.items():
    print(f"{key}: {value}")"""

"""print("Line names and number of stops:")
for key, value in validation.items():
    print(f"bus_id: {key}, stops{value}")"""


"""print("Arrival time test:")
k = time_check(jstring)
if k == False:
    print("OK")"""
print("On demand stops test:")
k = on_demand(jstring)
if k == False:
    print("OK")
else:
    print(f"Wrong stop type: {sorted(k)}")
