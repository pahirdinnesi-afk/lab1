fin=open("mailbox.txt","r")
fout=open("output.txt","w")

ls_names=[]
lines=fin.readlines()
for line in lines:
    if line.startswith("Details:"):

        name=line.split()[1].split("=")[-1]
        if name not in ls_names:
            ls_names.append(name)

for name in ls_names:
    fout.write(name+"\n")
fin.close()
fout.close()