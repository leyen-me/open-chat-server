from .base_prompt import BasePrompt


class DefaultPrompt(BasePrompt):

    def __init__(self):
        super().__init__()
        self.name = "通用"
        self.code = "default"
        self.system_prompt = "默认请使用中文和Markdown格式与我沟通。我的第一句话是: 你好!"