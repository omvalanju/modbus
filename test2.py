
from pyModbusTCP.client import ModbusClient

class modbusclient(ModbusClient):

    
    def read(self,addr,num):
        bits = c.read_holding_registers(addr,num) 
        print(str(bits)) 


    def write(self,addr,num):
        c.write_single_register(addr,num)


c = modbusclient(host='localhost', port=5020, auto_open=True)


c.write(0,43)

c.read(0,1)
