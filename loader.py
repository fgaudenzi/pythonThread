import json
from costFunction import CostCalculator
import random
def printCostf(costf):
    #print costf
    #ff=["f1","f2","f3","f4","f5"]
    ff=["f1"]
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
        sum={"costic":0,"costdc":0,"cost":0,"k":0}
        for item in allD:
            sum["costic"]=sum["costic"]+item[i]["costic"]
            sum["costdc"]=sum["costdc"]+item[i]["costdc"]
            sum["cost"]=sum["cost"]+item[i]["cost"]
            sum["k"]=sum["k"]+item[i]["newDeployment"]
        sum["costic"]=sum["costic"]/len(allD)
        sum["costdc"]=sum["costdc"]/len(allD)
        sum["cost"]=sum["cost"]/len(allD)
        sum["k"]=sum["k"]*1./len(allD)
        deployment.append(sum)
    costdc=0
    costic=0
    k=0
    costt=0
    print len(deployment)
    for d in deployment:
        k=k+d["k"]
        costic=costic+d["costic"]
        costdc=costdc+d["costdc"]
        costt=costt+d["cost"]
        print str(d["costdc"])+"\t"+str(d["costic"])+"\t"+str(d["cost"])+"\t"+str(costdc)+"\t"+str(costic)+"\t"+str(k)


def printDCIC(lista):
    costic=0
    costdc=0
    for l in lista:
        costic=costic+l["costic"]
        costdc=costdc+l["costdc"]
        print str(l["costdc"])+"\t"+str(l["costic"])+"\t"+str(l["costT"])+"\t"+str(costdc)+"\t"+str(costic)+"\t"+str(l["newDeployment"])



if __name__ == '__main__':
    sequence = json.loads(open('dataset.json').read())
    costf=json.loads(open('costf.json').read())
    app=CostCalculator()
    app.setCostDC(costf)
    allcost=[]
    alldeployment=[]
    for i in xrange(0,50):
        sequence = json.loads(open('dataset-'+str(i)+'.json').read())
        #random.shuffle(sequence)
        #deployed={"f1":None,"f2":None,"f3":None,"f4":None,"f5":None}
        deployed={"f1":None}
        costlist=[]
        density=0
        x=0
        result=[]
        for s in sequence:
            #print s
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
        alldeployment.append(result)
        allcost.append(costlist)

        #print "---------------------------\n\n\n\n\n\n"
    printAverageDeployment(alldeployment)
    printCostf(app.costf)

    #printDeployment(deployed)
    toprint=""
    for k in range(0,len(allcost[0])):
        for i in range(0,len(allcost)):
            toprint=toprint+str(allcost[i][k])+"\t"
        toprint=toprint+"\n"
    toprint=""
    print toprint
