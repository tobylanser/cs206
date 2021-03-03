import numpy
import matplotlib.pyplot

FrontLegtargetAngleValues = numpy.load("data/FrontLegTargetAngles.npy")
BackegtargetAngleValues = numpy.load("data/BackLegTargetAngles.npy")

# print(targetAngleValues)

matplotlib.pyplot.plot(FrontLegtargetAngleValues)
matplotlib.pyplot.plot(BackegtargetAngleValues)

# # add legend to plot
matplotlib.pyplot.legend()
## # show plot
matplotlib.pyplot.show()
#  draw the values in this vector
# load in sensor values from simulate.py
# backLegSensorValues=numpy.load("data/backLegSensor.npy")
# frontLegSensorValues=numpy.load("data/frontLegSensor.npy")
# print vector
# print(backLegSensorValues)
# print(frontLegSensorValues

# # plot sensor values
# matplotlib.pyplot.plot(backLegSensorValues, label="back leg", linewidth=4)
# matplotlib.pyplot.plot(frontLegSensorValues, label="front leg", linewidth=4)
# # add legend to plot
# matplotlib.pyplot.legend()
# # show plot
# matplotlib.pyplot.show()
