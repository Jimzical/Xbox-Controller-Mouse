'''
---------------------------------------------------
UPDATE LOG
---------------------------------------------------

 - Changed Mouse Movement to be more accurate with Dynamic Speed and More Optimized

---------------------------------------------------
Planned Updates
---------------------------------------------------

 - Short Term Goal is to be able to use the Controller as a Mouse and Keyboard
      - Update The README file
      - Be Able to open Applications
      - Be Able to Open Websites
      - Be Able to Play Sound Clips
      - Be Able to Type
      
      - Problematic Goals
      - Make the joystick movement map to WASD (current problem is that doing that heats up the cpu too much as its constaly checking for input)
 - Long Term Goal is to be able to use the Controller as a Mouse and Keyboard
      - Possibly Add a Long Press Functionality 
      - Add a GUI to make it easier to use
      - add threading or some other form of optimization to make it faster 

'''



from inputs import get_gamepad
import math
import threading
from plyer import notification
import pyautogui as auto
import json
import time

class XboxController(object):
    MAX_TRIG_VAL = math.pow(2, 8)
    MAX_JOY_VAL = math.pow(2, 15)

      # TODO: After Fixing all the major bugs, comment out or remove the Dpad Operations all together since they dont work
      # Optionally if im extra jobless, I can try to fix them
      # im not doing it right now because im lazy and they are not that important. plus they might break other things
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
            'start' : self.Back,          #for some reason these two are interchanged for my controller
            'select' : self.Start           #for some reason these two are interchanged for my controller
            # 'up' : self.UpDPad,           #these dont really work
            # 'down' : self.DownDPad,       #these dont really work
            # 'left' : self.LeftDPad,       #these dont really work
            # 'right' : self.RightDPad,      #these dont really work
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
def ButtonTap(button,tappedKey):
      # not for mouse movement      
      '''

      ---------------------------------------------------
      To Simulate a Key Press 
      ---------------------------------------------------
      ### @Parameters
      * button : the Button to be Pressed on the Controller
      * tappedKey : the Key which will be Simulated to be Pressed on the Keyboard
      '''    
      auto.press(tappedKey)
      print(tappedKey)    
      auto.sleep(0.1)     

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
            auto.leftClick()
      elif(tappedKey == 'right'):
            auto.rightClick()
      elif(tappedKey == 'middle'):
            auto.middleClick()
    
      print(tappedKey)  
      return None

# TODO: add types in the fucntion description
def CombinationTap(button,keys):
      '''
      ---------------------------------------------------
      To Simulate a Key Combination Press
      ---------------------------------------------------
      ### @Parameters
      * button : the Button to be Pressed on the Controller
      * keys : the Keys which will be Simulated to be Pressed on the Keyboard
      '''
      print(' + '.join(keys))

      auto.keyDown(keys[0])
      auto.keyDown(keys[1])
      if(len(keys) == 3):
            auto.press(keys[2])
      auto.keyUp(keys[0])
      auto.keyUp(keys[1])

def ButtonHoldTap(button,key):
      '''
      ---------------------------------------------------
      To Simulate a Key Hold Press
      ---------------------------------------------------
      ### @Parameters
      * button  : the Button to be Pressed on the Controller
      * key : the Key which will be Simulated to be Pressed on the Keyboard

      '''
      auto.keyDown(key)
      print(key +" Pressed")
      while(joy.read()[button] == 1):
            Actions()
      auto.keyUp(key)
            
def ButtonHoldClick(button,key = 'left'):
      '''
      
      ---------------------------------------------------
      To Simulate a Mouse Hold Click
      ---------------------------------------------------
      ### @Parameters
      * button  : the Button to be Pressed on the Controller
      * key : the Key which will be Simulated to be Pressed on the Keyboard (left,right,middle) [Default = left]

      '''
      auto.mouseDown(button = key)
      print(key+" Pressed")
      while(joy.read()[button] == 1):
            MouseControl()
      auto.mouseUp(button = key)
            

# TODO: a delay is present somewhere in the code making tge scroll not smooth anymore
# TODO: Fast SCroll is not working
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
                  auto.scroll(speed)
      if(joy.read()[yAxis] < -0.5):
            auto.scroll(-speed)

# TODO: add delay option for the json binding thing
# TODO: add comments for the parameters in json file
def MouseControl(joystick = 'right',LowerSensitivity = 0.30,Speed = 65):
      '''
      
      ---------------------------------------------------
      To Simulate a Mouse Movement
      ---------------------------------------------------
      ### @Parameters
      * joystick : the Joystick to be used on the Controller (left,right) [Default = right]
      * LowerSensitivity : the Lower Sensitivity Region of the Joystick (Basically an Area Percentage)[Default = 0.30]
      * Speed : the Speed of the Mouse Movement in the UpperSensitivity Region[Default = 65]
      
      # REMOVED TIME PARAMETER IN THIS VERSION
      * time : the Time Delay between the Mouse Movements (Changes the Smoothness of the Movement)(Optional)[Default = 0.00001]
      '''
      
      X_Axis = joystick + 'y'  #kind of messed up while mappig the inputs to the dictionary
      Y_Axis = joystick + 'x'

      y_speed = -int((joy.read()[X_Axis] * 100) * Speed / 100  )  #not sure why but im invertin the y axis. i dont remember why i did this but it works
      x_speed = int((joy.read()[Y_Axis] * 100) * Speed / 100  )

      # inverting
      # y_speed = -y_speed

      # print("x_speed = " + str(x_speed), "y_speed = " + str(y_speed))

      if (joy.read()[Y_Axis] > LowerSensitivity or joy.read()[X_Axis] > LowerSensitivity or joy.read()[Y_Axis] < LowerSensitivity or joy.read()[X_Axis] < LowerSensitivity ):
            auto.moveRel(x_speed,y_speed)


def KillSwitch(button = 'start'):
      # kill switch
      button = bindings["KillSwitch"]
      if(joy.read()[button] == 1): 
            notification.notify(
                  title = 'Ended',
                  message = 'You May Turn Off the Controller Now',
                  app_icon = "app-media\colored_con.ico",
                  timeout = 10,
            ) 
            print(button + " button pressed\nEnded")
            exit()

def ButtonActionConstructor(button,type,key):
      if type == "ButtonTap":
            ButtonTap(button,key)
      elif type == "ButtonClick":
            ButtonClick(button,key)
      elif type == "CombinationalTap":
            CombinationTap(button,key )
      elif type == "ButtonHoldTap":
            ButtonHoldTap(button,key)
      elif type == "ButtonHoldClick":
            ButtonHoldClick(button,key)

def NoTriggerCondition():
      NoTriggerButtons = bindings["NoTriggerCondition"]["ButtonAction"]
      NoTriggerJoystick = bindings["NoTriggerCondition"]["JoystickAction"]
      for ControllerButton in NoTriggerButtons.keys():
            if (joy.read()[ControllerButton] == 1):
      
                  type = NoTriggerButtons[ControllerButton]["type"]
                  key = NoTriggerButtons[ControllerButton]["key"]
      
                  ButtonActionConstructor(ControllerButton,type,key)
                  return
      
      if ("Scroll" in NoTriggerJoystick.keys()):
            joystick = NoTriggerJoystick["Scroll"]["joystick"]
            speed = NoTriggerJoystick["Scroll"]["speed"]
            Scroll(joystick,speed)
      if ("MouseControl" in NoTriggerJoystick.keys()):
            joystick = NoTriggerJoystick["MouseControl"]["joystick"]
            lowerSensitivity = NoTriggerJoystick["MouseControl"]["lowerSensitivity"]
            upperSensitivity = NoTriggerJoystick["MouseControl"]["upperSensitivity"]
            Speed = NoTriggerJoystick["MouseControl"]["Speed"]
            MouseControl(joystick,lowerSensitivity,upperSensitivity,Speed)      
      
def RightTriggerCondition():
      RightTriggerButtons = bindings["RightTriggerCondition"]["ButtonAction"]
      RightTriggerJoystick = bindings["RightTriggerCondition"]["JoystickAction"]
      for ControllerButton in RightTriggerButtons.keys():
            if (joy.read()[ControllerButton] == 1):
      
                  type = RightTriggerButtons[ControllerButton]["type"]
                  key = RightTriggerButtons[ControllerButton]["key"]
      
                  ButtonActionConstructor(ControllerButton,type,key)
      
      if ("Scroll" in RightTriggerJoystick.keys()):
            joystick = RightTriggerJoystick["Scroll"]["joystick"]
            speed = RightTriggerJoystick["Scroll"]["speed"]
            Scroll(joystick,speed)
      if ("MouseControl" in RightTriggerJoystick.keys()):
            joystick = RightTriggerJoystick["MouseControl"]["joystick"]
            lowerSensitivity = RightTriggerJoystick["MouseControl"]["LowerSensitivity"]
            Speed = RightTriggerJoystick["MouseControl"]["Speed"]
            MouseControl(joystick,lowerSensitivity,Speed)      
      return

def LeftTriggerCondition():
      LeftTriggerButtons = bindings["LeftTriggerCondition"]["ButtonAction"]
      LeftTriggerJoystick = bindings["LeftTriggerCondition"]["JoystickAction"]

      for ControllerButton in LeftTriggerButtons.keys():
            if (joy.read()[ControllerButton] == 1):
      
                  type = LeftTriggerButtons[ControllerButton]["type"]
                  key = LeftTriggerButtons[ControllerButton]["key"]
      
                  ButtonActionConstructor(ControllerButton,type,key)
      
      if ("Scroll" in LeftTriggerJoystick.keys()):
            joystick = LeftTriggerJoystick["Scroll"]["joystick"]
            speed = LeftTriggerJoystick["Scroll"]["speed"]
            Scroll(joystick,speed)  
      if ("MouseControl" in LeftTriggerJoystick.keys()):
            joystick = LeftTriggerJoystick["MouseControl"]["joystick"]
            lowerSensitivity = LeftTriggerJoystick["MouseControl"]["LowerSensitivity"]
            Speed = LeftTriggerJoystick["MouseControl"]["Speed"]
            MouseControl(joystick,lowerSensitivity,Speed)      
    
      return
def Actions():
# ====================================================================================
      if(joy.read()[bindings['Killswitch']] == 1): 
            notification.notify(
                  title = 'Ended',
                  message = 'You May Turn Off the Controller Now',
                  app_icon = "app-media\colored_con.ico",
                  timeout = 10,
            ) 
            print("Killswitch Activated\nended")
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
      global bindings
      with open('bindings.json', 'r') as f:
            bindings = json.load(f)
            
      joy = XboxController()
      notification.notify(
            title = 'Started',
            message = 'You May Use the Controller Now',
            app_icon = "app-media\colored_con.ico",
            timeout = 2,
            )
      print("Started")                      
      while True:
                  # print(joy.read())  #prints the list of inputs
                  Actions()
                  auto.sleep(0.1)
                  # make a simple machine leanring algorithm to guess how much time to sleep
      
    