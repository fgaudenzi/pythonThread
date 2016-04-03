import re


#var y{K,J} binary;
def getrange(a):

    if a==0:
        return [0,1,2]
    if a==1:
        return [0,1,2]
    if a==2:
        return [0,1,2]
    if a==3:
        return [3,4,5]
    if a==4:
        return [3,4,5]
    if a==5:
        return [3,4,5]
    if a==6:
        return [6,7,8]
    if a==7:
        return [6,7,8]
    if a==8:
        return [6,7,8]
    if a==9:
        return [9,10,11]
    if a==10:
        return [9,10,11]
    if a==11:
        return [9,10,11]
    if a==12:
        return [12,13,14]
    if a==13:
        return [12,13,14]
    if a==14:
        return [12,13,14]
    if a==15:
        return [15,16,17]
    if a==16:
        return [15,16,17]
    if a==17:
        return [15,16,17]


#    if a==0:
#        return [0,1,2,3]
#    if a==1:
#        return [0,1,2,3]
#    if a==2:
#        return [0,1,2,3]
#    if a==3:
#        return [0,1,2,3]
#    if a==4:
#        return [4,5,6,7]
#    if a==5:
#        return [4,5,6,7]
#    if a==6:
#        return [4,5,6,7]
#    if a==7:
#        return [4,5,6,7]
#    if a==8:
#        return [8,9,10,11]
#    if a==9:
#        return [8,9,10,11]
#    if a==10:
#        return [8,9,10,11]
#    if a==11:
#        return [8,9,10,11]
#    if a==12:
#        return [12,13,14,15]
#    if a==13:
#        return [12,13,14,15]
#    if a==14:
#        return [12,13,14,15]
#    if a==15:
#        return [12,13,14,15]
#    if a==16:
#        return [16,17,18,19]
#    if a==17:
#        return [16,17,18,19]
#    if a==18:
#        return [16,17,18,19]
#    if a==19:
#        return [16,17,18,19]
#    if a==20:
#        return [20,21,22,23]
#    if a==21:
#        return [20,21,22,23]
#    if a==22:
#        return [20,21,22,23]
#    if a==23:
#        return [20,21,22,23]
if __name__ == '__main__':
    i=9
    ff=["f1","f2","f3","f4","f5"]
    max_stop=41
    #all_dataset=0
    all_dataset=[]
    for i in xrange(0,10):
        c_result=[]
        tot_migc=0
        tot_r=0
        for fi in ff:
            f_result=[]
            for stop_at in xrange(20,max_stop,20):
                if(stop_at!=0):
                    fname="/Users/iridium/ris_12/newEXP/average_h3/dataset-"+str(i)+"-task_"+str(fi)+"k-"+str(stop_at)+".result"
                    #print fname
                    y=[]
                    with open(fname) as f:
                        content = f.readlines()
                        for row in content:
                            if "FILIPPO:" in row:
                                #print row
                                tot= str(float(re.findall(r"[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", row)[0]))
                            if "x[" in row:
                                ylist=map(int, re.findall(r'\d+', row))
                                #print ylist
                                #print ylist[2]
                                if ylist[2]==1:
                                    y.append(ylist)

                        f_result.append(y)
                        #print str(tot)+"\t"+str(scale)
                        f.close()
            migration=0;
            for z in xrange(0,len(f_result[0])):
                l=getrange(f_result[0][z][1])
                if f_result[1][z][1] not in l:
                    #print "richiesta:"+str(z+1)
                    #print str(f_result[0][z][1])+"vs"+ str(f_result[1][z][1])

                #if f_result[0][z][1]!=f_result[1][z][1]:
                    migration+=1
            #print migration
            value={"function":fi,"mig":migration,"tot":len(f_result[0])}
            c_result.append(value)
            tot_r+=len(f_result[0])
            tot_migc+=migration
            #print "-----------------"
        #print "-----------------"
        print str(tot_migc)+"/"+str(tot_r)
        #print "-----------------"
        all_dataset.append(1.*tot_migc/tot_r)#=tot_migc
    print "----"
    for a in all_dataset:
        print a