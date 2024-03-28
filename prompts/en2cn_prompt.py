from .base_prompt import BasePrompt


class En2CnPrompt(BasePrompt):

    def __init__(self):
        super().__init__()
        self.name = "英译汉"
        self.code = "en2cn"
        self.system_prompt = "我想让你充当翻译员"
        self.question_prompt = """请将'{}'翻译成中文, 仅仅只回答翻译后的结果。"""