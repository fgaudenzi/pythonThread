import json
from costFunction import CostCalculator
import itertools
from loader import printAverageDeployment, printCostf
from datetime import datetime


if __name__ == '__main__':


    costf=json.loads(open('dataset/costf.json').read())
    app=CostCalculator()
    app.setCostDC(costf)
    for i in xrange(0,1):
        sequence = json.loads(open('dataset/dataset-'+str(i)+'.json').read())
        for i in xrange(1,35,5):
            print "calcolo permutazioni"
            listas=list(xrange(0,i))
            #subsequences=list(itertools.permutations(sequence[:i],len(sequence[:i])))
            subsequences=list(itertools.permutations(listas,len(listas)))
            print "number of request:"+str(i)
            min=0
            first=True
            startTime = datetime.now()
            #[1,2,3], [2,1,3]
            for listrequest in subsequences:
                deployed={"f1":None}
                costlist=[]
                density=0
                x=0
                result=[]
                for s1 in listrequest:
                    #print s
                    s=sequence[s1]
                    cost=app.choseDeployment(deployed,s)
                    result.append(cost)
                    #print cost["newDeployment"]
                    density=density+cost["cost"]
                    cost["costT"]=density
                    costlist.append(density)
                    #print "-->"
                    #print deployed

                    #print x
                    #for f in ff:
                    #    print "-----------------"
                    #    print f
                    #    #print deployed[f]
                    #    if not deployed[f]:
                    #        print "NONE"
                    #    else:
                    #        for d in deployed[f]:
                    #            string=""
                    #            for c in d["cert"]:
                    #                string=string+"p:"+c["property"]+" -- "
                    #            string+=string+" k:"+str(d["k"])
                    #            print string
                    ##print "f1"
                    ##print deployed["f1"]
                    ##for p in deployed["f1"]["function"]
                    #if(x==258):
                    #    raw_input('click')
                    x=x+1
                 #printDCIC(result)
                #print str(i)
                if first:
                    min=density
                    toprint=result
                    first=False
                else:
                    if density<=min:
                        #print result
                        torprint=result
            print toprint
            print datetime.now() - startTime

