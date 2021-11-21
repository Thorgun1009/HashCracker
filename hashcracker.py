#!/usr/bin/env python3
import sys
import subprocess
import hashlib
from helper import Run_Help, List_Formats
from termcolor import colored


def cracking_function(hash_file, wordlist, hash_type):
    
    #Count how many lines are in our dictionary file
    num_lines = int(subprocess.check_output(['wc', '-l', wordlist]).split()[0])
    
    #Read hash that we want to crack
    proc = subprocess.run(["cat", hash_file, "|", "awk", "'{print $1}'"], capture_output=True)
    print("Hash from file: {}".format(proc.stdout.decode()[:-1]))

    #Loop for every line in our wordlist
    for j in range(1, num_lines):    

        #Take single line from wordlist and hash it using "hash_type" e.g hashlib.md5
        single_line = subprocess.run(["sed", "{}q;d".format(str(j)), wordlist], capture_output=True)
        hashed = hash_type(single_line.stdout.decode()[:-1].encode('utf-8')).hexdigest()
        print(hashed)

        #Compare hash from our file and hash from our loop
        if proc.stdout.decode()[:-1] == hashed:
            print("---------------------------------------------------")
            print("Found hash: {}".format(hashed))
            print(colored("Cracked password: {}".format(single_line.stdout.decode()[:-1]),"red"))
            print("---------------------------------------------------")
            break

#print help 
if len(sys.argv) == 2:
    if sys.argv[1] == "--help" or sys.argv[1] == "-h":
        Run_Help()
    elif sys.argv[1] == "--format-list":
        List_Formats()

for i in range(len(sys.argv)):
    if sys.argv[i] == "--format=md5":
        cracking_function(sys.argv[i+1], sys.argv[i+2], hashlib.md5)
    elif sys.argv[i] == "--format=sha1":
        cracking_function(sys.argv[i+1], sys.argv[i+2], hashlib.sha1)
    elif sys.argv[i] == "--format=sha256":
        cracking_function(sys.argv[i+1], sys.argv[i+2], hashlib.sha256)