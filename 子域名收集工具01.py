# coding=utf-8
#公共模块
import requests.packages.urllib3

#屏蔽警告
requests.packages.urllib3.disable_warnings()
import requests
import re
from config import *
import json


#get请求模块
def get(url):
    """
    get 请求
    :param url:需要访问的地址
    :return:
    """
    from fake_useragent import UserAgent
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random
    }
    try:
        #获取响应
        response01 = requests.get(url, headers=headers, timeout=10)
        if response01.status_code == 200:
            return "1"
    except Exception as e:
        print(e)


#post请求模块
def post(url, data):
    """
    post 请求
    :param url: 需要访问的地址
    :param data: 传递的参数
    :return:
    """
    from fake_useragent import UserAgent
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random
    }
    try:
        #获取响应
        response02 = requests.post(url, data=data, headers=headers, timeout=10)
        if response02.status_code == 200:
            return response02.text
    except Exception as e:
        print(e)


#判断是否为有效域名
#Python函数使用正则表达式编译了一个模式，用于验证字符串是否符合电子邮件地址的格式要求
#([a-zA-Z]{1}) 匹配一个字母；
#([a-zA-Z]{1}[a-zA-Z]{1}) 匹配两个连续的字母；
#([a-zA-Z]{1}[0-9]{1}) 匹配一个字母后跟一个数字；
#([0-9]{1}[a-zA-Z]{1}) 匹配一个数字后跟一个字母,
#([a-zA-Z0-9][-_.a-zA-Z0-9]{0,61}[a-zA-Z0-9]) 匹配一个字母或数字，后跟任意数量的连字符、下划线、点号或小写字母，再后跟一个字母或数字；
#. 匹配一个点号；
#([a-zA-Z]{2,13}|[a-zA-Z0-9-]{2,30}.[a-zA-Z]{2,3}) 匹配两个到十三个字母的顶级域名，或者匹配两个到三十个字母、数字或连字符的域名后跟一个点号和两个到三个字母的顶级域名；
#$ 表示匹配字符串的结尾
def domain(url):
    """
    判断是否是有效域名
    :param domain:
    :return:
    """
    pattern = re.compile(
        r'^(([a-zA-Z]{1})|([a-zA-Z]{1}[a-zA-Z]{1})|'
        r'([a-zA-Z]{1}[0-9]{1})|([0-9]{1}[a-zA-Z]{1})|'
        r'([a-zA-Z0-9][-_.a-zA-Z0-9]{0,61}[a-zA-Z0-9])).'
        r'([a-zA-Z]{2,13}|[a-zA-Z0-9-]{2,30}.[a-zA-Z]{2,3})$'
        )
    if re.match(pattern, url):  #如果pattern与url完全匹配，则返回真，否则返回假
        return url
    else:
        return url

#把域名写入文件
def write_file(url):
    """
    把域名写入文件
    :param url:
    :return:
    """
    with open('domain.txt', 'w') as f:
        f.write(url + '\n')


if __name__ == '__main__':
    url = input('请输入要判断的域名: ')
    domain(url)
    print(write_file(get(domain(url))))








