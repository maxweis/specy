#! /bin/python
import sys
import os

drive=(os.popen("df -h")).read()
print(drive.split())

