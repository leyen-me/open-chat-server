from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient(host='192.168.31.120', port=502)
if client.connect():
    print("Modbus RTU Client Connected")
else:
    print("Failed to connect to Modbus RTU Client")

response = client.read_coils(address=0, count=10, unit=1)
print(response.bits)