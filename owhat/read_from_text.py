import re

def get_data_from_file():
    data = []
    f = open("data.txt","r")
    for line in f.readlines():
        line = line.strip('\n')
        match = re.match(r'.*id=(.*)&utm.*',line)
        data.append(match.group(1))
    return data

#https://www.owhat.cn/prod/shop/shopdetail?id=128111&utm_source=owhat&utm_medium=copyurl
#https://www.owhat.cn/prod/shop/shopdetail?id=130859&utm_source=owhat&utm_medium=copyurl
#https://www.owhat.cn/prod/shop/shopdetail?id=134185&utm_source=owhat&utm_medium=copyurl
# matchObj = re.match(r'(.*?) are (.*?) .*', line, re.M | re.I)
# print(matchObj.group(1))