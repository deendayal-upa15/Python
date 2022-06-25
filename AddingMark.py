# -*- coding: utf-8 -*-
"""
Created on Sun Jun 5 22:33:16 2022

@author: Deendayal
"""

"""
This Programme Add Logos/signature/name to existing image/images.
"""

# importing Libraries
from PIL import Image, ImageDraw, ImageFont
import os

# Image, for Manipulating Images
# ImageDraw for drawing shapes and marks
# ImageFont for adding font and texts

"""
# Selecting logo file
# If you want to add logo to an image

logoPath = "Sign.jpg"
logo = Image.open(logoPath) #open logo/image
logo1 = logo.resize((216, 114))
logo1.save("logo.jpg")

# You can take input or just write it down in code. Resize image as you want.
"""

# Function to add logo:
# image.paste(logo, position) will add logo to image. you can directly use it while writing program.

def logoAdd(image,logo):
    image.paste(logo, (10,10))
    return image

# Function to add Text or mark image:
# It will take input as image, text and font (default is arial, type name of .ttf file). It gives image in return.

def textAdd(image, text, textfont='arial.ttf'):
    ImWidth, ImHeight = image.size
    draw = ImageDraw.Draw(image) # for drawing and text
    fontsFolder = 'FONT_FOLDER' # e.g. ‘/Library/Fonts'
    fontSize = int((45/4624)*ImWidth)
    Font = ImageFont.truetype(os.path.join(fontsFolder, textfont), fontSize)
    print("adding signature text...")
    draw.text((10,10), text, fill='white', font=Font)
    return image
# ImageDraw.Draw(image) makes a drawing canvas to write text. choose font library in fontsFolder. We get desired font in Font in preferable font size and write text with draw.text(position, text, fill, font) and return image. (fill and font have default value as None.)

# Here is a hack. Images can have different sizes in that case, if we are having same font size for all images may lead us to destruction of image. We use font size according to width of image, fontSize = (45/4624)*ImWidth.

"""
# ImageDraw:
# With ImageDraw we can draw lines, circles and other shapes. We can use draw.line([points to join], fill) to draw line between points.

# Just like line we can also draw rectangle(points,fill=None, outline=None, width=1); ellipse(); polygon().

# for drawing shapes

im = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(im)

draw.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill='black')
draw.rectangle((20, 30, 60, 60), fill='blue')
draw.ellipse((120, 30, 160, 60), fill='red')
draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)), fill='brown')

im.save('drawing.png')
"""

# Main function (single image):
# Takes path, filename and text from the user. checks path is correct or not with exception handling. If a file exists in folder then modify that image and save it as file_modified.png. else shows file doesn't exist.

while True:
    start = str(input("Press y to start... \n"))
    if start == 'y' or start == 'Y':
        filePath = str(input("Enter file Path: "))
        try:
            os.chdir(filePath)
        except FileNotFoundError:  
            print("Input is invalid. Please Enter valid path.")
            continue
        filename = str(input("Enter Image name(with extention (.jpg/.png)): "))
        if filename in os.listdir('.'):
            os.makedirs('Modified', exist_ok=True) # for saving modified file
            text = str(input("Enter text/name you want to add: "))
            img =Image.open(filename)
            CopyImg = img.copy()

            CopyImg2 = textAdd(CopyImg, text)

            #saving file
            name = filename[:-4] + "_modified.png"
            CopyImg2.save(os.path.join('Modified', name))
        else:
            print("File doesn't exist in given folder. if you typed wrong please type with extension.")
        
    else:
        print('See you Soon...')
        break
    
# Note: You can also save image as jpg. just replace png with jpg.

# FileNotFoundError:
# If file doesn't exist (or invalid path) os raises this error.

# os.makedirs('Modified', exist_ok=True) makes new folder to save modified images, it skips if folder already exists.
"""
# Main function (multiple images):
# Takes path and text from the user. checks path is correct or not with exception handling. check every file if an image or not then modify that file and save it as file_modified.png. else shows file doesn't exist.


while True:
    start = str(input("Press y to start... \n"))
    if start == 'y' or start == 'Y':
        filePath = str(input("Enter file Path: "))
        try:
            os.chdir(filePath)
            os.makedirs('Modified', exist_ok=True) # for saving modified file
        except FileNotFoundError:  
            print("Input is invalid. Please Enter valid path.")
            continue
        text = str(input("Enter text/name you want to add: "))
        for filename in os.listdir('.'):
            #filtering image files
            if not (filename.endswith('.png') or filename.endswith('.jpg')): #or filename == logofile (if logo is in same folder)
                continue #pass if file is not image file
                
            #open file
            img =Image.open(filename) 
            CopyImg = img.copy() #making a copy, it doesn't effect original image.

            CopyImg2 = textAdd(CopyImg, text) #calling textAdding function and saving file in second copy

            #saving file
            name = filename[:-4] + "_modified.png"  # modifying name
            CopyImg2.save(os.path.join('Modified', name))
        
    else:
        print('See you Soon...')
        break
"""  

##############   END OF SCRIPT   ############
