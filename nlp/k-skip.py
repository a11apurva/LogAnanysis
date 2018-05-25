line= "insurgents killed in ongoing fighting"

n=2
k=1

line=line.split()



for i in range(len(line)):
    try:
        gram=[]
        for l in range(k):
            

        
            
    except:
        pass




##for i in range(len(line)):
##    try:        
##        
##        for l in range(k+1):
##            gram=[]
##            for j in range(n):
##                print [i,l,j]
##                gram.append(line[i+j])
##            print gram
##    except:
##        pass



def ngram(n):
    for i in range(len(line)):
        try:
            gram=[]
            for j in range(n):
                gram.append(line[i+j])
            print gram
        except:
            pass


def kskip(n,k):
    for i in range(len(line)):
        #print "i="+str(i)
        for j in range(n):
            #print "j="+str(j)
            for l in range(k):
                #print "l="+str(l)
                #gram.append(line[i+j])
                if i+j != i+j+l :
                    print [i+j,i+j+l]
