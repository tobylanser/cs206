import pyrosim.pyrosim as pyrosim
import numpy as numpy
import time as t

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = numpy.zeros(1000)
    def Get_Value(self, x):
        self.values[x] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        if(x == 999):
            print(self.values)
