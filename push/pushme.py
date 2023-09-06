# -*- coding: utf-8 -*-

import requests

import json

  
  

def getKey(data):

    config = data['config']

    if len(config['pushMe_key']) == 0:

        return None

    return (config['module'], config['pushMe_key'], config['title'], config['template'])

  
  

def push(title, mdmsg, textmsg, config):

    msg = mdmsg

    token = config['pushMe_key']

    # title = config['title']

    template = config['template']

    if not config['pushMe_key']:

        print("PushMe 服务的 PUSHME_KEY 未设置!!\n取消推送")

        return

    print("PushMe 服务启动")

  

    url = f'https://push.i-i.me/?push_key={config["pushMe_key"]}'

    data = {

        "title": title,

        "content": msg,

    }

    response = requests.post(url, data=data)

  

    if response.status_code == 200 and response.text == "success":

        print("PushMe 推送成功！")

    else:

        print(f"PushMe 推送失败！{response.status_code} {response.text}")
