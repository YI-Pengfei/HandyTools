"""
百度API图片文字识别
"""
# encoding:utf-8
import requests 
import base64

TOKEN = ""  # 签名
EXPIRES = -1  # 签名过期时间
def get_token():
    """Acess Token获取 
        网址: https://ai.baidu.com/ai-doc/REFERENCE/Ck3dwjgn3
        服务器返回的JSON文本参数如下：
            access_token： 要获取的Access Token；
            expires_in： Access Token的有效期(秒为单位，一般为1个月)；
            其他参数忽略，暂时不用;
        Access Token的有效期为30天（以秒为单位），请您集成时注意在程序中定期请求新的token
    """
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    AK = 'cNhWvLGqpSZzpAMNTU3ibfYx'
    SK = 'GxylATKF5OlV5YyuV749oREFMqpQD71D'
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(AK,SK)
    response = requests.get(host)
    if response:
        token = response.json()['access_token']
        expires = response.json()['expires_in']
        return token, expires

if not (TOKEN and EXPIRES>24*3*3600):  # 有效期在三天以上
    TOKEN, EXPIRES = get_token()



# 通用文字识别 （调用量限制 50000次/天免费）
request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
# 二进制方式打开图片文件
f = open('C:/Users/y1064/Desktop/temp.jpg', 'rb') ######## 
img = base64.b64encode(f.read())

params = {"image":img,
          'access_token':TOKEN}

headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers) # post请求 
if response:
    content = ""
    for item in response.json()['words_result']:
        content+= item["words"]+ "\n"
    