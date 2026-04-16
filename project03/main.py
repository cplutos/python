import os
from openai import OpenAI

from project03.ai_model.glm_model import ChatGLMModel
from project03.ai_model.openai_model import OpenAIModel
from project03.utils.argument_utils import ArgumentUtils
from project03.utils.loader_config import LoaderConfig

if __name__ == '__main__':

    os.environ["http_proxy"] = "127.0.0.1:7890"
    os.environ["https_proxy"] = "127.0.0.1:7890"

    # 启动命令中的参数解析和验证,并返回所有参数
    arg_utils = ArgumentUtils()
    args = arg_utils.parse_arg()

    #读取配置文件
    load_config = LoaderConfig(args.config)
    config = load_config.load_config()
    # 模型的名字，先从命令行参数中获取，否则 从配置文件中获取，
    model_name = args.model_name if args.model_name else config['OpenAIModel']['model']
    # api_key
    api_key = args.openai_api_key if args.openai_api_key else config['OpenAIModel']['api_key']
    # 代理地址
    base_url = args.base_url if args.base_url else config['OpenAIModel']['base_url']

    # 初始化模型对象
    if args.model_type == 'OpenAIModel':
        model = OpenAIModel(model_name,api_key,base_url)
    else:
        model = ChatGLMModel()

