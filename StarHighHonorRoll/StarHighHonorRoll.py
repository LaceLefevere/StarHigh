#Program: KatieKingStarHighHonorRoll
#Author: Katie King
#Description: a Python program that reads from the grades.dat file and processes the records in order to produce the following:
#The total number of students in the file
#The number and percentage of A Honor Roll students
#The number and percentage of B Honor Roll students
#An output file named AHonorRoll.dat that contains the names of the A Honor Roll students, sorted by last name alphabetically from A-Z
#An output file named BHonorRoll.dat that contains the names of the B Honor Roll students, sorted by last name alphabetically from A-Z.


# Open the file Grades.dat
from posixpath import split


grades = open("grades.dat")

aHonorRollStudents = []
bHonorRollStudents = []
totalStudents = 0

print("Processing student grades...") 

for line in grades:

# Split delimited input records into individual fields 
    studentInfo = line.split(",")
    names = studentInfo[0].strip()  # student names
    studentID = int(studentInfo[1])  # student ID
    gradeAvg = int(studentInfo[2])  # Student grade
    totalStudents = totalStudents + 1 # accumulate total number of students in input file

# append A & b honor roll student names to approprate lists
    if (gradeAvg >= 90):

        aHonorRollStudents.append(names)
    else:
        if (gradeAvg >= 80 < 90):

            bHonorRollStudents.append(names)

# close all files 
grades.close()

# sort A and B honor roll student names in acending order
aHonorRollStudents.sort()
bHonorRollStudents.sort()

# identify number and percent of A and B honor roll students 
AHonorRollTotal = int(len(aHonorRollStudents))
aHonorRollPercent =  (AHonorRollTotal / totalStudents)* 100
BHonorRollTotal = len(bHonorRollStudents)
bHonorRollPercent = (BHonorRollTotal / totalStudents) * 100

# display "summary status" as seen in sample run image 
print("processing complete")
print("")
print("SUMMARY STATISTICS")
print(" - - - - - - - - - -")
print("Total students: ", totalStudents)
print("A Honor Roll Students: ", AHonorRollTotal, "({:,.2f}".format (aHonorRollPercent), "%)" )
print("B Honor Roll Students: ", BHonorRollTotal, "({:,.2f}".format (bHonorRollPercent), "%)" )
print("")


# write A honor roll students to aHonorRoll.dat
outputFile = open("AHonorRoll.dat", "w")
for student in aHonorRollStudents:
    outputFile.write(student)
outputFile.close()
print("AHonorRoll.dat file created...")

# write b honor roll students to bHonorRoll.dat
outputFile = open("BHonorRoll.dat", "w")
for student in bHonorRollStudents:
    outputFile.write(student)
outputFile.close()

print("BHonorRoll.dat file created...")
print("")
print ("End of program")
