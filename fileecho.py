#Read in the echo.txt file and display it in the terminal using print()
#This is a guided practice. Either follow the video or your instructor in class.

EchoFile = open("echo.txt")

Curline = EchoFile.readline()
Junkline = EchoFile.readline()
TheRest = EchoFile.read()

EchoFile.close()

print(Curline)
print(TheRest)