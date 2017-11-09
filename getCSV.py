#requires that this file be run from the GetFonts folder


from PIL import Image, ImageFilter, ImageOps
import csv
import sys
import os

def sumArray(A):
    sum = 0
    for x in A:
        sum = sum + x
    return sum


#gets the center of mass of a 2-dimensional array of numbers,
    #flattened to 1 dimension
def getCOM(valueList, height, width):
    column = [0]*height              #a single column to hold row sums
    for i in range(0, height):
        rowSum = 0
        for j in range(0, width):
            rowSum = rowSum + valueList[i*width + j]
        column[i] = rowSum
    sumZ = sumArray(column)     #sum of whole file

    sumYZ = 0
    for i in range(0, height):
        sumYZ = sumYZ + i*column[i]
    yBar = sumYZ/sumZ


    row = [0]*width                  #a single row to hold column vectors
    for i in range(0, width):
        colSum = 0
        for j in range(0, height):
            colSum = colSum + valueList[j*width + i]
        try:
            row[i] = colSum;
        except IndexError:
            print(i)
            print(width)
            raise(IndexError)
    #sumZ is the same

    sumXZ = 0
    for i in range(0, width):
        sumXZ = sumXZ + i*row[i]
    xBar = sumXZ/sumZ

    return (int(xBar), int(yBar))   #both rouned down to put the center of mass within the right pixel

def getCSV(fontName, fileName):
    currentDir = os.getcwd()        #returns a string of the current directory
    currentDir = currentDir.replace('\\','/');  #formats directory name

    fullFileName = currentDir + '/Fonts/' + str(fontName) + '/' + str(fileName)

    im = Image.open(fullFileName).convert('L')    ##convert to greyscale
    mi = ImageOps.invert(im)       #invert to get number to be nonzero
    cropped = mi.crop(mi.getbbox())    #replace 'box' with a 4-tuple
    null, null, width, height = cropped.getbbox()    #store width and length

    if(height > width):
        newHeight = 20
        newWidth = 20*width/height
    else:
        newWidth = 20
        newHeight = 20*height/width

    newWidth = int(newWidth)                #rounding introduces a little error
    newHeight = int(newHeight)

    resized = cropped.resize((newWidth,newHeight))

    #get coordinates of center of mass
    xBar, yBar = getCOM(list(resized.getdata()), newHeight, newWidth)

    #create 28x28 canvas
    canvas = Image.new('L', (28,28))

    #get upper left corner of character on canvas
    (x,y) = (13 - xBar, 13 - yBar)      #xBar and yBar should never be more than 13

    #paste character onto canvas
    canvas.paste(resized, (x,y))

    #getdata() -> save as csv
    dataList = list(canvas.getdata())

    with open(currentDir + '/Fonts/' + str(fontName) + '/' + str(fontName) + '.csv', 'a+') as myfile:
        wr = csv.writer(myfile, lineterminator='\n')
        row = [fileName[0]]
        for i in range(len(dataList)):
            row.append(dataList[i])
        wr.writerow(row)
        myfile.close()

#TODO: write file to CSV all on one line, appending if it already exists
