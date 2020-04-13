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

### BEGIN PROGRAM ###
p1s1 = []
p1s2 = []
p1s3 = []

p2s1 = []
p2s2 = []
p2s3 = []

p3s1 = []
p3s2 = []
p3s3 = []

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

with open (log_file_path, "r") as file:
	print ("filename: ", file.name)
	print ("read/write privleges: ", file.mode, '\n')

	logContents = file.readlines()

regex_probePosition = '(?<=PROBE POSITION: )\d'
regex_activeSensor = '(?<=ACTIVE SENSOR: )\d'
regex_sensorReadout = '(?<=SENSOR READOUT: )\d*.{4}'
regex_ZValue = '(?<=Z HEIGHT:   )\d*.{4}'

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

	#results = compute(probePosition.value, activeSensor.value, sensorReadout.value, ZValue.value, n)
	#results.makeList(probePosition.value, activeSensor.value, sensorReadout.value, ZValue.value, n)

file.close()