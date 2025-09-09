import numpy
import matplotlib.pyplot

#  draw the values in this vector
# load in sensor values from simulate.py
backLegSensorValues=numpy.load("data/backLegSensor.npy")
frontLegSensorValues=numpy.load("data/frontLegSensor.npy")
# print vector
# print(backLegSensorValues)
# print(frontLegSensorValues

matplotlib.pyplot.plot(backLegSensorValues, label="back leg", linewidth=4)
matplotlib.pyplot.plot(frontLegSensorValues, label="front leg", linewidth=4)
# add legend to plot
matplotlib.pyplot.legend()
# show plot
matplotlib.pyplot.show()
