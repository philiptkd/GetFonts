@echo off

rem - this batch file calls bmfont once each for the digits 0 - 9

rem - the config.bmfc file still needs to be edited manually to change fontName and fontFile
rem - TODO: once font names in .ttf have been changed to match file names, find and replace fontName and fontFile to match %%~nf in the for loop
 
setlocal enabledelayedexpansion

rem - for every .ttf file in Fonts/
for %%f in (Fonts/*.ttf) do (	
rem - make a folder named after the .ttf file
	md Fonts\%%~nf
	
	rem - 48-57 are the characters '0'-'9'
	for /l %%x in (48, 1, 57) do (	
		rem - edit the config file to update the character we want a .png of		
		python replace.py config.bmfc chars=.. chars=%%x
		
		set /a "y=%%x-48"
		
		rem - call bmfont to create the .png
		bmfont.com -c config.bmfc -o Fonts/%%~nf/!y!.fnt

		rem - call python script to convert .png to .csv
		python getCSV.py %%~nf !y!_0.png
	)
	
	rem - delete all the .fnt files
	del Fonts\%%~nf\*.fnt			

	rem - simplify names of .png files	
	rename Fonts\%%~nf\?_0.png ?.png	
)

endlocal