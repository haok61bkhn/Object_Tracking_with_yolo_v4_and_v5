import glob
import os
for x in glob.glob("label/*.txt"):
    f=open(x,"r")
    s=f.read().split("\n")[:-1]
    f.close()
    os.remove(x)
    f=open(x,"w+")
    res=""
    for y in s:
        res+=("0 "+y[3:])+"\n"
    f.write(res[:-1])
    f.close()

