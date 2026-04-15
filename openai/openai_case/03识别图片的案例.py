import base64
import os
from openai import OpenAI
import requests

os.environ['http_proxy']='127.0.0.1:7890'
os.environ['https_proxy']='127.0.0.1:7890'

API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = "https://api.zhizengzeng.com/v1"
client = OpenAI(api_key=API_KEY,base_url=BASE_URL)

# 图片 URL（可以是任何公开图片地址）
image_url_http = "https://img.freepik.com/premium-photo/pretty-woman-hairstyle-fun-posing-cosmetics-fashion-isolated-background-person_1048944-28429422.jpg?size=626&ext=jpg"

# 1. 下载图片
resp_img = requests.get(image_url_http, timeout=30)
resp_img.raise_for_status()

# 2. 获取 MIME 类型（优先使用响应头，也可根据内容推断）
content_type = resp_img.headers.get('Content-Type', 'image/jpeg')
# 如果 Content-Type 缺失或不可靠，可简单处理：根据 URL 后缀或默认 jpeg
if 'image' not in content_type:
    # 兜底：常见后缀
    if image_url_http.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
        ext = image_url_http.split('.')[-1].lower()
        if ext in ('jpg', 'jpeg'): content_type = 'image/jpeg'
        elif ext == 'png': content_type = 'image/png'
        elif ext == 'gif': content_type = 'image/gif'
        elif ext == 'webp': content_type = 'image/webp'
        else: content_type = 'image/jpeg'  # 默认
    else:
        content_type = 'image/jpeg'

# 3. Base64 编码
image_base64 = base64.b64encode(resp_img.content).decode('utf-8')
data_url = f"data:{content_type};base64,{image_base64}"


# 处理在线图片
resp = client.chat.completions.create(
    model='gpt-4-turbo',
    messages=[
        {
            'role': 'user',
            'content': [
                {'type': 'text', 'text': '介绍一下这张图片'},
                {'type': 'image_url',
                 'image_url': {
                     'url':data_url
                 }
                }
            ]
        }
    ],
    max_tokens=400
)

print(resp.choices[0].message.content)