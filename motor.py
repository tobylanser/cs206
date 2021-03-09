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
        self.Prepare_To_Act()
    def Prepare_To_Act(self):
        if self.jointName =="Torso_FrontLeg":
            self.frequency = c.BackAmplitude / 2
        else:
            pass
        self.motorValues = self.amplitude * numpy.sin(self.frequency * (numpy.linspace(-numpy.math.pi, numpy.math.pi, 1000))+ self.offset)

    # for i in range (len(c.FrontLegtargetAngles)):
    #     c.FrontLegtargetAngles [i] = self.amplitude * numpy.sin(self.frequency * c.FrontLegtargetAngles[i] + self.offset)

    def Set_Value(self, t, robot):
        self.robot = robot
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = self.robot,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = self.motorValues[t],
            maxForce = 20)
    def Save_Values():
        numpy.save("data/" + self.linkName + "SensorValues.npy", self.values)
