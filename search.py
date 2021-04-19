import os as os
from parallelHillClimber import PARALLEL_HILL_CLIMBER

# for i in range (0,4):
#     os.system("python3 generate.py")
#     os.system("python3 simulate.py")
#     i = i + 1

phc = PARALLEL_HILL_CLIMBER()
phc.Evovle()
phc.Show_Best()
