import os
import re
import deauth


def listInterfaces():
    os.system("sudo airmon-ng > output.txt")
    lines = os.popen("wc -l output.txt | awk '{print $1}'").read()
    interfaces = []

    for n in range(int(lines)):
        result = os.popen("cat output.txt | awk 'NR==" +
                          str(n) + "{print $2}'").read()
        pattern = re.compile(r'\s+')
        result = re.sub(pattern, '', result)
        result = '/' + result + '-Remove'
        if result.find("Interface") == -1 and result.find("/-Remove") == -1:
            result = result.replace("/", "")
            result = result.replace("-Remove", "")
            interfaces.append(result)

    for number in range(len(interfaces)):
        print(str(number) + ' -> ' + interfaces[number])
    chosse = input('Select your interface: ')
    print(chosse)
    try:
        chosse = int(chosse)
        return interfaces[chosse]
    except:
        return "This is not a interface available"


def getInterfaceOn(interface):
    return_res = os.popen("sudo airmon-ng | awk '{print $2}'").read()
    arrayInterfaces = return_res.split(sep="\n")
    print(arrayInterfaces)
    for n in range(int(len(arrayInterfaces))):
        if arrayInterfaces[n].find(interface) != -1:
            deauth.scan(arrayInterfaces[n])

def startMonitorMode(interface):
    if interface.find("This is not a interface available") == -1:
        os.system("sudo airmon-ng start " + interface)
        chosse = input('Start deauth attack ?:')
        if chosse in ['yes', 'Yes', 'YES', 'Y', 'y']:
            getInterfaceOn(interface)

print("Listing available interfaces")
print("|------------------------|")
startMonitorMode(listInterfaces())
