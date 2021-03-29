import os as os
import random as r
import numpy as numpy

class SOLUTION():
    def __init__(self):
        self.weights = numpy.random.rand(3, 2)
        self.weights * 2 - 1
        # print(self.weights)
        # exit()

    def Create_World():
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[6, 0, 0.5] , size=[1,1,1])
        pyrosim.End()

    def Generate_Body():
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

    def Generate_Brain():
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

    def Evaluate(self):
        os.system("python3 simulate.py")
