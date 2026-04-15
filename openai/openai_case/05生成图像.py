import base64
import os
import requests
from openai import OpenAI

os.environ['http_proxy']='127.0.0.1:7890'
os.environ['https_proxy']='127.0.0.1:7890'

API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = "https://api.zhizengzeng.com/v1"
client = OpenAI(api_key=API_KEY,base_url=BASE_URL)

# resp = client.images.generate(
#     model='dall-e-3',
#     prompt='一只可爱的哈士奇犬',
#     size='1024x1024',
#     quality='standard',
#     n=1 #生成数量,当前模型仅支持一张
# )
# print(resp)
# print(resp.data[0].url)


# resp = client.images.generate(
#     model='dall-e-3',
#     prompt='一只可爱的哈士奇犬,在海滩上奔跑',
#     size='1024x1024',
#     quality='hd',
#     n=1, #生成数量,当前模型仅支持一张
#     style='natural',
#     response_format='b64_json'
# )
#
# print(resp)
# b64_img = resp.data[0].b64_json
#
# with open('./images/output01.jpg', 'wb') as f:
#     f.write(base64.b64decode(b64_img))

resp = client.images.generate(
    model='dall-e-3',
    prompt='生成一位美女在海边晒日光浴',
    size='1024x1024',
    quality='hd',
    n=1, #生成数量,当前模型仅支持一张
    style='vivid',
    response_format='b64_json'
)

# print(resp)
b64_img = resp.data[0].b64_json

with open('./images/output03.jpg', 'wb') as f:
    f.write(base64.b64decode(b64_img))