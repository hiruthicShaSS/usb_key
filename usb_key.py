"""
+ If you are a noob, then dont change anything and go to line 57 and enter your drive letter in the
    dashes provided.
+ If you are an expert..Wel, then you know what you have to do...

+++Any change in this code can be done and dont forget to do a pull request in my repo
~ instagram : hiruthicsha
~ twitter        : hiruthicsha
~ github        : hiruthic2002
"""

import platform as p
import hashlib as h
import win32api
import win32com.client
import os, time, getpass, shutil
import datetime as dt

# failsafe codes:
# os.system("taskkill /IM cmd.exe")

def run():  
    usbID = ""
    DL = "E" # Enter your drive letter

    arc = p.machine()
    ver = p.version()
    platf = p.platform()
    platf_ver = p.uname()
    proc = p.processor()
    hdd = str(win32api.GetVolumeInformation("D:\\")[1::]) + str(win32api.GetVolumeInformation("C:\\")[1::]) + str(win32api.GetVolumeInformation("E:\\")[1::])
    wmi = win32com.client.GetObject("winmgmts:")
    for usb in wmi.InstancesOf("Win32_USBHub"):
        usbID += usb.DeviceID
        
    total = h.sha3_512((arc + ver + platf + str(platf_ver) + proc + hdd + usbID).encode()).hexdigest()
    minute = 0

    while True:
        t = dt.datetime.now()
        t = str(t).split(' ')[-1]
        t = str(t).split(':')
        content = ""
        for pos in t:
            content += h.sha3_512(pos.encode()).hexdigest()
        if int(t[1]) > int(minute):
            ck_content = content
            main_file = open("key.sha", 'w+')
            key_file = open(f"{DL}:/{total}", 'w+')
            key_file.write(h.sha3_512(content.encode()).hexdigest())
            main_file.write(h.sha3_512(content.encode()).hexdigest())
            key_file.close()
            main_file.close()
        
        minute = int(t[1])
        file = open(f"{DL}:/{total}", 'r')
        file2 = open("key.sha", 'r')
        if file.readlines() == file2.readlines():
            pass
        else:
            print("somethings wrong")

        while True:
            os.system("title usb_Key status: ACTIVE       Press \"Ctrl + c\" to stop")
            os.system("mode con:cols=60 lines=20")
            os.system("cls")
            dr = ""
            
            try:
                drive = open(f"{DL}:/{total}", 'r')
                Key_file = open("key.sha", 'r')
                dr = drive.readlines()
            except:
                try:
                    os.system("color 04")
                    print("\n\n\n\n\n\tAccess denied")
                    #os.system("rundll32.exe user32.dll,LockWorkStation")
                except:
                    time.sleep(1)
            if dr == Key_file.readlines():
                os.system("color 0a")
                print("\n\n\n\n\n\tAccess granted!")
                time.sleep(1)
            

os.system("cls")
os.system("mode con:cols=60 lines=20")
os.system("color f1")
user = getpass.getuser()
try:
    f = open(f"C:/Users/{user}/appdata/roaming/Microsoft/Windows/Start Menu/Programs/usb_key.py")
    run()
except KeyboardInterrupt:
    os.system("cls")
    print("Stopping service...stopped")
    os.system("pause")
    os.system("exit")
except FileNotFoundError:
    os.system("title Installation.")
    prompt = input("If you install this script everytime you turn on your systemyou will have to plug the USB with the system. Do you reallywant to install this script? (Y / N). ")
    if prompt.upper() == 'N':
        os.system("taskkill /IM cmd.exe")
    elif prompt.upper() == 'Y':
        try:
            dl = input("Enter the drive letter: ")
            shutil.copy("usb_key.py", f"C:/Users/{user}/appdata/roaming/Microsoft/Windows/Start Menu/Programs")
            print("Installation successful!")
            #os.system("echo Restarting in: ")
            os.system("timeout \t 5")
            #os.system(f"python \"C:/Users/{user}/appdata/roaming/Microsoft/Windows/Start Menu/usb_key.py\"")
            os.system("exit")
            
        except:
            print("Error installing the script. Installation ABORTED.")
            exit(1)
        else:
            print("Come out of your dream world and open your eyes!!")
            exit(1) 
    #print(win32api.GetVolumeInformation("D:\\")[1::])
exit()
