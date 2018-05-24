line= "insurgents killed in ongoing fighting"

n=3

line=line.split()

for i in range(len(line)):
    gram=[]
    try:
        for j in range(n):
            gram.append(line[i+j])
        print gram
    except:
        pass
        
