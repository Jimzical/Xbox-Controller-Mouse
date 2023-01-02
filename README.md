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
 - There a Three Main Keys
    - "NoTriggerConditon"(for No Combitation Controller Presses)
    - "LeftTriggerCondition"(for Left Trigger Combintaions on the Controller)
    - "RightTriggerCondition" (for Right Trigger Combinations on the Controller)

- Each of These Have Two Keys
    - "ButtonAction" (for Button Presses)
        - They have a Key for Each Button on the Controller
        - Each Button has Three Keys
            - "Key" (for the Key that will be Simulated to be Pressed)
            - "type" (for the Type of Action that will be Performed)
                - "buttonTap" (for a Single Key Press)
                - "CombinationalTap" (for a Combination of Keys Pressed)    
                - "ButtonHold" (for a Key to be Held Down)
                - "ButtonClick" (Simulate Mouse Click)
                - "ButtonHoldClick" (Simulate Mouse Click and Hold)
            - "delay" (for the Delay between the Key Presses)
    - "JoystickAction" (for Joystick Movements)
        - They May Have a Key for Scroll Action or Mouse Action
            - "Scroll" (for Scroll Action)
                - "joystick" (for the Joystick that will be used)
                - "speed" (for the Speed of the Scroll)
            - "MouseControl" (for Mouse Action)
                - "joystick" (for the Joystick that will be used)
                - "LowerSensitivity" (Region of LowerSpeed [0-1])
                - "UpperSensitivity" (Region of UpperSpeed [0-1])
                - "LowerSpeed" (Speed of LowerSensitivity Region)
                - "UpperSpeed" (Speed of UpperSensitivity Region)
                - "time" (Time for the Mouse to Move [smoothening])


## Updates
 - Added json file to make customizability easier
 - Fixed Some Small Errors
 - Made Code more Readable
 - Added Documentation
 - Fixed README.md

## Know Issues
 - Issue: If the code is being run with a terminal and the terminal is closed without ending the program it might cause some issues
 - Solution: So Far the easiest way to fix it is either to close it through the Task Manager or ctrl+alt+del and log out

## Contact

Arish Kumar - arishkumar2003@gmail.com

Project Link: [https://github.com/Jimzical/Xbox-Controller-Mouse](https://github.com/Jimzical/Xbox-Controller-Mouse)


       
       
{
    "Killswitch" : "start",

    "NoTriggerCondition": {
        "ButtonAction":{
            "a": {
                "type": "ButtonTap",
                "key": "enter",
                "delay": 0.1
            },
            "b": {
                "type": "ButtonTap",
                "key": "tab",
                "delay": 0
            },
            "x": {
                "type": "CombinationalTap",
                "key": ["ctrl","w","NULL"],
                "delay": 0
            },
            "y": {
                "type": "CombinationalTap",
                "key": ["ctrl","shift","t"],
                "delay": 0
            },
            "select": {
                "type": "CombinationalTap",
                "key": ["alt","f4","NULL"],
                "delay": 0
            },
            "lb": {
                "type": "ButtonClick",
                "key": "left"
            },
            "rb": {
                "type": "ButtonClick",
                "key": "right"
            },
            "leftthumb": {
                "type": "ButtonTap",
                "key": "volumedown",
                "delay": 0
            },
            "rightthumb": {
                "type": "ButtonTap",
                "key": "volumeup",
                "delay": 0
            }
        },


        "JoystickAction":{

            "Scroll": {
                "joystick": "left",
                "speed": 50
            }
        }
    },

    "LeftTriggerCondition":{
        "ButtonAction":{
            "a":{
                "type": "ButtonTap",
                "key": "down",
                "delay": 0
            },
            "b":{
                "type": "ButtonTap",
                "key": "right",
                "delay": 0
            },
            "x":{
                "type": "ButtonTap",
                "key": "left",
                "delay": 0
            },
            "y":{
                "type": "ButtonTap",
                "key": "up",
                "delay": 0
            },
            "select":{
                "type": "ButtonTap",
                "key": "esc",
                "delay": 0
            },
            "lb":{
                "type": "CombinationalTap",
                "key": ["ctrl","super","left"],
                "delay": 0
            },
            "rb":{
                "type": "CombinationalTap",
                "key": ["ctrl","super","right"],
                "delay": 0
            },
            "leftthumb":{
                "type": "CombinationalTap",
                "key": ["super","up"],
                "delay": 0
            },
            "rightthumb":{
                "type": "CombinationalTap",
                "key": ["super","down"],
                "delay": 0
            }
        },
        "JoystickAction":{
            "None": "None"
        }
        
    },

    "RightTriggerCondition":{
        "ButtonAction":{
            "a":{
            "type": "CombinationalTap",
            "key": ["ctrl","super","1"],
            "delay": 0                
            },  
            "b":{
            "type": "CombinationalTap",
            "key": ["shift","tab"],
            "delay": 0                
            },
            "x":{
            "type": "CombinationalTap",
            "key": ["alt","tab"],
            "delay": 0                
            },
            "y":{
            "type": "CombinationalTap",
            "key": ["ctrl","super","3"],
            "delay": 0                
            },
            "select":{
            "type": "ButtonTap",
            "key": "volumemute",
            "delay": 0                
            },
            "lb":{
            "type": "CombinationalTap",
            "key": ["ctrl","tab","shift"],
            "delay": 0                
            },
            "rb":{
            "type": "CombinationalTap",
            "key": ["ctrl","tab"],
            "delay": 0                
            },
            "leftthumb":{
            "type": "ButtonHoldTap",
            "key": "alt",
            "delay": 0                
            },
            "rightthumb":{
            "type": "ButtonHoldClick",
            "key": "left",
            "delay": 0               
            }
        },
        "JoystickAction":{
            "MouseControl": {
                "joystick": "right",
                "LowerSensitivity": 0.30,
                "UpperSensitivity": 0.75,
                "LowerSpeed": 15,
                "UpperSpeed": 65,
                "time": 0.00001
            }
        }
    }
}

