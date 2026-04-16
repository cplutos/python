import argparse

class ArgumentUtils:
    def __init__(self):
        """
        命令行参数解析
        """
        self.parser = argparse.ArgumentParser(description='书籍自动翻译器')
        self.parser.add_argument('--config',type=str,default='config.yaml',help='项目整体配置文件')
        self.parser.add_argument('--model_type',type=str,required=True,default='OpenAIModel',choices=['CLMModel','OpenAIModel'],help='选择OpenAI还是GLM模型')
        self.parser.add_argument('--timeout',type=int,help='API接口请求的超时时间')
        self.parser.add_argument('--openai_model',type=str,help='OpenAI中所使用的模型名字')
        self.parser.add_argument('--open_api_key',type=str,help='OpenAI中的api_key')
        self.parser.add_argument('--book',type=str,help='需要翻译的书籍所属的文件路径')
        self.parser.add_argument('--file_format',type=str,help='翻译之后生成的文件格式')
        self.parser.add_argument('--base_url',type=str,help='代理地址，为空时使用OpenAI官网地址')
    def parse_arg(self):
        """
        解析和验证命令行参数
        :return:
        """
        # 解析参数
        args = self.parser.parse_args()
        # 参数验证还可以传更多
        if args.model_type == 'OpenAIModel' and not args.openai_model and not args.openai_api_key:
            self.parser.error('当选择OpenAI后，--openai_model和--openai_api_key参数，必须要传！')
