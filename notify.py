
# -*- coding: utf-8 -*-
# @Time    : 2021/4/9 06:30
# @Author  : skywolf627
# @Email   : skywolf627@qq.com

import smtplib
import traceback
import os
import requests
import urllib
import json

# 发送push+通知
def sendPushplus(token):
    try:
        # 发送内容
        data = {
            "token": token,
            "title": "VMESS每日节点",
            "content": readFile_html('./log.txt')
        }
        url = 'http://www.pushplus.plus/send'
        headers = {'Content-Type': 'application/json'}
        body = json.dumps(data).encode(encoding='utf-8')
        resp = requests.post(url, data=body, headers=headers)
        print(resp)
    except Exception as e:
        print('push+通知推送异常，原因为: ' + str(e))
        print(traceback.format_exc())

# 发送wxpusher 群消息
def sendWxPusherByTopic(appToken, topicId):
    try:
        data = {
            "appToken": appToken,
            "content": readFile_html('./log.txt'),
            "summary": "最新VMESS节点",
            "contentType": 1,
            "topicIds":  [topicId],
            "url": "https://fund.lsj8.ltd"
        }
        url = 'http://wxpusher.zjiecode.com/api/send/message'
        headers = {'Content-Type': 'application/json'}
        body = json.dumps(data).encode(encoding='utf-8')
        resp = requests.post(url, data=body, headers=headers)
        print(resp)
    except Exception as e:
        print('wxpusher通知推送异常，原因为: ' + str(e))
        print(traceback.format_exc())



# 返回要推送的通知内容
# 对html的适配要更好
# 增加文件关闭操作
def readFile_html(filepath):
    content = ''
    with open(filepath, "r", encoding='utf-8') as f:
        for line in f.readlines():
            content += line + '<br>'
    return content
