#File organization
import os 
import shutil

#Input the path the user wants to enter 
path= input("Enter your directory: ")
files= os.listdir(path)

for file in files:
    filename, extension = os.path.splitext(file)
    extension= extension[1:]

    if os.path.exists(path+ "/"+ extension):
        shutil.move(path+ "/" +file, path+ "/" +extension+ "/" +file)
    else:
        os.makedirs(path+ "/" +extension)
        shutil.move(path+ "/" +file, path+ "/" +extension+ "/" +file) 