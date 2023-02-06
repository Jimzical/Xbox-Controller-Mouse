from inputs import get_gamepad
import math
import threading
# import mouse
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

def tap(tappedkey):
      gui.press(tappedkey)
      print(tappedkey)

def combinatonTap(key1,key2,key3 = 'NULL', time = 0):
      print(key1+' + '+key2+' + '+key3)
      gui.keyDown(key1)
      gui.keyDown(key2)
      if(key3 != 'NULL'):
            gui.sleep(time)
            gui.press(key3)
      gui.keyUp(key1)
      gui.keyUp(key2)

# def weirdHoldCombinationTap(key1,key2)

def scrollz():
# +++++++++++++++++++++++++++++++base cases+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++base cases+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++base cases+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++base cases+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ====================================================================================
      # killswitch
      if(joy.read()['start'] == 1):  
            print("start button pressed\nended")
            exit()
# ====================================================================================
      # enter
      if(joy.read()['a'] == 1): 
            tap('enter') 
            pass
# ====================================================================================
      # tab
      if(joy.read()['b'] == 1):
            tap('tab')
            pass
# ====================================================================================
      # close tab
      if(joy.read()['x'] == 1):  
            combinatonTap('ctrl','w') 
            pass
# ====================================================================================
      # reopen tab
      if(joy.read()['y'] == 1):  
            combinatonTap('ctrl','shift','t')
            pass
# ====================================================================================
      # undo
      if(joy.read()['select'] == 1):  
            combinatonTap('ctrl','z')
            pass
# ====================================================================================
      # left click
      if(joy.read()['lb'] == 1):  
            gui.leftClick()
            pass
# ====================================================================================
      # right click
      if(joy.read()['rb'] == 1):  
            gui.rightClick()
            pass
# ====================================================================================
      # clsoe window
      if(joy.read()['leftthumb'] == 1 and joy.read()['rightthumb'] == 1):  
            combinatonTap('alt','f4')
            pass
# ====================================================================================
      #  Browser Back
      if(joy.read()['leftthumb'] == 1):  
            tap('browserback')
            pass
# ====================================================================================
      # Browser forward
      if(joy.read()['rightthumb'] == 1): 
            tap('browserforward') 
            pass
# ====================================================================================
      # left joystick
      if(joy.read()['lefty'] > 0.5):
            gui.scroll(50)
      if(joy.read()['lefty'] < -0.5):
            gui.scroll(-50)
# ====================================================================================

# +++++++++++++++++++++++++++++++Right Trigger cases++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++Right Trigger cases++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++Right Trigger cases++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++Right Trigger cases++++++++++++++++++++++++++++++++++++++++++++++++++

      while(joy.read()['rt'] > 0.5):
      # ====================================================================================
            # chrome
            if(joy.read()['a'] == 1):  
                  combinatonTap('super','1')
                  pass
      # ====================================================================================
            # shift tab
            if(joy.read()['b'] == 1):
                  combinatonTap('shift','tab')
                  pass
      # ====================================================================================
            # alt tab
            if(joy.read()['x'] == 1):
                  combinatonTap('alt','tab',time = 2)  
                  pass
      # ====================================================================================
            # terminal
            if(joy.read()['y'] == 1):  
                  combinatonTap('super','3')
                  pass
      # ====================================================================================
            # mute
            if(joy.read()['select'] == 1):
                  tap('volumemute')  
                  pass
      # ====================================================================================
  
            # reverse swtic chrome tab 
            if(joy.read()['lb'] == 1):  
                  combinatonTap('ctrl','tab','shift')
                  pass
      # ====================================================================================
            # switch chrome tab
            if(joy.read()['rb'] == 1):
                  combinatonTap('ctrl','tab')  
                  pass
      # ====================================================================================
            #  vol down
            if(joy.read()['leftthumb'] == 1):  
                  tap('volumedown')
                  pass
      # ====================================================================================
            # vol up
            if(joy.read()['rightthumb'] == 1):  
                  tap('volumeup')
                  pass
      # ====================================================================================
            # left joystick Movement But Fast
            if(joy.read()['lefty'] > 0.5):
                  gui.scroll(250)
            if(joy.read()['lefty'] < -0.5):
                  gui.scroll(-250)
      # ====================================================================================
            # Right Joystick Movement
            # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ TRY USING A FIXED VARIABLE AS ADDDING USING MOVE
            # right
            if(joy.read()['rightx'] > 0.90):
                  gui.moveRel(15,0,0.001) 
            # left
            if(joy.read()['rightx'] < -0.90):
                  gui.moveRel(-15,0,0.001)
            # down
            if(joy.read()['righty'] > 0.90):
                  gui.moveRel(0,-15) 
            # up
            if(joy.read()['righty'] < -0.90):
                  gui.moveRel(0,15)
            # same but faster 
            # right
            if(joy.read()['rightx'] > 0.95):
                  gui.moveRel(65,0,0.001) 
            # left
            if(joy.read()['rightx'] < -0.95):
                  gui.moveRel(-65,0,0.001)
            # down
            if(joy.read()['righty'] > 0.95):
                  gui.moveRel(0,-65) 
            # up
            if(joy.read()['righty'] == -1):
                  gui.moveRel(0,65)
            # faster left joustuck
            if(joy.read()['lefty'] > 0.5):
                gui.scroll(250)
            if(joy.read()['lefty'] < -0.5):
                gui.scroll(-250)
      
# +++++++++++++++++++++++++++++++Left Trigger cases++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++Left Trigger cases++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++Left Trigger cases++++++++++++++++++++++++++++++++++++++++++++++++++

      while(joy.read()['lt'] > 0.5):
      # ====================================================================================
            # A
            if(joy.read()['a'] == 1):
                  tap('down')
                  pass
      # ====================================================================================
            # B
            if(joy.read()['b'] == 1):
                  tap('right')
                  pass
      # ====================================================================================
            # X
            if(joy.read()['x'] == 1):
                  tap('left')
                  pass

      # ====================================================================================
            # Y
            if(joy.read()['y'] == 1):  
                  tap('up')
                  pass
      # ====================================================================================
            # Select
            if(joy.read()['select'] == 1):
                  pass
      # ====================================================================================
            # Left Bumper
            if(joy.read()['lb'] == 1):
                  combinatonTap('ctrl','super','left')
                  pass
      # ====================================================================================
            # Right Bumper
            if(joy.read()['rb'] == 1):
                  combinatonTap('ctrl','super','right')
                  pass
      # ====================================================================================
            #  Left Thumb
            if(joy.read()['leftthumb'] == 1):
                  # combinatonTap('option','f2')
                  combinatonTap('super','up')
                  pass
      # ====================================================================================
            # Right Thumb
            if(joy.read()['rightthumb'] == 1):
                  # combinatonTap('option','f3')
                  combinatonTap('super','down')
                  pass
      # ====================================================================================

      # Doesent work for some reason
            # Right Joystick Movement Drag
            # currentPositionX= list(gui.position())[0]
            # currentPositionY= list(gui.position())[1]
            # right
            if(joy.read()['rightx'] > 0.35):
                  gui.dragRel(15,0,0.001) 
            # left
            if(joy.read()['rightx'] < -0.35):
                  gui.dragRel(-15,0,0.001)
            # down
            if(joy.read()['righty'] > 0.35):
                  gui.dragRel(0,-15) 
            # up
            if(joy.read()['righty'] < -0.5):
                  gui.dragRel(0,15)
            # same but faster 
            # right
            if(joy.read()['rightx'] > 0.95):
                  gui.dragRel(65,0,0.001) 
            # left
            if(joy.read()['rightx'] < -0.95):
                  gui.dragRel(-65,0,0.001)
            # down
            if(joy.read()['righty'] > 0.95):
                  gui.dragRel(0,-65) 
            # up
            if(joy.read()['righty'] == -1):
                  gui.dragRel(0,65)



if __name__ == '__main__':
    joy = XboxController()
    print("started")
    while True:
            # print(joy.read())  #prints the list of inputs
            scrollz()
    print("ended")

# base cases for trigger
      # # ====================================================================================
      #       # A
      #       if(joy.read()['a'] == 1):  
      #             pass
      # # ====================================================================================
      #       # B
      #       if(joy.read()['b'] == 1):
      #             # pass
      # # ====================================================================================
      #       # X
      #       if(joy.read()['x'] == 1):  
      #             pass
      # # ====================================================================================
      #       # Y
      #       if(joy.read()['y'] == 1):  
      #             pass
      # # ====================================================================================
      #       # Select
      #       if(joy.read()['select'] == 1):  
      #             pass
      # # ====================================================================================
      #       # Left Bumper
      #       if(joy.read()['lb'] == 1):  
      #             pass
      # # ====================================================================================
      #       # Right Bumper
      #       if(joy.read()['rb'] == 1):  
      #             pass
      # # ====================================================================================
      #       #  Left Thumb
      #       if(joy.read()['leftthumb'] == 1):  
      #             pass
      # # ====================================================================================
      #       # Right Thumb
      #       if(joy.read()['rightthumb'] == 1):  
      #             pass
