import os
import glob
def help():
    print('adduser(user),removeuser(user),listusers(),getpoints(user),setpoints(user) in setpoints or getpoints, press CTRL+x to exit, and if asked to save, Y then [enter]')
limit = False
limitnum = 0
def adduser(user):
    a = len(glob.glob('*.user'))
    if limit == True:
        if a > limitnum:
            Warning('User limit reached - buy a better edition!')
        else:
            os.system('touch ' + user + '.user')

    else:
        os.system('touch ' + user + '.user')

def removeuser(user):
    os.system('rm ' + user + '.user')


def listusers():
    os.system('find . -name \"*.user\"')

def getpoints(user):
    #file1 = file(user+'.user','w+')
    #pts = file1.read()
    #print(pts)
    a = len(glob.glob('*.user'))
    if limit == True:
        if a > limitnum:
            Warning('Amount of users greater than user limit - buy a better edition or remove a user!')
            print('Amount of users greater than user limit - buy a better edition or remove a user!')
        else:
            os.system('nano ' + user + '.user')

    else:
        os.system('nano ' + user + '.user')


def setpoints(usertoset):
    a = len(glob.glob('*.user'))
    if limit == True:
        if a > limitnum:
            Warning('Amount of users greater than user limit - buy a better edition or remove a user!')
            print('Amount of users greater than user limit - buy a better edition or remove a user!')
        else:
            os.system('nano ' + usertoset + '.user')

    else:
        os.system('nano ' + usertoset + '.user')



while True:
    input('[command]() or help()')
