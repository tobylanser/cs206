import constants as c
import pyrosim.pyrosim as pyrosim
import numpy as numpy
import pybullet as p

class MOTOR:
    def __init__(self, jointName):
        self.robot = None
        self.jointName = jointName
        self.values = numpy.zeros(1000)
        self.motorValues = None
        self.amplitude = c.FrontAmplitude
        self.frequency = c.FrontFrequency
        self.offset = c.FrontPhaseOffset

    def Set_Value(self, desiredAngle, robot):
        self.robot = robot
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = self.robot,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = desiredAngle,
            maxForce = 20)
