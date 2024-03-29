import os
from openai import OpenAI
from zhipuai import ZhipuAI

"""
name: openai
url:  https://platform.openai.com/api-keys
proxy-url: https://api.openai-proxy.com/v1
"""
# API_KEY = os.getenv('OPENAI_API_KEY')
# BASE_URL = None
# BASE_MODEL = "gpt-3.5-turbo-1106"


"""
name: kimi
url:  https://platform.moonshot.cn/console/api-keys
"""
# API_KEY = os.getenv('KIMI_API_KEY')
# BASE_URL = "https://api.moonshot.cn/v1"
# BASE_MODEL = "moonshot-v1-8k"


"""
name: qwen:14b
url:  https://ollama.com/library/qwen
"""

# BASE_URL = "http://qwen.natapp1.cc/v1"
# BASE_MODEL = "qwen:14b"
# API_KEY = BASE_MODEL

# base_client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

API_KEY = os.getenv('ZHIPU_API_KEY')
BASE_MODEL = 'glm-4'
base_client = ZhipuAI(api_key=API_KEY)