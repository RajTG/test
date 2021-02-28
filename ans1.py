import json
'''
{
"Atlanta, GA: Hartsfield-Jackson Atlanta International": 152,
"Baltimore, MD: Baltimore/Washington International Thurgood Marshall": 152
}

['BWI', '"Baltimore', ' MD: Baltimore/Washington International Thurgood Marshall"', '2003', '29\n']
        1="Baltimore 2= MD: Baltimore/Washington International Thurgood Marshall"
''' 
count=0
airportcodes=dict()
alist=[]
with open("airlines.csv", "r") as file:
    
    for line in file: 
        word = line.split(',') 
        if(count>0):
            alist.append(word)
        count+=1
        


for details in alist:
    
    if(details[0] not in airportcodes.keys()):
        airportcodes[details[0]]=1
    else:
        airportcodes[details[0]]+=1


#updated part(since I misinterpreted first output) ==============================================
fullnamecodes=dict()
for mdetails in alist:
    fname=mdetails[1]+mdetails[2]
    if(fname not in fullnamecodes.keys()):
        fullnamecodes[fname]=1
    else:
        fullnamecodes[fname]+=1

#updated part end============================================

maxtimes=(max(airportcodes, key=airportcodes.get))
maxnum=airportcodes[maxtimes]


minn=min(airportcodes.items(), key=lambda x: x[1])

codeset=set()
mincodeset=set()
fullcodeset=set()

for code,times in airportcodes.items():
    if(times==maxnum):
        codeset.add(code)

        
for code,times in airportcodes.items():
    if(times==minn[1]):
        mincodeset.add(code)


finaldict=dict()
minfinaldict=dict()

for k in alist:
    if(k[0] in codeset):
        fullname=k[1]+k[2]
    finaldict[fullname]=maxnum
mfullname=""
for m in alist:
    if(m[0] in mincodeset):
        mfullname=m[1]+m[2]
    minfinaldict[mfullname]=minn[1]



json_object = json.dumps(fullnamecodes, indent = 2)   
print(json_object)  

print(" Most number of times is ",list(finaldict.keys())[0],": ",maxnum)

print(" Least number of times is ",list(minfinaldict.keys())[1],": ",minn[1])
        


