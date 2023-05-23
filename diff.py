import os

different = False
# Get file names form users
fileName1 = input("What file do you want to select? ")
fileName2 = input("What file do you want to compare? ")

# Reading in files
sample0 = open("./lab/" + fileName1, "r")
sample1 = open("./lab/" + fileName2, "r")

# Breaking up files into a list of lines
sample0Text = sample0.read()
sample0Lines = sample0Text.split("\n")

sample1Text = sample1.read()
sample1Lines = sample1Text.split("\n")

for sample1Line in sample0Lines:
    for sample2Line in sample1Lines:
        if(sample1Line == sample2Line):
            print("Yes")
        else:
            print("No")
            different = True
            break
        
os.mkdir("./lab/Reports")

if(different):
    diffResult = open("./lab/Reports/sampleDifferent.txt", "W")
    different.write(fileName1 + "is not the same as " + fileName2)
            
