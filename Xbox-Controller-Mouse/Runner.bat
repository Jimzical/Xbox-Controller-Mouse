@echo off
echo start

if not EXIST "C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python310\Lib\site-packages\pyautogui" (pip install pyautogui)
if not EXIST "C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python310\Lib\site-packages\inputs.py" (pip install inputs)

"C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python310\python.exe" "controller.py"

echo done
Exit
