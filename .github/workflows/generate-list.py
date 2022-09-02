#!/usr/bin/python3
import glob
import os
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree

GITHUB_REPOSITORY_URL = 'https://github.com/PAPAMICA/img.papamica.com'

try:
    os.remove("./list.xml")
    os.remove("./list") 
  #  os.remove("./README.md") 
except:
    print ("file don't exist")

imglist = Element('imglist')
imglist2 = open('list', 'a')

for filename in sorted(glob.glob("./*/*.*", recursive = True)):
    try:
        print(os.path.basename(filename) + " " + (filename[1:]))
        child = SubElement(imglist, "img")
        name = SubElement(child, "name")
        name.text = os.path.basename(filename)
        link = SubElement(child, "link")
        link.text = filename[1:]
        imglist2.write("https://img.papamica.com" + filename[1:] + "\n")

    except:
         print (f" ❌ {filename} error !")

tree = ElementTree(imglist)
  
save_path_file = "list.xml"
  
with open (save_path_file, "wb") as files :
        tree.write(files)
