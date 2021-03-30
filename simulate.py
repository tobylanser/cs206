
import sys
from simulation import SIMULATION

directOrGUI = sys.argv[1]

# Pass direct or GUI into simulations constructor
simulation = SIMULATION(directOrGUI)
simulation.Run()
simulation.Get_Fitness()
