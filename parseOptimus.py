import re


#var y{K,J} binary;

if __name__ == '__main__':

    ff=["f1","f2","f3","f4","f5"]
    max_stop=51
    all_dataset=[]
    for i in xrange(0,10):
        c_result=[]
        for fi in ff:
            f_result=[]
            for stop_at in xrange(50,max_stop,1):
                if(stop_at!=0):
                    fname="/Users/iridium/ris_12/newEXP/50result/fit50/dataset-"+str(i)+"-task_"+str(fi)+"k-"+str(stop_at)+".result"

                    y=[]
                    with open(fname) as f:
                        content = f.readlines()
                        for row in content:
                            if "FILIPPO:" in row:
                                #print row
                                tot= str(float(re.findall(r"[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", row)[0]))
                            if "y[" in row:
                                ylist=map(int, re.findall(r'\d+', row))
                                #print ylist
                                #print ylist[2]
                                if ylist[2]==1:
                                    y.append(ylist)
                        maxh=[]
                        for j in xrange(0,9):
                            maxh.append([])
                            for item in y:
                                if item[1]==j:
                                    maxh[j].append(item[0])
                        j=0
                        hscale=[]
                        for k in maxh:
                            if len(k)>0:
                                #print str(j)+"\t"+str(k[len(k)-1])
                                hscale.append([j,k[len(k)-1]])
                            j+=1
                        if(len(hscale)>3):
                            scale=len(hscale)%3
                        else:
                            scale=0
                        f_result.append({"value":tot,"hscale":scale})
                        #print str(tot)+"\t"+str(scale)
                        f.close()
            value={"function":fi,"optimum":f_result}
            c_result.append(value)
            #print "-----------------"
        all_dataset.append(c_result)
    for dataset in all_dataset:
        for i in xrange(0,1):
            ctotal=0
            htotal=0
            for d in dataset:
                ctotal+=float(d["optimum"][i]["value"])
                htotal+=int(d["optimum"][i]["hscale"])
            print str(ctotal)+"\t"+str(htotal)
        print "---------"