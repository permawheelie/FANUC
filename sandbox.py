import re

log_file_path = r"H:\FANUC\KAREL\logfile"

lineIterator = 0
sensorIterator = 0
count = 0

class pattern:

	def __init__(self, expression, entry):
		self.expression = expression
		self.entry = entry
		self.value = None
	def performSearch(self, expression, entry):
		self.value = int(re.search(self.expression, self.entry).group())
		return self.value

### BEGIN PROGRAM ###

with open (log_file_path, "r") as file:
	print ("filename: ", file.name)
	print ("read/write privleges: ", file.mode)

	result = file.readlines()


for n, entry in enumerate(result):
 	probePosition = pattern('(?<=PROBE POSITION: )\d', entry)

probePosition.value = probePosition.performSearch(probePosition.expression, entry)
print("performSearch result is: ", probePosition.value)
print("type is: ", type(probePosition.value))

file.close()
