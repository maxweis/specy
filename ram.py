#! /bin/python


#specy:  an Arch Linux system command line description tool
   
#Copyright (C) 2014-2015  Max Weis


#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 3
#of the License, or (at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.


import os
import sys

#Get readable free memory output
memory = (os.popen("free -h")).read()

memory = memory.split('\n')

used_memory = memory[1].split()[2]
total_memory = memory[1].split()[1]

if (len(sys.argv) < 2):
    print("Usage:  " + sys.argv[0] + " [-t] [-u]")

elif sys.argv[1] == '-t' or sys.argv[1] == "--total":
    print(total_memory)

elif sys.argv[1] == '-u' or sys.argv[1] == "--used":
    print(used_memory)

else:
    print("Usage:  " + sys.argv[0] + "[-t] [f]")
