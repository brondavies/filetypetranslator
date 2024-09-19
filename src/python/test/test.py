#Runs tests for a python build
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from fttlib import FTT

mimeType = FTT.getMimeType("Path/To/My/File.doc")
print(mimeType)

mimeType = FTT.getMimeType("Path/To/My/File.docx")
print(mimeType)

category = FTT.getFileCategory("Path/To/My/File.docx")
print(category)

category = FTT.getFileCategory("Path/To/My/File.jpg")
print(category)

extensions = FTT.getMimeTypeFileExtensions("text/csv")
print(extensions[0])
