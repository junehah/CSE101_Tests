#!/usr/bin/python
#!/python
# -*- coding: utf-8 -*-
import filecmp, os, shutil

#you may have to change the directory path
path = os.getenv('HOME') + '/Documents/101/lab8'
os.chdir('/home/jables/Documents/101/lab8/')

def createFolders():
    for f in os.listdir(path):
        f_name, f_ext = os.path.splitext(f)
        counter = 0
        i = 0
        #extracting ubitname ==> will be in variable name
        name = f_name
        name = name[6:]
        while name[i]!='_' and i!= len(f_name):
            counter = counter + 1
            i = i + 1
        name = name[:counter]
        #creating folder with ubitname as its title
        #in the chance the assignment requires multiple files, code will avoid
        #making duplicate folders: hence the try-catch statements
        try:
            os.mkdir(name)
            print("folder made")
        except:
            print("already made - ignoring duplicate")

        #moving folders into the made folders
        #this part is NOT in the try in case of duplicate folders
        if name in f_name:
            old = str(path) + '/' + str(f_name) + f_ext
            new = str(path) + '/' + str(name) + '/' + str(f_name) + f_ext
            shutil.move(old, new)

createFolders()
