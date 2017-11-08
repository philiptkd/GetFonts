import glob, os
from PIL import Image
from PIL.ImageOps import invert

def transform(dir):
    # Pull a list of all .png files in the CWD
    image_list = glob.glob(dir+'/*.png')

    # Iterate through Images and perform 29 mutations of each.
    for i in image_list:
        filename, extension = os.path.splitext(i)
        image = Image.open(i)
        count = 0
        for j in range (-16, 17, 2):
            for k in range (-16, 17, 2):
                # invert so backgroud values are 0
                new_image = invert(image)

                # Deform image based on k
                new_image = deform(new_image, k)

                # Rotate image based on j
                new_image = rotate(new_image, j)

                new_image = new_image.crop(new_image.getbbox())

                # invert back
                new_image = invert(new_image)

                # Save new mutation to a new file
                new_filename = filename + "_" + str(count) + extension
                new_image.save(new_filename)
                new_image.close()
                count += 1
        image.close()
        os.remove(filename+extension)

# Subroutine for randomly rotating an image up to 16 degrees left or right
def rotate(image, degrees):
    mod_file = image.rotate(degrees, expand=True)
    return mod_file

# Subroutine for randomly stretching or squishing an image up to 16% vertically
def deform(image, magnitude):
    width, height = image.size
    magnitude = magnitude / 100
    mod_file = image.resize((width, int(height+height*magnitude)))
    return mod_file
