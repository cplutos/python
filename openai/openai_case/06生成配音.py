import os
from openai import OpenAI

os.environ['http_proxy']='127.0.0.1:7890'
os.environ['https_proxy']='127.0.0.1:7890'

API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = "https://api.zhizengzeng.com/v1"
client = OpenAI(api_key=API_KEY,base_url=BASE_URL)
#
# with client.audio.speech.with_streaming_response.create(
#     model='tts-1',
#     voice='onyx',
#     input='二营长！你他娘的意大利炮呢?给我拉来！'
# ) as resp:
#     resp.stream_to_file('./audio/test2.mp3')

with client.audio.speech.with_streaming_response.create(
    model='tts-1',
    voice='nova',
    response_format='wav',
    speed=1.5,
    input='''美国《华尔街日报》星期二（4月14日）报道，法国总统马克龙透露，这项计划旨在开展一项不包括“交战方”的国际防御任务。他所指的交战方即美国、以色列和伊朗。熟悉计划的欧洲外交人士也透露，欧洲舰艇不会接受美军指挥。
报道说，这项计划有三大目标：建立后勤机制，确保目前滞留霍尔木兹海峡内的数百艘船能够离开；开展大规模扫雷行动，为更多船只安全通行开辟更宽阔的航道；通过护卫舰和驱逐舰提供常态化军事护航与监视，让航运公司确信穿越海峡是安全的。'''
) as resp:
    resp.stream_to_file('./audio/test3.wav')

