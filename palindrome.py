#For this assignment use the words.txt file.
#Read in all the words. Count how many are palindromes, or words that are spelled the same forwads and backwards.
#For example, wow is a paldindrome.
#A different file wile be used for grading.
#Correct answer for this file: 


#Open words.txt file. Lets get this started.
PalindromeFile = open("words.txt")

#Read all lines and split information into separate lines.
ListedWords = PalindromeFile.read().splitlines()

#Close the file, no need to crash the system
PalindromeFile.close()

#Initialize palindrome counter to zero since its good practice.
PalindromeCounter = 0

#Loop and Look through the words and check for words that are palindromes.
for Word in ListedWords:
    #Check to see if the word is the same if reversed and add one to counter if true.
    if Word == Word[::-1]:
        PalindromeCounter += 1

#Display the total amount of palindromes in the file. Quest Completed. +100 Gold
print(f"The number of palindromes in the file is {PalindromeCounter}")