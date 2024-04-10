from .base_agent import BaseAgent
from qwen_agent.agents import Assistant
from constants.base_client import BASE_MODEL, BASE_URL, API_KEY
from tools import *
from common import register_agent


@register_agent(name="common_agent")
class CommonAgent(BaseAgent):

    name = "common_agent"

    def __init__(self):
        super().__init__()

    def run(self, messages, **kwargs):
        llm = {
            'model': BASE_MODEL,
            'model_server': BASE_URL,
            'api_key': API_KEY,
        }

        self.tool_agent = Assistant(llm=llm, function_list=[
                                    'amap_weather', 'code_interpreter'])
        for rsp in self.tool_agent.run(messages=messages):
            yield rsp
        messages.extend(rsp)
