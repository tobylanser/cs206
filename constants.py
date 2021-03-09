import numpy
import math
import constants as c

#import variables and vectors

frontLegSensorValues = numpy.zeros(1000)
backLegSensorValues = numpy.zeros(1000)

FrontAmplitude = -numpy.pi/4
FrontFrequency = 20
FrontPhaseOffset = 0

BackAmplitude = numpy.pi/5
BackFrequency = 10
BackPhaseOffset = 0

FrontLegtargetAngles = numpy.linspace(-numpy.pi, numpy.pi, 1000)

BackLegtargetAngles = numpy.linspace(-numpy.pi, numpy.pi, 1000)
