import PROTO_msg_pb2  as MENSAGEM
from binascii import hexlify, unhexlify
import time
import random

############################################################################
#contar bytes 

def _counterBytes_(data):
    hex = hexlify(data)
    result = len(hex)
    return result

############################################################################

def payload():
    mensagem = MENSAGEM.Payload()

    mensagem.timestamp          = time.time()

    metrics1 = mensagem.metrics.add()
    metrics1.name               = 'DeviceName'
    metrics1.timestamp          = time.time()
    metrics1.datatype           = 12
    metrics1.string_value       = 'LogBox'

    metrics2 = mensagem.metrics.add()
    metrics2.name               = 'sn'
    metrics2.timestamp          = time.time()
    metrics2.datatype           = 3
    metrics2.int_value          = round(random.randint(0, 90000000),8)

    metrics3 = mensagem.metrics.add()
    metrics3.name               = 'Firmware'
    metrics3.timestamp          = time.time()
    metrics3.datatype           = 9
    metrics3.float_value        = round(random.uniform(0.0,40.0),1)
    
    metrics4 = mensagem.metrics.add()
    metrics4.name               = 'Temperature'
    metrics4.timestamp          = time.time()
    metrics4.datatype           = 9
    metrics4.float_value        = round(random.uniform(0.0,40.0),1)
    
    metrics5 = mensagem.metrics.add()
    metrics5.name               = 'Humidity'
    metrics5.timestamp          = time.time()
    metrics5.datatype           = 9
    metrics5.float_value        = round(random.uniform(0.0,40.0),1)
    mensagem.seq                = 1

    return (mensagem)

