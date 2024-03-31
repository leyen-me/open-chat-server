from .base_prompt import BasePrompt


class VueInterviewerPrompt(BasePrompt):

    def __init__(self):
        super().__init__()
        self.name = "Vue面试官"
        self.code = "vue_interviewer"
        self.system_prompt = """我想让你担任Vue3开发工程师面试官。我将成为候选人，您将向我询问Vue3开发工程师职位的面试问题。我希望你只作为面试官回答。不要一次写出所有的问题。我希望你只对我进行采访。问我问题，等待我的回答。不要写解释。像面试官一样一个一个问我，等我回答。"""