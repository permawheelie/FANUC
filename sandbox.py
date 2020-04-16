# This script parses an existing logfile and extracts pertinent information to create 
# variables from the data contained within. With this data, computations are performed on the
# logfile generated from a 5,000 cycle sesnor probe FANUC .tp program (this generates a 45,000 
# line logfile (5,000 entries per sensor/position combination with 3 sensors and 3 positons))
# to create a 9-element list, with each element containg a 2-elemetn list. Each 2- element list
# contains the average reading from an Ultrasonic sensor, and the height of the FANUC 
# robot at the time the sensor captured its reading. Sensor readings that occur outside of a 
# user specefied tolerance range (determined in find Avg()) will be subsequently stored in a 
# separate list of outlier lists (the list element being [sensor reading , z height])
# The purpose of this script is to determine the precision adn accuracy of different ultrasonic 
# sensors when reading from different heights. # This script, upon completion will output to the
# terminal the following:
	# filepath and filename of the log file being parsed
	# log file file access privileges for the parser
	# outlier count at the user specefied tolerance
	# Averages per p#s# list
	# script process runtime 

# To access the FANUC .kl and .tp code that captures sensor data and generates the log file 
# parsed here, please use the following github link to access the repo:

#  https://github.com/haleyJ121/FANUC

# Author: Josh Haley (github @haleyJ121)
# Creation Date: 04/08/2020
# Revision index: V1.0

import re

class pattern:

	def __init__(self, expression, entry):
		self.expression = expression
		self.entry = entry
		self.value = self.performSearch(self.expression, self.entry)

	def performSearch(self, expression, entry):
		_expType = self.expression.find("d*.{", 0, -1)
		# print("expType is: ", expType)
		if (_expType == -1):
			self.value = int(re.search(self.expression, self.entry).group())
		elif (_expType != -1):
			self.value = float(re.search(self.expression, self.entry).group())
		return self.value

### VARAIBLE INITIALIZATION ###

log_file_path = r"H:\FANUC\KAREL\logfile"

regex_probePosition = '(?<=PROBE POSITION: )\d'
regex_activeSensor = '(?<=ACTIVE SENSOR: )\d'
regex_sensorReadout = '(?<=SENSOR READOUT: )\d*.{4}'
regex_ZValue = '(?<=Z HEIGHT:   )\d*.{4}'

resultingAverages = []
outliers = []

# p[probe vale]s[sensor value] lists for each of the 9 unique combinations

p1s1 = []
p1s2 = []
p1s3 = []

p2s1 = []
p2s2 = []
p2s3 = []

p3s1 = []
p3s2 = []
p3s3 = []

listNames = [p1s1, p1s2, p1s3, p2s1, p2s2, p2s3, p3s1, p3s2, p3s3]

### FUNCTION DEEFININTIONS ###

# assesses the variables into p#s# lists from the .value components of each object
def recordData():

		# high probe position
		if (probePosition.value == 1 and activeSensor.value == 1):
			p1s1.append([sensorReadout.value, ZValue.value])
		elif (probePosition.value == 1 and activeSensor.value == 2):
			p1s2.append([sensorReadout.value, ZValue.value])
		elif (probePosition.value == 1 and activeSensor.value == 3):
			p1s3.append([sensorReadout.value, ZValue.value])

		# medium probe position
		elif (probePosition.value == 2 and activeSensor.value == 1):
			p2s1.append([sensorReadout.value, ZValue.value])
		elif (probePosition.value == 2 and activeSensor.value == 2):
			p2s2.append([sensorReadout.value, ZValue.value])
		elif (probePosition.value == 2 and activeSensor.value == 3):
			p2s3.append([sensorReadout.value, ZValue.value])

		# low probe postion
		elif (probePosition.value == 3 and activeSensor.value == 1):
			p3s1.append([sensorReadout.value, ZValue.value])
		elif (probePosition.value == 3 and activeSensor.value == 2):
			p3s2.append([sensorReadout.value, ZValue.value])
		elif (probePosition.value == 3 and activeSensor.value == 3):
			p3s3.append([sensorReadout.value, ZValue.value])

def findAvg():

	for i in listNames: #iterate by p#s# list
		# print (len(i))
		sensorSum = 0
		robotSum = 0
		tolerance = 3.000 #this is a percentage
		for j in i: #iterate by current p#s# list element (should be 5000)
			sensorVal = j[0]
			robotVal = j[1]

			sensorSum = sensorVal + sensorSum
			sensorAvg = sensorSum / len(i)
			
			robotSum = robotVal + robotSum
			robotAvg = robotSum / len(i)

	
	resultingAverages.append([round(sensorAvg, 3), round(robotAvg, 3)])
	toleranceLower = sensorAvg * ((100 - tolerance) / 100)
	toleranceLower = round(toleranceLower, 3)
	toleranceUpper = sensorAvg * ((100 + tolerance) / 100)
	toleranceUpper = round(toleranceUpper, 3)
	
	for m in i: #interate by current p#s# element again
		sensorVal = m[0]
		robotVal = m[1]
		if ((sensorVal <= toleranceLower) | (sensorVal >= toleranceUpper)): #if sensorVal is out of tolerance
			outliers.append([sensorVal, robotVal])

	outlierCount = len(outliers)
	#add which p#p# list as arg 1 below
	print ("total outlier count with a ", tolerance, "% tolerance: ", outlierCount)
	return


### BEGIN PROGRAM ###


with open (log_file_path, "r") as file:
	print ("filename: ", file.name)
	print ("read/write privleges: ", file.mode, '\n')

	logContents = file.readlines()

for n, entry in enumerate(logContents): # iterates for however many lines are in the logfile that is being read
	# print ("n is:", n + 1)
	probePosition = pattern(regex_probePosition, entry) # creates probePosition object
	# print ("probePostion is: ", probePosition.value, "its type is: ", type(probePosition.value))

	activeSensor = pattern(regex_activeSensor, entry) # creates activeSensor object
	# print ("activeSensor is: ", activeSensor.value, "its type is: ", type(activeSensor.value))

	sensorReadout = pattern(regex_sensorReadout, entry) # creates sensorReadout object
	# print ("sensorReadout is: ", sensorReadout.value, "its type is: ", type(sensorReadout.value))

	ZValue = pattern(regex_ZValue, entry) # creates ZValue object
	# print ("ZValue is: ", ZValue.value, "its type is: ", type(ZValue.value),  '\n')

	recordData() #extracts pertinet variables from object data

findAvg()
# print ("resulting p#s# averages are:", '\n',"p1s1: ", resultingAverages[0], '\n',"p1s2: ", resultingAverages[1], '\n',"p1s3: ", resultingAverages[2], '\n',"p2s1: ", resultingAverages[3], '\n',"p2s2: ", resultingAverages[4], '\n',"p2s3: ", resultingAverages[5], '\n',"p3s1: ", resultingAverages[6], '\n',"p3s2: ", resultingAverages[7], '\n',"p3s3: ", resultingAverages[8])
print ("p3s3 averages:", resultingAverages[0])

file.close()