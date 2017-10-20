@echo off

rem - this batch file converts .ttf files into .csv files with the digits 0-9 each represented
rem - the digits are size-normalized to 20x20 and centered by mass into a 28x28 field

setlocal enabledelayedexpansion

rem - for every .ttf file in Fonts/
for %%f in (Fonts/*.ttf) do (	
rem - make a folder named after the .ttf file
	md Fonts\%%~nf
	
	rem - change font name associated with .ttf file
	python changeFontName.py %%~nf
	
	rem - change the fontName in the bmfont config file
	python -c "import replace; replace.replace('config.bmfc', '(?<=fontName=)(.*)', '%%~nf'); replace.replace('config.bmfc', '(?<=fontFile=Fonts/)(.*?)(?=\.ttf)', '%%~nf')"
	
	rem - 48-57 are the characters '0'-'9'
	for /l %%x in (48, 1, 57) do (	
		rem - edit the config file to update the character we want a .png of		
		python -c "import replace; replace.replace('config.bmfc', 'chars=..', 'chars=%%x')"
		
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