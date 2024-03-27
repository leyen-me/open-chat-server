import os
from openai import OpenAI


"""
name: openai
url:  https://platform.openai.com/api-keys
proxy-url: https://api.openai-proxy.com/v1
"""
API_KEY = os.getenv('OPENAI_API_KEY')
BASE_URL = None
BASE_MODEL = "gpt-3.5-turbo-1106"


"""
name: kimi
url:  https://platform.moonshot.cn/console/api-keys
"""
# API_KEY = os.getenv('KIMI_API_KEY')
# BASE_URL = "https://api.moonshot.cn/v1"
# BASE_MODEL = "moonshot-v1-8k"


"""
name: mistral
url:  https://ollama.com/library/mistral
"""
# API_KEY = "sk-mistral"
# BASE_URL = "http://localhost:11434/v1"
# BASE_MODEL = "mistral"

base_client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
