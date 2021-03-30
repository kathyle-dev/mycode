#!/usr/bin/env python3
import shutil
import os

# using os.chdir() to be able to use this program from any location
os.chdir('/home/student/mycode/')

# use shutil.move() to movefile or folder to destination path
shutil.move('raynor.obj', 'ceph_storage/')
    ## if the file of the same name already exists, it will be OVERWRITTEN

# prompt for new file name for kerrigan.obj
xname = input('What is the new name for kerrigan.obj? ')

# rename current kerrigan.obj file
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

