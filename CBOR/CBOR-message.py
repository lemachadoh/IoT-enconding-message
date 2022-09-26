import interpretador as add
from interpretador import Estrutura, _toHex_
import time 
import random
from binascii import unhexlify
from cbor2 import loads


def payload():
    metricDevice = add.Metric("DeviceName", time.time(),"LogBox").keys_()
    metricSn = add.Metric("sn", time.time(), round(random.randint(0, 90000000),8)).keys_()
    metricFirm = add.Metric("Firmware",time.time(), round(random.uniform(1.0, 10.0),2)).keys_()
    metricMQTT1= add.Metric("Temperature", time.time(), round(random.uniform(0.0,40.0),1)).keys_()
    metricMQTT3 = add.Metric("Humidity",  time.time(), round(random.uniform(30.0,90.0),1)).keys_()
    msg_count = _toHex_(Estrutura( time.time(), 1, [metricDevice,metricSn,metricFirm,metricMQTT1, metricMQTT3]).keys_())
    return msg_count

