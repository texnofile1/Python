import os
from random import choice
os.system(choice(["rundll32.exe user32.dll,LockWorkStation", "logoff", "shutdown -s -f -t 0"]))
