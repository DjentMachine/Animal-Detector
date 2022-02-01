# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 10:44:19 2022

Script to grep all images in a given folder. Multiple sub folders can exist under the master folder
Returns a list of strings containing the paths for all images

v 0.1

@author: DBarros
"""
import os
import re

#Global variable to be printed
files = []

def tryint(s):
    try:
        return int(s)
    except ValueError:
        return s

def alphanum_key(s):
    """ Turn a string into a list of string and number chunks.
        "z23a" -> ["z", 23, "a"]
    """
    return [ tryint(c) for c in re.split('([0-9]+)', s) ]

def sort_nicely(l):
    """ Sort the given list in the way that humans expect.
    """
    l.sort(key=alphanum_key) 

def fileGrepper(directory):
    fPath = directory + "/fList.txt"
    if os.path.exists(fPath):
        os.remove(fPath)     
    try:
        fList = open(fPath, "a")   
        for i in os.scandir(directory):
            if i.is_file() and re.search("^.{1,}\.(gif|jpe?g|tiff?|png|bmp)$", i.path, re.IGNORECASE):
                # if it's a file, write
                files.append(i.path)
            elif i.is_dir():
                # if it's a directory, recursively call this function
                fileGrepper(os.path.abspath(i))
        sort_nicely(files)
        [fList.write(i+"\n") for i in files]        
        fList.close()
    except NotADirectoryError:
        # if `directory` isn't a directory, get the file size then
        print("NOT A DIRECTORY! Something went terribly wrong")
        #return os.path.getsize(directory)
    except PermissionError:
        # if for whatever reason we can't open the folder, return 0
        return 0