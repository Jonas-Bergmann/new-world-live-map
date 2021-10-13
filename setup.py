from cx_Freeze import setup, Executable

base = None    

executables = [Executable("live-map.py", base=base)]

packages = ["idna", "cv2", "numpy", "time", "pyautogui", "pytesseract", "PIL", "re", "matplotlib.pyplot", "matplotlib.image", "keyboard"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "<any name>",
    options = options,
    version = "<any number>",
    description = '<any description>',
    executables = executables
)