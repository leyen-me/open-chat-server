from .base_prompt import BasePrompt


class TestPrompt(BasePrompt):

    def __init__(self):
        super().__init__()
        self.name = "测试"
        self.code = "test"
        self.system_prompt = """
        test
        """