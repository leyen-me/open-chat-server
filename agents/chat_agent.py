from .base_agent import BaseAgent
from qwen_agent.agents import Assistant
from constants.base_client import BASE_MODEL, BASE_URL, API_KEY


class ChatAgent(BaseAgent):

    name = "chat_agent"

    def __init__(self):
        super().__init__()

    def run(self, messages, **kwargs):
        llm = {
            'model': BASE_MODEL,
            'model_server': BASE_URL,
            'api_key': API_KEY,
        }
        self.agent = Assistant(llm=llm)
        for rsp in self.agent.run(messages=messages):
            yield rsp
        messages.extend(rsp)
