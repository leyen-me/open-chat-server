from .base_agent import BaseAgent
from qwen_agent.agents import Assistant
from constants.base_client import BASE_MODEL, BASE_URL, API_KEY
from constants import CHAT_ROLES
from tools import *


class ResumeAgent(BaseAgent):

    name = "resume_agent"

    def __init__(self):
        super().__init__()

    def run(self, messages, **kwargs):
        llm = {
            'model': BASE_MODEL,
            'model_server': BASE_URL,
            'api_key': API_KEY,
        }
        messages.append({
            "role": CHAT_ROLES.USER.value,
            "content": "请使用中文给上述对话起一个 15 个字以内的标题, 不要任何注释",
        })
        self.tool_agent = Assistant(llm=llm)
        for rsp in self.tool_agent.run(messages=messages):
            yield rsp
        messages.extend(rsp)
