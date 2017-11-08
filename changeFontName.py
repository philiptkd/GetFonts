import subprocess
import sys
import replace
import os

#changes the font name in a .ttf file to be the same as the file name (no spaces)

def changeFontName(fileName):
	#make the ttx file
	subprocess.run(["ttx", "Fonts/" + fileName + ".ttf"])

	#create new string of fileName with a space inserted after every captial letter that's not the first character in the string
	spacedName = "";
	for c in fileName:
		if(c.isupper() and c != fileName[0]):
			spacedName = spacedName + " "
		spacedName = spacedName + c

	#look for spacedName string in fileName.ttx, replace with fileName
	replace.replace("Fonts/" + fileName + ".ttx", spacedName, fileName)

	#make new ttf file
	subprocess.run(["ttx", "-f", "Fonts/" + fileName + ".ttx"])

	#delete ttx file
	os.remove("Fonts/" + fileName + ".ttx")
