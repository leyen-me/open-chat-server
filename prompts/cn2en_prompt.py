from .base_prompt import BasePrompt


class Cn2EnPrompt(BasePrompt):

    def __init__(self):
        super().__init__()
        self.name = "汉译英"
        self.code = "cn2en"
        self.system_prompt = "我想让你充当翻译员"
        self.question_prompt = """请将'{}'翻译成英语, 仅仅只回答翻译后的结果。"""
