import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c
class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons) * 2 - 1
        self.length= random.random()*3 +0.1
        self.fitness=0
        self.myID = nextAvailableID

    def Set_ID(self, ID):
        self.myId = ID

    def Evaluate(self, runType):
        pass
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        os.system("start /B python simulate.py " + runType + " " + str(self.myID))

        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.01)

        f = open("fitness" + str(self.myID) + ".txt", 'r')
        self.fitness = float(f.readline())
        print(self.fitness)

    def Start_Simulation(self, runType):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("python3 simulate.py " + runType + " " + str(self.myID) + " &")
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.01)

    def Wait_For_Simulation_To_End(self):
        f = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(f.read())
        f.close()
        os.system("rm fitness" + str(self.myID) + ".txt")

    def Mutate(self):
        currentRow = random.randint(0, c.numSensorNeurons-1)
        currentCol = random.randint(0, c.numMotorNeurons-1)
        mutatedWeight = random.random() * 2 - 1
        self.weights[currentRow][currentCol] = mutatedWeight
        mutatedLength = random.random() * 3 +0.1
        self.length = mutatedLength

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[6, 0, 0.5], size=[1, 1, 1])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, self.length], size=[1, 1, 1])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position="0 -0.5 "+str(self.length), jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position="0 0.5 "+str(self.length), jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])
        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute", position="-0.5 0 "+str(self.length), jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, 0, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute", position="0.5 0 "+str(self.length), jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5, 0, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Joint(name="BackLeg_BackLegBottom", parent="BackLeg", child="BackLegBottom", type="revolute", position="0 -1 0", jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLegBottom", pos=[0, 0, -self.length/2], size=[0.2, 0.2, self.length])
        pyrosim.Send_Joint(name="FrontLeg_FrontLegBottom", parent="FrontLeg", child="FrontLegBottom", type="revolute", position="0 1 0", jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLegBottom", pos=[0, 0, -self.length/2], size=[0.2, 0.2, self.length])
        pyrosim.Send_Joint(name="LeftLeg_LeftLegBottom", parent="LeftLeg", child="LeftLegBottom", type="revolute", position="-1 0 0", jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLegBottom", pos=[0, 0, -self.length/2], size=[0.2, 0.2, self.length])
        pyrosim.Send_Joint(name="RightLeg_RightLegBottom", parent="RightLeg", child="RightLegBottom", type="revolute", position="1 0 0", jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLegBottom", pos=[0, 0, -self.length/2], size=[0.2, 0.2, self.length])
        pyrosim.End()

        while not os.path.exists("body.urdf"):
            time.sleep(0.01)

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="FrontLegBottom")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLegBottom")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="LeftLegBottom")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="RightLegBottom")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=5, jointName="Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name=6, jointName="Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name=7, jointName="Torso_RightLeg")
        pyrosim.Send_Motor_Neuron(name=8, jointName="BackLeg_BackLegBottom")
        pyrosim.Send_Motor_Neuron(name=9, jointName="FrontLeg_FrontLegBottom")
        pyrosim.Send_Motor_Neuron(name=10, jointName="LeftLeg_LeftLegBottom")
        pyrosim.Send_Motor_Neuron(name=11, jointName="RightLeg_RightLegBottom")
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+c.numSensorNeurons, weight=self.weights[currentRow][currentColumn])
        pyrosim.End()
        while not os.path.exists("brain"+str(self.myID)+".nndf"):
            time.sleep(0.01)
