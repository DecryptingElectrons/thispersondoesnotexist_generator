import os


#create some vars
site = "https://thispersondoesnotexist.com/image"

wgetcommand = "wget %s"%(site)

cpcommand = "cp image ../pics/image"

rmcommand = "rm image"



#this section simply discovers the last image number since last shutdown
#######
os.chdir("pics")

files = []

for name in os.listdir(os.curdir):
    if(os.path.isfile(name)):
        files.append(name)
try:
    lastpicnum = int(files[len(files)-1].split("image")[1].split(".")[0])
except Exception as e:
    lastpicnum = 0

print("LAST NUM - " + str(lastpicnum))

del files

os.chdir("..")
########


#removes last tmp file
os.chdir("tmp")
os.system(rmcommand)
    

#use wget in tmp and copy the image to the pics dir
while(1):
    lastpicnum += 1

    os.system(wgetcommand)

    os.system(cpcommand+str(lastpicnum)+".jpg")

    os.system(rmcommand)

