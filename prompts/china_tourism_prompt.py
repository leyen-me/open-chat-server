from .base_prompt import BasePrompt


class ChinaTourismPrompt(BasePrompt):

    def __init__(self):
        super().__init__()
        self.name = "中国旅游指南"
        self.code = "china_tourism"
        self.system_prompt = """我想让你做一个旅游指南。我会把我的位置写给你，你会推荐一个靠近我的位置的地方。在某些情况下，我还会告诉您我将访问的地方类型。您还会向我推荐靠近我的第一个位置的类似类型的地方。"""