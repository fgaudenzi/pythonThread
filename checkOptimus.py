import re
from collections import defaultdict

#var y{K,J} binary;
def getrange(a):
    if a==0:
        return 0
    if a==1:
        return 0
    if a==2:
        return 0
    if a==3:
        return 1
    if a==4:
        return 1
    if a==5:
        return 1
    if a==6:
        return 2
    if a==7:
        return 2
    if a==8:
        return 2
    if a==9:
        return 3
    if a==10:
        return 3
    if a==11:
        return 3
    if a==12:
        return 4
    if a==13:
        return 4
    if a==14:
        return 4
    if a==15:
        return 5
    if a==16:
        return 5
    if a==17:
        return 5
    if a==18:
        return 6
    if a==19:
        return 6
    if a==20:
        return 5
    if a==21:
        return 5
    if a==22:
        return 5
    if a==23:
        return 5

if __name__ == '__main__':
    i=9
    ff=["f1","f2","f3","f4","f5"]
    max_stop=51
    all_dataset=0
    for i in [1,5]:
            #xrange(0,10):
        c_result=[]
        tot_migc=0
        for fi in ff:
            f_result=[]
            for stop_at in xrange(50,max_stop,10):
                if(stop_at!=0):
                    fname="/Users/iridium/ris_12/newEXP/50result/fit50/dataset-"+str(i)+"-task_"+str(fi)+"k-"+str(stop_at)+".result"
                    print fname
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

                        hscale_checker=defaultdict(int)
                        for dev in y:
                            hscale_checker[dev[1]]+=1
                        counter=defaultdict(int)
                        for dev in hscale_checker:
                            counter[getrange(dev)]+=1
                            print str(dev)+"-"+str(hscale_checker[dev])
                        print "-------"
                        for dev in counter:
                            print str(dev)+"-"+str(counter[dev])
                            if counter[dev]>3:
                                print "UPPER BUON FALSE"


