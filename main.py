import requests
import json
import time
import re
import logging
import traceback
import os
import random
import datetime
import utils
import base64


def main(event, context):
    # 初始化日志文件
    utils.initLog('log.txt')
    utils.clearLog()
    savePoint(
        'https://proxies.bihai.cf/vmess/sub?nc=CN&type=vmess,trojan', 'vmess.txt')

    # savePoint(
    #     'https://etproxypool.ga/clash/proxies?nc=CN&speed=30&type=ss', 'ss.txt')

    # savePoint(
    #     'https://etproxypool.ga/clash/proxies?nc=CN&speed=30&type=ssr', 'ssr.txt')

    # savePoint(
    #     'https://etproxypool.ga/clash/proxies?nc=CN&speed=30&type=trojan', 'trojan.txt')


# 获取文章地址


def savePoint(url, name):
    resp = requests.get(url)
    dirs = './subscribe'
    day = time.strftime('%Y.%m.%d', time.localtime(time.time()))
    result = base64.b64encode(resp.text.encode('utf-8'))
    #if 'proxies' in result:
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    with open(dirs + '/' + name, 'w', encoding='utf-8') as f:
        f.write(result)
        print(name+'生成成功')


# 主函数入口
if __name__ == '__main__':
    main("", "")
