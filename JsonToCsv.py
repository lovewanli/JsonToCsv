#!/usr/bin/python
# _*_coding:utf-8 _*_
import json
import sys
import time

reload(sys)
sys.setdefaultencoding('utf8')


def fileread(filepath):
    result = ""
    for line in open(filepath):
        result = result + line
    dict1 = json.loads(result)
    for masterline in dict1.keys():
        key = masterline.encode('utf-8')
        typestr = type(dict1[key])
        if typestr == list:
            listprint(dict1[key], )
        elif typestr == dict:
            for masterline1 in dict1[key].keys():
                key1 = masterline1.encode('utf-8')
                if type(dict1[key][key1]) == list:
                    listprint(dict1[key][key1], filepath)


def listprint(lists, filepath):
    with open(filepath + ".csv", "w") as fo:
        fo.write('\xEF\xBB\xBF')
        keys = []
        for line in lists:
            if len(keys) == 0:
                lines = ''
                for key in line.keys():
                    keys.append(key.encode('utf-8'))
                    lines = lines + '"' + key.encode('utf-8') + '",'
                print(lines[0:len(lines) - 1])
                fo.write(lines[0:len(lines) - 1]+'\n')
            else:
                lines = ''
                for key in keys:
                    value = 'NULL'
                    if line.has_key(key):
                        value = str(line[key])
                        if value.find('"'):
                            value.replace('"', '""')
                        valuelength = len(value)
                    if value.isdigit():
                        if valuelength == 10:
                            try:
                                value = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(value)))
                            except Exception as e:
                                pass
                        if valuelength == 13:
                            try:
                                value = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(value) / 1000))
                            except Exception as e:
                                pass
                    lines = lines + '"' + value + '",'
                print(lines[0:len(lines) - 1])
                fo.write(lines[0:len(lines) - 1]+'\n')
        print ''
    fo.close()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        fileread(sys.argv[1])
