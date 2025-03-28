#For this assignment use the numbers.txt file.
#A different numbers.txt will be used for grading.
#Read in all the numbers. Display the following information:
#How many numbers in the file
#Total of all the number
#Average
#Highest number
#Lowest number
#Correct answers for the included file:


#Open numbers file. It has Begun!
NumFile = open("numbers.txt")

#Read all lines and split information into lines.
ListedNumbers = NumFile.read().splitlines()

#Close file before Processes.
NumFile.close()

#Convert and Store listed numbers from the txt file.
NumList = [int(Nums) for Nums in ListedNumbers]

#Total numbers in txt file.
TotalNumbers = len(NumList)

#Sum of all Numbers in txt file.
TotalSum = sum(NumList)

#Average of Numbers in txt file.
Average = TotalSum / TotalNumbers if TotalNumbers != 0 else 0

#Highest Number in txt file.
HighestNum = max(NumList)

#Lowest Number in txt file.
LowestNum = min(NumList)

#Displays for Resulting Information. Mission Accomplished!
print(f"The Total numbers in the list: {TotalNumbers}")
print(f"Total sum of the numbers: {TotalSum}")
print(f"The Average of the numbers: {Average}")
print(f"Highest number in the list: {HighestNum}")
print(f"Lowest number in the list: {LowestNum}")