Call script.bat from the command line (on Windows).

It uses bmfont.exe to output .png files for each digit 0-9 in the font specified.
It uses ttx command from python package fonttools to rename fonts within .ttf files.
It uses the pillow python package to convert from .png to .csv

Working on having it convert every .ttf in a directory
Font name is hardcoded in bmfont config file right now
Also, each digit is output to .csv in multiple lines to be readable in a spreadsheet viewer.
For input into the existing neural net, each must be output as a single line instead