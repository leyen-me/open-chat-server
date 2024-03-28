from .base_prompt import BasePrompt


class DefaultPrompt(BasePrompt):

    def __init__(self):
        super().__init__()
        self.name = "通用"
        self.code = "default"
        self.system_prompt = "我想让你充当我的朋友，默认请使用中文与我沟通"