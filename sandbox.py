import re

log_file_path = r"H:\FANUC\KAREL\logfile"

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

regex_probePosition = '(?<=PROBE POSITION: )\d'
regex_activeSensor = '(?<=ACTIVE SENSOR: )\d'
regex_sensorReadout = '(?<=SENSOR READOUT: )\d*.{4}'
regex_ZValue = '(?<=Z HEIGHT:   )\d*.{4}'

averages = []

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

def recordData():
		if (probePosition.value == 1 and activeSensor.value == 1):
			p1s1.append([sensorReadout.value, ZValue.value])
		elif (probePosition.value == 1 and activeSensor.value == 2):
			p1s2.append([sensorReadout.value, ZValue.value])
		elif (probePosition.value == 1 and activeSensor.value == 3):
			p1s3.append([sensorReadout.value, ZValue.value])

		elif (probePosition.value == 2 and activeSensor.value == 1):
			p2s1.append([sensorReadout.value, ZValue.value])
		elif (probePosition.value == 2 and activeSensor.value == 2):
			p2s2.append([sensorReadout.value, ZValue.value])
		elif (probePosition.value == 2 and activeSensor.value == 3):
			p2s3.append([sensorReadout.value, ZValue.value])

		elif (probePosition.value == 3 and activeSensor.value == 1):
			p3s1.append([sensorReadout.value, ZValue.value])
		elif (probePosition.value == 3 and activeSensor.value == 2):
			p3s2.append([sensorReadout.value, ZValue.value])
		elif (probePosition.value == 3 and activeSensor.value == 3):
			p3s3.append([sensorReadout.value, ZValue.value])

### BEGIN PROGRAM ###

with open (log_file_path, "r") as file:
	print ("filename: ", file.name)
	print ("read/write privleges: ", file.mode, '\n')

	logContents = file.readlines()

for n, entry in enumerate(logContents):
	print ("n is:", n + 1)
	probePosition = pattern(regex_probePosition, entry)
	print ("probePostion is: ", probePosition.value, "its type is: ", type(probePosition.value))

	activeSensor = pattern(regex_activeSensor, entry)
	print ("activeSensor is: ", activeSensor.value, "its type is: ", type(activeSensor.value))

	sensorReadout = pattern(regex_sensorReadout, entry)
	print ("sensorReadout is: ", sensorReadout.value, "its type is: ", type(sensorReadout.value))

	ZValue = pattern(regex_ZValue, entry)
	print ("ZValue is: ", ZValue.value, "its type is: ", type(ZValue.value),  '\n')

	recordData()

#print ("this:", (listNames[3])[0])

def findAvg():

	for i in listNames: #iterate by list
		print (len(i))
		sensorSum = 0
		robotSum = 0
		for j in i: #iterate by current list element (should be 5000)
			sensorVal = j[0]
			robotVal = j[1]

			sensorSum = sensorVal + sensorSum
			print ("sensorSum is:", sensorSum)
			sensorAvg = sensorSum / len(i)
			print ("sensorAvg is:", sensorAvg)
			# prevValue = currentValue # looks at previous value (holds this iterations value of currentValue in the next iteration of the for loop)

			#currentRobotValue = j[1]
			robotSum = robotVal + robotSum
			print ("robotSum is:", robotSum)
			robotAvg = robotSum / len(i)
			print ("robotAvg is:", robotAvg)
	
	#write robtAvg and sensorAvg to a result list in order to average each of its entries. thi slist elemts are also 2 element lists, except they are sensor avg and robot avg
	averages.append([sensorAvg, robotAvg])

findAvg()

print (averages[0])

file.close()