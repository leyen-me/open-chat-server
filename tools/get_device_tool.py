import json
import json5
from qwen_agent.tools.base import BaseTool, register_tool


@register_tool("get_device_tool")
class GetDeviceTool(BaseTool):

    # 描述
    description = "读取物联网设备数据, 线圈"

    # 参数
    parameters = [
        {
            'name': 'DEVICE_ADDRESS',
            'type': 'int',
            'description': '访问寄存器起始地址',
            'required': True
        },
        {
            'name': 'DEVICE_COUNT',
            'type': 'int',
            'description': '寄存器数量',
            'required': True
        },
        {
            'name': 'DEVICE_PROTOCOL',
            'type': 'string',
            'description': '读取协议:TCP/RTU',
            'required': True
        },
        {
            'name': 'DEVICE_HOST',
            'type': 'string',
            'description': '设备地址',
            'required': True
        },
        {
            'name': 'DEVICE_PORT',
            'type': 'int',
            'description': '设备端口',
            'required': True
        },
        {
            'name': 'DEVICE_UNIT',
            'type': 'int',
            'description': '从机地址',
            'required': True
        },
    ]

    def call(self, params: str, **kwargs):
        from pymodbus.client import ModbusTcpClient

        DEVICE_PROTOCOL = json5.loads(params)['DEVICE_PROTOCOL']
        DEVICE_HOST = json5.loads(params)['DEVICE_HOST']
        DEVICE_PORT = json5.loads(params)['DEVICE_PORT']
        DEVICE_ADDRESS = json5.loads(params)['DEVICE_ADDRESS']
        DEVICE_COUNT = json5.loads(params)['DEVICE_COUNT']
        DEVICE_UNIT = json5.loads(params)['DEVICE_UNIT']

        client = ModbusTcpClient(host=DEVICE_HOST, port=DEVICE_PORT)
        if client.connect():
            response = client.read_coils(
                address=DEVICE_ADDRESS, count=DEVICE_COUNT, unit=DEVICE_UNIT)
            return json.dumps([(1 if item == True else 0) for item in response.bits])
        else:
            return json.dumps({
                "err_message": "Failed to connect to Modbus RTU Client"
            })
