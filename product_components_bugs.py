import os


count=0

files=os.listdir("filtered_xml")

product=dict()
component=dict()
product_component=dict()

for file_name in files:
    prod_comp=""
    bug_id=""
    
    for line in open("filtered_xml//"+file_name):
        line=line.rstrip()

        if "<bug_id>" in line:
            line=line.replace("<bug_id>","")
            line=line.replace("</bug_id>","")
            bug_id=line
        
        if "<product>" in line:
            line=line.replace("<product>","")
            line=line.replace("</product>","")

            prod_comp=line
            
        if "<component>" in line:
            line=line.replace("<component>","")
            line=line.replace("</component>","")

            prod_comp=prod_comp+"\t"+line

    if prod_comp not in product_component:
        product_component[prod_comp] = [int(bug_id),]
    else:
        product_component[prod_comp].append(int(bug_id)) 

    

                

g=open('product_components_bugs.csv','w')
g.write("Product,Component,Count,Bugs->\n")
print "\nProduct [Components] : Count"
print "---------------------------\n"
for key, value in sorted(product_component.iteritems(), key=lambda (k,v): (len(v),k), reverse=True):
    strx = "%s" % key
    prod=strx.split('\t')[0]
    comp=strx.split('\t')[1]
    g.write(prod+",")
    g.write(comp+",")
    g.write(str(len(value)))
    strx=""
    for ele in value:
        strx+=","+str(ele)
    #print strx
    g.write(strx+"\n")
g.close()



















