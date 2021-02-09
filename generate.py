import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

x1 = 0
y1 = 0
z1 = 0.5
# box2 variable position
x2 = 0
y2 = 1
z2 = 1.5

# pyrosim.Send_Cube(name="Box2", pos=[x2,y2,z2] , size=[1,1,1])
for a in range (0, 6):
    for b in range (0, 6):
        # for loop
        for i in range (11,0, -1):
            pyrosim.Send_Cube(name="Box", pos=[a, b ,(((-i + 11.5)* 0.9)/1.01)] ,
            size=[(i * 0.9)/10, (i * 0.9)/10, (i * 0.9)/10])

pyrosim.End()
