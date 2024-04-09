import json
from qwen_agent.tools.base import BaseTool, register_tool


@register_tool("get_current_weather")
class GetCurrentWeatherTool(BaseTool):

    # 描述
    description = "Get the current weather in a given location"
    
    # 参数
    parameters = [
        {
            'name': 'location',
            'type': 'string',
            'description': 'The city and state, e.g. San Francisco, CA',
            'required': True
        }
    ]
    
    def call(self, params: str, **kwargs):
        # prompt = json5.loads(params)['prompt']
        # prompt = urllib.parse.quote(prompt)
        return json.dumps({
            'location': 'San Francisco',
            'temperature': '72',
            'unit': 'fahrenheit'
        }, ensure_ascii=False)
