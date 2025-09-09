import pyrosim.pyrosim as pyrosim

import random as r

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
    for i in range(0, 3):
        for j in range(3, 5):
            pyrosim.Send_Synapse( sourceNeuronName = i , targetNeuronName = j , weight = (r.random() * 2 -1) )
    pyrosim.End()

# loops for creating 6x6 descending block towers
# for a in range (0, 6):
# for b in range (0, 6):
    # for i in range (11,0, -1):
        # pyrosim.Send_Cube(name="Box", pos=[a, b ,(((-i + 11.5)* 0.9)/1.01)] ,
        # size=[(i * 0.9)/10, (i * 0.9)/10, (i * 0.9)/10])

Create_World()
Generate_Body()
Generate_Brain()
