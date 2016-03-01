from __future__ import print_function
from dataset import generator,get_property_card,load_functionality
from costFunction import CostCalculator
from json_serializer import Requests

if __name__ == '__main__':
    alg=CostCalculator()
    log = open("loag1.txt", "w")
    n=5
    print ("Combination Generator",file = log)
    #generator(10)
    print ("Loading DataSet Property",file = log)
    print ("...",file = log)
    combination=get_property_card("data/property.json")
    print ("....",file = log)
    i=0
    for combo in combination:
        i=i+1
        print ("%d)\t  %s" % (i,combo),file = log)
    res=load_functionality("data/function.json")
    costp=alg.property_based_fc(combination,[0,1,1,2,0,5,7,8,9])
    i=0
    print ("combination",file=log)
    for combo in res:
        i=i+1
        print ("%d)\t  %s" % (i,combo),file = log)
    i=0
    print ("cost function p",file=log)
    for combo in costp:
        i=i+1
        print ("%d)\t  %s" % (i,combo),file = log)
    costf=alg.function_cost_assignment([{"function":"f1"},{"function":"f2"},{"function":"f3"},{"function":"f4"},{"function":"f5"}])
    i=0
    print ("cost function f",file=log)
    for combo in costf:
        i=i+1
        print ("%d)\t  %s" % (i,combo),file = log)

    deployed={"f1":None,"f2":None,"f3":None,"f4":None,"f5":None}


    #alg.choseDeployment(deployed,{'id': 0, 'requestComposition': [{'function': 'f2', 'cert': [{'property': 'p1', 'level': 0}, {'property': 'p2', 'level': 1}]}, {'function': 'f4', 'cert': [{'property': 'p1', 'level': 1}, {'property': 'p2', 'level': 0}]}]})
    #alg.choseDeployment(deployed,{'id': 0, 'requestComposition': [{'function': 'f2', 'cert': [{'property': 'p1', 'level': 0}, {'property': 'p2', 'level': 1}]}, {'function': 'f4', 'cert': [{'property': 'p1', 'level': 1}, {'property': 'p2', 'level': 0}]}]})

    sequence=generator(8,res,combination)
    time=0
    for s in sequence:
        alg.choseDeployment(deployed,s)
        print (s,file = log)
        #print ("Combination "+str(i)+"  is requested at time t"+str(time),file =log)
        time=time+1
        #print ("\t %s" %(combination[i]),file = log)



    import io, json
    with io.open('data.json', 'w', encoding='utf-8') as f:
        f.write(unicode(json.dumps(sequence, ensure_ascii=False)))

    with io.open('deployment.json', 'w', encoding='utf-8') as f:
        f.write(unicode(json.dumps(deployed, ensure_ascii=False)))

