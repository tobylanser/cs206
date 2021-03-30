import os as os
import random as random
import numpy as numpy
import pyrosim.pyrosim as pyrosim

class SOLUTION():
    def __init__(self):
        self.weights = numpy.random.rand(3, 2)
        self.weights * 2 - 1

    def Evaluate(self, directOrGUI):
        self.Generate_Brain()
        self.Generate_Body()
        self.Create_World()
        os.system("python3 simulate.py " + directOrGUI)
        f = open("fitness.txt", "r")
        self.fitness = float(f.read())

    def Mutate(self):
        currentRow = random.randint(0,2)
        currentCol = random.randint(0,1)
        mutatedWeight = random.random() * 2 - 1
        self.weights[currentRow][currentCol] = mutatedWeight

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[6, 0, 0.5] , size=[1,1,1])
        pyrosim.End()

    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf")
        # create torso cube
        pyrosim.Send_Cube(name="Torso", pos=[1, 0, 1.5] , size=[1,1,1])

        # Create joint for torso & back leg
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" ,
                            child = "BackLeg" ,
                            type = "revolute",
                            position = "0.5 0 1")

        # create black leg cube
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5] , size=[1,1,1])

        # Create joint for torso & front leg
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" ,
                            child = "FrontLeg" ,
                            type = "revolute",
                            position = "1.5 0 1")

        # create front leg cube
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5] , size=[1,1,1])
        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Motor_Neuron(name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name = 4 , jointName = "Torso_FrontLeg")

        for currentRow in range (3):
            for currentColumn in range (2):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + 3 , weight = self.weights[currentRow][currentColumn] )
        pyrosim.End()
