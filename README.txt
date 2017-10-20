Converts every .ttf file in the Fonts/ folder into a .csv with one line per digit 0-9
Each digit is size-normalized to 20x20 and centered by mass in a 28x28 field

Call script.bat from the command line (on Windows).

It uses bmfont.exe to output .png files for each digit 0-9 in the font specified.
It uses ttx command from python package fonttools to rename fonts within .ttf files.
It uses the pillow python package to convert from .png to .csv

Each digit is output to .csv in multiple lines to be readable in a spreadsheet viewer.
For input into the existing neural net, each must be output as a single line instead

The next step is to put .csv representations of the digits from all .ttf files in the same file