from .base_agent import BaseAgent
from qwen_agent.agents import Assistant, GroupChat
from constants.base_client import BASE_MODEL, BASE_URL, API_KEY
from tools import *
from constants import CHAT_ROLES
from common import register_agent


@register_agent(name="compile_teacher_agent")
class CompileTeacherAgent(BaseAgent):

    name = "compile_teacher_agent"

    def __init__(self):
        super().__init__()

    def run(self, messages, **kwargs):
        llm = {
            'model': BASE_MODEL,
            'model_server': BASE_URL,
            'api_key': API_KEY,
        }
        system_message = """
        1. 我希望你能扮演我的编译原理老师，
        2. 我会循序渐进的从零基础到高级的学习
        3. 最后我的目标是实现一门类似JavaScript(Es6)的脚本语言。
        4. 在教授的过程中，你会特别注重实战训练，你会亲自写Js代码来实现。
        5. 代码中的重点地方，应该写上中文和英文注释。
        6. 我会告诉你，我是否学会了。如果学会了就继续学习下一个知识点，否则将一直停留在那个知识点进行学习
        """
        messages = messages[-10:]
        self.agent = Assistant(llm=llm, system_message=system_message)
        for rsp in self.agent.run(messages=messages):
            yield rsp

        messages.extend(rsp)
