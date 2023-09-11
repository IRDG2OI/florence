"""
***************************************************************************
    Florence
    ---------------------
    Date                 : July 2023
    Copyright            : (C) Matteo Contini & Sylvain POULAIN
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation version 3+ of the License, or (at your   *
*   option) any later version.                                            *
*                                                                         *
***************************************************************************
"""
import os
# Importing the PIL library
from PIL import Image
from PIL import ImageDraw, ImageFont
# Define the directory path
dir_path = "/home/sylvain/Documents/IRD/admin/deplacement/Madagascar2"
# Get a list of all files in the directory
files = os.listdir(dir_path)
fillcolor = "black"
shadowcolor = "white"
# Custom font style and font size
font = '/usr/share/fonts/TTF/verdana.ttf'
x = y = 20

for file in files :
    img_path = os.path.join(dir_path, file)
    if file.endswith(('.jpg', '.png', 'jpeg', '.JPG')):
        img = Image.open(img_path)
        text = os.path.splitext(file)[0].replace("_", " ")
        # fontsize = 1  # starting font size # portion of image width you want text width to be
        # img_fraction = 1
        # myFont = ImageFont.truetype('{}'.format(font), fontsize)
        # while myFont.size(text)[0] < img_fraction*img.size[0]:
        # while myFont.size < img_fraction*img.size[0]:
        #     # iterate until the text size is just larger than the criteria
        #     fontsize += 1
        #     myFont = ImageFont.truetype('{}'.format(font), fontsize)
        # optionally de-increment to be sure it is less than criteria
        # fontsize -= 1
        # fontsize = img.size[0]/1024*20.48
        fontsize = img.size[0]/1024*48
        myFont = ImageFont.truetype('{}'.format(font), fontsize)
        # Open an Image
        draw = ImageDraw.Draw(img)
        # thin border
        draw.text((x-1, y), text, font=myFont, fill=shadowcolor)
        draw.text((x+1, y), text, font=myFont, fill=shadowcolor)
        draw.text((x, y-1), text, font=myFont, fill=shadowcolor)
        draw.text((x, y+1), text, font=myFont, fill=shadowcolor)
        # thicker border
        draw.text((x-1, y-1), text, font=myFont, fill=shadowcolor)
        draw.text((x+1, y-1), text, font=myFont, fill=shadowcolor)
        draw.text((x-1, y+1), text, font=myFont, fill=shadowcolor)
        draw.text((x+1, y+1), text, font=myFont, fill=shadowcolor)
        # now draw the text over it
        draw.text((x, y), text, font=myFont, fill=fillcolor)
        # Save the edited image
        img.save(img_path)
