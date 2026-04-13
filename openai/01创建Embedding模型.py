import pandas as pd
import os
from openai import OpenAI
import tiktoken

os.environ['http_proxy'] = '127.0.0.1:7890'
os.environ['https_proxy'] = '127.0.0.1:7890'
# 需要的依赖库
# pip install tiktoken openai pandas matplotlib plotly scikit-learn numpy
# 运行可能报错是因为pandas中的numpy和其他环境中的numpy冲突,卸载重装pandas即可
# pip uninstall numpy scipy pandas
# pip install numpy scipy pandas

"""
该数据集包含截至2012年10月份用户在亚马逊上留下共计586454条美食评论
"""

# 1.首选读取数据，预处理数据
df = pd.read_csv('datas/fine_food_reviews_1k.csv', index_col=0)

df = df[['Time', 'ProductId', 'UserId', 'Score', 'Summary', 'Text']]

# 删除cvs中缺失的数据，NaN，NaT的数据
df = df.dropna()

# 把Summary，Text两个字段合并
df['combined'] = "Title:" + df.Summary.str.strip() + ";Content:" + df.Text.str.strip()

# print(df.head(2))

# 2.生成Embedding之后的向量空间，并且保存
# 建议使用官方推荐的第二代嵌入模型：text-embedding-ada-002
embedding_mode = "text-embedding-ada-002"

# 对文本进行处理的分词器
tokenizer_name = 'cl100k_base'
max_tokens = 8191
top_n = 1000
df = df.sort_values('Time')
df.drop("Time", axis=1, inplace=True)

# 创建一个分词器
tokenizer = tiktoken.get_encoding(encoding_name=tokenizer_name)

# 控制输入数据的token数量
# 计算token数量
df['count_token'] = df.combined.apply(lambda x: len(tokenizer.encode(x)))

# 判断token数量不能超过官方的阈值：8191,超过了就不要，tail是截断函数
df = df[df.count_token <= max_tokens].tail(top_n)

print(len(df))

# 初始化openai的客户端
API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=API_KEY,base_url="https://api.zhizengzeng.com/v1")

def embedding_text(text, model=embedding_mode):
    """
    通过OpenAI的Embedding模型处理文本数据
    :param text: 需要处理的文本
    :param model:
    :return:
    """

    resp = client.embeddings.create(input=text, model=model)
    return resp.data[0].embedding




# 使用Embedding处理文本
df['embedding'] = df.combined.apply(embedding_text)

df.to_csv('datas/embedding_output_1k.csv')

print(df['embedding'][0])
