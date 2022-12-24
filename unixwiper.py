#!/usr/bin/env python

import os

# Unixwiper banner
print("##############################################")
print(""" 
 _____ _                 _     _           
|  ___| | ___  _   _  __| | __| | ___ _ __ 
| |_  | |/ _ \| | | |/ _` |/ _` |/ _ \ '__|
|  _| | | (_) | |_| | (_| | (_| |  __/ |      
|_|   |_|\___/ \__,_|\__,_|\__,_|\___|_| 
\n""")
print("# Unixwiper: Clean unwanted system data     #")
print("##############################################")

# Print usage
print("Usage: python unixwiper.py\n")

# Remove temporary files
print("Removing temporary files...")
os.system("rm -rf /private/var/folders/*")

# Remove system logs
print("Removing system logs...")
os.system("rm -rf /private/var/log/*")

# Remove cache files
print("Removing cache files...")
os.system("rm -rf /Library/Caches/*")

print("Done!")


