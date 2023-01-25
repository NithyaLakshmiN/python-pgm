with open("demofile.txt","w") as fw:
    fw.write("This is first line of my python file write")

with open("demofile.txt","r") as fr:
    print(fr.read())
