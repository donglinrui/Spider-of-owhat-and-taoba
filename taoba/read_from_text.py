import re

def get_data_from_file():
    data = []
    f = open("data.txt","r")
    for line in f.readlines():
        line = line.strip('\n')
        match = re.match(r'.*id=(.*)',line)
        data.append(match.group(1))
    return data

# line = "https://www.taoba.club/#/pages/idols/detail?id=10109"
#
# matchObj = re.match(r'(.*?) are (.*?) .*', line, re.M | re.I)
# print(matchObj.group(1))