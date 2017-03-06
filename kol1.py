#Bartlomiej Nikliborc
import random
maxTiltCorrectionDegree = 10

def planeSimulator():
	NofStep = 1
	plane_orientation = 0
	while True:
		NofStep += 1
		turbulations = random.gauss(0, 20)
		print  "turbulations %s" % turbulations
		plane_orientation += turbulations
		print "plane_orientation %s" % plane_orientation
		correction = getCorrection(plane_orientation)
		print "correction %s" % correction
		plane_orientation += correction
		print "corrected_Plane_orietnation %s" % plane_orientation
		

def getCorrection(orientation):
	if orientation > maxTiltCorrectionDegree:
		return orientation - maxTiltCorrectionDegree
	elif orientation <  -maxTiltCorrectionDegree:
		return orientation + maxTiltCorrectionDegree
	else:
		return orientation - maxTiltCorrectionDegree

planeSimulator()	


