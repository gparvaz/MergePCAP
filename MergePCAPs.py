import os
import sys
#import turtle
import glob
import random 

#s=turtle.Screen()
#s.title("Input Directory")
#s.screensize(50,50)
#s.forward(50)
#user_input = input("Enter the path of your file: ")
#print(user_input)
#print(type(user_input))
#print(glob.glob("D:\\Python\\Programm\\1\\*.pcap"))
#arr = os.listdir("D:\\Python\\Programm\\1\\")


def filebrowser():
    "Returns files with a pcap extension"
    return [f for f in glob.glob("D:\\Python\\Programm\\1\\*.pcap")]

x = filebrowser()

firsrpcap=open(x[0],'rb')
firstpcapdata = firsrpcap.read()
fsize=os.path.getsize('D:\\Python\\Programm\\1\\First.pcap')
firsrpcap.close()
xs = bytearray(firstpcapdata)
firstfiledatalink=firstpcapdata[20]



del x[0]
for i in x:
    secondpcap=open(i,'rb')
    secondpcapdata = secondpcap.read()
    if secondpcapdata[20]==firstfiledatalink: #check datalink of pcaps in directory
        ssize=os.path.getsize(i)
        secondpcap.close() 
        ys = bytearray(secondpcapdata[24:ssize])
        j=0
        while j < ssize-24:  
            xs.append(ys[j])
            j=j+1
  
        
mergedpcapname=""
d=random.randrange(1, 100)

fname = ['Merged_OutPut', str(d) ,'.pcap']
mergedpcapname = mergedpcapname.join(fname)
fw = open(mergedpcapname,'wb')
fw.write(xs)
fw.close()
