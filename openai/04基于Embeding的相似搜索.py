import ast

import pandas as pd
import numpy as np
from openai import OpenAI
import os

API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=API_KEY,base_url="https://api.zhizengzeng.com/v1")
df = pd.read_csv('datas/embedding_output_1k.csv')

# 把str转成矩阵
df['embedding_vec'] = df['embedding'].apply(ast.literal_eval)


def embedding_text(text, model="text-embedding-ada-002"):
    """
    通过OpenAI的Embedding模型处理文本数据
    :param text: 需要处理的文本
    :param model:
    :return:
    """
    resp = client.embeddings.create(input=text, model=model)
    return resp.data[0].embedding


# 在向量空间中，语义相似的词或者文本单位，距离是相近的

def cosine_distance(a, b):
    """
    计算两个向量之间的余弦距离
    :param a:
    :param b:
    :return:
    """
    # 得到这两个向量之间的夹角余弦值，如果余弦相似度接近于1，则表示这两个向量非常相似；接近于-1，表示他们方向相反
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def search_by_word(df, work_key, n_result=3, print_flag=True):
    """
    根据指定的关键词（句子），去向量空间中进行相似搜索
    :param df: 已经Embedding之后的向量空间
    :param work_key:
    :param n_result: 返回结果中的数量
    :param print_flag: 是否打印
    :return:
    """
    # 把关键词向量化
    word_embedding = embedding_text(work_key)

    # 计算相似度
    df['similarity'] = df.embedding_vec.apply(lambda x: cosine_distance(x, word_embedding))

    res = (
        df.sort_values('similarity',ascending=False)
        .head(n_result)
        .combined.str.replace("Title:","")
        .str.replace(";Content:",';')
    )

    if print_flag:
        for r in res:
            print(r)
            print()
    return res

if __name__ == '__main__':
    search_by_word(df, 'delicious beans')