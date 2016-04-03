for i in xrange(0,10):
    for x in xrange(1,6):
        print "glpsol -m deploy.mod -d profile3/dataset-"+str(i)+"-task_f"+str(x)+"k-100 > profile3x/dataset-"+str(i)+"-task_f"+str(x)+"k-100.xres &"
        print "glpsol -m deploy.mod -d profile3/dataset-"+str(i)+"-task_f"+str(x)+"k-50 > profile3x/dataset-"+str(i)+"-task_f"+str(x)+"k-50.xres &"