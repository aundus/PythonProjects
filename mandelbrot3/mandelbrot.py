'''
Created on Nov 2, 2017
Description: Creates a mandlebrot set based on complex numbers
@author: Adam Undus
'''

from cs5png import PNGImage

def update(c,n):
    """ updates the sum of the complex values c"""
    z = 0
    ct = 0
    while ct < n:
        z = z ** 2 + c
        ct += 1
    return z

def inMSet(c,n):
    """ checks if the complex number c is in the set"""
    ct = 0
    z = 0
    while ct < n:
        if abs(z) > 2:
            return False
        z = z ** 2 + c
        ct += 1
    return True

def scale(pix, pixMax, floatMin, floatMax):
    ''' scale takes in pix, the CURRENT pixel column (or row) pixMax, the total # of pixel columns
    floatMin, the min floating-point value floatMax, the max floating-point value scale returns the floating-point value thatcorresponds to pi'''
    mult = pix/pixMax
    diff = (floatMax - floatMin)/floatMax
    return diff * mult + floatMin


def mset():
    """ creates a 300x200 image of the Mandelbrot set"""
    width = 300
    height = 200
    image = PNGImage(width, height)
    for col in range(width):
        for row in range(height):
create the complex number, c!
            x = scale(col, width, -2.0, 1.0)
            y = scale(row, height, -1.0, 1.0)
            c = x + y*1j
            if inMSet( c, 25 ) == True:
                image.plotPoint(col, row)
    image.saveFile()
mset()
    
