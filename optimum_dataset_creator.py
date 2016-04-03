from __future__ import print_function
import json
from costFunction import CostCalculator

#param NJ:=
#param NK:=
#param NI:=
#ff=["f5"]
ff=["f5"]
property=[0,1,2,3,4,5]

max_stop=51
###param r:=  per ogni richiesta il livello di proprieta richiesto (Attenzione NK,NI dipende dal max di r)

###param deltac := ogni sal
horizontal_dep=3
max=100
def printSequence(sequence,stop_at):
    toprint=""
    #print sequence
    toprint=toprint+ "param r:=\n"
    h=1
    x=1
    for s in sequence:
        for r in s["requestComposition"]:
            if r["function"]==ff[0]:
                toprint=toprint+ str(h)+" "+str(r["cert"][0]["level"]*horizontal_dep)+"\n"
                h+=1
        if x==stop_at:
            break
        x+=1
    toprint=toprint+ ";"+"\n"
    toprint=toprint+ "param NJ:="+str(horizontal_dep*len(property)-1)+";"+"\n"
    toprint=toprint+ "param NK:="+str(h-1)+";"+"\n"
    toprint=toprint+ "param NI:="+str(h-1)+";"+"\n"
    return toprint,h-1



def printCostf(costf,stop_at):
    #print costf
    #ff=["f1","f2","f3","f4","f5"]
    toprint=""
    for f in ff:
                toprint=toprint+ "#-----------------"+"\n"
                toprint=toprint+ "#"+str(f)+"\n"
                toprint=toprint+ "param deltadc:="+"\n"
                for fcost in costf:
                    if fcost["function"]==f:
                        for d in fcost["deployment"]:
                            string=""
                            for c in d["cert"]:
                                #print c["name"]+ " "+ str(c["rank"])
                                string=string+"p:"+c["name"]+" level"+str(c["rank"])+" -- "

                            for px in xrange(horizontal_dep*c["rank"],c["rank"]*horizontal_dep+horizontal_dep):
                                #print px
                                x=0
                                for v in d["fcost"]:
                                    if v!=0:
                                        string=string+" - cost at"+str(px)+" of "+str(v)
                                        toprint=toprint+ str(x)+" "+str(px)+" "+str(v)+"\n"
                                    #x=x+1
                                    if x == stop_at:
                                        break
                                    x=x+1
    toprint=toprint+ ";"+"\n"
    return toprint;


def printCost_cert(costf,stop_at):
    #print costf
    #ff=["f1","f2","f3","f4","f5"]
    toprint=""
    for f in ff:
                toprint=toprint+ "#-----------------"+"\n"
                toprint=toprint+ "#"+str(f)+"\n"
                toprint=toprint+ "param deltacc:="+"\n"
                for fcost in costf:
                    if fcost["function"]==f:
                        for d in fcost["deployment"]:
                            string=""
                            for c in d["cert"]:
                                #print c["name"]+ " "+ str(c["rank"])
                                string=string+"p:"+c["name"]+" level"+str(c["rank"])+" -- "

                            for px in xrange(horizontal_dep*c["rank"],c["rank"]*horizontal_dep+horizontal_dep):
                                #print px
                                x=0
                                for v in d["fcost"]:
                                    if v!=0:
                                        string=string+" - cost at"+str(px)+" of "+str(v)
                                        toprint=toprint+ str(x)+" "+str(px)+" "+str(v)+"\n"
                                    x=x+1
                                    if x == stop_at:
                                        break
    toprint=toprint+ ";"  +"\n"
    return toprint#print string


if __name__ == '__main__':

    costf=json.loads(open('dataset/costf.json').read())
    cost_cert=json.loads(open('dataset/costf_cert.json').read())
    app=CostCalculator()
    app.setCostDC(costf)


    for i in xrange(0,10):
        for stop_at in xrange(50,max_stop,10):
            if(stop_at!=0):
                log = open("dataset/dataset-"+str(i)+"-task_"+str(ff[0])+"k-"+str(stop_at), "w")
                sequence = json.loads(open('dataset/dataset-'+str(i)+'.json').read())

                toprint,lunghezza=printSequence(sequence,stop_at)
                costfprint=printCostf(costf, lunghezza)
                print (costfprint,file = log)
                costfprint=printCost_cert(cost_cert,lunghezza)
                print (costfprint,file = log)
                print (toprint,file = log)
                print ("param wdc:="+str(app.wdc)+";",file = log)
                print ("param wcc:="+str(app.wcc)+";",file = log)
                print ("param wic:="+str(app.wic)+";",file = log)
                print ("param deltaIC:=",file = log)
                maxCERT=horizontal_dep*len(property)
                #arrayprop=[[0,1],[2,3],[4,5],[6,7],[8,9],[10,11]]
                #arrayprop=[[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15],[16,17,18,19],[20,21,22,23]]
                arrayprop=[[0,1,2],[3,4,5],[6,7,8],[9,10,11],[12,13,14],[15,16,17]]

                for indexa in xrange(0,len(arrayprop)):
                    molt=1
                    for indexp in xrange(indexa+1,len(arrayprop)):
                        for indexs in xrange(0,len(arrayprop[indexa])):
                            for appp in arrayprop[indexp]:
                                print (str(arrayprop[indexa][indexs])+" "+str(appp)+" "+str(molt*0.1),file=log)

                        molt+=1


               # #for px in xrange(0,horizontal_dep):
                #    for pxc in xrange(horizontal_dep,horizontal_dep*2):
                #        print (str(px)+" "+str(pxc)+" 0.1",file = log)
                #    for pxc in xrange(horizontal_dep*2,horizontal_dep*3):
                #        print (str(px)+" "+str(pxc)+" 0.2",file = log)
                #for px in xrange(horizontal_dep,horizontal_dep*2):
                #    for pxc in xrange(horizontal_dep*2,horizontal_dep*3):
                #        print (str(px)+" "+str(pxc)+" 0.33",file = log)
                print (";",file = log)
                log.close()