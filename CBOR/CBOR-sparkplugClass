import numpy
from typing import Type 
from binascii import hexlify, unhexlify
from cbor2 import dumps, loads

class Metric():
    def __init__(self, name,timestamp_data,value):
        self.metrics= {
            "name":name,
            "timestamp":timestamp_data,
            "dataType": Metric.__type__(self,value),
            "value":value}

        self.name = name; self.timestamp_data = timestamp_data; self.value = value
    def __type__(self, value):
        cbor = dumps(value)
        head = cbor[0]
        valueT = head.to_bytes(2,'big')
        return valueT[1:]

    def keys_(self):
        return [self.name, self.timestamp_data, Metric.__type__(self, self.value), self.value]

class Estrutura(object):
    def __init__(self,timestamp,seq:numpy.int8, metrics:Type[Metric]):
        self.timestamp = timestamp
        self.metrics = metrics
        self.seq = seq

    def __str__(self):
        return str(self.__dict__)

    def keys_(self):
        return [self.timestamp, self.metrics, self.seq]

def _toHex_(x):
    seri = dumps(x)
    return (hexlify(seri))


def _deserializar_(hex_message):
    msg =   unhexlify(hex_message) 
    return loads(msg)

def _toJson_(x):
    estrutura = ["Timestamp", "Metrics", "Seq"]
    metrica_estrutura = ["Name", "Timestamp", "Type", "Value"]
    metrics = []
    for i in range(len(x)):
        if type(x[i]) == list:
            for j in range(len(x[i])):
                obj = x[i][j]
                json = dict(zip(metrica_estrutura,obj))
                metrics.append(json)
    data =(x[0], metrics, x[2])
    mensagem = dict(zip(estrutura, data))
    return mensagem

def _counterString_(data):
    result = [len(word) for word in str(data)]
    return sum(result)

def _counterBytes_(data):
    result = len(data)
    return result
