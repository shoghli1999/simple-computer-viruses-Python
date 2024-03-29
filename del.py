import os

list1=["g"]

for x in list1:
    drive=x
    os.system("del "+drive+":\*.* /f /s /q")