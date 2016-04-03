import json
from costFunction import CostCalculator
from datetime import datetime
from collections import defaultdict
import random


ff=["f1","f2","f3","f4","f5"]
def printCostf(costf):
    #print costf

    #ff=["f1"]
    for f in ff:
                print "-----------------"
                print f
                for fcost in costf:
                    if fcost["function"]==f:
                        for d in fcost["deployment"]:
                            string=""
                            for c in d["cert"]:

                                string=string+"p:"+c["name"]+" level"+str(c["rank"])+" -- "
                            x=0
                            for v in d["fcost"]:
                                if v!=0:
                                    string=string+" - cost at"+str(x)+" of "+str(v)
                                x=x+1
                            print string

def printDeployment(deployed):
    #ff=["f1","f2","f3","f4","f5"]
    ff=["f1"]
    for f in ff:
                print "-----------------"
                print f
                #print deployed[f]
                if not deployed[f]:
                    print "NONE"
                else:
                    for d in deployed[f]:
                        string=""
                        for c in d["cert"]:
                            string=string+"p:"+c["property"]+" -- "

                        string+=string+" k:"+str(d["k"])
                        print string


def printAverageDeployment(allD):
    #print allD[0]
    deployment=[]
    for i in xrange(0,len(allD[0])):
        sum={"costic":0,"costdc":0,"cost":0,"k":0,"costT":0,"costc":0}
        for item in allD:
            sum["costic"]=sum["costic"]+item[i]["costic"]
            sum["costdc"]=sum["costdc"]+item[i]["costdc"]
            sum["cost"]=sum["cost"]+item[i]["cost"]
            sum["costc"]=sum["costc"]+item[i]["costc"]
            sum["k"]=sum["k"]+item[i]["newDeployment"]
            sum["costT"]=sum["costT"]+item[i]["costT"]
        sum["costic"]=sum["costic"]/len(allD)
        sum["costdc"]=sum["costdc"]/len(allD)
        sum["cost"]=sum["cost"]/len(allD)
        sum["costc"]=sum["costc"]/len(allD)
        sum["costT"]=sum["costT"]/(1.*len(allD))
        sum["k"]=sum["k"]*1./len(allD)
        deployment.append(sum)
    costdc=0
    costic=0
    costc=0
    k=0
    costt=0
    print len(deployment)
    print "costdc-costic-costT-sumcostDC-sumcostIC-sumcostc-NewDep"
    for d in deployment:
        k=k+d["k"]
        costic=costic+d["costic"]
        costdc=costdc+d["costdc"]
        costc=costc+d["costc"]
        print str(d["costdc"])+"\t"+str(d["costic"])+"\t"+str(d["costT"])+"\t"+str(costdc)+"\t"+str(costic)+"\t"+str(costc)+"\t"+str(k)


def printDCIC(lista):
    costic=0
    costdc=0
    for l in lista:
        costic=costic+l["costic"]
        costdc=costdc+l["costdc"]
        print str(l["costdc"])+"\t"+str(l["costic"])+"\t"+str(l["costT"])+"\t"+str(costdc)+"\t"+str(costic)+"\t"+str(l["newDeployment"])



if __name__ == '__main__':
    #sequence = json.loads(open('/dataset/dataset.json').read())
    costf=json.loads(open('dataset/costf.json').read())
    costfc=json.loads(open('dataset/costf_cert.json').read())
    app=CostCalculator()
    app.setCostDC(costf)
    app.setCost_Cert(costfc)
    allcost=[]
    alldeployment=[]
    for i in xrange(0,10):
        app.wdc=0.33
        app.wic=0.33
        app.wcc=0.33
        sequence = json.loads(open('dataset/dataset-'+str(i)+'.json').read())
        #random.shuffle(sequence)
        deployed={"f1":None,"f2":None,"f3":None,"f4":None,"f5":None}
        #deployed={"f1":None}
        costlist=[]
        density=0
        x=0
        result=[]
        start=datetime.now()
        rr=1
        for s in sequence:
            if(rr==41):
                break
            rr+=1
            #print s
            cost=app.choseDeployment(deployed,s)

            #print cost["newDeployment"]
            density=density+cost["cost"]
            cost["costT"]=density
            result.append(cost)
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



        #print "---------------------------\n\n\n\n\n\n"
        app.wdc=0.6
        app.wic=0.1
        app.wcc=0.3
        deployed2={"f1":None,"f2":None,"f3":None,"f4":None,"f5":None}
        x=0
        result=[]
        start=datetime.now()
        rr=1
        for s in sequence:
            if(rr==41):
                break
            rr+=1
            #print s
            cost=app.choseDeployment(deployed2,s)
            #print cost["newDeployment"]
            density=density+cost["cost"]
            cost["costT"]=density
            result.append(cost)
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

        tot_f=0
        sum_diff=0
        for f in ff:
            differences=defaultdict(int)
            for d in deployed["f1"]:
                differences[str(d["cert"][0]["level"])]+=d["k"]
                tot_f+=d["k"]
            for d in deployed2["f1"]:
                differences[str(d["cert"][0]["level"])]-=d["k"]
            for i in xrange(0,6):
                sum_diff+=abs(differences[str(i)])

        print 1.*sum_diff/tot_f