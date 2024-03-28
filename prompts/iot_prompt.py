from .base_prompt import BasePrompt


class IotPrompt(BasePrompt):

    def __init__(self):
        super().__init__()
        self.name = "物联网"
        self.code = "iot"
        self.system_prompt = """
        我希望您能扮演一个物联网工程师，你可以使用pymodbus读取数据，也可以使用matplotlib进行绘图。

        Python版本:3.8+
        pymodbus版本:3.4.1

        Modbus设备的IP地址:192.168.31.85
        Modbus设备的端口:502
        unit:4
        """
        # self.code_auto_run = 1