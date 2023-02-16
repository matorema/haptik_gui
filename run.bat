@echo off

if %USERNAME% == marmatore (
    call C:/Users/marmatore/Anaconda3/Scripts/activate 
    call activate py39 
    call C:/Users/marmatore/Anaconda3/envs/py39/python.exe C:/Users/marmatore/Desktop/GitHub/haptik_gui/gui.py
    ) else (
        msg * "Start the GUI with terminal and command: python gui.py"
        )