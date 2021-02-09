import pybullet as p
import pybullet_data
import time as t

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
# p.disconnect()

# simulate earth gravity
p.setGravity(0,0,-9.8)

# build floor
planeId = p.loadURDF("plane.urdf")

#build body
planeId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

for x in range (0, 1000):
    p.stepSimulation()
    t.sleep(1/60)
