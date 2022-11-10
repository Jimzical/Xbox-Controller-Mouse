from inputs import get_gamepad
import math
import threading
from plyer import notification
import pyautogui as gui
class XboxController(object):
    MAX_TRIG_VAL = math.pow(2, 8)
    MAX_JOY_VAL = math.pow(2, 15)

    def __init__(self):

        self.LeftJoystickY = 0
        self.LeftJoystickX = 0
        self.RightJoystickY = 0
        self.RightJoystickX = 0
        self.LeftTrigger = 0
        self.RightTrigger = 0
        self.LeftBumper = 0
        self.RightBumper = 0
        self.A = 0
        self.X = 0
        self.Y = 0
        self.B = 0
        self.LeftThumb = 0
        self.RightThumb = 0
        self.Back = 0
        self.Start = 0
        self.LeftDPad = 0
        self.RightDPad = 0
        self.UpDPad = 0
        self.DownDPad = 0

        self._monitor_thread = threading.Thread(target=self._monitor_controller, args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()


    def read(self): # return the buttons/triggers that you care about in this methode
            dict ={
            'leftx' : self.LeftJoystickX,
            'lefty' : self.LeftJoystickY,
            'rightx':self.RightJoystickX,
            'righty':self.RightJoystickY,
            'a' : self.A,
            'x' : self.X,
            'b' : self.B,
            'y' : self.Y,
            'rb' : self.RightBumper,
            'lb' : self.LeftBumper,
            'rt' : self.RightTrigger,
            'lt' : self.LeftTrigger,
            'leftthumb' : self.LeftThumb,
            'rightthumb' : self.RightThumb,
            'up' : self.UpDPad,           #these dont really work
            'down' : self.DownDPad,       #these dont really work
            'left' : self.LeftDPad,       #these dont really work
            'right' : self.RightDPad,      #these dont really work
            'start' : self.Back,          #for some reason these two are interchanged for my controller
            'select' : self.Start           #for some reason these two are interchanged for my controller
            }
            # return [leftx, lefty, a, x, rb, rightx, righty , rt, b,lt ,lb,leftthumb,rightthumb,y,down]
            return dict


    def _monitor_controller(self):
        while True:
            events = get_gamepad()                      
            for event in events:
                if event.code == 'ABS_Y':
                    self.LeftJoystickY = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_X':
                    self.LeftJoystickX = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_RY':
                    self.RightJoystickY = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_RX':
                    self.RightJoystickX = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_Z':
                    self.LeftTrigger = event.state / XboxController.MAX_TRIG_VAL # normalize between 0 and 1
                elif event.code == 'ABS_RZ':
                    self.RightTrigger = event.state / XboxController.MAX_TRIG_VAL # normalize between 0 and 1
                elif event.code == 'BTN_TL':
                    self.LeftBumper = event.state
                elif event.code == 'BTN_TR':
                    self.RightBumper = event.state
                elif event.code == 'BTN_SOUTH':
                    self.A = event.state
                elif event.code == 'BTN_NORTH':
                    self.Y = event.state #previously switched with X
                elif event.code == 'BTN_WEST':
                    self.X = event.state #previously switched with Y
                elif event.code == 'BTN_EAST':
                    self.B = event.state
                elif event.code == 'BTN_THUMBL':
                    self.LeftThumb = event.state
                elif event.code == 'BTN_THUMBR':
                    self.RightThumb = event.state
                elif event.code == 'BTN_SELECT':
                    self.Back = event.state
                elif event.code == 'BTN_START':
                    self.Start = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY1':
                    self.LeftDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY2':
                    self.RightDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY3':
                    self.UpDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY4':
                    self.DownDPad = event.state

def ButtonTap(button,tappedKey,delay = 0):
      # not for mouse movement          
      if(joy.read()[button] == 1):
            gui.press(tappedKey)
            print(tappedKey)    
            gui.sleep(delay)     
            pass


def ButtonClick(button,tappedKey = 'left'):
      # not for mouse movement          
      if(joy.read()[button] == 1):
            if(tappedKey == 'left'):
                  gui.leftClick()
            elif(tappedKey == 'right'):
                  gui.rightClick()
            elif(tappedKey == 'middle'):
                  gui.middleClick()
            print(tappedKey)       
            pass
      return None

def CombinationTap(button,key1,key2,key3 = 'NULL', time = 0):
      if(joy.read()[button] == 1):      
            print(key1+' + '+key2+' + '+key3)
            gui.keyDown(key1)
            gui.keyDown(key2)
            if(key3 != 'NULL'):
                  gui.sleep(time)
                  gui.press(key3)
            gui.keyUp(key1)
            gui.keyUp(key2)
            
def ButtonHoldTap(button,key):
      if(joy.read()[button] == 1):
            gui.keyDown(key)
            print(button+" Pressed")
            while(joy.read()[button] == 1):
                  Actions()
            gui.keyUp(key)
            
def ButtonHoldClick(button,key = 'left'):
      if(joy.read()[button] == 1):
            gui.mouseDown(button = key)
            print(button+" Pressed")
            while(joy.read()[button] == 1):
                  MouseControl()
            gui.mouseUp(button = key)
            


def Scroll(joystick = 'left',speed = 50):
      # joystick will be left or right
      yAxis = joystick + 'y'
      if(joy.read()[yAxis] > 0.5):
                  gui.scroll(speed)
      if(joy.read()[yAxis] < -0.5):
            gui.scroll(-speed)

def MouseControl(joystick = 'right',LowerSensitivity = 0.30,UpperSensitivity = 0.75,LowerSpeed = 15,UpperSpeed = 65,time = 0.00001):
      X_Axis = joystick + 'y'  #kind of messed up while mappig the inputs to the dictionary
      Y_Axis = joystick + 'x'

      #Diagonal Right Up
      if(joy.read()[Y_Axis] > LowerSensitivity and joy.read()[X_Axis] < -LowerSensitivity):
            gui.moveRel(LowerSpeed,LowerSpeed,time) 
      #Diagonal Right Down
      elif(joy.read()[Y_Axis] > LowerSensitivity and joy.read()[X_Axis] > LowerSensitivity):
            gui.moveRel(LowerSpeed,-LowerSpeed,time) 
      #Diagonal Left Up
      elif(joy.read()[Y_Axis] < -LowerSensitivity and joy.read()[X_Axis] < -LowerSensitivity):
            gui.moveRel(-LowerSpeed,LowerSpeed,time) 
      #Diagonal Left Down
      elif(joy.read()[Y_Axis] < -LowerSensitivity and joy.read()[X_Axis] > LowerSensitivity):
            gui.moveRel(-LowerSpeed,-LowerSpeed,time) 
      
      # right
      elif(joy.read()[Y_Axis] > LowerSensitivity):
            gui.moveRel(LowerSpeed,0,time) 
      # left
      elif(joy.read()[Y_Axis] < -LowerSensitivity):
            gui.moveRel(-LowerSpeed,0,time)
      # down
      elif(joy.read()[X_Axis] > LowerSensitivity):
            gui.moveRel(0,-LowerSpeed,time) 
      # up
      elif(joy.read()[X_Axis] < -LowerSensitivity):
            gui.moveRel(0,LowerSpeed,time)

      # same but faster 
      #Diagonal Right Up
      if(joy.read()[Y_Axis] > UpperSensitivity and joy.read()[X_Axis] < -UpperSensitivity):
            gui.moveRel(UpperSpeed,UpperSpeed,time) 
      #Diagonal Right Down
      elif(joy.read()[Y_Axis] > UpperSensitivity and joy.read()[X_Axis] > UpperSensitivity):
            gui.moveRel(UpperSpeed,-UpperSpeed,time) 
      #Diagonal Left Up
      elif(joy.read()[Y_Axis] < -UpperSensitivity and joy.read()[X_Axis] < -UpperSensitivity):
            gui.moveRel(-UpperSpeed,UpperSpeed,time) 
      #Diagonal Left Down
      elif(joy.read()[Y_Axis] < -UpperSensitivity and joy.read()[X_Axis] > UpperSensitivity):
            gui.moveRel(-UpperSpeed,-UpperSpeed,time) 
      # right
      elif(joy.read()[Y_Axis] > UpperSensitivity):
            gui.moveRel(UpperSpeed,0,time) 
      # left
      elif(joy.read()[Y_Axis] < -UpperSensitivity):
            gui.moveRel(-UpperSpeed,0,time)
      # down
      elif(joy.read()[X_Axis] > UpperSensitivity):
            gui.moveRel(0,-UpperSpeed,time) 
      # up
      elif(joy.read()[X_Axis] == -1): #odd case where it only worked with -1 properly for some reason
            gui.moveRel(0,UpperSpeed,time)


def KillSwitch(button = 'start'):
# ====================================================================================
      if(joy.read()[button] == 1): 
            notification.notify(
                  title = 'Ended',
                  message = 'You May Turn Off the Controller Now',
                  app_icon = "app-media\colored_con.ico",
                  timeout = 10,
            ) 
            print(button + " button pressed\nended")
            exit()

def NoTriggerCondition():
# ====================================================================================
      # enter
      ButtonTap('a','enter',delay = 0.1)
# ====================================================================================
      # tab
      ButtonTap('b','tab')
# ====================================================================================
      # close tab
      CombinationTap('x','ctrl','w') 
# ====================================================================================
      # reopen tab
      CombinationTap('y','ctrl','shift','t')
# ====================================================================================
      # close window
      CombinationTap('select','alt','f4')
# ====================================================================================
      # left click
      ButtonClick('lb','left')
# ====================================================================================
      # right click
      ButtonClick('rb','right')
# ====================================================================================
      #  Holds Alt
      ButtonTap('leftthumb','volumedown')
# ====================================================================================
      # Holds shift
      ButtonTap('rightthumb','volumeup')
      # ButtonHoldTap('rightthumb','shift')
# ====================================================================================
      # left joystick
      Scroll(joystick = 'left',speed = 50)
# ====================================================================================

def RightTriggerCondition():
# ====================================================================================
            # chrome
            CombinationTap('a','super','1')
# ====================================================================================
            # shift tab
            CombinationTap('b','shift','tab')
# ====================================================================================
            # alt tab
            CombinationTap('x','alt','tab',time = 2)  
# ====================================================================================
            # terminal
            CombinationTap('y','super','3')
# ====================================================================================
            # mute
            ButtonTap('select','volumemute',0.1)
# ====================================================================================  
            # reverse swtic chrome tab 
            CombinationTap('lb','ctrl','tab',key3='shift')
# ====================================================================================
            # switch chrome tab
            CombinationTap('rb','ctrl','tab')  
# ====================================================================================
            #  vol down
            ButtonHoldTap('leftthumb','alt')
# ====================================================================================
            # vol up
            ButtonHoldClick('rightthumb',key='left')
# ====================================================================================
            # left joystick Movement But Fast
            Scroll('left',250)
# ====================================================================================
            # Right Joystick Movement
            MouseControl()

def LeftTriggerCondition():
# ====================================================================================
            # down arrow
            ButtonTap('a','down')
# ====================================================================================
            # right arrow
            ButtonTap('b','right')
# ====================================================================================
            # left arrow
            ButtonTap('x','left')
# ====================================================================================
            # up arrow
            ButtonTap('y','up')
# ====================================================================================
            # esc
            ButtonTap('select','esc')
# ====================================================================================
            # Left Bumper
            CombinationTap('lb','ctrl','super','left')
# ====================================================================================
            # Right Bumper
            CombinationTap('rb','ctrl','super','right')
# ====================================================================================
            #  Left Thumb
            CombinationTap('leftthumb','super','up')
# ====================================================================================
            # Right Thumb
            CombinationTap('rightthumb','super','down')
# ====================================================================================/
      # Doesent work for some reason
            # Right Joystick Movement Drag
            # currentPositionX= list(gui.position())[0


def Actions():
# ====================================================================================
      # KillSwitch
# ====================================================================================
      if(joy.read()['start'] == 1): 
            notification.notify(
                  title = 'Ended',
                  message = 'You May Turn Off the Controller Now',
                  app_icon = "app-media\colored_con.ico",
                  timeout = 10,
            ) 
            print("start button pressed\nended")
            exit()
# +++++++++++++++++++++++++++++++No Trigger cases++++++++++++++++++++++++++++++++++++++++++++++++++
      NoTriggerCondition()
# +++++++++++++++++++++++++++++++Right Trigger cases++++++++++++++++++++++++++++++++++++++++++++++++++
      while(joy.read()['rt'] > 0.5):
            RightTriggerCondition()
# +++++++++++++++++++++++++++++++Left Trigger cases++++++++++++++++++++++++++++++++++++++++++++++++++
      while(joy.read()['lt'] > 0.5):
            LeftTriggerCondition()


if __name__ == '__main__':
      joy = XboxController()
      notification.notify(
            title = 'Started',
            message = 'You May Use the Controller Now',
            app_icon = "app-media\colored_con.ico",
            timeout = 10,
            )
      print("started")                      
      while True:
                  # print(joy.read())  #prints the list of inputs
                  Actions()
      print("ended")
    
