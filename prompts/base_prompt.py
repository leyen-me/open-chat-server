
class BasePrompt:

    def __init__(self):
        self.name = ""
        self.code = ""
        self.system_prompt = ""
        self.question_prompt = None
        self.code_auto_run = 0
