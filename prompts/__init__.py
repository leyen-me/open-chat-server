from .default_prompt import DefaultPrompt
from .en2cn_prompt import En2CnPrompt
from .cn2en_prompt import Cn2EnPrompt
from .iot_prompt import IotPrompt


prompts = [
    DefaultPrompt(),
    En2CnPrompt(),
    Cn2EnPrompt(),
    IotPrompt(),
]
