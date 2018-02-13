import os

g=open('filtered_products.txt','w')
for line in open("products.txt"):
    line=line.split(':')
    g.write(line[0]+'\n')

g.close()

os.remove('products.txt')
os.rename('filtered_products.txt','products.txt')



invalid_products=[]
for line in open("filters.txt"):
    invalid_products.append(line.strip())    

g=open('filtered_products.txt','w')

for line in open("products.txt"):
    flag=0
    for p in invalid_products:
        if p in line.lower():
            flag=1
            break
    if flag==0:
        g.write(line)
        

g.close()


            

##files=os.listdir("filtered_xml")
##
##for file_name in files:
##
##    id=''
##    product=''
##    bug_status=''
##
##    
##    for line in open('filtered_xml//'+file_name,'r'):
##        line=line.strip()
##      
##        if "<"+tags[0]+">" in line:
##            product=line
##            product=product.replace("<"+tags[0]+">",'')
##            product=product.replace("</"+tags[0]+">",'')
##        elif "<"+tags[1]+">" in line:
##            bug_status=line
##            bug_status=bug_status.replace("<"+tags[1]+">",'')
##            bug_status=bug_status.replace("</"+tags[1]+">",'')
##          
##    if bug_status.lower()=='invalid':
##        os.remove('filtered_xml//'+file_name)
##    else:
##        for p in invalid_products:
##            if p in product.lower():
##                os.remove('filtered_xml//'+file_name)
##                break
##
