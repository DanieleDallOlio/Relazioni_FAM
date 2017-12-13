import matplotlib.pyplot as plt
import numpy as np
import sys

## Import given files

files = []

#for i in range(1, len(sys.argv)-1):
#	files.append(open(sys.argv[i], 'r'))
files.append(open("C:\\Users\\carli\\Dropbox\\UNIVERSITY!\\Fisica applicata alla medicina\\RELAZIONI\\PRIMA PROVA\\Dall\'Olio_Montanari\\ALBUME\\CPMG\\CPMGalbume1B.dat", 'r'))

## Extract columns sigT and sig

sigT = []
sig  = []

j = -1

for file in files:
	line = [lines for lines in file]
	sigT.append([])
	sig.append([])
	++j
	for i in range(1, len(line)-1):
		columns = line[i].split(",")
		if len(columns) > 7:
			sigT[j].append(float(columns[5]))
			sig[j].append(float(columns[7]))

fig, ax = plt.subplots()

# the histogram of the data
ax.plot(sigT[0], sig[0], 'o')
plt.show()




