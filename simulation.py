from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import time as t

class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        self.world = WORLD()
        self.robot = ROBOT()
        # simulate earth gravity
        p.setGravity(0,0,-9.8)

    def Run(self):
        for x in range (0, 100):
            p.stepSimulation()
            self.robot.Sense(x)
            self.robot.Think()
            self.robot.Act(x)
            # # log for sensor values
            t.sleep(1/10)
            # print(x)
        p.disconnect()

def __del__(self):
    p.disconnect()
