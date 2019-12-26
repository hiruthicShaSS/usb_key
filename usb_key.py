import platform as p
import hashlib as h
import win32api
import win32com.client
import os, time, getpass, shutil

def run():
    usbID = ""

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

    while True:
        os.system("title usb_Key status: ACTIVE       Press \"Ctrl + c\" to stop")
        os.system("mode con:cols=60 lines=20")
        os.system("cls")
        dr = ""
        
        try:
            drive = open("F:\\autorun.inf", 'r')
            dr = drive.readlines(1)[0].split('\n')[0]
        except:
            try:
                os.system("color 04")
                print("\n\n\n\n\n\tAccess denied")
                os.system("rundll32.exe user32.dll,LockWorkStation")
            except:
                time.sleep(1)
        if dr == "[autorun]":
            os.system("color 0a")
            print("\n\n\n\n\n\tAccess granted!")
            time.sleep(1)
            

os.system("cls")
os.system("mode con:cols=60 lines=20")
os.system("color f1")
user = getpass.getuser()
try:
    f = open(f"C:/Users/{user}/appdata/roaming/Microsoft/Windows/Start Menu/Programs/Startup/usb_key.py")
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
            shutil.copy("usb_key.py", f"C:/Users/{user}/appdata/roaming/Microsoft/Windows/Start Menu/Programs/Startup")
            print("Installation successful!")
        except:
            print("Error installing the script. Installation ABORTED.")
    else:
        print("Come out of your dream world and open your eyes!!")

    
            

    #print(win32api.GetVolumeInformation("D:\\")[1::])



