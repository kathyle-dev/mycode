#!/usr/bin/env python3
import shutil
import os

# force the program to start in the home directory so that the program can be run from anywhere
os.chdir("/home/student/mycode/")

# use shutil.copy() to make a copy of this file
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

# use shutill.copytree() to copy an entire directory
shutil.copytree("5g_research/", "5g_research_backup/")

