import os
from openai import OpenAI
from zhipuai import ZhipuAI



"""
name: openai
url: https://platform.openai.com/api-keys
base-url: https://api.openai.com/v1
"""
# API_KEY = os.getenv('OPENAI_API_KEY')
# BASE_URL = None
# BASE_MODEL = "gpt-3.5-turbo-1106"


"""
name: kimi
url: https://platform.moonshot.cn/console/api-keys
base-url: https://api.moonshot.cn/v1
"""
# API_KEY = os.getenv('KIMI_API_KEY')
# BASE_URL = "https://api.moonshot.cn/v1"
# BASE_MODEL = "moonshot-v1-8k"


"""
name: ollama
url: https://ollama.com/library/qwen
base-url: http://localhost:11434/v1
"""
BASE_URL = "http://qwen.natapp1.cc/v1"
BASE_MODEL = "/home/lgy/model/Qwen1___5-14B-Chat-GPTQ-Int4"
API_KEY = BASE_MODEL


"""
name: zhipu
url: https://open.bigmodel.cn/usercenter/apikeys
base-url: https://open.bigmodel.cn/api/paas/v4
"""
# API_KEY = os.getenv('ZHIPU_API_KEY')
# BASE_MODEL = 'glm-4'


###############################CLIENT###############################

base_client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

# base_client = ZhipuAI(api_key=API_KEY)