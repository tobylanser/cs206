# import pybullet as p
# import pybullet_data
# import time as t
# import pyrosim.pyrosim as pyrosim
# import numpy
# import math
# import random
# import constants as c
#
from simulation import SIMULATION
#
# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())
# # p.disconnect()
#
# # simulate earth gravity
# p.setGravity(0,0,-9.8)
#
# # build floor
# planeId = p.loadURDF("plane.urdf")
#
# #build body
# robot = p.loadURDF("body.urdf")
#
# p.loadSDF("world.sdf")
#
# pyrosim.Prepare_To_Simulate("body.urdf")
#
# c.backLegSensorValues = numpy.zeros(1000)
# c.frontLegSensorValues = numpy.zeros(1000)
#
# c.min = -(math.pi)/4
# c.max = +(math.pi)/4
#
# c.FrontAmplitude = -numpy.pi/4
# c.FrontFrequency = 20
# c.FrontPhaseOffset = 0
#
# c.BackAmplitude = numpy.pi/5
# c.BackFrequency = 10
# c.BackPhaseOffset = 0
#
# c.FrontLegtargetAngles = numpy.linspace(-numpy.pi, numpy.pi, 1000)
#
# for i in range (len(c.FrontLegtargetAngles)):
#     c.FrontLegtargetAngles [i] = c.FrontAmplitude * numpy.sin(c.FrontFrequency * c.FrontLegtargetAngles[i] + c.FrontPhaseOffset)
#
# c.BackLegtargetAngles = numpy.linspace(-numpy.pi, numpy.pi, 1000)
#
# for i in range (len(c.BackLegtargetAngles)):
#     c.BackLegtargetAngles [i] = c.BackAmplitude * numpy.sin(c.BackFrequency * c.BackLegtargetAngles[i] + c.BackPhaseOffset)
#
# # print(BackLegTargetAngles)
# # print(FrontLegTargetAngles)
# # modify motor cmd vector value
# # amplitude * sin(frequency * x + phaseOffset)
#
# # loop iteration for timed sim
# for x in range (0, 1000):
#     p.stepSimulation()
#     # log for sensor values
#     c.backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     c.frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex = robot,
#         jointName = "Torso_BackLeg",
#         controlMode = p.POSITION_CONTROL,
#         targetPosition = c.BackLegtargetAngles[x],
#         maxForce = 20)
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex = robot,
#         jointName = "Torso_FrontLeg",
#         controlMode = p.POSITION_CONTROL,
#         targetPosition = c.FrontLegtargetAngles[x],
#         maxForce = 20)
#     t.sleep(1/60)
#
# # print(backLegSensorValues)
# numpy.save("data/backlegsensor.npy", backLegSensorValues)
# numpy.save("data/frontlegsensor.npy", frontLegSensorValues)
#
# numpy.save("data/FrontLegTargetAngles.npy", frontLegSensorValues)
# numpy.save("data/BackLegTargetAngles.npy", backLegSensorValues)


simulation = SIMULATION()
simulation.Run()
