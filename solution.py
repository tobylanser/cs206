import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c
class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons)
        self.weights * 2 - 1
        self.myID = nextAvailableID

    def Set_ID(self, ID):
        self.myId = ID

    # def Evaluate(self, runType):
    #     pass
        # self.Create_World()
        # self.Generate_Body()
        # self.Generate_Brain()
        # os.system("start /B python simulate.py " + runType + " " + str(self.myID))
        #
        # while not os.path.exists("fitness" + str(self.myID) + ".txt"):
        #     time.sleep(0.01)
        #
        # f = open("fitness" + str(self.myID) + ".txt", 'r')
        # self.fitness = float(f.readline())
        # print(self.fitness)

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

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[6, 0, 0.5], size=[1, 1, 1])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        # create torso cube
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[1, 1, 1])

        # Create joint for torso & back leg
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso",
                           child="BackLeg",
                           type="revolute",
                           position="0 -0.5 1",
                           jointAxis = "1 0 0")

        # create black leg cube
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[0.2, 1.0, 0.2])

        # Create joint for torso & front leg
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso",
                           child="FrontLeg",
                           type="revolute",
                           position="0 0.5 1",
                           jointAxis = "1 0 0")

        # create front leg cube
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2, 1.0, 0.2])

        # Create joint for torso & left leg
        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso",
                           child="LeftLeg",
                           type="revolute",
                           position="-0.5 0 1",
                           jointAxis = "0 1 0")

        # create left leg cube
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, 0, 0], size=[1.0, 0.2, 0.2])

        # Create joint for torso & back lower leg
        pyrosim.Send_Joint(name="Back_BackLowerLeg", parent="BackLeg",
                           child="BackLowerLeg",
                           type="revolute",
                           position="0 -1 0",
                           jointAxis = "-1 0 0")

        # create black lower leg cube
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])



        # Create joint for left leg & lower left leg
        pyrosim.Send_Joint(name="Left_LeftLowerLeg", parent="LeftLeg",
                           child="LeftLowerLeg",
                           type="revolute",
                           position="-1 0 0",
                           jointAxis = "0 1 0")

        # create left leg cube
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        # Create joint for torso & right leg
        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso",
                           child="RightLeg",
                           type="revolute",
                           position="0.5 0 1",
                           jointAxis = "0 -1 0")

        # create right leg cube
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5, 0, 0], size=[1.0, 0.2, 0.2])

        # Create joint for right leg & lower right leg
        pyrosim.Send_Joint(name="Right_RightLowerLeg", parent="RightLeg",
                           child="RightLowerLeg",
                           type="revolute",
                           position="1 0 0",
                           jointAxis = "0 0 1")

        # create right lower leg cube
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])


        # Create joint for torso & front lower leg
        pyrosim.Send_Joint(name="Front_FrontLowerLeg", parent="FrontLeg",
                           child="FrontLowerLeg",
                           type="revolute",
                           position="0 1 0",
                           jointAxis = "1 0 0")

        # create front lower leg cube
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1.0])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="LeftLeg")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="RightLeg")
        pyrosim.Send_Sensor_Neuron(name=5, linkName="FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=6, linkName="BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=7, linkName="LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=8, linkName="RightLowerLeg")
        pyrosim.Send_Motor_Neuron(name=9, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=10, jointName="Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name=11, jointName="Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name=12, jointName="Torso_RightLeg")
        pyrosim.Send_Motor_Neuron(name=13, jointName="Front_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron(name=14, jointName="Back_BackLowerLeg")
        pyrosim.Send_Motor_Neuron(name=15, jointName="Left_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron(name=16, jointName="Right_RightLowerLeg")

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+c.numSensorNeurons,
                                     weight=self.weights[currentRow][currentColumn])
        pyrosim.End()
