import pyrosim.pyrosim as pyrosim

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[4, 0, 0.5] , size=[1,1,1])
    pyrosim.End()


def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    # create leg cube
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5] , size=[1,1,1])
    # Create joint for torso & back leg
    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" ,
                        child = "BackLeg" ,
                        type = "revolute",
                        position = "0.5 0 1")

    # create torso cube
    pyrosim.Send_Cube(name="Torso", pos=[1, 0, 1.5] , size=[1,1,1])

    # Create joint for torso & front leg
    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" ,
                        child = "FrontLeg" ,
                        type = "revolute",
                        position = "1.5 0 1")

    # create front leg cube
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5] , size=[1,1,1])

    pyrosim.End()

# loops for creating 6x6 descending block towers
# for a in range (0, 6):
    # for b in range (0, 6):
        # for i in range (11,0, -1):
            # pyrosim.Send_Cube(name="Box", pos=[a, b ,(((-i + 11.5)* 0.9)/1.01)] ,
            # size=[(i * 0.9)/10, (i * 0.9)/10, (i * 0.9)/10])

Create_World()
Create_Robot()
