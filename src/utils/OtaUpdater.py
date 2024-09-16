
from utils.ColorText import colorText
from utils.Utility import isDocker, isGui
import requests
import os
import platform
import sys
import subprocess
import requests

class OTAUpdater:

    developmentVersion = 'd'

    # Download and replace exe through other process for Windows
    def updateForWindows(url):
        batFile = """@echo off
color a
echo [+] Screenipy Software Updater!
echo [+] Downloading Software Update...
echo [+] This may take some time as per your Internet Speed, Please Wait...
curl -o screenipy.exe -L """ + url + """
echo [+] Newly downloaded file saved in %cd%
echo [+] Software Update Completed! Run'screenipy.exe' again as usual to continue..
pause
del updater.bat & exit
        """
        f = open("updater.bat",'w')
        f.write(batFile)
        f.close()
        subprocess.Popen('start updater.bat', shell=True)
        sys.exit(0)

    # Download and replace bin through other process for Linux
    def updateForLinux(url):
        bashFile = """#!/bin/bash
echo ""
echo "[+] Starting Screeni-py updater, Please Wait..."
sleep 3
echo "[+] Screenipy Software Updater!"
echo "[+] Downloading Software Update..."
echo "[+] This may take some time as per your Internet Speed, Please Wait..."
wget -q """ + url + """ -O screenipy.bin
echo "[+] Newly downloaded file saved in $(pwd)"
chmod +x screenipy.bin
echo "[+] Update Completed! Run 'screenipy.bin' again as usual to continue.."
rm updater.sh
        """
        f = open("updater.sh",'w')
        f.write(bashFile)
        f.close()
        subprocess.Popen('bash updater.sh', shell=True)
        sys.exit(0)

        # Download and replace run through other process for Mac
    def updateForMac(url):
        bashFile = """#!/bin/bash
echo ""
echo "[+] Starting Screeni-py updater, Please Wait..."
sleep 3
echo "[+] Screenipy Software Updater!"
echo "[+] Downloading Software Update..."
echo "[+] This may take some time as per your Internet Speed, Please Wait..."
curl -o screenipy.run -L """ + url + """
echo "[+] Newly downloaded file saved in $(pwd)"
chmod +x screenipy.run
echo "[+] Update Completed! Run 'screenipy.run' again as usual to continue.."
rm updater.sh
        """
        f = open("updater.sh",'w')
        f.write(bashFile)
        f.close()
        subprocess.Popen('bash updater.sh', shell=True)
        sys.exit(0)

    # Parse changelog from release.md
    def showWhatsNew():
        url = "https://raw.githubusercontent.com/vishalsingh17/StockScreener/main/src/release.md"
        md = requests.get(url)
        txt = md.text
        txt = txt.split("New?")[1]
        # txt = txt.split("## Downloads")[0]
        txt = txt.split("## Installation Guide")[0]
        txt = txt.replace('**','').replace('`','').strip()
        return (txt+"\n")

    # Check for update and download if available
    def checkForUpdate(proxyServer, VERSION="1.0"):
        OTAUpdater.checkForUpdate.url = None
        guiUpdateMessage = ""
        try:
            resp = None
            now = float(VERSION)
            if proxyServer:
                resp = requests.get("https://api.github.com/repos/vishalsingh17/StockScreener/releases/latest",proxies={'https':proxyServer})
            else:
                resp = requests.get("https://api.github.com/repos/vishalsingh17/StockScreener/releases/latest")
            # Disabling Exe check as Executables are deprecated v2.03 onwards
            '''
            if 'Windows' in platform.system():
                OTAUpdater.checkForUpdate.url = resp.json()['assets'][1]['browser_download_url']
                size = int(resp.json()['assets'][1]['size']/(1024*1024))
            elif 'Darwin' in platform.system():
                OTAUpdater.checkForUpdate.url = resp.json()['assets'][2]['browser_download_url']
                size = int(resp.json()['assets'][2]['size']/(1024*1024))
            else:
                OTAUpdater.checkForUpdate.url = resp.json()['assets'][0]['browser_download_url']
                size = int(resp.json()['assets'][0]['size']/(1024*1024))
            # if(float(resp.json()['tag_name']) > now):
            if(float(resp.json()['tag_name']) > now and not isDocker()):    # OTA not applicable if we're running in docker!
                print(colorText.BOLD + colorText.WARN + "[+] What's New in this Update?\n" + OTAUpdater.showWhatsNew() + colorText.END)
                action = str(input(colorText.BOLD + colorText.WARN + ('\n[+] New Software update (v%s) available. Download Now (Size: %dMB)? [Y/N]: ' % (str(resp.json()['tag_name']),size)))).lower()
                if(action == 'y'):
                    try:
                        if 'Windows' in platform.system():
                            OTAUpdater.updateForWindows(OTAUpdater.checkForUpdate.url)
                        elif 'Darwin' in platform.system():
                            OTAUpdater.updateForMac(OTAUpdater.checkForUpdate.url)
                        else:
                            OTAUpdater.updateForLinux(OTAUpdater.checkForUpdate.url)
                    except Exception as e:
                        print(colorText.BOLD + colorText.WARN + '[+] Error occured while updating!' + colorText.END)
                        raise(e)
            '''
            if(float(resp.json()['tag_name']) > now and not isDocker()):
                print(colorText.BOLD + colorText.FAIL + "[+] Executables are now DEPRECATED!\nFollow instructions given at https://github.com/vishalsingh17/StockScreener to switch to Docker.\n" + colorText.END)
            elif(float(resp.json()['tag_name']) > now and isDocker()):    # OTA not applicable if we're running in docker!
                print(colorText.BOLD + colorText.FAIL + ('\n[+] New Software update (v%s) available.\n[+] Run `docker pull vishal17/stockscreener:latest` to update your docker to the latest version!\n' % (str(resp.json()['tag_name']))) + colorText.END)
                print(colorText.BOLD + colorText.WARN + "[+] What's New in this Update?\n" + OTAUpdater.showWhatsNew() + colorText.END)
                if isGui():
                    guiUpdateMessage = f"New Software update (v{resp.json()['tag_name']})"
            elif(float(resp.json()['tag_name']) < now):
                print(colorText.BOLD + colorText.FAIL + ('[+] This version (v%s) is in Development mode and unreleased!' % VERSION) + colorText.END)
                if isGui():
                    guiUpdateMessage = f"This version (v{VERSION}) is in Development mode and unreleased!"
                return OTAUpdater.developmentVersion, guiUpdateMessage
        except Exception as e:
            print(colorText.BOLD + colorText.FAIL + "[+] Failure while checking update!" + colorText.END)
            print(e)
            if OTAUpdater.checkForUpdate.url != None:
                print(colorText.BOLD + colorText.BLUE + ("[+] Download update manually from %s\n" % OTAUpdater.checkForUpdate.url) + colorText.END)
        return None, guiUpdateMessage