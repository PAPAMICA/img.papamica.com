#!/usr/bin/python3
import glob
import os
from xml.dom import minidom

GITHUB_REPOSITORY_URL = 'https://github.com/PAPAMICA/img.papamica.com'

try:
    os.remove("./list.xml") 
  #  os.remove("./README.md") 
except:
    print ("file don't exist")

imglist = minidom.Document()

xml = imglist.createElement('imglist') 
imglist.appendChild(xml)
for filename in sorted(glob.glob(os.getcwd() + "./*/*.*", recursive = True)):
    try:
        print(os.path.basename(filename) + " " + (filename))
        img = imglist.createElement('img')
        img.setAttribute('name', os.path.basename(filename))
        img.setAttribute('link', filename)
        
        xml.appendChild(img)
    except:
         print (f" ❌ {filename} error !")

xml_str = imglist.toprettyxml(indent ="\t") 
  
save_path_file = "list.xml"
  
with open(save_path_file, "w") as f:
    f.write(xml_str) 
