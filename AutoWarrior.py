import keyboard
import time
import PIL
from random import randrange

def get_pixel_colour(i_x, i_y):
	import PIL.ImageGrab
	return PIL.ImageGrab.grab().load()[1090, 894]

def get_pixel_colourrage(i_x, i_y):
	import PIL.ImageGrab
	return PIL.ImageGrab.grab().load()[219, 79]

def get_pixel_colourhp(i_x, i_y):
	import PIL.ImageGrab
	return PIL.ImageGrab.grab().load()[356, 63]

def get_pixel_colourcom(i_x, i_y):
	import PIL.ImageGrab
	return PIL.ImageGrab.grab().load()[40, 90]



check = get_pixel_colourcom(0, 0)
print(check);



def hs_helper():


     while True:
          
          check = get_pixel_colourcom(0, 0)
          print(check);
            

          first = 0

          col = get_pixel_colour(0, 0)
          rage = get_pixel_colourrage(0, 0)
          hp = get_pixel_colourhp(0, 0)
          com = get_pixel_colourcom(0, 0)

        
          #if rage is above a certain threshold cast heroic strike to dump rage
          if rage[0] == 155 and hp == (0, 166, 0):
               
                    print("HS Dump!")
                    #cast bloodthirst
                    keyboard.press('f')
                    keyboard.release('f')
                    #cast heroic strike
                    keyboard.press('2')
                    keyboard.release('2')

 
          #if rage is above a certain threshold cast heroic strike to dump rage
          elif rage[0] == 162 and hp == (0, 166, 0):

                    print("HS Dump!")
                    keyboard.press('f')
                    keyboard.release('f')
                    keyboard.press('2')
                    keyboard.release('2')
                    

          #if in combat and enemy hp bar is above 20% cast bloodthirst
          elif hp == (0, 166, 0) and com[1] == 59 and com[2] == 49:

                    print("Bloodthirst!")
                    keyboard.press('f')
                    keyboard.release('f')
                    #time.sleep(.15)


# optional casting of execute, took this out since in many scenarios you might want to save rage
##          elif col[1] > 25:
##
##                    print("Execute")
##                    keyboard.press('1')
##                    keyboard.release('1')           

          else:
               pass

          
         


        
#call the method to run the script
hs_helper()


