from .base_agent import BaseAgent
from qwen_agent.agents import Assistant
from constants.base_client import BASE_MODEL, BASE_URL, API_KEY


class IotAgent(BaseAgent):

    name = "iot_agent"

    def __init__(self):
        super().__init__()

    def run(self, messages, **kwargs):
        llm = {
            'model': BASE_MODEL,
            'model_server': BASE_URL,
            'api_key': API_KEY,
        }
        temp = """
        我希望您能扮演一个物联网工程师。
        
        以下是默认设备的信息:
        DEVICE_ADDRESS: 0
        DEVICE_COUNT: 10
        DEVICE_PROTOCOL: TCP
        DEVICE_HOST: 192.168.31.120
        DEVICE_PORT: 502
        DEVICE_UNIT: 1
        """

        # DATABASE_HOST: 192.168.31.120
        # DATABASE_PORT: 3307
        # DATABASE_USER: root
        # DATABASE_PASSWORD: pdBGKGjRyX3Jb2Hn
        # DATABASE_NAME: iot-mysql
        self.agent = Assistant(llm=llm, function_list=[
            'get_device_tool', 'code_interpreter'])
        for rsp in self.agent.run(messages=messages):
            yield rsp
        messages.extend(rsp)