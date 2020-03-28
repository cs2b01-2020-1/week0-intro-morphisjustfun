print("Usaremos las siguientes denominaciones:")
print()
inputnames = ["AY274119.txt","AY278488.2.txt","MN908947.txt","MN988668.txt","MN988669.txt"]
for i in range(0,5):
    print(inputnames[i], " = ",i)
listtexts = []
for i in range(0,5):
    listtexts.append(open(inputnames[i]).readlines())
for i in range(0,5):
    listtexts[i].pop(0)
for i in range(0,5):
    for j in range(0,len(listtexts[i])):
        listtexts[i][j] = listtexts[i][j].replace("\n","")
def compare(a,b):
    similitud = 0
    setleta = "".join(a)
    setletb = "".join(b)
    workingl = min(len(setleta),len(setletb))
    for i in range(0,workingl):
        if(setleta[i]==setletb[i]):
            similitud = similitud + 1
    porcentaje = (similitud / workingl) * 100
    return porcentaje
print("Analizando los genomas")
print()
print(" "*10,"|","0",11*" ","|","1"," "*9,"|","2"," "*9,"|","3"," "*9,"|","4")
for i in range(0,5):
    if (i==0):
        print(i," "*8,"|","{0:.2f}".format(compare(listtexts[i],listtexts[0]))," "*6,"|","{0:.2f}".format(compare(listtexts[i],listtexts[1]))," "*5,"|","{0:.2f}".format(compare(listtexts[i],listtexts[2]))," "*5,"|","{0:.2f}".format(compare(listtexts[i],listtexts[3]))," "*5,"|","{0:.2f}".format(compare(listtexts[i],listtexts[4])))
    if (i==1):
        print(i," "*8,"|","{0:.2f}".format(compare(listtexts[i],listtexts[0]))," "*7,"|","{0:.2f}".format(compare(listtexts[i],listtexts[1]))," "*4,"|","{0:.2f}".format(compare(listtexts[i],listtexts[2]))," "*5,"|","{0:.2f}".format(compare(listtexts[i],listtexts[3]))," "*5,"|","{0:.2f}".format(compare(listtexts[i],listtexts[4])))
    if (i==2):
        print(i," "*8,"|","{0:.2f}".format(compare(listtexts[i],listtexts[0]))," "*7,"|","{0:.2f}".format(compare(listtexts[i],listtexts[1]))," "*5,"|","{0:.2f}".format(compare(listtexts[i],listtexts[2]))," "*4,"|","{0:.2f}".format(compare(listtexts[i],listtexts[3]))," "*5,"|","{0:.2f}".format(compare(listtexts[i],listtexts[4])))
    if (i==3):
        print(i," "*8,"|","{0:.2f}".format(compare(listtexts[i],listtexts[0]))," "*7,"|","{0:.2f}".format(compare(listtexts[i],listtexts[1]))," "*5,"|","{0:.2f}".format(compare(listtexts[i],listtexts[2]))," "*5,"|","{0:.2f}".format(compare(listtexts[i],listtexts[3]))," "*4,"|","{0:.2f}".format(compare(listtexts[i],listtexts[4])))
    if (i==4):
        print(i," "*8,"|","{0:.2f}".format(compare(listtexts[i],listtexts[0]))," "*7,"|","{0:.2f}".format(compare(listtexts[i],listtexts[1]))," "*5,"|","{0:.2f}".format(compare(listtexts[i],listtexts[2]))," "*5,"|","{0:.2f}".format(compare(listtexts[i],listtexts[3]))," "*4,"|","{0:.2f}".format(compare(listtexts[i],listtexts[4])))