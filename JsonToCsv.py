#!/usr/bin/python
# _*_coding:utf-8 _*_
import datetime
import json
import sys
import time

reload(sys)
sys.setdefaultencoding('utf8')

bodystat = {
    "reqStatus": {
        "1": "需求提出",
        "21": "部门审核",
        "22": "分公司办结",
        "31": "需求受理",
        "41": "架构初评",
        "51": "委员会初审",
        "52": "立项中",
        "61": "需求分析",
        "71": "架构设计",
        "81": "需求排期",
        "91": "解决方案阅知",
        "101": "需求评审",
        "111": "业务确认",
        "121": "部门确认",
        "131": "委员会终审",
        "141": "需求实施",
        "151": "需求完成",
        "161": "需求取消",
        "171": "需求暂停",
        "181": "审批中"},
    "reqType": {
        "1": "功能类",
        "2": "配置类",
        "3": "数据提取",
        "5": "新项目类",
        "7": "技术优化类"
    }
}
title = {
    "systemName": "系统名称",
    "systemCode": "系统代码",
    "reqName": "需求名称",
    "reqCode": "需求代码",
    "submitterName": "提交人",
    "reqType": "需求类型",
    "reqStatus": "需求状态",
    "createDate": "创建时间",
    "planRealeaseTime": "计划上线时间",
    "orderStatusStore": "订单状态存储",
    "orderStatus": "订单状态",
    "orderCode": "订单代码",
    "actId": "不知道什么意思",
    "dealMan": "当前处理人"
}


def checkjson(dict1, filepath):
    for masterline in dict1.keys():
        key = masterline.encode('utf-8')
        # print key
        typestr = type(dict1[key])
        if typestr == list:
            listprint(dict1[key], filepath)
        elif typestr == dict:
            checkjson(dict1[key], filepath)


def fileread(filepath):
    result = ""
    for line in open(filepath):
        result = result + line
    try:
        dict1 = json.loads(result)
        checkjson(dict1, filepath)
    except Exception as e:
        print e.message


def listprint(lists, filepath):
    keys1 = set()
    for line in lists:
        for key in line.keys():
            keys1.add(key.encode('utf-8'))

    keys = []
    lines = ""
    for key in keys1:
        keys.append(key)
        if title.has_key(key):
            lines = lines + '"' + title[key.encode('utf-8')] + '",'
        else:
            lines = lines + '"' + key.encode('utf-8') + '",'

    with open(filepath.split('.')[0] + " " + datetime.datetime.now().strftime('%Y%m%d%H%M%S%f') + ".csv", "w") as fo:
        fo.write('\xEF\xBB\xBF')
        fo.write(lines[0:len(lines) - 1] + '\n')
        for line in lists:
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
                if bodystat.has_key(key):
                    if bodystat[key].has_key(value):
                        lines = lines + '"' + bodystat[key][value] + '",'
                    else:
                        lines = lines + '"' + value + '",'
                else:
                    lines = lines + '"' + value + '",'
            # print(lines[0:len(lines) - 1])
            fo.write(lines[0:len(lines) - 1] + '\n')
        print filepath + ' finish'
    fo.close()


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        i = 0
        for name in sys.argv:
            if i != 0:
                print sys.argv[i]
                fileread(sys.argv[i])
            i = i + 1
