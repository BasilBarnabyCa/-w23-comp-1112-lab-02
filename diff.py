# Imports
import os

different = False
firstDifferentLine = ""
secondDifferentLine = ""

# Get file names form users
fileName1 = input("What file do you want to select? ")
fileName2 = input("What file do you want to compare? ")

# Reading in files
firstFile = open(fileName1, "r")
secondFile = open(fileName2, "r")

# Breaking up files into a list of lines
#firstText = firstFile.read()
#firstFileLines = firstText.split("\n")
firstFileLines = firstFile.readlines()

#secondText = secondFile.read()
#secondFileLines = secondText.split("\n")
secondFileLines = secondFile.readlines()

# Loop breaks when lines do not match
for i in range(len(firstFileLines)):
	if(firstFileLines[i] == secondFileLines[i]):
		print("Yes")
	else:
		print("No")
		firstDifferentLine = firstFileLines[i]
		secondDifferentLine = secondFileLines[i]
		different = True
	 
	if(different):
		break

# Checking if Reports folder exists and creating if it doesn't
if not os.path.exists("Reports"):   
	os.mkdir("Reports")

# Creating report files based whether or not all lines in both files match
if(different):
	result = open("Reports/sampleDifferent.txt", "w")
	result.write(fileName1 + " is not the same as " + fileName2 + ".\nThey differ at the following lines:\n")
	result.write(fileName1 + ": " + firstDifferentLine)
	result.write(fileName2 + ": " + secondDifferentLine)
	result.truncate()
	result.close()
else:
	result = open("Reports/sampleSame.txt", "w")
	result.write(fileName1 + " is the same as " + fileName2)
	result.truncate()
	result.close()
