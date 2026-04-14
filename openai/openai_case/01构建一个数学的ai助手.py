import os
from openai import OpenAI

os.environ["http_proxy"]="http://127.0.0.1:7890"
os.environ["https_proxy"]="http://127.0.0.1:7890"

API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = "https://api.zhizengzeng.com/v1"
client = OpenAI(api_key=API_KEY,base_url=BASE_URL)

# 第一步
assistant = client.beta.assistants.create(
    name='Lao Chen',
    instructions='你是一个个人数学辅导老师。这个助手能解答数学问题和数学计算。',
    tools=[{'type':'code_interpreter'}], #指定的工具
    model='gpt-4o'
)

# 第二步：创建线程
thread = client.beta.threads.create()

# 第三步：
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role='user',
    content='请帮我解一个方程：3x + 2x + 8 = 5'
)

# 第四步：
# 1.等待处理完成后，在得到所有结果
# run = client.beta.threads.runs.create_and_poll(
#     thread_id=thread.id,
#     assistant_id=assistant.id,
#     instructions='请用“老陈”来称呼用户，并且用户拥有高级用户权限。'
# )
#
# print('run的状态为：',run.status)
# if run.status == 'completed':
#     # 输出最终结果
#     messages = client.beta.threads.messages.list(thread_id=thread.id)
#     print('\n消息：')
#     for msg in messages:
#         print(f'Role:{msg.role.capitalize()}')
#         # print(msg)
#         print(msg.content[0].text.value + '\n')

# 2.采用流的方式来得到结果：逐个token返回
stream = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
    instructions='请用“老陈”来称呼用户，并且用户拥有高级用户权限。',
    stream=True # 采用持续的流方式来返回结果
)

# 遍历流中的事件
for event in stream:
    # 返回的每一个token都是一个json对象
    print(event.model_dump_json(indent=2,exclude_unset=True))

client.beta.threads.delete(thread_id=thread.id)
client.beta.assistants.delete(assistant_id=assistant.id)

