import json

costf=json.loads(open('dataset/costf.json').read())
for f in costf:
    print f["function"]
    for d in f["deployment"]:
        print d["cert"][0]["rank"]
        i=1
        for value in d["fcost"]:
            #if value!=0:
            print str(value)
            i=i+1
        print "------------------"