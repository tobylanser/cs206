import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
import math
import constants as c
import time as t
from motor import MOTOR

class ROBOT:
    def __init__(self):
        self.robot = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate("body.urdf")
        self.motors = {}
        ROBOT.Prepare_To_Sense(self)
        ROBOT.Prepare_To_Act(self)
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    def Sense(self, t):
        for i in self.sensors.values():
            i.Get_Value(t)
    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
    def Act(self, t):
        for i in self.motors:
            self.motors[i].Set_Value(t, self.robot)
