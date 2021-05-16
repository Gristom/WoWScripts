import keyboard
import time
#import the pillow library for tracking pixel colors on the screen
import PIL
from random import randrange
#used for simulating mouseclicks
import pyautogui


def get_pixel_colour(i_x, i_y):
	import PIL.ImageGrab
	return PIL.ImageGrab.grab().load()[1090, 894]

def get_pixel_colourmana(i_x, i_y):
	import PIL.ImageGrab
	return PIL.ImageGrab.grab().load()[245, 79]

def get_pixel_colourmh(i_x, i_y):
	import PIL.ImageGrab
	return PIL.ImageGrab.grab().load()[1124, 876]

def get_pixel_colourhp(i_x, i_y):
	import PIL.ImageGrab
	return PIL.ImageGrab.grab().load()[356, 63]

def get_pixel_colourcom(i_x, i_y):
	import PIL.ImageGrab
	return PIL.ImageGrab.grab().load()[746, 893]

def get_pixel_enemyhpmin(i_x, i_y):
	import PIL.ImageGrab
	return PIL.ImageGrab.grab().load()[325, 64]

def get_pixel_rangeindicator(i_x, i_y):
	import PIL.ImageGrab
	return PIL.ImageGrab.grab().load()[409, 1031]

def get_pixel_enemybarcol(i_x, i_y):
	import PIL.ImageGrab
	return PIL.ImageGrab.grab().load()[328, 44]

def get_pixel_castbar(i_x, i_y):
	import PIL.ImageGrab
	return PIL.ImageGrab.grab().load()[837, 869]

def get_pixel_target(i_x, i_y):
	import PIL.ImageGrab
	return PIL.ImageGrab.grab().load()[802, 159]

def get_pixel_myhp(i_x, i_y):
	import PIL.ImageGrab
	return PIL.ImageGrab.grab().load()[232, 63]

def get_pixel_lowhp(i_x, i_y):
	import PIL.ImageGrab
	return PIL.ImageGrab.grab().load()[160, 63]

def get_pixel_hphit(i_x, i_y):
	import PIL.ImageGrab
	return PIL.ImageGrab.grab().load()[258, 63]

def get_pixel_enemycastbar(i_x, i_y):
	import PIL.ImageGrab
	return PIL.ImageGrab.grab().load()[368, 163]

def get_pixel_enemyhplow(i_x, i_y):
	import PIL.ImageGrab
	return PIL.ImageGrab.grab().load()[345, 64]


def image():


     #tracks whether you are in combat
     combat = 0
     #tracks whether you have recently drank to full mana
     drink = 0
     #tracks if you have started to drink
     starteddrink = 0
     #tracks how many turns you have made
     turns = 0
     #tracks how many times you have executed running around
     executions = 0
     #tracks conjuring of food
     conj = 0
     #tracks if the emergency procedure for low hp has been run
     ran = 0
     #tracks inching forward
     inch = 0
     running = 0
     #counts how many times small inches forward have been done
     inchcount = 0
     #tracks if you have shielded yourself recently
     shield = 0
     #tracks if you have been hit by an enemy
     hitfirst = 0
     #tracks if an enemy has been sighted
     sighted = 0
     #tracks if you need to turn
     turnswitch = 0
     #tracks the time the program has been executing for
     start = time.time()





     


     while True:


          end = time.time()

          timer = (end - start)




          

          col = get_pixel_colour(0, 0)
          mana = get_pixel_colourmana(0, 0)
          hp = get_pixel_colourhp(0, 0)
          com = get_pixel_colourcom(0, 0)
          enemyhpmin = get_pixel_enemyhpmin(0, 0)
          rangeindicator = get_pixel_rangeindicator(0, 0)
          barcol = get_pixel_enemybarcol(0, 0)
          castbar = get_pixel_castbar(0, 0)
          target = get_pixel_target(0, 0)
          myhp = get_pixel_myhp(0, 0)
          lowhp = get_pixel_lowhp(0, 0)
          enemylowhp = get_pixel_enemyhplow(0, 0)

          enemycastbar = get_pixel_enemycastbar(0, 0)

          washit = get_pixel_hphit(0,0)

          test = get_pixel_hphit(0, 0)
          

          print(executions);
          print("")
          print(washit);
         
 







          #Low Hp emergency procedure

          #if hp is dangerously low while in combat
          if lowhp != (0, 175, 0) and ran == 0 and combat == 1:


                print('run away');

                keyboard.release('w')
            
                #cast cold snap
                keyboard.press('u')
                keyboard.release('u')
                
                time.sleep(1.7)

                #cast frost nova
                keyboard.press('1')
                keyboard.release('1')

                #move backwards for 1.8 secs
                keyboard.press('s')
                time.sleep(1.8)

                #cast ice barrier
                keyboard.press('5')
                keyboard.release('5')

                #move backwards for 1.7 secs
                keyboard.release('s')
                
                time.sleep(1.7)
 
                #cast evocation for 8 secs
                keyboard.press('g')               
                time.sleep(8)
                keyboard.release('g')
                
                #cast mana shield
                keyboard.press('x')
                keyboard.release('x')
        
                
                #indicate that there was an attempt to run away from an enemy
                ran = 1

                #indicate the character will need to drink
                starteddrink = 0





          #interrupt a cast  

          #if the enemy has a cast bar showing  
          elif enemycastbar == (255, 176, 0):

                  keyboard.release('w')

                  #wait .9 seconds  
                  time.sleep(.9)

                  #cast counterspell  
                  keyboard.press('i')
                  keyboard.release('i')

                  starteddrink = 0

          #Turn to face target
        
          #if there is an error message indicating your are not facing the target
          elif target == (0, 255, 0) or target == (102, 10, 10):

                print('spin to find target');
                  
                keyboard.release('w')
                keyboard.press('a')
                time.sleep(.35)
                keyboard.release('a')

                turns = turns + 1

                starteddrink = 0
                 
          
          #Inch closer to enemy

          elif enemyhpmin[0] == 0 and enemyhpmin[1] > 100 and enemyhpmin[2] == 0 and rangeindicator == (255, 26, 26) and(barcol == (209, 206, 0) or barcol == (209, 0, 0)) and sighted == 0:

                time.sleep(1.5)
                keyboard.release('w')

                inch = inch + 2
                inchcount = inchcount + 2

                sighted = 1
                shield = 0

                starteddrink = 0
                

          #Inch closer to enemy
            
          elif enemyhpmin[0] == 0 and enemyhpmin[1] > 100 and enemyhpmin[2] == 0 and rangeindicator == (255, 26, 26) and(barcol == (209, 206, 0) or barcol == (209, 0, 0)) and sighted == 1:

                print("inch closer")

                keyboard.release('w')    
                keyboard.press('w')
                time.sleep(.75)
                keyboard.release('w')

                
                inch = inch + 1
                inchcount = inchcount + 1
                starteddrink = 0

                executions = executions + 1


                if inch > 5:

                        pyautogui.moveTo(143, 616, duration=.1)
                        pyautogui.leftClick(143, 616)
                        sighted = 0
                

                else:
                        pass



          #Attack


          elif enemyhpmin[0] == 0 and enemyhpmin[1] > 100 and enemyhpmin[2] == 0 and(barcol == (209, 206, 0) or barcol == (209, 0, 0)):

                print("attack")

                inch = 0
                keyboard.release('w')
                starteddrink = 0

                attackselect = randrange(3)

                #if you have not been hit yet and your hp starts to fall
                if washit != (0, 210, 0) and hitfirst == 0:
                        
                        keyboard.press('s')
                        time.sleep(0.05)
                        keyboard.release('s')
                        time.sleep(0.1)
                        #cast fire blast
                        keyboard.press('4')
                        keyboard.release('4')
                        time.sleep(1.7)
                        #cast frost nova
                        keyboard.press('1')
                        keyboard.release('1')
                        #move back for .8 secs
                        keyboard.press('s')
                        time.sleep(0.8)
                        keyboard.release('s')

                        hitfirst = 1
                        
                #cast fire blast
                elif attackselect == 0 or attackselect == 1:

                        keyboard.press('4')
                        keyboard.release('4')

                #cast ice barrier        
                elif attackselect == 2 or attackselect == 3:
                        
                        keyboard.press('5')
                        keyboard.release('5')               

                else:
                        pass

                #cast frostbolt
                keyboard.press('2')
                keyboard.release('2')

                #indicate that you have entered combat     
                combat = 1


          #Drinking

          #if mana or hp are below a threshold  
          elif mana != (0, 0, 155) or myhp != (0, 211, 0):

                keyboard.release('w')  

                print('drink');

                #indicate you have started drinking
                drink = 1

                keyboard.release('w')

                        
                if starteddrink == 0:

                       starteddrink = starteddrink + 1

                #eat and drink
                if starteddrink == 3:

                        keyboard.press('o')
                        keyboard.release('o')
                        keyboard.press('t')
                        keyboard.release('t')

                        starteddrink = starteddrink + 1                        
                
                
                elif starteddrink < 18:

                        starteddrink = starteddrink + 1
                        time.sleep(1)

                else:
                        starteddrink = 0


                

          #Looting                

          elif combat == 1 and (barcol != (209, 206, 0) or barcol != (209, 0, 0)):

                print('loot');
           

                starteddrink = 0
                
                keyboard.release('w')

                #wand just in case the enemy had a sliver of hp left not shown on hp bar    
                keyboard.press('k')
                keyboard.release('k')

                #inch back forward if you backed up from getting hit
                if hitfirst == 1:

                        keyboard.press('w')
                        time.sleep(0.4)
                        keyboard.release('w')

                else:

                hitfirst = 0

                keyboard.press('w')
                keyboard.release('w')
                keyboard.press('s')
                keyboard.release('s')

                #right click all over the middle of the screen to attempt to loot the corpse

                pyautogui.moveTo(960, 540, duration=.3)
                pyautogui.rightClick(960, 540)


                pyautogui.moveTo(1150, 540, duration=.1)
                pyautogui.rightClick(1150, 540)

                pyautogui.moveTo(870, 540, duration=.1)
                pyautogui.rightClick(870, 540)

                pyautogui.moveTo(960, 620, duration=.1)
                pyautogui.rightClick(960, 620)

                pyautogui.moveTo(960, 400, duration=.1)
                pyautogui.rightClick(960, 400)
                

                pyautogui.moveTo(1150, 500, duration=.1)
                pyautogui.rightClick(1150, 500)

                pyautogui.moveTo(870, 500, duration=.1)
                pyautogui.rightClick(870, 500)

                pyautogui.moveTo(1050, 620, duration=.1)
                pyautogui.rightClick(1050, 620)

                pyautogui.moveTo(870, 630, duration=.1)
                pyautogui.rightClick(870, 630)

                pyautogui.moveTo(960, 540, duration=.1)
                pyautogui.rightClick(960, 540)

                pyautogui.moveTo(960, 620, duration=.1)
                pyautogui.rightClick(960, 620)

                pyautogui.moveTo(1050, 540, duration=.1)
                pyautogui.rightClick(1050, 540)
                

                pyautogui.moveTo(143, 616, duration=.1)
                pyautogui.leftClick(143, 616)

                #run backwards the same distance you inched forward

                if inchcount > 0:

                        sleepytime = 1*inchcount

                        keyboard.release('w')
                        keyboard.press('a')
                        time.sleep(1.0007)
                        keyboard.release('a')

                        keyboard.release('w')    
                        keyboard.press('w')
                        time.sleep(sleepytime)
                        keyboard.release('w')

                        keyboard.press('d')
                        time.sleep(1.0007)
                        keyboard.release('d')

                        inchcount = 0
                        inch = 0

                else:
                        pass


                #reset variables for being in combat and sighting an enemy
                combat = 0
                sighted = 0

          #reface same direction after spinning to find target

          elif turns > 0:

                starteddrink = 0

                print('reface same direction');

                keyboard.release('w')
                keyboard.press('d')
                time.sleep(.35)
                keyboard.release('d')

                turns = turns - 1
          

          elif inch > 0:

                starteddrink = 0

                keyboard.press('a')
                time.sleep(1.0007)
                keyboard.release('a')
                keyboard.press('w')
                time.sleep(.75*inch)
                keyboard.release('w')
                keyboard.press('d')
                time.sleep(1.0007)
                keyboard.release('d')

                

                inch = 0
                inchcount = 0


          #Change directions
 

          elif executions >= 115 and conj < 2:

                keyboard.release('w')  


                conj = conj + 1

                if conj == 1:

                        time.sleep(1)
                        keyboard.press('9')
                        keyboard.release('9')
                        time.sleep(3.5)
                        keyboard.press('0')
                        keyboard.release('0')
                        time.sleep(3.5)


                        
                        
                        keyboard.press('7')
                        keyboard.release('7')
                        time.sleep(2)
                        keyboard.press('8')
                        keyboard.release('8')

                elif conj == 2:

                        conj = 0

                else:
                        pass
        
                executions = 0


              
                if turnswitch == 0:

                        keyboard.release('w')
                        keyboard.press('a')
                        time.sleep(1.0007)
                        keyboard.release('a')

                        turnswitch = 1

                else:

                        keyboard.release('w')
                        keyboard.press('d')
                        time.sleep(1.0007)
                        keyboard.release('d')

                        turnswitch = 0


                 
                  




          #exit game after this many seconds elapsed


          elif timer > 14000:

                keyboard.release('w')      
                keyboard.press('esc')
                keyboard.release('esc')

                pyautogui.moveTo(949, 641, duration=.1)
                pyautogui.leftClick(949, 641)

                pyautogui.moveTo(865, 225, duration=.1)
                pyautogui.leftClick(865, 225)

                  

                break



        
          #run around and find stuff

          else:

                  
               starteddrink = 0    

               executions = executions + 1

               keyboard.press('5')
               keyboard.release('5')

               
               keyboard.release('w')
               keyboard.press('w')

               random = randrange(20)

               #hit the spacebar to make the character look more natural by jumping 
               if random == 1:

                       keyboard.press('space')
                       keyboard.release('space')

               else:
                       pass
                
               keyboard.press('tab')
               keyboard.release('tab')




        
#Call the main method "image"
image()


