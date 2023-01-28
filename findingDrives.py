import os  #to communicate with underlying operating system
class SystemDriveFinder:
    def __init__(self):
        pass
    def find_drives(self):
        print('This is the find drives method of system Drive Finder class')
        drives=[]
        for x in range(65,91):
            if os.path.exists(chr(x)+ ':'):
                drives.append(chr(x))
        return drives





