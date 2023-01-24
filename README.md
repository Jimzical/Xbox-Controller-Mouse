# Xbox-Controller-Mouse

 #### This Program allows us to use a Xbox Controller as a Mouse along with other Common Keyboard Shortcuts

## Download
- [Direct Zip Download](https://github.com/Jimzical/Xbox-Controller-Mouse/archive/refs/heads/main.zip)

## Requirements

- Python, if You want to Download Python, go to the [Website(get Python 3.10)](https://www.python.org/downloads/) or [Direct Zip Download](https://www.python.org/downloads/release/python-3108/)
- All Requirements other (pyautogui, inputs, plyer) will be downloaded automatically if Code Run Through Installer.bat or Xbox-Mouse.exe
> You can open the Installer.bat file to check what all is being downloaded, If Python is not already downloaded, you will need to install it after the file is downloaded, make sure not to change the save location, and to add the path(this option will be given during installation, just a tick box)
> Make Sure You Have Internet For The First Time You Run For The Program To Download The Required Libraries When Code Run Through Installer.bat or Xbox-Mouse.exe

## How To Run Code
###  Easy Way (Windows Only) 
 > This might only work with python 3.10, not tested
 - Click on Xbox-Mouse.exe (It'll Download all the required Dependencies on its own so make sure to have internet the first time you run it)
 - Or Click on the Installer.bat (Basically does the same thing as the exe but the Terminal will be shown)

### Manual Method (Windows,MacOS,Linux)
 - Download the Libraries using (they only need to be done once)
 ```
 pip install -r Requirements.txt
 ```
 OR
 ```
 pip install pyautogui
 pip install inputs
 pip install plyer
 ```
 - Go to the Directory Where the Folder is Saved and Run
 ```
 python.exe controller.py
 ```
 <br>
 
 ## Combinations
 > Hold The Trigger to Use the Combinations
 <br>
 
| *Combination / Key* | *What it Does* |
| ------------------- | -------------: |
| `A` | Enter | 
| `B` | Tab | 
| `X` | Close Tab | 
| `Y` | Reopen Tab | 
| `START` | Killswitch | 
| `SELECT` | Close Window | 
| `LB` | Left Click | 
| `RB` | Right Click |  
| `LEFT THUMB` | Volume Down | 
| `RIGHT THUMB` | Volume Up | 
| `Left Joystick` | Scroll |
| `A + RT` | Opens First App on Taskbar | 
| `B + RT` | Shift Tab | 
| `X + RT` | Alt Tab | 
| `Y + RT` | Opens Third App on Taskbar | 
| `SELECT + RT` | Volume Mute | 
| `LB + RT` | Ctrl Shift Tab | 
| `RB + RT` | Ctrl Tab |  
| `LEFT THUMB + RT` | Holds Alt | 
| `RIGHT THUMB + RT + Right Joystick` | Drag Mouse | 
| `Right Joystick + RT` | Move Mouse|
| `Left Joystick + RT` | Fast Scroll |
| `A + LT` | Down Arrow Key | 
| `B + LT` | Right Arrow Key | 
| `X + LT` | Left Arrow Key | 
| `Y + LT` | Up Arrow Key | 
| `LB + LT` | Move to Left Desktop | 
| `RB + LT` | Move to Right Desktop | 
| `SELECT + LT` | Esc |
| `LEFT THUMB + LT` | Windows + Up (fullscreen) | 
| `RIGHT THUMB + LT` | Windows + Down (home screen)| 

## Customizing
### To Customize the bindings, they can be done by changing the values in mapping.json
 - There a Three Main Keys ***"LeftTriggerCondition"***, ***"RightTriggerCondition"***, ***"NoTriggerCondition"***
 
    - `"NoTriggerConditon"`                   (for No Combitation Controller Presses)
    - `"LeftTriggerCondition"`                (for Left Trigger Combintaions on the Controller)
    - `"RightTriggerCondition"`             (for Right Trigger Combinations on the Controller)

- Each of These Have Two Keys ***"ButtonAction"***, ***"JoystickAction"***

    - `"ButtonAction"`                        (for Button Presses)
        - They have a Key for Each Button on the Controller
        - Each Button has Three Keys ***"Key"***, ***"Type"***, ***"delay"***
        
            - `"Key"`                         (for the Key that will be Simulated to be Pressed)
            
            - `"Type"`                        (for the Type of Action that will be Performed) [All of these are Fucntions in controller.py, You can check their Documentation for Better Understanding]
                - `"buttonTap" `              (for a Single Key Press) [Make sure to keep delay: "0" even if no Delays Required]
                - `"CombinationalTap"`        (for a Combination of Keys Pressed) [Make sure to keep delay: "0" even if no Delays Required and keep key's Third Element as "NULL" in case no Third Key is Used]
                - `"ButtonHold"`              (for a Key to be Held Down)
                - `"ButtonClick"`             (Simulate Mouse Click)
                - `"ButtonHoldClick"`         (Simulate Mouse Click and Hold)
                
            - `"delay"`                       (for the Delay between the Key Presses)
            
    - `"JoystickAction"`                      (for Joystick Movements)
        - They May Have a Key for ***Scroll Action*** or ***Mouse Action***
        
            - `"Scroll"`                      (for Scroll Action)
                - `"joystick"`                (for the Joystick that will be used)
                - `"speed"`                   (for the Speed of the Scroll)
                
            - `"MouseControl"`                (for Mouse Action)
                - `"joystick"`                (for the Joystick that will be used)
                - `"LowerSensitivity"`        (Region of LowerSpeed [0-1])
                - `"UpperSensitivity"`        (Region of UpperSpeed [0-1])
                - `"LowerSpeed"`              (Speed of LowerSensitivity Region)
                - `"UpperSpeed"`              (Speed of UpperSensitivity Region)
                - `"time"`                    (Time for the Mouse to Move [smoothening])


## Updates
 - Added json file to make customizability easier
 - Fixed Some Small Errors
 - Made Code more Readable
 - Added Documentation
 - Fixed README.md

## Future Features
 - Add a WASD control to the joystick
 - Add a GUI Controller Detector to check if the controller is Connected properly
 - Add a GUI mapping system
 - Figure out a way to use Pyinstaller with this
 
## Know Issues
 - Issue: If the code is being run with a terminal and the terminal is closed without ending the program it might cause some issues
 - Solution: So Far the easiest way to fix it is either to close it through the Task Manager or ctrl+alt+del and log out

## Contact

Project Link: [https://github.com/Jimzical/Xbox-Controller-Mouse](https://github.com/Jimzical/Xbox-Controller-Mouse)

