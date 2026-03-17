import os
os.remove("demofile.txt")

if os.path.exists("demofile.txt"): #checjking if it exists, to prevent errors
    os.remove("demofile.txt")
else:
    print("file doesnt exist")   

os.rmdir("myfolder")    #a folder can be deleted only if its empty 


#copying using shutil
import shutil
shutil.copy('source.txt' , 'copy.txt') #copy.txt will contain same text as source.txt

with open('copy.txt', 'a') as f:
    f.write("!!") #added !! at the end

#backing up
shutil.copy2('copy.txt', 'back_up.txt')    