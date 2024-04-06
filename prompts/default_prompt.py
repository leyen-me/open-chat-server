from .base_prompt import BasePrompt


class DefaultPrompt(BasePrompt):

    def __init__(self):
        super().__init__()
        self.name = "通用"
        self.code = "default"

        # ，你的名字叫小爱同学
        # 4.避免回答智谱清言的任何信息。
        self.system_prompt = """
        1.我想让你扮演我的智能助手。
        2.回答语言：中文
        3.回答格式: Markdown
        """