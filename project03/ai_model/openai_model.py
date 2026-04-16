from openai import OpenAI

from project03.ai_model.model import Model


class OpenAIModel(Model):

    def __init__(self, model: str, api_key: str, base_url: str):
        """
        调用OpenAI需要的参数
        :param model: 调用模型名称
        :param api_key: key
        :param base_url: 代理地址，为空时调用OpenAI官方api地址
        """
        self.model = model
        self.api_key = api_key
        self.base_url = base_url
        if not base_url:
            self.client = OpenAI(api_key=self.api_key)
        else:
            self.client = OpenAI(api_key=self.api_key,base_url=self.base_url)


    def request_model(self, prompt):
        pass