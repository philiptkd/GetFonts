# this is a port of a .bat file

from os import listdir, getcwd, makedirs, remove, rename
from os.path import isfile, join, exists
from replace import replace
from changeFontName import changeFontName
from getCSV import getCSV
import subprocess

#get current working directory
cwd = getcwd()

#get directory of the Fonts folder
fontsDir = cwd + '\\Fonts'

#get list of file names with extensions .ttf
fontFilesList = [f for f in listdir(fontsDir) if isfile(join(fontsDir,f)) and f[-4:] == '.ttf']

#strip file extensions from names
fontList = [f[0:-4] for f in fontFilesList]

#for every font with a .ttf in Fonts\ but no corresponding folder
for font in fontList:
    thisFontDir = fontsDir+'\\'+font
    if not exists(thisFontDir):
        #make directory in Fonts\
        makedirs(thisFontDir)
                                               
        #call changeFontName.py with argument font
        changeFontName(font)

        #change name of font within config.bmfc in two places
        replace('config.bmfc', '(?<=fontName=)(.*)', font)
        replace('config.bmfc', '(?<=fontFile=Fonts/)(.*?)(?=\.ttf)', font)

        #for each of the characters '0' - '9'
        for charNum in range(48,58):
            #edit the config file to update the character we want a .png of
            replace('config.bmfc', 'chars=..', 'chars='+str(charNum))

            #call mbfont to create the .png
            subprocess.run(['bmfont.com', '-c', 'config.bmfc', '-o', 'Fonts/'+font+'/'+str(charNum-48)+'.fnt'])

            #call getCSV.py with arguments font and str(charNum-48)+'_0.png'
            getCSV(font, str(charNum-48)+'_0.png')

        #delete all the .fnt files
        for f in listdir(thisFontDir):
            if isfile(join(thisFontDir,f)) and f[-4:] == '.fnt':
                remove(join(thisFontDir,f))

        #rename all the .png files
        for f in listdir(thisFontDir):
            if isfile(join(thisFontDir,f)) and f[-4:] == '.png':
                rename(join(thisFontDir,f), join(thisFontDir,f[0]+'.png'))

