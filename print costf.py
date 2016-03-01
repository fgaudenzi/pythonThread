import json

costf=json.loads(open('costf.json').read())
for f in costf:
    print f["function"]
    for d in f["deployment"]:
        #print d
        i=0
        for value in d["fcost"]:
            if value!=0:
                print i
            i=i+1
