import pybullet as p
import pybullet_data
import time as t
import pyrosim.pyrosim as pyrosim
import numpy
import math
import random



physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
# p.disconnect()

# simulate earth gravity
p.setGravity(0,0,-9.8)

# build floor
planeId = p.loadURDF("plane.urdf")

#build body
robot = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate("body.urdf")

backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

min = -(math.pi)/4
max = +(math.pi)/4

FrontAmplitude = -numpy.pi/4
FrontFrequency = 20
FrontPhaseOffset = 0

BackAmplitude = numpy.pi/5
BackFrequency = 10
BackPhaseOffset = 0

FrontLegtargetAngles = numpy.linspace(-numpy.pi, numpy.pi, 1000)

for i in range (len(FrontLegtargetAngles)):
    FrontLegtargetAngles [i] = FrontAmplitude * numpy.sin(FrontFrequency * FrontLegtargetAngles[i] + FrontPhaseOffset)

BackLegtargetAngles = numpy.linspace(-numpy.pi, numpy.pi, 1000)

for i in range (len(BackLegtargetAngles)):
    BackLegtargetAngles [i] = BackAmplitude * numpy.sin(BackFrequency * BackLegtargetAngles[i] + BackPhaseOffset)

print(BackLegTargetAngles)
print(FrontLegTargetAngles)
# modify motor cmd vector value
# amplitude * sin(frequency * x + phaseOffset)

# loop iteration for timed sim
for x in range (0, 1000):
    p.stepSimulation()
    # log for sensor values
    backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robot,
        jointName = "Torso_BackLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = BackLegtargetAngles[x],
        maxForce = 20)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robot,
        jointName = "Torso_FrontLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = FrontLegtargetAngles[x],
        maxForce = 20)
    t.sleep(1/60)

# print(backLegSensorValues)
numpy.save("data/backlegsensor.npy", backLegSensorValues)
numpy.save("data/frontlegsensor.npy", frontLegSensorValues)

numpy.save("data/FrontLegTargetAngles.npy", frontLegSensorValues)
numpy.save("data/BackLegTargetAngles.npy", backLegSensorValues)
