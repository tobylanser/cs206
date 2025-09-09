from solution import SOLUTION
import constants as c
import copy
import os


class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        self.parent = {}
        self.nextAvailableID = 0
        for i in range(0, c.populationSize):
            s = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
            self.parent[i] = s

    def Evovle(self):
        self.Evaluate(self.parent)
        for currentGeneration in range(0, c.numberOfGenerations):
             self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        # self.Select()
        self.Print()
        self.Select()

    def Evaluate(self, solutions):
        for i in range(len(solutions)):
            solutions[i].Start_Simulation("DIRECT")
        for i in range(len(solutions)):
            solutions[i].Wait_For_Simulation_To_End()


    def Show_Best(self):
        minFitness = 1000
        minIndex = -1
        for i in range(len(self.parent)):
            if self.parent[i].fitness < minFitness:
                minIndex = i
                minFitness = self.parent[i].fitness
        self.parent[minIndex].Start_Simulation("GUI")

    def Print(self):
        print("\n")
        for key in range(len(self.parent)):
            print("Parent: " + str(self.parent[key].fitness) + ", " + "Child: " + str(self.children[key].fitness))
            print("\n")

    def Spawn(self):
        self.children = {}
        for i in range(len(self.parent)):
            self.children[i] = copy.deepcopy(self.parent[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for i in range(len(self.children)):
            self.children[i].Mutate()

    def Select(self):
        for i in range(len(self.parent)):
            if self.parent[i].fitness > self.children[i].fitness:
                self.parent[i] = self.children[i]
