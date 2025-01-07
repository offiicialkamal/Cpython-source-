import requests
import subprocess
import os, sys
import time
#import requests
logs_check = True
version = '1.0.0'

def printTheLogo(ascii_art):
    try:
        subprocess.run(["lolcat"], input=ascii_art.encode())
    except subprocess.CalledProcessError as ss:
        print(f'unable to find the logo retrying to get the logo  {ss}')
        ascii_art = downloadTheLogo()
        printTheLogo(ascii_art)
      
def downloadTheLogo():
    try:
        g = 'hackesofice/Z/refs/heads/main/CPYTHON-TOOL/Ascii'
        url = f'https://raw.githubusercontent.com/{g}'
        re = requests.get(url).text
        ascii_art = f"""{re.format(version=version)}"""
        return ascii_art
    except requests.RequestException as e:
        print('Unable To Detect Internet Connection')
        time.sleep(1)
        print(f'Retrying To Connect Make Sure You Are Connected To internet {e}')
        time.sleep(2)
        downloadTheLogo()
ascii_art = downloadTheLogo()
main_code = '''
from modules import enc2'''
try:
  #  os.system('clear')
    print('make sure to follow us on github')
    time.sleep(3)
    os.system('xdg-open https://github.com/hackesofice')
    os.system('pkg update && pkg upgrade && pkg install git -y && pkg install cython -y && pip install requests && gem install lolcat')
    os.system('clear')
    printTheLogo(ascii_art)

    subprocess.run(
        ["python", "-c", main_code, "build_ext", "--inplace"],
        check=logs_check
    )
    print("Build completed successfully!")
except subprocess.CalledProcessError as e:
    print(f"Build failed: {e}")
