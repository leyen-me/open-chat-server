
class BasePrompt:

    def __init__(self):
        """
        给预训练好的大语言模型一个提示，以帮助模型更好的理解人类的问题
        Provide a prompt to a pre-trained large language model to help the model better understand human questions.
        
        https://github.com/PlexPt/awesome-chatgpt-prompts-zh/blob/main/prompts-zh.json
        """

        self.name = ""
        self.code = ""
        self.system_prompt = ""
        self.question_prompt = None
        self.code_auto_run = 0
        self.context_length = None