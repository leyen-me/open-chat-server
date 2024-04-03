from .default_prompt import DefaultPrompt
from .en2cn_prompt import En2CnPrompt
from .cn2en_prompt import Cn2EnPrompt
from .iot_prompt import IotPrompt
from .vue_interviewer_prompt import VueInterviewerPrompt
from .java_interviewer_prompt import JavaInterviewerPrompt
from .china_tourism_prompt import ChinaTourismPrompt
from .compiler_teacher_prompt import CompilerTeacherPrompt
from .test_prompt import TestPrompt

prompts = [
    DefaultPrompt(),
    En2CnPrompt(),
    Cn2EnPrompt(),
    IotPrompt(),
    VueInterviewerPrompt(),
    JavaInterviewerPrompt(),
    ChinaTourismPrompt(),
    CompilerTeacherPrompt(),
    TestPrompt(),
]