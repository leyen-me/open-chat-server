from .base_prompt import BasePrompt

class IotPrompt(BasePrompt):

    def __init__(self):
        super().__init__()
        self.name = "物联网"
        self.code = "iot"
        self.system_prompt = """
        我希望您能扮演一个物联网工程师，操作数据库时默认使用SQLAlchemy库，连接数据库请遵循MYSQL_URI_FORMAT规范。

        以下是一些系统信息，供你参考:
        Python: 3.8.0
        MYSQL_URI_FORMAT: mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_database}?charset=utf8mb4
        
        # 依赖库版本
        SQLAlchemy: 2.0.28
        pymodbus: 2.5.3
        """
        # self.code_auto_run = 1

        # 192.168.31.120

        self.demo = """
        你好，我现在有一台设备，帮我读取一下设备的线圈数据，设备的IP地址是192.168.31.120，端口是502，串口是4

        1.读取数据的时候从0开始，每次读取10条，
        2.读取完成后帮我存到数据库中，数据库的HOST是 192.168.31.120 ，端口是 3307 ，用户名是 root ， 密码是 pdBGKGjRyX3Jb2Hn， 数据库是 iot-mysql
        3.数据库我已经帮你建好了，你需要自动创建表和存储数据，表名叫demo。
        4.读取数据需要每个5秒读取一次
        """