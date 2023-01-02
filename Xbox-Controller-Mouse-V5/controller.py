from inputs import get_gamepad
import math
import threading
from plyer import notification
import pyautogui as gui
import json

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
      '''

      ---------------------------------------------------
      To Simulate a Key Press 
      ---------------------------------------------------
      ### @Parameters
      * button : the Button to be Pressed on the Controller
      * tappedKey : the Key which will be Simulated to be Pressed on the Keyboard
      * delay : the Delay between the Key Press and Release (It is the Duration of the Key Press)

      '''    
      gui.press(tappedKey)
      print(tappedKey)    
      gui.sleep(delay)     
 

def ButtonClick(button,tappedKey = 'left'):
      # not for mouse movement   
      '''
      
      ---------------------------------------------------
      To Simulate a Mouse Click
      ---------------------------------------------------
      ### @Parameters
      * button : the Button to be Pressed on the Controller
      * tappedKey : the Key which will be Simulated to be Pressed on the Keyboard (left,right,middle) [Default = left]

      '''       

      if(tappedKey == 'left'):
            gui.leftClick()
      elif(tappedKey == 'right'):
            gui.rightClick()
      elif(tappedKey == 'middle'):
            gui.middleClick()
    
      print(tappedKey)       
      return None

def CombinationTap(button,key1,key2,key3 = 'NULL', delay = 0):
      '''
      ---------------------------------------------------
      To Simulate a Key Combination Press
      ---------------------------------------------------
      ### @Parameters
      * button : the Button to be Pressed on the Controller
      * key1 : the First Key which will be Simulated to be Pressed on the Keyboard
      * key2 : the Second Key which will be Simulated to be Pressed on the Keyboard
      * key3 : the Third Key which will be Simulated to be Pressed on the Keyboard (Optional) [Default = NULL]
      * delay : the Delay between the Key Press and Release (It is the Duration of the Key Press) [Default = 0]
      '''
      print(key1+' + '+key2+' + '+key3)
      gui.keyDown(key1)
      gui.keyDown(key2)
      if(key3 != 'NULL'):
            gui.sleep(delay)
            gui.press(key3)
      gui.keyUp(key1)
      gui.keyUp(key2)
            
def ButtonHoldTap(button,key):
      '''
      ---------------------------------------------------
      To Simulate a Key Hold Press
      ---------------------------------------------------
      ### @Parameters
      * button  : the Button to be Pressed on the Controller
      * key : the Key which will be Simulated to be Pressed on the Keyboard

      '''
      gui.keyDown(key)
      print(button+" Pressed")
      while(joy.read()[button] == 1):
            Actions()
      gui.keyUp(key)
            
def ButtonHoldClick(button,key = 'left'):
      '''
      
      ---------------------------------------------------
      To Simulate a Mouse Hold Click
      ---------------------------------------------------
      ### @Parameters
      * button  : the Button to be Pressed on the Controller
      * key : the Key which will be Simulated to be Pressed on the Keyboard (left,right,middle) [Default = left]

      '''
      gui.mouseDown(button = key)
      print(button+" Pressed")
      while(joy.read()[button] == 1):
            MouseControl()
      gui.mouseUp(button = key)
            


def Scroll(joystick = 'left',speed = 50):
      '''
      
      ---------------------------------------------------
      To Simulate a Mouse Scroll
      ---------------------------------------------------
      ### @Parameters
      * joystick : the Joystick to be used on the Controller (left,right) [Default = left]
      * speed : the Speed of the Scroll [Default = 50]

      '''      
      yAxis = joystick + 'y'
      if(joy.read()[yAxis] > 0.5):
                  gui.scroll(speed)
      if(joy.read()[yAxis] < -0.5):
            gui.scroll(-speed)

def MouseControl(joystick = 'right',LowerSensitivity = 0.30,UpperSensitivity = 0.75,LowerSpeed = 15,UpperSpeed = 65,time = 0.00001):
      '''
      
      ---------------------------------------------------
      To Simulate a Mouse Movement
      ---------------------------------------------------
      ### @Parameters
      * joystick : the Joystick to be used on the Controller (left,right) [Default = right]
      * LowerSensitivity : the Lower Sensitivity Region of the Joystick (Basically an Area Percentage)[Default = 0.30]
      * UpperSensitivity : the Upper Sensitivity Region of the Joystick (Basically an Area Percentage)[Default = 0.75]
      * LowerSpeed : the Speed of the Mouse Movement in the LowerSensitivity Region[Default = 15]
      * UpperSpeed : the Speed of the Mouse Movement in the UpperSensitivity Region[Default = 65]
      * time : the Time Delay between the Mouse Movements (Changes the Smoothness of the Movement)(Optional)[Default = 0.00001]
      '''
      
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
      # kill switch
      button = mapping["KillSwitch"]
      if(joy.read()[button] == 1): 
            notification.notify(
                  title = 'Ended',
                  message = 'You May Turn Off the Controller Now',
                  app_icon = "app-media\colored_con.ico",
                  timeout = 10,
            ) 
            print(button + " button pressed\nended")
            exit()

def ButtonActionConstructor(button,type,key, delay = 0):
      if type == "ButtonTap":
            ButtonTap(button,key,delay = delay)
      elif type == "ButtonClick":
            ButtonClick(button,key,delay = delay)
      elif type == "CombinationalTap":
            CombinationTap(button,key1 = key[0],key2 = key[1], key3 = key[2],delay = delay)
      elif type == "ButtonHoldTap":
            ButtonHoldTap(button,key,delay = delay)
      elif type == "ButtonHoldClick":
            ButtonHoldClick(button,key,delay = delay)


def NoTriggerCondition():
      NoTriggerButtons = mapping["NoTriggerCondition"]["ButtonAction"]
      NoTriggerJoystick = mapping["NoTriggerCondition"]["JoystickAction"]
      for ControllerButton in NoTriggerButtons.keys():
            if (joy.read()[ControllerButton] == 1):
      
                  type = NoTriggerButtons[ControllerButton]["type"]
                  key = NoTriggerButtons[ControllerButton]["key"]
                  delay = NoTriggerButtons[ControllerButton]["delay"]
      
                  ButtonActionConstructor(ControllerButton,type,key,delay)
                  return
      
      if ("Scroll" in NoTriggerJoystick.keys()):
            joystick = NoTriggerJoystick["Scroll"]["joystick"]
            speed = NoTriggerJoystick["Scroll"]["speed"]
            Scroll(joystick,speed)
      if ("MouseControl" in NoTriggerJoystick.keys()):
            joystick = NoTriggerJoystick["MouseControl"]["joystick"]
            lowerSensitivity = NoTriggerJoystick["MouseControl"]["lowerSensitivity"]
            upperSensitivity = NoTriggerJoystick["MouseControl"]["upperSensitivity"]
            lowerSpeed = NoTriggerJoystick["MouseControl"]["lowerSpeed"]
            upperSpeed = NoTriggerJoystick["MouseControl"]["upperSpeed"]
            Time = NoTriggerJoystick["MouseControl"]["time"]
            MouseControl(joystick,lowerSensitivity,upperSensitivity,lowerSpeed,upperSpeed,Time)      
      
def RightTriggerCondition():
      RightTriggerButtons = mapping["RightTriggerCondition"]["ButtonAction"]
      RightTriggerJoystick = mapping["RightTriggerCondition"]["JoystickAction"]
      for ControllerButton in RightTriggerButtons.keys():
            if (joy.read()[ControllerButton] == 1):
      
                  type = RightTriggerButtons[ControllerButton]["type"]
                  key = RightTriggerButtons[ControllerButton]["key"]
                  delay = RightTriggerButtons[ControllerButton]["delay"]
      
                  ButtonActionConstructor(ControllerButton,type,key,delay)
      
      if ("Scroll" in RightTriggerJoystick.keys()):
            joystick = RightTriggerJoystick["Scroll"]["joystick"]
            speed = RightTriggerJoystick["Scroll"]["speed"]
            Scroll(joystick,speed)
      if ("MouseControl" in RightTriggerJoystick.keys()):
            joystick = RightTriggerJoystick["MouseControl"]["joystick"]
            lowerSensitivity = RightTriggerJoystick["MouseControl"]["LowerSensitivity"]
            upperSensitivity = RightTriggerJoystick["MouseControl"]["UpperSensitivity"]
            lowerSpeed = RightTriggerJoystick["MouseControl"]["LowerSpeed"]
            upperSpeed = RightTriggerJoystick["MouseControl"]["UpperSpeed"]
            Time = RightTriggerJoystick["MouseControl"]["time"]
            MouseControl(joystick,lowerSensitivity,upperSensitivity,lowerSpeed,upperSpeed,Time)      
      return

def LeftTriggerCondition():
      LeftTriggerButtons = mapping["LeftTriggerCondition"]["ButtonAction"]
      LeftTriggerJoystick = mapping["LeftTriggerCondition"]["JoystickAction"]

      for ControllerButton in LeftTriggerButtons.keys():
            if (joy.read()[ControllerButton] == 1):
      
                  type = LeftTriggerButtons[ControllerButton]["type"]
                  key = LeftTriggerButtons[ControllerButton]["key"]
                  delay = LeftTriggerButtons[ControllerButton]["delay"]
      
                  ButtonActionConstructor(ControllerButton,type,key,delay)
      
      if ("Scroll" in LeftTriggerJoystick.keys()):
            joystick = LeftTriggerJoystick["Scroll"]["joystick"]
            speed = LeftTriggerJoystick["Scroll"]["speed"]
            Scroll(joystick,speed)  
      if ("MouseControl" in LeftTriggerJoystick.keys()):
            joystick = LeftTriggerJoystick["MouseControl"]["joystick"]
            lowerSensitivity = LeftTriggerJoystick["MouseControl"]["lowerSensitivity"]
            upperSensitivity = LeftTriggerJoystick["MouseControl"]["upperSensitivity"]
            lowerSpeed = LeftTriggerJoystick["MouseControl"]["lowerSpeed"]
            upperSpeed = LeftTriggerJoystick["MouseControl"]["upperSpeed"]
            Time = LeftTriggerJoystick["MouseControl"]["time"]
            MouseControl(joystick,lowerSensitivity,upperSensitivity,lowerSpeed,upperSpeed,Time)      
    
      return
def Actions():
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
      global mapping
      with open('mapping.json', 'r') as f:
            mapping = json.load(f)
      
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
                  gui.sleep(0.1)
      print("ended")
    
