import json
from costFunction import CostCalculator
import itertools
from loader import printAverageDeployment, printCostf
from datetime import datetime
from multiprocessing import Pool

nproc=20

def minT(risultato):

    first=True

    for r in risultato:
                if first:
                    min=r["costT"]
                    toprint=r
                    first=False
                else:
                    if r["costT"]<=min:
                        #print result
                        torprint=r
    return toprint



def multiT(listrequest):
    deployed={"f1":None}
    costlist=[]
    density=0
    x=0
    result=[]
    for s in listrequest:
                    #print s
                    #s=sequence[s1]
                    cost=app.choseDeployment(deployed,s)

                    #print cost["newDeployment"]
                    density=density+cost["cost"]
                    cost["costT"]=density
                    #costlist.append(density)
                    #result.append(cost)
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
    return cost

if __name__ == '__main__':


    costf=json.loads(open('dataset/costf.json').read())
    app=CostCalculator()
    app.setCostDC(costf)
    for i in xrange(0,1):
        sequence = json.loads(open('dataset/dataset-'+str(i)+'.json').read())
        for i in xrange(11,12):
            start=datetime.now()
            print "number of request:"+str(i)
            print "calcolo permutazioni"
            listas=list(xrange(0,i))
            lung=len(sequence[:i])
            subsequences=list(itertools.permutations(sequence[:i],lung))
            #subsequences=list(itertools.permutations(listas,len(listas)))
            print datetime.now()-start
            start=datetime.now()
            print "calcolo costo"
            min=0
            first=True
            startTime = datetime.now()
            #[1,2,3], [2,1,3]
            list2pool=[]
            p = Pool(processes=nproc)
            lung=len(subsequences)
            #max  10Million
            nsec=4
            print "0 TO "+ str(lung/nsec)
            risultato=p.map(multiT,subsequences[:(lung/nsec)])
            for div in xrange(1,nsec):
                print "TAGLIATO"
                print str((lung/nsec)*div+1)+" TO "+str((lung/nsec)*(div+1))
                risultato.extend(p.map(multiT,subsequences[(lung/nsec)*div+1:(lung/nsec)*(div+1)]))
            print str((lung/nsec)*div+1)+" TO"+str(lung)
            risultato.extend(p.map(multiT,subsequences[((lung/nsec)*div+1):lung]))
            print datetime.now()-start
            start=datetime.now()
            print "index per minimi"
            minimi=[]
            ind=0
            nminimi=lung/nproc
            checker=lung%nproc
            if(checker!=0):
                nminimi += 1
            print "nm"+str(nminimi)
            while(ind<lung-nminimi):
                ind=ind+nminimi
                minimi.append(risultato[ind-nminimi:ind])
            if(checker!=0):
                minimi.append(risultato[ind:lung])


            minarray=p.map(minT,minimi)
            print minarray
            print datetime.now()-start

            #for r in minarray:
            #    if first:
            #        min=r["costT"]
            #        toprint=r
            #        first=False
            #    else:
            #        if r["costT"]<=min:
            #            #print result
            #            torprint=r
            #print r


















            #for listrequest in subsequences:
            #    deployed={"f1":None}
            #    costlist=[]
            #    density=0
            #    x=0
            #    result=[]
#
#
#
#
#
#
#
            #    for s in listrequest:
            #        #print s
            #        #s=sequence[s1]
            #        cost=app.choseDeployment(deployed,s)
            #        result.append(cost)
            #        #print cost["newDeployment"]
            #        density=density+cost["cost"]
            #        cost["costT"]=density
            #        costlist.append(density)
            #        #print "-->"
            #        #print deployed
#
            #        #print x
            #        #for f in ff:
            #        #    print "-----------------"
            #        #    print f
            #        #    #print deployed[f]
            #        #    if not deployed[f]:
            #        #        print "NONE"
            #        #    else:
            #        #        for d in deployed[f]:
            #        #            string=""
            #        #            for c in d["cert"]:
            #        #                string=string+"p:"+c["property"]+" -- "
            #        #            string+=string+" k:"+str(d["k"])
            #        #            print string
            #        ##print "f1"
            #        ##print deployed["f1"]
            #        ##for p in deployed["f1"]["function"]
            #        #if(x==258):
            #        #    raw_input('click')
            #        x=x+1
            #     #printDCIC(result)
            #    #print str(i)
            #    if first:
            #        min=density
            #        toprint=result
            #        first=False
            #    else:
            #        if density<=min:
            #            #print result
            #            torprint=result
            #print toprint
            #print datetime.now() - startTime
#
